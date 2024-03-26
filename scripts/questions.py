import random

puzzles = {
    "2, 4, 6, 8, ____": "10",
    "10, 20, 30, 40, ____": "50",
    "1, 4, 9, 16, ____": "25",
    "3, 6, 9, 12, ____": "15",
    "5, 10, 15, 20, ____": "25",
    "Apple, Banana, Orange, Carrot, Pineapple": "Carrot",
    "Chair, Table, Sofa, Desk, Bed": "Bed",
    "Dog, Cat, Rabbit, Cow, Fish": "Cow",
    "Monday, Tuesday, Wednesday, January, Thursday": "January",
    "Guitar, Piano, Drum, Violin, Elephant": "Elephant",
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "Which planet is known as the Red Planet?": "Mars",
    "What is the chemical symbol for water?": "H2O",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "AB, BC, CD, DE, ____": "EF",
    "1, 4, 9, 16, 25, ____": "36",
    "A, E, I, O, ____": "U",
    "2, 4, 8, 16, 32, ____": "64",
    "Sun, Moon, Stars, Galaxy, ____": "Universe",
    "Cat, Dog, Horse, Snake, Cow": "Snake",
    "Blue, Green, Red, Chair, Yellow": "Chair",
    "Circle, Square, Triangle, Rectangle, Oval": "Oval",
    "Earth, Mars, Jupiter, Pluto, Sun": "Sun",
    "Carrot, Tomato, Potato, Apple, Banana": "Apple",
    "What 5-letter word becomes shorter when you add two letters to it?": "Short",
    "What has a neck but no head?": "Bottle",
    "What can travel around the world while staying in a corner?": "Stamp",
    "What can you catch but not throw?": "Cold",
    "What has keys but can't open locks?": "Piano",
    "What comes next in the sequence: 1, 4, 9, 16, 25, ____?": "36",
    "What comes next in the sequence: 2, 4, 8, 16, 32, ____?": "64",
    "What is half of 30, plus 10?": "25",
    "If you have 5 apples and you give away 3, how many do you have left?": "2",
    "What is the sum of the first 10 prime numbers?": "129",
    "TAP, RAT, CAR, ART, ____ (Hint: A type of bird)": "PARROT",
    "ACT, CAT, TAC, SAT, ____ (Hint: A type of fish)": "CATFISH",
    "MEAT, TEAM, MATE, TAME, ____ (Hint: A type of fruit)": "DATE",
    "STAR, RATS, ARTS, TSAR, ____ (Hint: A type of planet)": "MARS",
    "LISTEN, SILENT, ENLIST, INLETS, ____ (Hint: A type of weather)": "TINSEL",
    "A farmer has 17 sheep, and all but 9 die. How many are left?": "9",
    "How many months have 28 days?": "All",
    "If you’re running in a race and you pass the person in 2nd place, what place are you in?": "2nd",
    "If you have 3 apples and you take away 2, how many do you have?": "1",
    "If you multiply me by any other number, the answer will always be the same. What am I?": "0",
    "What is the next number in the sequence: 1, 11, 21, 1211, 111221?": "312211",
    "What is the value of π (pi) rounded to five decimal places?": "3.14159",
    "How many birthdays does the average person have?": "1",
    "Moon + Night = _____": "Stars",
    "Rain + Umbrella = _____": "Dry",
    "Winter + Snow = _____": "Cold",
    "Book + Pages = _____": "Reading",
    "Ocean + Waves = _____": "Beach",
}


def ask_random_question():
    global puzzles
    # Select a random item from the dictionary
    question, answer = random.choice(list(puzzles.items()))

    # Print the question
    print(question)

    # Get the user's input
    user_input = input("Your answer: ")

    # Compare the user's input with the answer
    if user_input.lower() == answer.lower():
        return True
    else:
        return False


print(ask_random_question())
