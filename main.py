import random
from words import word_list
def words():
    word=random.choice(word_list)
    return  word.upper()
def play(word):
    correct_words = "_" * len(word)
    guessed=False
    guessed_letters = []
    guessed_words = []
    tries=6
    print("let's play hangman dear user")
    print(display_hangman(tries))
    print(correct_words)
    print("\n")
    while not guessed and tries>0:
        guess=input("please input your answer").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_words:
                print(" you have already guessed this leter",guess)
            elif guess not in word:
                print(guess ," is not in the word")
                tries-=1
                guessed_letters.append(guess)
            else:
                print("good job",guess,"is the word")
                guessed_letters.append(guess)
                word_as_list=list(correct_words)
                indicies=[i for i,letter in enumerate(word) if letter == guess]
                for index in indicies:
                    word_as_list[index]=guess
                correct_words="".join(word_as_list)
                if "_" not in correct_words:
                    guessed=True

        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you have already guessed the word",guess)
            elif guess != word:
                print(guess, " not the correct word")
                tries-=1
                guessed_words.append(guess)
            else:
                guessed=True
                correct_words=guess

        else:
            print("Not a valid guess")
        print(display_hangman(tries))
        print(correct_words)
        print("\n")
    if guessed :
        print('congrats you guessed the word! you win!!!!!')
    else:
        print("sorry you lost the word was ",word)
def main():
    word=words()
    play(word)
    while input("play again")=="y":
        word=words()
        play(word)

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]



if __name__=="__main__":
    main()








