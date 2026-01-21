#ROCK-PAPER-SCISSORS
import random
print("Game_ON-kiddo")
print("Welcome to the Game!")

rock =    "Rock_🪨     = 0"
paper =   "Paper_📜   = 1"
scissor = "scissor_✂️  = 2"
print(f"{rock}\n{paper}\n{scissor}")
print("Enter 1, 2, or 0 to continue. Enter 3 or more to quit.")

#score-tracking
user_score = 0
computer_score = 0
draws = 0

#user_choice
while True:
    user_input = int(input("Your choice : "))

    if (user_input == 0):
        print("You have opted for Rock_🪨 ")
    elif (user_input == 1 ):
        print(f"hey,you have opted for Paper_📜")
    elif (user_input == 2 ):
        print("hey,you have opted for scissor_✂️")
    else:
        print("hey,you have exited the game,check the game score")
        break
    
#computer choice
    computer_attack = random.randint(0,2)
    print("wait for computers's Decision")
    if (computer_attack == 0):
        print(f"hahaa,computer have opted for Rock_🪨 ")
    elif (computer_attack ==  1):
        print(f"hahaa,computer have opted for Paper_📜 ")
    elif (computer_attack == 2):
        print("hahaa,computer have opted for scissor_✂️ ")
    
#Game-Result:
    print("Decision on going")
    if (user_input == computer_attack):
        print("🤝 It's a draw! Great minds think alike")
        print("Clash of titans! But neither falls... yet. ⚔️")
        draws += 0
    
    elif(user_input == 2 and computer_attack==0):
        print("Roasted! That was too easy, you lost")
        computer_score += 1

    elif (user_input == 0 and computer_attack ==2):
        print("You win! 🥳 That’s some sharp thinking!")
        user_score += 1

    elif (user_input<computer_attack):
        print("Error 404: Victory not found—for you.")
        computer_score += 1
    
    elif (user_input>computer_attack):
        print("Boom! The AI just took a nap, you won 🙂‍↔️")
        user_score += 1
print(f"\n📊 Scoreboard:")
print(f"👨 You: {user_score} | 🤖 Computer: {computer_score} | ⚖️ Draws: {draws}\n")