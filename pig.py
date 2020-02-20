from random import choice
player_score = 0
computer_score = 0


class Game:
    def __init__(self):
        pass

    def start(self):
        start_game = input("Enter 'start' to roll your first dice ")
        if start_game == "start":
            print("")
            Dice(0).roll_player()
        else:
            Game().start()

    def reset(self):
        global player_score
        global computer_score
        reset_game = input("Enter 'reset' to restart the game and roll your first dice. Enter anything else to exit ")
        if reset_game == "reset":
            player_score = 0
            computer_score = 0
            print("")
            Dice(0).roll_player()


class Dice:
    def __init__(self, temp_score):
        self.temp_score = temp_score
        self.faces = {"PIG!": 1, "Two": 2, "Three": 3,
                      "Four": 4, "Five": 5, "Six": 6}

    def roll_player(self):
        face = choice(list(self.faces.items()))
        Player(self.temp_score, face).play()

    def roll_computer(self):
        face = choice(list(self.faces.items()))
        Computer(self.temp_score, face).play()


class Player:
    def __init__(self, temp_score, face):
        self.temp_score = temp_score
        self.face = face

    def play(self):
        global player_score
        if self.face[1] == 1:
            print(f"You rolled a {self.face[0]} | Your permanent score is still {player_score} | Lose turn")
            print("")
            Dice(0).roll_computer()
        else:
            self.temp_score = self.temp_score + self.face[1]
            print(f"You rolled a {self.face[0]} | Your current temporary score is {self.temp_score}")
            choice = input("Enter 'roll' to roll again, or enter 'pass' to pass your turn ")
            if choice == "roll":
                Dice(self.temp_score).roll_player()
            elif choice == "pass":
                player_score = player_score + self.temp_score
                print(f"Your permanent score is {player_score}")
                print("")
                if player_score >= 100:
                    print("YOU WIN!")
                    print("YOU WIN!!")
                    print("YOU WIN!!!")
                    print("")
                    Game().reset()
                else:
                    Dice(0).roll_computer()
            else:
                print("Please enter a valid command")
                print("")
                Player(self.temp_score - self.face[1], self.face).play()


class Computer:
    def __init__(self, temp_score, face):
        self.temp_score = temp_score
        self.face = face

    def play(self):
        global computer_score
        if self.face[1] == 1:
            print(f"The computer rolled a {self.face[0]} | the computer's permanent score is still {computer_score} | your turn")
            print("")
            start_turn = input("Enter 'roll' to start your turn again and roll the dice ")
            if start_turn == "roll":
                    Dice(0).roll_player()
            else:
                print("Please enter a valid command")
                print("")
                Computer(self.temp_score, self.face)
        else:
            print(f"The computer rolled a {self.face[0]}")
            self.temp_score = self.temp_score + self.face[1]
            if self.temp_score <= 20:
                Dice(self.temp_score).roll_computer()
            else:
                computer_score = computer_score + self.temp_score
                print(f"The computer passed | Their permanent score is {computer_score}")
                print("")
                if computer_score >= 100:
                    print("The computer wins!")
                    print("")
                    Game().reset()
                else:
                    start_turn = input("Enter 'roll' to start your turn again and roll the dice ")
                    if start_turn == "roll":
                        Dice(0).roll_player()

        
Game().start()