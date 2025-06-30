import random
stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]
list = ["alia","walia","samim"]

lives = 6
chosen_word = random.choice(list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)



game_over = False
correct_letters = []
while not game_over:
    guess = input("enter a letter ?")
    
    display =""
    for letter in chosen_word:
        if letter == guess:
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter 
        else:
            display += "_"
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        if lives ==0:
            game_over = True
            print("you lose")
    
    if "_" not in display:
        game_over = True
        print("you win")
    print(stages[lives])    
        
