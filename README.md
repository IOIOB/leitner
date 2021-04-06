# leitner

This is a skeleton app which can be used from the command line, though it is made to be intergated into a graphical application. 
It emulates the [Leitner system](https://en.wikipedia.org/wiki/Leitner_system) of spaced learning,
which consists of a box filled with cards.

Cards have the following properties:
- **Id:** Unique identifier
- **Question:** The question, on the 'front' of the card
- **Answer:** The answer, on the 'back' of the card
- **Colour:** Colour string, optional
- **Image:** Image string, optional
- **Streak:** Tells you how many times in a row the card was answered correctly
- **SessionAsked:** Tells you the last session when the question was asked

When you want to learn a fact, you take a card, you write the question on the front, the answer on the back,
you write '1' as the streak, and the current day (we are assuming one session happens per day) as the SessionAsked.

Each day, you go through the cards. If the sessions since they were last asked is equal to their streak, you take them out of the box
and put them in front of you.
(for example, today is session 12, the card streak is 3, and it was last asked on (i.e. its sessionAsked is) session 9. 12 - 9 = 3,
so you take put it in front of you).

Then, for each card in front of you, ask yourself the question, then check the answer. If it was correct, increment the card's streak,
else set it to 0. In either case, replace the sessionAsked with today's session.

When you go through all the cards, put them back in the box. The session is over, repeat it tomorrow.

## Doing this with the program

If you are using the program from the command line, there are two files which you will be using, main.py and cardUtils.py.

#### cardutils.py

If you run cardUtils.py (```python3 cardutils.py```), you will be asked

```
You can list/add/modify/delete
What to do:
```
- Entering 'list' will simply list out all the cards, including all of their properties. 
- 'add' will prompt you to enter the question, answer, colour, and image properties, from which it will construct a new card and add it to the database ('box').
- 'modify' will ask you for an id, then a property, and finally the value. 
Then it will set the select the card with a matching id and set the selected property to the new value.
- Finally, 'delete' will ask you for an id, then delete the card with the matching id from the database.

#### main.py

Running main.py, it will automatically retrieve the correct cards from the database and present them to you, then ask you the questions,
let you check the answers, and tell the program if you got it right or not. After running through all the cards it will automatically
save everything to the database. It also increments the session counter automatically.
