# Game with Python

# Print first text
print("Welcome To Escaping The Dungeon!")

# Input player info
playerName = input("What is your name? ")
playerGender = input("What is your gender? (man or female) ").lower()

# Gender input handling
if playerGender == "man":
    print("Let's play, man!")

elif playerGender == "female":
    print("Let's play, woman!")

else:
    print("Invalid gender input, proceeding with the game.")

# Input player age
playerAge = input("What is your age? ")

# Initialize player stats
playerLevel = 0
playerLife = 100
enemyNames = ["a", "b", "c", "d", "e"]

# Welcome player
print(f"Welcome {playerName} to Escaping the Dungeon. You were imprisoned by some {enemyNames[0]}.")
print(f"You are about to be eaten by {enemyNames[0]}.")

# Start the game
ans = input("Are you ready to play? (yes/no) ").lower()
if ans == "yes":
    print(f"You are starting with {playerLife} health and {playerLevel} Level.")
    print(f"Lucky you! The prison gate was left unlocked. You manage to escape and find a sleeping {enemyNames[1]}.")
    
    # Player's choice on encountering an enemy
    ans = input("What would you do? (Walk past him - type 'wph' or Walk around him - type 'wah'): ").lower()
    
    if ans == "wph" or ans == "walk past him":
        print(f"The {enemyNames[1]} woke up and put you back in prison.")
    
    elif ans == "wah" or ans == "walk around him":
        print(f"You successfully sneaked past the {enemyNames[1]}.")
        print(f"You find a man in a cell asking for help to escape.")
        
        # Player's choice on helping
        ans = input("Would you help him? (yes or no) ").lower()
        if ans == "yes":
            print(f"The man tells you that the guard, {enemyNames[1]}, has the key.")
            print("Their weak spot is on top of their head, but they have a strong sense of smell.")
        elif ans == "no":
            print("You decided to move on.")
    else:
        print("Invalid choice, game continues.")

elif ans == "no":
    print("Game Ended.")

print("Code Ended.")
