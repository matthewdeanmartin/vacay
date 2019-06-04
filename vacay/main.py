"""
General idea- a game that plays like a lotto game- not a lot of input. You can run many games in parallel,
the state of the game is *you*, i.e. your own wallet, etc.

"""
import random

from vacay.worlds import cities


from vacay.game_class import Game

if __name__ == "__main__":
    def run():
        game = Game()
        game.go()


    run()
