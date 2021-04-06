import card
import database
import playSession


if __name__ == "__main__":
    db = database.loadDatabase("box.db")

    session = database.loadSession(db)
    cards = database.loadCards(db, session)


    (session, cards) = playSession.play(session, cards)

    database.saveCards(db, cards)
    database.saveSession(db, session)
