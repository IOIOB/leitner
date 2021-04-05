import card

def play(session, cards):
    newCards = []
    for card in cards:
        print(str(card))
        guess = input("Got it?")
        if guess.lower().startswith("y"):
            card.streak = card.streak + 1
            card.sessionAsked = session
            newCards.insert(card)
    newSession = session + 1
    return (newSession, newCards)
