from model import *


def main():
    leo = FootballPlayer("Leo", "Messi", 910, 450)
    cristiano = FootballPlayer("Crictiano", "Ronaldo", 840, 300)
    alex = FootballPlayer("Alex", "Del Piego", 750, 800)
    ivan = FootballPlayer("Ivan", "Ivanov")

    players = (leo, cristiano, alex, ivan)

    player = Manager. give_golden_ball(players)
    print(player)

if __name__ == "__main__":
    main()