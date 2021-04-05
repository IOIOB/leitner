import card
import database
import playSession


if __name__ == "__main__":
    db = database.loadDatabase("cards.db")

    session = database.loadSession(db)
    cards = database.loadCards(db, session)


    (session, cards) = playSession.play(session, cards)

    saveCards(db, cards)
    saveSession(db, session)
