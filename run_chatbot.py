"""Main entry point for the command-line chatbot."""
import warnings
import pandas as pd
import spacy
from pattern.en import number, ngrams
from transformers import pipeline

from src.chatbot.core.dialog_manager import assist
from src.chatbot.core.actions import addOrder, removeOrder, queryMenu, completeOrder
from src.chatbot.services.speech import text_to_speech
from src.chatbot.services.translation import translate
from src.chatbot import config

warnings.simplefilter("ignore", UserWarning)


def main():
    """Run the command-line chatbot interface."""
    nlp = spacy.load(config.SPACY_MODEL)
    classifier = pipeline("token-classification", model=config.BERT_MODEL)

    for word in config.NUMBER_WORDS:
        nlp.Defaults.stop_words.discard(word)

    data = pd.read_csv(config.DATA_CSV).values.tolist()
    menu = pd.read_csv(config.MENU_CSV)
    menu_items = menu.values.tolist()

    request = ""
    language = ""
    orders = []
    transactions = []
    slots = ["none", [], [], "", 0]
    old_slots = ["none", [], [], "", 0]

    is_complete = False
    while not is_complete:
        filled = False
        while not filled:
            old_slots = list(slots)
            old_slots[1] = list(slots[1])
            old_slots[2] = list(slots[2])
            request, slots, language = assist(slots, orders, menu_items, nlp, classifier, language, data)
            if old_slots == slots:
                text_to_speech(translate("Sorry, I didn't understand your request.", language), language)
            if slots[0] == "add":
                if len(slots[1]) > 0 and not (slots[3] == "" or slots[4] == 0) or (slots[1] == [] and slots[4] > 0):
                    filled = True
            elif slots[0] == "query" or slots[0] == "complete" or slots[0] == "remove" and len(slots[1]) > 0:
                filled = True

        if slots[0] == "add":
            orders, transactions = addOrder(slots, orders, transactions, menu_items, language)
        elif slots[0] == "remove":
            orders, transactions = removeOrder(slots, orders, transactions, menu_items, language)
        elif slots[0] == "query":
            transactions = queryMenu(request, transactions, menu_items, nlp, classifier, language)
        elif slots[0] == "complete":
            transactions, is_complete = completeOrder(orders, transactions, menu_items, language)
        
        if slots[0] == "query":
            slots = list(old_slots)
            slots[1] = list(old_slots[1])
            slots[2] = list(old_slots[2])
        else:
            slots = ["none", [], [], "", 0]
    
    text_to_speech(translate("Thank you for eating with us today!", language), language)

    return 0


if __name__ == '__main__':
    main()
