from random import randint


def predict() -> str:
    a = randint(1, 5)
    if a == 1:
        return "предсказываю вам сегодня удачный день"
    elif a == 2:
        return "сегодня вам надо быть внимательнее"
    elif a == 3:
        return "⎛⎝( ` ᢍ ´ )⎠⎞ᵐᵘʰᵃʰᵃ"
    elif a == 4:
        return "рядом предатель ඞ ඞ ඞ ඞ ඞ ඞ ඞ"
    else:
        return "погладь сегодня кота ᓚᘏᗢ"


def main():
    print(predict())