import random

name = input("What is your name? ")

print("Good Luck ! ", name)

words= ['rainbow', 'computer', 'science', 'programming',
		'python', 'mathematics', 'player', 'condition',
		'reverse', 'water', 'board', 'geeks']
word=random.choice(words)
# print(word)

def hangman():
    turn=10
    guesses=''
    valid_input=set("abcdefghijklmnopqrstuvwxyz")
    while(len(word)>0):
        main=""
        missed=0
        for letter in word:
            if letter in guesses:
                main=main+letter
            else:
                main=main+"_ "
        print("\n",main,"  \n")
        if(main==word):
            print("\nYou Gussed it right! You Won\n")
            break
        guess=input("Enter your guess")
        if guess in valid_input:
            guesses=guesses+guess
            
        else:
            print("Enter the valid input")
            continue
        
        if guess not in word:
            turn=turn-1
            if(turn==9):
                print("you have 9 turn left")
                print("\n-----------------------")
            if(turn==8):
                print("You have 8 turn left")
                print("\n-----------------------")
                print("          0            ")
            if(turn==7):
                print("You have 7 turn left")
                print("\n-----------------------")
                print("          0            ")
                print("          |            ")
            if(turn==6):
                print("You have 6 turn left")
                print("\n-----------------------")
                print("          0            ")
                print("        __|__            ")
                print("       |  |  |           ")
                print("          |              ")
            if(turn==5):
                print("You have 5 turn left")
                print("\n-----------------------")
                print("          0            ")
                print("        __|__            ")
                print("       |  |  |           ")
                print("          |              ")
                print("         / \             ")
            if(turn==4):
                print("You have 4 turn left")
                print("\n-----------------------")
                print("          0 __          ")
                print("        __|__            ")
                print("       |  |  |           ")
                print("          |              ")
                print("         / \             ")
            if(turn==3):
                print("You have 3 turn left")
                print("\n-----------------------")
                print("          0 __|           ")
                print("        __|__            ")
                print("       |  |  |           ")
                print("          |              ")
                print("         / \             ")
            if(turn==2):
                print("You have 2 turn left")
                print("\n-----------------------")
                print("          0 __|           ")
                print("        __|__            ")
                print("       |  |  |           ")
                print("          |              ")
                print("         / \             ")
            if(turn==1):
                print("You have 1 turn left")
                print("\n-----------------------")
                print("          0 __|   Bacha lo!!!!!!        ")
                print("          |            ")
                print("       __/|\__             ")
                print("          |              ")
                print("         / \             ")
            if turn==0:
                print("You Loose!,No chance left ")
                break
hangman()


    
