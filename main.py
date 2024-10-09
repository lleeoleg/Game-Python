from game.game import Game

def main() -> None:
    game = Game.create_game()
    game.start()

if __name__ == "__main__":
    main()