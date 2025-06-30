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
      #This creates an empty string called placeholder
word_length = len(chosen_word)    #This calculates the length of the secret word (how many letters it contains)
for position in range(word_length):
     placeholder += "_" 
:#For every iteration, it adds one underscore _ to the placeholder string.So, if word_length is 4, the loop runs 4 times, appending _ each time
   
print(placeholder) #____



game_over = False #False means “not true” or “the game is not over yet.”
correct_letters = [] #It’s assigned an empty list ([]).
while not game_over:
    guess = input("enter a letter ?")
    
    display =""
    for letter in chosen_word: #Loops through each letter in the secret word (chosen_word).
        if letter == guess:
            correct_letters.append(guess)
            #If the current letter matches the player's latest guess, add that guessed letter to the correct_letters list.
        elif letter in correct_letters#If the current letter has already been guessed before (exists in correct_letters), add that letter to display.
            display += letter 
        else:
            display += "_"#If the letter has not been guessed yet, add an underscore (_) to display.
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
        
        
