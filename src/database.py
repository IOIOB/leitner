from card import Card
import sqlite3


def loadDatabase(filename):
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS session(
            id INTEGER PRIMARY KEY CHECK (id = 0),
            number INTEGER
        )""")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cards(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            colour TEXT,
            image TEXT,
            streak INTEGER NOT NULL,
            sessionAsked INTEGER NOT NULL)""")
    db.commit()
    cursor.close()
    return db


def loadSession(db):
    cursor = db.cursor()
    cursor.execute("""
        SELECT number FROM session""")
    session = cursor.fetchone()
    if session is None:
        session = 1
    cursor.close()
    return session


def loadCards(db, session):
    cursor = db.cursor()
    cursor.execute("""
        SELECT * FROM cards""")
    cardTuples = cursor.fetchall()
    cursor.close()
    cards = [ Card(*c) for c in cardTuples ]
    return cards


def insertCard(db, card):
    _, *cardTupleWithoutId = tuple(card)
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO cards
            (question,
             answer,
             colour,
             image,
             streak,
             sessionAsked)
        VALUES (?,?,?,?,?,?)""",
        cardTupleWithoutId)
    db.commit()
    cursor.close()


def saveCards(db, cards):
    cardTuples = [
        (*tail, head) for head, *tail in cards]
    cursor = db.cursor()
    cursor.executemany("""
        UPDATE cards
        SET question = ?,
            answer = ?,
            colour = ?,
            image = ?,
            streak = ?,
            sessionAsked = ?
        WHERE
            id == ?""",
        cardTuples)
    db.commit()
    cursor.close()


def saveSession(db, session):
    pass


if __name__ == "__main__":
    db = loadDatabase("test.db")
    session = loadSession(db)
    cards = loadCards(db, session)
    print(session)
    print(cards)
    card = Card(0,"Poo","Pee",None,None,1, 1)
    insertCard(db, card)
    card.id = 1
    card.question = "SHITTERD"
    saveCards(db, [card])










