import card

def getAnswerInput():
    print("Did you get it?")
    print("('y' if you did, 'n' if you didn't): ", end="")
    rawInput = input()

    if rawInput.lower() == "y":
        return True
    elif rawInput.lower() == "n":
        return False
    else:
        print(f"{rawInput} is not a valid answer...")
        return getAnswerInput()

def play(session, cards):
    newCards = []

    print(f"Current session: {session}")
    print("")
    
    for i, card in enumerate(cards):
        print("")
        print(f"Question {i}:")
        print(f"  {card.question}")
        print("(Press Enter to show answer)")

        input()

        print("Answer:")
        print(f"  {card.answer}")
        print("")

        isAnswerCorrect = getAnswerInput()
        
        if isAnswerCorrect:
            card.streak = card.streak + 1
            card.sessionAsked = session
        else:
            card.streak = 1
            card.sessionAsked = session
        newCards.insert(0, card)

    newSession = session + 1
    return (newSession, newCards)
