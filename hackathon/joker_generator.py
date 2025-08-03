import random

def joke_generator():
    jokes = [
        "Why don't programmers like nature?\nIt has too many bugs.",
        "How do you tell an introverted computer scientist from an extroverted one?\nThe extroverted one looks at YOUR shoes when talking to you.",
        "Why do Python programmers prefer snakes?\nBecause they're afraid of camelCase.",
        "Why did the programmer quit his job?\nBecause he didn't get arrays.",
        "How many programmers does it take to change a light bulb?\nNone. It's a hardware problem.",
        "Why do Java programmers have to wear glasses?\nBecause they don't C#.",
        "What's the object-oriented way to become wealthy?\nInheritance.",
        "Why did the developer go broke?\nBecause he used up all his cache.",
        "What do you call a programmer from Finland?\nNerdic.",
        "Why do programmers always mix up Halloween and Christmas?\nBecause Oct 31 == Dec 25.",
        "What's the difference between a programmer and a non-programmer?\nThe non-programmer thinks a kilobyte is 1000 bytes.",
        "Why was the JavaScript developer sad?\nBecause he didn't know how to 'null' his feelings.",
        "Why did the programmer get stuck in the shower?\nBecause the instructions on the shampoo said: Lather, Rinse, Repeat.",
        "What do you call a programmer who doesn't comment their code?\nA future job security specialist.",
        "Why do Python developers prefer dark mode?\nBecause light attracts bugs.",
        "How do you comfort a JavaScript bug?\nYou console it.",
        "Why don't programmers like to go outside?\nThe sunlight causes syntax errors.",
        "What's a programmer's favorite hangout place?\nThe Foo Bar.",
        "Why did the programmer name their dog 'Value'?\nSo it can return.",
        "What's a programmer's favorite snack?\nChips and dip (and salsa)."
    ]
    
    print("\n" + "="*40)
    print("  Here's your random programming joke:")
    print("="*40 + "\n")
    print(random.choice(jokes))
    print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    joke_generator()