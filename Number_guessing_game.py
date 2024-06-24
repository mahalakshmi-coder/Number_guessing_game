import logo_art
import random

def no_guess(attempts,i):
    if attempts-i!=0:
        print('guess again')    
        return(f'You have {attempts-i} attempts remaining to guess the number')
    else:
        return("You are out of guesses...You lose!!!")

def easy_hard(choose_num,attempts):
    print("You have ",attempts," attempts remaining to guess the number!")
    for i in range(1,attempts+1):
        guess = int(input('make a guess'))
        if guess > choose_num:
            print("Your guess is too high")
            print(no_guess(attempts,i))
        elif guess < choose_num:
            print("Your guess is too low")
            print(no_guess(attempts,i))
        else:
            print("Your guess is right..The answer was ",choose_num)
            break

print(logo_art.logo)
print("Let me think of a number between 1 to 50.")

choice = "Y"
while(choice == "Y"):
    num_list = list(range(51))
    choose_num = random.choice(num_list)
    level = input("Choose level of difficulty...Type 'easy' or 'hard': ").lower().strip()
    if level == 'easy':
        easy_hard(choose_num,attempts=10)
    elif level == 'hard':
        easy_hard(choose_num,attempts=5)
    else:
        print("you've entered wrong input, try again")
        continue
    choice =input("Do you want to play again(Y/N)?:").upper().strip()



