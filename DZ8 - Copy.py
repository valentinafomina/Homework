from random import sample, choice

dump = []


def call_number():
    current_number = choice(range(1, 90))
    while current_number in dump:
        current_number = choice(range(1, 90))
    dump.append(current_number)
    print(f"Новый бочонок {current_number}")
    return current_number


class Card:

    def __init__(self):
        self.card = []
        self.data = sample(range(1, 90), 15)
        self.data.sort()
        self.bingo_count = 0

    def make_card(self, name):
        self.user_name = name
        numbers = iter(self.data)

        def make_card_line():
            empty_card_line = " " * 9
            empty_cell = [i for i in range(9)]
            sam = sample(empty_cell, 5)
            sam.sort()
            lst = list(empty_card_line)
            for ind in sam:
                lst[ind] = next(numbers)
            self.card.append(lst)

        for _ in range(3): make_card_line()

    def show_card(self):
        print(f"Карточка игрока {self.user_name}")
        print("_" * 35)
        for line in self.card:
            print("\t".join(str(elem) for elem in line))
        print("_" * 35)

    def check_number(self, number):
        for line in self.card:
            i_cell = 0
            for cell in line:
                if cell == x:
                    line[i_cell] = "-"
                    self.bingo_count += 1
                    return True
                i_cell += 1
        return False

    def is_winner(self):
        return self.bingo_count == 15


player_card = Card()
player_card.make_card("Player")

computer_card = Card()
computer_card.make_card("Computer")

while not player_card.is_winner() and not computer_card.is_winner():
    print("\n"*25)
    x = call_number()
    player_card.show_card()
    computer_card.show_card()

    user_answer = input(f"Игрок 1, хотите зачеркнуть число в вашей карте, y/n?")
    if user_answer == "y":
        if not player_card.check_number(x):
            print("Вы проиграли! Такого числа нет в вашей карточке!")
            exit(0)
    else:
        if player_card.check_number(x):
            print("Вы проиграли! Такое число есть в вашей карточке!")
            exit(0)

    computer_card.check_number(x)
if player_card.is_winner() and computer_card.is_winner():
    print("Ничья! Игра закончена")
elif player_card.is_winner():
    print("Поздравляем! Вы победили!")
else:
    print("Вы проиграли!")
