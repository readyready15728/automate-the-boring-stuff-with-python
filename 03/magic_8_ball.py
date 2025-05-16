import random


def get_answer():
    answers = [
        "It is certain",
        "It is decidely so",
        "Yes",
        "Reply hazy; try again",
        "Ask again later",
        "Concentrate and ask again",
        "My reply is no",
        "Outlook not so good",
        "Very doubtful",
    ]

    return random.choice(answers)


fortune = get_answer()
print(fortune)
