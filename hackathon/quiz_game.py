#this is a simple python quiz game
# This is a simple Python multiple choice quiz game

def run_quiz():
    score = 0
    print("Welcome to the Quiz Game!\n")

    # Question 1
    print("1. What does the print() function do in Python?")
    print("A. Prints output to the screen")
    print("B. Reads input from the user")
    print("C. Saves data to a file")
    answer = input("Your answer (A/B/C): ")
    if answer.lower() == "a":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is A.\n")

    # Question 2
    print("2. Who directed the movie 'Jurassic Park'?")
    print("A. James Cameron")
    print("B. Steven Spielberg")
    print("C. Christopher Nolan")
    answer = input("Your answer (A/B/C): ")
    if answer.lower() == "b":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is B.\n")

    # Question 3
    print("3. What is the largest planet in our solar system?")
    print("A. Earth")
    print("B. Jupiter")
    print("C. Mars")
    answer = input("Your answer (A/B/C): ")
    if answer.lower() == "b":
        print("Correct!\n")
        score += 1
    else:
        print("Incorrect. The correct answer is B.\n")

    # Final score
    print("Your final score is:", score, "out of 3")

if __name__ == "__main__":
    thank_you = input("Would you like to play the quiz game? (yes/no): ")
    if thank_you.lower() == "yes":
        run_quiz()