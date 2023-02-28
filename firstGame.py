# Game with Python

# Print first text
print("Welcome To Escaping The Dungeon!")

# input player info

playerName = input("What is your name? ")
playerGender = input("What is your gender? (man or female) ")

# gender prevention
if playerGender == " man":
    print("Let's play man")


elif playerGender == "female":
    print("Let's play woman")


else:
    playerAge = input("What is your age? ")
playerLevel = 0
playerLive = 100
enemyName = ["a", "b", "c", "d", "e"]
# Hello player
print("Welcome", playerName, "to the Escaping the Dungeon. You were imprisoned by some ",
      enemyName[0], ". You are about to be eaten by couples ", enemyName[0], ".")

ans = input("Are you ready to play? (yes/no) ").lower()
if ans == "yes":
    print("You are starting with ", playerLive, "health", playerLevel, "Level")
    print("Lucky, The prison's gate was let unlocked from the preview guide. You were able to escape the prison. You find  one ",
          enemyName[1], "sound as sleep. What would you do? ")
    ans = input(
        "What would you do ? (Walk pass him (type: wph) or Walk around him (type: wah))").lower()
    if ans == "walk pass him" or "wph":
        print("The enemy woke up and put you back into the prison")
    elif ans == "walk around him" or "wah":
        print("You were able to escape the enemy")
        print("You found yourself by a prison' cell where a young man was asking you for your help to also escape the prison")
        ans == input(
            "Would you help him (type: yes or no) ").lower()
        if ans == "yes":
            print("The young man said the guard by your prison's cell has the key to my cell. The guard is ",
                  enemyName[1], "There are weak located on top of their head. They are very good with smell.")
        elif ans == "no":
            print("Next step")
elif ans == "no":
    print("Game Ended")
print("code ended")
