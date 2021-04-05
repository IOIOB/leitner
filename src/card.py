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

    def __str__(self):
        return (
            f"Card:\n"
            f"  id:\n\t{self.id}\n"
            f"  question:\n \t{self.question}\n"
            f"  answer:\n\t{self.answer}\n"
            f"  colour:\n\t{self.colour}\n"
            f"  image:\n\t{self.image}\n"
            f"  streak:\n\t{self.streak}\n"
            f"  sessionAsked:\n\t{self.sessionAsked}\n")
