from pattern.en import number
from math import ceil
import config

THRESHOLD = config.SIMILARITY_THRESHOLD


def identifyAction(nlp, token):
    """Identify action type from token using similarity matching."""
    actions = [["order", "add", "take", "purchase", "buy", "get", "have"],
               ["replace", "substitute"],
               ["remove", "leave", "subtract", "cancel", "delete"],
               ["query", "search", "list", "find", "show", "look"],
               ["finish", "exit", "complete", "checkout", "done", "nothing", "review"]]
    function = "none"
    maxScore = THRESHOLD
    for i, group in enumerate(actions):
        for action in group:
            similarity = nlp(token).similarity(nlp(action))
            if similarity > maxScore:
                maxScore = similarity
                if i == 0:
                    function = "add"
                elif i == 1:
                    function = "replace"
                elif i == 2:
                    function = "remove"
                elif i == 3:
                    function = "query"
                elif i == 4:
                    function = "complete"

    return function, maxScore


def fillAction(slots, tokens, nlp):
    """Extract action intent from POS-tagged tokens."""
    max_score = 0
    req_action = "none"
    for token in tokens:
        if token["entity"] == 'VERB' and token["score"] > max_score:
            max_score = token["score"]
            req_action = token["word"]

    function, max_score = identifyAction(nlp, req_action)
    if not function == "none" or slots[0] == "none":
        slots[0] = function

    if slots[0] == "none":
        max_score = THRESHOLD
        for token in tokens:
            function, score = identifyAction(nlp, token["word"])
            if score > max_score:
                max_score = score
                slots[0] = function
    return slots


def fillItem(slots, nlp, menu_items, response):
    """Extract menu items from response using NLP similarity matching."""
    matches = []
    doc = nlp(response)
    doc = nlp(' '.join([str(token.lemma_) for token in doc if not token.is_stop and not token.is_punct]))
    
    for n in range(1, len(doc) + 1):
        for i in range(len(doc) + 1 - n):
            phrase = ""
            for j in range(n):
                phrase += str(doc[i + j])
                if j < n - 1:
                    phrase += " "
            for item in menu_items:
                similarity = nlp(item[2].lower()).similarity(nlp(phrase))
                if similarity > THRESHOLD:
                    matches += [[item[0], similarity, i, i + n]]
                if item[1] == phrase:
                    matches += [[item[0], 1, i, i + n]]

    best_matches = []
    while len(matches) > 0:
        max_score = 0
        best_match = 0
        for i, match in enumerate(matches):
            if match[1] > max_score:
                max_score = match[1]
                best_match = i
        best_matches += [matches[best_match]]
        needs_removed = []
        for match in matches:
            if not (match[3] <= matches[best_match][2] or matches[best_match][3] <= match[2]):
                needs_removed += [match]
        for i in range(len(needs_removed)):
            matches.remove(needs_removed[i])

    entities = doc.ents
    quantities = []
    for entity in entities:
        if entity.label_ == "CARDINAL" and number(str(entity)) > 0:
            quantities += [[entity, entity.start, entity.end, -1]]
    # Find the dependency head of each number
    for quantity in quantities:
        for i in range(quantity[1], quantity[2]):
            for j in range(len(doc)):
                if doc[i].head == doc[j] and (j < quantity[1] or j >= quantity[2]):
                    quantity[3] = j
                    break
    # For each menu item, find the number that shares a common ancestor, or default to 1 if no common ancestors
    for match in bestMatches:
        quant = 1
        flag = False
        for quantity in quantities:
            for i in range(match[2], match[3]):
                head = doc[i]
                while True:
                    if doc[quantity[3]] == head:
                        quant = ceil(number(str(quantity[0])))
                        flag = True
                        break
                    if head.head == head:
                        break
                    head = head.head
                if flag:
                    break
            if flag:
                break
        # Fill a slot by adding the menu items and corresponding quantities one at a time
        slots[1] += [match[0]]
        slots[2] += [quant]
    # If any orders are drinks, assign the first one to the drink slot
    for i, item in enumerate(slots[1]):
        if menuItems[item - 1][1][0] == "D":
            slots[4] = item
            if slots[2][i] > 1:
                slots[2][i] -= 1
            else:
                slots[1].pop(i)
                slots[2].pop(i)
            break
    return slots
