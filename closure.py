# closure is  afunction having access to the scope of the parent function
#function after the parent function has retuned

def parent_function(person , coins):
    #coins = 3
    
    def play_game():
        nonlocal coins
        coins -= 1
        
        if coins >1:
            print("\n " + person + "has" + str(coins) + "coins left.")
        elif coins == 1:
            print("\n " + person + "has" + str(coins) + "coin left.")
        else:
            print("\n " + person + "is out of the game")
        
    return play_game
    
tommy = parent_function("tommy",3)
jenny = parent_function("jenny",5)

tommy()
tommy()


jenny()
jenny()


