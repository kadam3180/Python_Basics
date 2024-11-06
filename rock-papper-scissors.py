class Game:
    def __init__(self, message):
        self.score1 = 0
        self.score2 = 0
        self.round = 0
        print(f"{message}")

    def score(self, player):
        match player:
            case "player1":
                self.round += 1
                self.score1 = self.score1 + 1
                print(self.score1)
                pass
            case "player2":
                self.round += 1
                self.score2 = self.score2 + 1
                print(self.score2)
            case _:
                print("Invalid player")


def is_game_over() -> bool:
    # 2nd round and a player has 2 points
    if self.round == 2 and abs(self.score1 - self.score2):
        return True


welcome_message = "Hello, let's play!"
game = Game(welcome_message)


game.score("player1")
# Init


def init():
    pass
