import database
from card import Card

def listCards(fileName):
    db = database.loadDatabase(fileName)
    cards = database.loadCards(db=db)
    for card in cards:
        print(str(card))


if __name__ == "__main__":
    db = database.loadDatabase("box.db")
    print("You can list/add/modify/delete")
    command = input("What to do: ").lower()
    if command == "list":
        print("Listing...")
        listCards("box.db")
    elif command == "add":
        question = input("Question: ")
        answer = input("answer: ")
        colour = input("colour: ")
        image = input("image: ")
        card = Card(
                None,
                question,
                answer,
                colour,
                image,
                1, 0)
        database.insertCard(db, card)
    elif command == "modify":
        cardId = input("Id of card to replace: ")
        card = database.loadCard(db, cardId)
        property_ = input("Property to modify: ").lower()
        value = input("New value: ")
        if property_ == "question":
            card.question = value
        elif property_ == "answer":
            card.answer = value
        elif property_ == "colour":
            card.colour = value
        elif property_ == "image":
            card.image = value
        database.replaceCard(db, cardId, card)
    elif command == "delete":
        cardId = input("Id of card to delete: ")
        database.deleteCard(db, cardId)
    else:
        print("Unrecognised command")







