import shutil

BOLD = '\033[1m'
END = '\033[0m'

terminal_width = shutil.get_terminal_size().columns

text = "Test users skills"

formatted_text = f"{BOLD}{text}{END}"
centered_formatted_text = formatted_text.center(terminal_width + len(BOLD) + len(END))

print(centered_formatted_text)

First_Name = input(f"\033[1mFirst Name:")
Last_Name = input(f"\033[1mLast Name:")

print(f"\033[1m\033[4mInstructions\033[0m: Fill in the blank spaces\n")

print(f"Hello {First_Name} {Last_Name} I am Fosso Mirenda a FullStack developer\n")
response = input(f"Thank you to have followed my courses, now you are going to answer to the following questions to test your skills\n Are you ready for the course (YES or NO):")

if response.upper() == "YES":
    questions = {
        "1. What is a correct syntax to output \033[1mHello World in Python?": "print('Hello World')",
        "2. How do you insert COMMENTS in Python code?": "#",
        "3. How do we define variables in python?": "my_var = twat",
        "4. How do you create a variable with the numeric value 5?": "x = 5",
        "5. What is the file extension for Python files?": ".py",
        "6. How do you create a variable with the floating number 2.8?": "x = 2.8",
        "7. What is the correct syntax to output the type of a variable or object in Python?": "type()",
        "8. What is the correct way to create a function in Python?": "def function_name():",
        "9. In Python, 'Hello', is the same as \"Hello\"": "Yes",
        "10. What is a correct syntax to return the first character in a string?": "string[0]",
        "11. Which method can be used to remove any whitespace from both the beginning and the end of a string?": "strip()",
        "12. Which method can be used to return a string in upper case letters?": "upper()",
        "13. Which operator is used to multiply numbers?": "*",
        "14. Which operator can be used to compare two values?": "==",
        "15. How to represent list in python": "[\"apple\", \"kiwi\"]",
        "16. How to represent a SET in python?": "{\"apple\", \"kiwi\"}",
        "17. How to represent a DICTIONARY in python?": "{\"apple\" : \"green\", \"kiwi\" : \"fruit\"}",
        "18. Which collection is ordered, changeable, and allows duplicate members?": "list",
        "19. Which collection does not allow duplicate members?": "set",
        "20. How do you start writing an if statement in Python?": "if x > y:",
        "21. How do you start writing a while loop in Python?": "while x > y:",
        "22. How do you start writing a for loop in Python?": "for x in range(y):",
        "23. Which statement is used to stop a loop in Python?": "break",
    }

    def conduct_questions():
        score = 0
        user_answers = []
        incorrect_answers = []

        question_list = list(questions.keys())
        correct_answer_list = list(questions.values())

        for i, question in enumerate(question_list):
            user_answer = input(f"\n{question}\nYour answer: ")
            user_answers.append(user_answer)

            if user_answer.lower().strip() == correct_answer_list[i].lower().strip():
                score += 1
            else:
                incorrect_answers.append({
                    "question": question,
                    "user_answer": user_answer,
                    "correct_answer": correct_answer_list[i]
                })

        print("\n--- Quiz Finished ---\n")
        print(f"[1mYour final score is: \033[1m{score}/{len(questions)}\033[0m 📝")

        if incorrect_answers:
            corrections_prompt = input("You have some incorrect answers. Would you like to see the corrections? (YES or NO): ")
            if corrections_prompt.upper() == "YES":
                print("\n--- Corrections ---")
                for item in incorrect_answers:
                    print(f"\n{item['question']}")
                    print(f"Your answer: {item['user_answer']} ❌")
                    print(f"Correct answer: {item['correct_answer']} ✅")
            else:
                print("Okay, no problem. You can review the course materials for a refresher!")
        else:
            print("Great job! You answered all the questions correctly. 💯")

    conduct_questions()

else:

    print("\nOkay, we'll start when you are ready.")
