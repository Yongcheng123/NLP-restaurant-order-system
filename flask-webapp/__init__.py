import os
import pandas as pd
import spacy
from transformers import pipeline
from flask import Flask, request, Response, render_template, session

import nlu
import assistant_actions
import web_actions
import config

ACTION_WORDS = {
    "order", "add", "take", "purchase", "buy", "get", "have",
    "replace", "substitute",
    "remove", "leave", "subtract", "cancel", "delete",
    "query", "search", "list", "find", "show",
    "finish", "exit", "complete", "checkout", "done", "nothing"
}


    nlp = spacy.load(config.SPACY_MODEL)
    classifier = pipeline("token-classification", model=config.BERT_MODEL)

    data = pd.read_csv(config.DATA_CSV)
    glossary = web_actions.initialize_glossary(data)
    menu = pd.read_csv(config.MENU_CSV)ize_glossary(data)
    menu = pd.read_csv("menu.csv")
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/submit-prompt', methods=['POST'])
    def handle_prompt():
        prompt = request.json['textPrompt']
        response = render_template('chat-bubble-sent.html', message=prompt)
        tokens = classifier(prompt)
        
        try:
            action, _ = max(
                [nlu.identifyAction(nlp, token['word']) for token in tokens 
                 if token["entity"] == "VERB" or token['word'] in ACTION_WORDS],
                key=lambda x: x[1]
            )
        except ValueError:
            response += render_template('chat-bubble-received.html',
                                        message="I'm not sure what you mean, can you rephrase?")
            return Response(response, mimetype='text/html')

        if action == 'add':
            response += web_actions.add_html(prompt, menu, glossary)
        elif action == 'remove':
            response += web_actions.remove_html(prompt, glossary)
        elif action == 'query':
            response += web_actions.query_html(prompt, menu, glossary)
        elif action == 'complete':
            response += render_template(
                'checkout.html', 
                cart=session["order"], 
                total=session["order_total"]
            )
        
        return Response(response, mimetype='text/html')

    @app.route('/', methods=['GET'])
    def home_page():
        if "order" not in session:
            session["order"] = []
            session["order_total"] = 0
        return render_template('index.html')

    return app
