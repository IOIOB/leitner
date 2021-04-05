from dataclasses import dataclass

@dataclass(frozen=True)
class Card:
    id: int
    question: str
    answer: str
    colour: str
    image: str
    streak: int
    sessionAsked: int
