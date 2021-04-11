import sys
import random

def main():
        questions = {"Who is the author of \"The Little Prince\"": "Antoine de Saint-Exupéry",
                             "What is the capital city of Turkey": "Ankara",
                             "Who is the creator of Facebook?": "Mark Zuckerberg",
	             "How many hours are there in a day?": "24",
                             "How many days are there in a week?": "7",
                             "How many days are there in a year?": "365",
                             "What is 2 times 2?": "4",
                             "Who is the creator of Microsoft?": "Bill Gates",
                             "Who is the creator of Apple?": "Steve Jobs",
                             "What is the square of 2?": "4"}

        score = 0
        correctAnswers = 0

        for i in range(len(questions)):
                #Pick a random question then delete it.
                question, answer = random.choice(list(questions.items()))
                del questions[question]
                
                print(f"Question {i+1})", question)
                userAnswer = input("Answer: ")

                #Check if the answer is correct.
                if(userAnswer == answer):
                        print("Correct.")
                        score += 10
                        correctAnswers += 1
                else:
                        print("Wrong")

        #Endgame message.
        wasUserSuccessful = "Congratulations! You did a very good job." if correctAnswers > 5 else "You need to study more."
        print(f"You answered {correctAnswers} question(s) correctly. Your score is {score}.\n" + wasUserSuccessful)

        #Play again
        playAgain = input("Would you like to play again?(y/n) ")

        if(playAgain == "y"):
                main()
        else:
                sys.exit()

if __name__ == "__main__":
        print("Welcome to my knowledge competition game. \nIn this game, you are going to answer 10 questions.\n" 
	  "You will be considered successful if you answer more than 5 questions correctly and unsuccessful otherwise. Also one final thing, answers are case sensitive, so be careful.\n"
	  "Here comes your first question.")

        main()


