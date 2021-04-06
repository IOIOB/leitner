import card

def play(session, cards):
    newCards = []
    print(f"Session: {session}")
    for card in cards:
        print(str(card))
        guess = input("Got it?")
        if guess.lower().startswith("y"):
            card.streak = card.streak + 1
            card.sessionAsked = session
        else:
            card.streak = 1
            card.sessionAsked = session
        newCards.insert(0, card)
    newSession = session + 1
    return (newSession, newCards)
