import random

symbols = {'r': '🪨', 'p': '📃', 's': '✂️'}
choices = ['r', 'p', 's']

while True:
    ch = input("Rock, Paper or Scissors? (r/p/s):: ").lower()
    
    if ch not in choices:
        print("Invalid choice! Try again.\n")
        continue

    cmp_choice = random.choice(choices)

    print(f"\nYou chose {symbols[ch]}")
    print(f"Computer chose {symbols[cmp_choice]}")

    if ch == cmp_choice:
        print("It's a TIE!")
    elif (ch == 'r' and cmp_choice == 's') or \
         (ch == 's' and cmp_choice == 'p') or \
         (ch == 'p' and cmp_choice == 'r'):
        print("You WIN! 🎉")
    else:
        print("You LOSE! 💀")
    
    should_continue = input("\nContinue...? (y/n):: ").lower()
    if should_continue == 'n':
        print("Thanks for playing! 👋")
        break
