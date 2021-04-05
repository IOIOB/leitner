from dataclasses import dataclass

@dataclass
class Card:
    id: int
    question: str
    answer: str
    colour: str
    image: str
    streak: int
    sessionAsked: int

    def __iter__(self):
        return iter(
            [value for key, value in self.__dict__.items() ])
