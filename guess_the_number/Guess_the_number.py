import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    count = 0
    while (count!=3 or random_number==guess):
        print(f"\nYou have {3-count} chances left")
        guess = int(input(f"Guess the number between 1 and {x}\n"))
        count+=1
        if(guess==random_number):
            print("\nAmazing, you guessed it!!")

        elif(guess>random_number):
            print("\nA little smaller")
            hint = input('Do you need any hint, then type "YES"')
            if(hint == "YES"):
                num = random_number%10
                print(f"The last digit is {num}")
            else:
                print("As you wish")

                
        else:
            print("\nA little larger")
            hint = input('Do you need any hint, then type "YES"')
                        
            if(hint == "YES"):
                num = random_number%2
                print(f"The last digit is {num}")
            else:
                print("As you wish")
               
    print(f"\nThe number was {random_number}")              
                
guess(100)                
