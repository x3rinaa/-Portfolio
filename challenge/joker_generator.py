import random
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Joke categories
jokes = {
    "Python": [
        "Why do Python programmers prefer snakes?\nBecause they're afraid of camelCase.",
        "Why do Python developers prefer dark mode?\nBecause light attracts bugs.",
    ],
    "JavaScript": [
        "Why was the JavaScript developer sad?\nBecause he didn't know how to 'null' his feelings.",
        "How do you comfort a JavaScript bug?\nYou console it.",
    ],
    "General": [
        "Why don't programmers like nature?\nIt has too many bugs.",
        "Why did the programmer quit his job?\nBecause he didn't get arrays.",
        "How many programmers does it take to change a light bulb?\nNone. It's a hardware problem.",
        "What's the object-oriented way to become wealthy?\nInheritance.",
        "Why did the developer go broke?\nBecause he used up all his cache.",
        "What do you call a programmer from Finland?\nNerdic.",
        "Why do programmers always mix up Halloween and Christmas?\nBecause Oct 31 == Dec 25.",
        "What's the difference between a programmer and a non-programmer?\nThe non-programmer thinks a kilobyte is 1000 bytes.",
        "Why did the programmer get stuck in the shower?\nBecause the instructions on the shampoo said: Lather, Rinse, Repeat.",
        "What do you call a programmer who doesn't comment their code?\nA future job security specialist.",
        "Why don't programmers like to go outside?\nThe sunlight causes syntax errors.",
        "What's a programmer's favorite hangout place?\nThe Foo Bar.",
        "Why did the programmer name their dog 'Value'?\nSo it can return.",
        "What's a programmer's favorite snack?\nChips and dip (and salsa)."
    ]
}

def display_joke(category=None):
    print("\n" + "="*50)
    print(Fore.CYAN + "  Here's your programming joke:")
    print("="*50)
    
    if category and category in jokes:
        joke = random.choice(jokes[category])
    else:
        all_jokes = sum(jokes.values(), [])
        joke = random.choice(all_jokes)

    print(Fore.YELLOW + joke)
    print("="*50)

def main_menu():
    while True:
        print("\nChoose a category or action:")
        print("1. Python Jokes")
        print("2. JavaScript Jokes")
        print("3. General Programming Jokes")
        print("4. Random Joke")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_joke("Python")
        elif choice == "2":
            display_joke("JavaScript")
        elif choice == "3":
            display_joke("General")
        elif choice == "4":
            display_joke()
        elif choice == "5":
            print(Fore.GREEN + "\nThanks for laughing with us! Goodbye!\n")
            sys.exit()
        else:
            print(Fore.RED + "Invalid choice. Please enter a number from 1 to 5.")

        rate = input(Fore.MAGENTA + "\nRate this joke from 1 to 5 (or press Enter to skip): ")
        if rate.strip().isdigit():
            print(Fore.GREEN + "Thanks for your feedback!\n")

if __name__ == "__main__":
    main_menu()