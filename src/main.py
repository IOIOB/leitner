import card
import database


def play(session, cards):
    pass


if __name__ == "__main__":
    db = database.loadDatabase("cards.db")

    session = database.loadSession(db)
    cards = database.loadCards(db, session)


    (session, cards) = play(session, cards)

    saveCards(db, cards)
    saveSession(db, cards)
