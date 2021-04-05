import card


def loadDatabase(filename):
    pass

def loadSession(db):
    pass


def loadCards(db, session):
    pass


def play(session, cards):
    pass


def saveCards(db, cards):
    pass


def saveSession(db, session):
    pass


if __name__ == "__main__":
    db = loadDatabase("cards.db")
    session = loadSession(db)
    cards = loadCards(db, session)

    (session, cards) = play(session, cards)

    saveCards(db, cards)
    saveSession(db, cards)
