import sys
import random
from enum import Enum

def rps(name='gustplayer'):    
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class rps(Enum):
            ROCK=1
            PAPER =2
            SCISSORS = 3
        print("   ")
        playerchoice = input(
            f"hello {name}, enter...\n1 for Rock,\n2 for paper, \n3 for scissors:\n\n"
            )

        if playerchoice not in ["1","2","3"]:
            print(f"{name} please enter valid number!")
            return play_rps()
        player = int(playerchoice)

        comp_chose = random.choice("123")


        comp = int(comp_chose)

        print("")
        print(f"{name},you've choosed {str(rps(player)).replace("rps.", "").title()}.")    
        print(f"python choosed {str(rps(comp)).replace("rps.", "").title()}.") 

        def decide_winner(player, comp):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and comp == 3:
                
                player_wins += 1
                return f"{name} wons🥳🥳"
            elif player == 2 and comp == 1:
                player_wins += 1
                return f"{name} wons🥳🥳"
            elif player == 3 and comp == 2:
                player_wins += 1
                return f"{name} wons🥳🥳"
            elif player == comp:
                # player_wins += 1
                return "draw"   
            else:
                python_wins += 1
                return "python winns"
        game_result = decide_winner(player,comp)    
        print(game_result)    
        nonlocal game_count
        game_count+=1
        print(f"\nGame Count:{(game_count)}")
        print(f"\n {name}, won: { (player_wins)}")
        print(f"\npython won: {(python_wins)}")
        
        print("\n play again?" )

        while True:
            play_again = input("\nY for yes or \nQ for quit"+" >")   

            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break
        if play_again.lower() == "y":
            return play_rps()
        else:
            print("congrats")
            print("thank you for playing")
            if __name__=="__main__":
                sys.exit(f"Bye {name}!")
            else:
                return             

    return play_rps            


if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="provides a personalized game experiance."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="the name of the person who is playing this game!!!."
    )

    args = parser.parse_args()
    
    rock_paper_scissors= rps(args.name)
    rock_paper_scissors()
  