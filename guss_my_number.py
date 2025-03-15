import sys
import random

def rnum(name):
    gamecout = 0
    player_wins = 0
    
    def playgame():
        nonlocal name
        nonlocal gamecout
        nonlocal player_wins
        
        print(" ")
        print(f"========== hello {name} welcome to my guss my number game!==========")
        playerchoice = input(
            f"{name},guss the number I'am thinking of ...1, 2 or 3\n>"
        )
        if playerchoice not in ["1","2","3"]:
            print(f"{name} please choose a correct number!")
            return playgame()
        
        player = int(playerchoice)
        
        computer = random.choice("123")
        
        comp = int(computer)
        
        print(f"{name.capitalize()}, you've choosed==>{str(player)} ")
        print(f"I was thinking about ==> {str(comp)}")
        
        def decide_winner(player,comp):
            nonlocal player_wins
            if player == comp:
                player_wins += 1
                return "You got me! 🎉🎉"
            else:
                return "Computer wins"
        gameresult = decide_winner(player,comp)
        print(gameresult)
        
        nonlocal gamecout
        gamecout +=1
        win_percentage = (player_wins / gamecout) * 100
        print(f"\n Game Count:{(gamecout)}")
        print(f"\n {name} won :{(player_wins)} games")
        print(f"\n Your winning percentage :{(win_percentage)}%")
        
        print("\n play again?" )

        while True:
            play_again = input("\nY for yes or \nQ for quit"+" >")   

            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break
        if play_again.lower() == "y":
            return playgame()
        else:
            print("congrats")
            print("thank you for playing")
            if __name__=="__main__":
                sys.exit(f"Bye {name}!")
            else:
                return        

    return playgame

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
    
    Gusse_my_number = rnum(args.name)
    Gusse_my_number()