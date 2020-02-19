from random import choice
player_score = 0
computer_score = 0


class Game:
    def __init__(self):
        pass

    def start(self):
        start_game = input("enter 'start' to roll your first dice ")
        if start_game == "start":
            print("Game Started!")
            Dice(0, 0).roll()
        else:
            Game().start()


class Dice:
    def __init__(self, temp_score, perm_score):
        self.temp_score = temp_score
        self.perm_score = perm_score
        self.faces = {"PIG!": 1, "Two": 2, "Three": 3,
                      "Four": 4, "Five": 5, "Six": 6}

    def roll(self):
        face = choice(list(self.faces.items()))
        Player(self.temp_score, self.perm_score, face[1]).play()
        pass


class Player:
    def __init__(self, temp_score, perm_score, face):
        self.temp_score = temp_score
        self.perm_score = perm_score
        self.face = face

    def play(self):
        global player_score
        if self.face == 1:
            print(f"you rolled a {self.face}, lose turn")
            print(f"your permanent score is still {player_score}")
        else:
            print(f"you rolled a {self.face}")
            self.temp_score = self.temp_score + self.face
            print(f"Your current temporary score is {self.temp_score}")
            choice = input(
                "enter 'roll' to roll again, or enter 'pass' to pass your turn ")
            if choice == "roll":
                Dice(self.temp_score, self.perm_score).roll()
            elif choice == "pass":
                player_score = player_score + self.temp_score
                print(f"your permanent score is {player_score}")


class Computer:
    def __init__(self,):
        pass


class Mechanics:
    def __init__(self):
        pass


# Dice().roll()
# Player(0, 0, 3).play()
# Player(3, 0, 6).play()

Game().start()
