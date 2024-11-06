class Game:
    def __init__(self, message):
        print(f"{message}")
        pass

    def score(self, player):
        match player:
            case "player1":
                pass
            case "player2":
                pass
            case _:
                print("Invalid player")


welcome_message = "Hello, let's play!"
game = Game(welcome_message)

# Init


def init():
    pass
