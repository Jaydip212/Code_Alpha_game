import random  

# Word list  
words = ["python", "hangman", "developer", "challenge", "github"]  

# Random word select  
word = random.choice(words)  
guessed_word = ["_"] * len(word)  
attempts = 6  
guessed_letters = []  

print("Welcome to Hangman Game!")  

while attempts > 0 and "_" in guessed_word:  
    print("\nWord:", " ".join(guessed_word))  
    print(f"Attempts left: {attempts}")  
    guess = input("Guess a letter: ").lower()  

    if len(guess) != 1 and not guess.isalpha():  
        print("Invalid input. Enter a single letter.")  
        continue  

    if guess in guessed_letters:  
        print("You already guessed that letter.")  
        continue  

    guessed_letters.append(guess)  

    if guess in word:  
        for i in range(len(word)):  
            if word[i] == guess:  
                guessed_word[i] = guess  
    else:  
        attempts -= 1  
        print("Incorrect guess!")  

if "_" not in guessed_word:  
    print("\nCongratulations! You guessed the word:", word)  
else:  
    print("\nGame Over! The word was:", word)