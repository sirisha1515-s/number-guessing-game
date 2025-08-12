import random
print("🎯 Welcome to the number guessing Game")
print("Think of a number between 1 to 100")
difficulty=input("Choose difficulty(easy/hard): ").lower()
if difficulty=="easy":
    attempts=10
else:
    attempts=5
secrete_number=random.randint(1,100)
for attempt in range(attempts):
    guess=int(input("Make a guess"))
    
    if guess==secrete_number:
        print("🎉 You guessed it right")
        print("YOU WON🎊")
        break
    elif guess > secrete_number:
        print("Too High")
    else:
        print("Too Low")
    print(f"You have {attempts - (attempt + 1)} attempts left.\n")
else:
    print(f"😢 You've run out of attempts! The number was {secrete_number}.")
