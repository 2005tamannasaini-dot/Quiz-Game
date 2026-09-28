# Quiz Game Project

import random
questions = [
            {
                "question" : "Python kis type ki language hai?",
                "options" : ["Programming language", "Markup language", "Database", "Operating system"] ,
                "answer"  : "Programming language",
                "explanation": "Python ek high-level programming language hai.",
                "difficulty": "Easy",
                "Category"  : "Python"},

            {
                "question": "Python me variable banane ke liye kya zaroori hai?",
                "options": ["Data type declare karna", "Sirf variable name likhna", "Variable ko value assign karna", "Function banana"],
                "answer": "Variable ko value assign karna",
                "explanation": "Python me variable ko value assign karke banaya ja sakta hai.",
                "difficulty": "Easy",
                "Category": "Python"},

            {
                "question": "Python me output dikhane ke liye kaunsa function use hota hai?",
                "options": ["input()", "display()", "print()", "output()"],
                "answer": "print()",
                "explanation": "Python me screen par output dikhane ke liye print() function use hota hai.",
                "difficulty": "Easy",
                "Category": "Python"},

            {
                "question": "Python me user se input lene ke liye kaunsa function use hota hai?",
                "options": ["get()", "input()", "scan()", "read()"],
                "answer": "input()",
                "explanation": "Python me user se value lene ke liye input() function use hota hai.",
                "difficulty": "Easy",
                "Category": "Python"
            },

            {
                "question": "Python me comment likhne ke liye kaunsa symbol use hota hai?",
                "options": ["//", "#", "/*", "--"],
                "answer": "#",
                "explanation": "Python me single-line comment ke liye # symbol use hota hai.",
                "difficulty": "Easy",
                "Category": "Python"
            },

            {
                "question" : "Python me function banane ke liye kaunsa keyword use hota hai?",
                "options" : ["func", "def", "function", "define"],
                "answer"  : "def",
                "explanation": "Python me function define karne ke liye def keyword use hota hai.",
                "difficulty": "Easy",
                "Category"  : "Programming"},

            {
                "question": "Python me tuple kaunse brackets me banti hai?",
                "options": ["[]", "{}", "()", "<>"],
                "answer": "()",
                "explanation": "Python me tuple normally round brackets () me banayi jati hai.",
                "difficulty": "Easy",
                "Category": "Programming"
            },

            {
                "question": "Python me dictionary kis brackets ka use karti hai?",
                "options": ["[]", "{}", "()", "<>"],
                "answer": "{}",
                "explanation": "Python me dictionary curly brackets {} ka use karti hai.",
                "difficulty": "Easy",
                "Category": "Programming"
            },

            {
                "question": "Python me loop ke liye kaunsa keyword use hota hai?",
                "options": ["loop", "repeat", "for", "iterate"],
                "answer": "for",
                "explanation": "Python me sequence par iteration ke liye for loop use kiya jata hai.",
                "difficulty": "Easy",
                "Category": "Programming"
            },    

            {
                "question" : "Python me list kaunse brackets me banti hai?",
                "options" : ["()", "{}", "[]", "<>"],
                "answer"  : "[]",
                "explanation": "Python me list square brackets [] ke andar banayi jati hai.",
                "difficulty": "Easy",
                "Category"  : "Programming"},

            {
                "question" : "10 + 5 kitna hota hai?",
                "options" : ["20", "10", "25", "15"],
                "answer"  : "15",
                "explanation": "10 me 5 add karne par result 15 hota hai.",
                "difficulty": "Easy",
                "Category"  : "Math" },

            {
                "question": "20 - 8 kitna hota hai?",
                "options": ["10", "12", "14", "16"],
                "answer": "12",
                "explanation": "20 me se 8 subtract karne par result 12 hota hai.",
                "difficulty": "Easy",
                "Category": "Math"
            },

            {
                "question": "6 × 7 kitna hota hai?",
                "options": ["36", "42", "48", "54"],
                "answer": "42",
                "explanation": "6 ko 7 se multiply karne par result 42 hota hai.",
                "difficulty": "Easy",
                "Category": "Math"
            },

            {
                "question": "81 ÷ 9 kitna hota hai?",
                "options": ["7", "8", "9", "10"],
                "answer": "9",
                "explanation": "81 ko 9 se divide karne par result 9 hota hai.",
                "difficulty": "Easy",
                "Category": "Math"
            },

            {
                "question": "15 + 25 kitna hota hai?",
                "options": ["30", "35", "40", "45"],
                "answer": "40",
                "explanation": "15 me 25 add karne par result 40 hota hai.",
                "difficulty": "Easy",
                "Category": "Math"
            },

            {
                "question" : "Computer me RAM ka full form kya hai?",
                "options" : ["Random Access Memory", "Read Access Memory","Rapid Access Machine", "Random Application Memory"],
                "answer"  : "Random Access Memory",
                "explanation": "RAM ka full form Random Access Memory hai. Ye computer ki temporary memory hoti hai.",
                "difficulty": "Easy",
                "Category" : "Computer"},


            {
                "question": "CPU ka full form kya hai?",
                "options": ["Central Processing Unit", "Computer Processing Unit", "Central Program Unit", "Computer Program Utility"],
                "answer": "Central Processing Unit",
                "explanation": "CPU ka full form Central Processing Unit hai. Ye computer ke instructions ko process karta hai.",
                "difficulty": "Easy",
                "Category": "Computer"
            },

            {
                "question": "Computer me data permanently store karne ke liye kya use hota hai?",
                "options": ["RAM", "Keyboard", "Hard Disk", "Monitor"],
                "answer": "Hard Disk",
                "explanation": "Hard Disk data ko long-term ya permanently store karne ke liye use hoti hai.",
                "difficulty": "Easy",
                "Category": "Computer"
            },

            {
                "question": "Keyboard ka use kis liye kiya jata hai?",
                "options": [ "Data enter karne ke liye", "Sound sunne ke liye", "Video dekhne ke liye", "Internet connect karne ke liye"],
                "answer": "Data enter karne ke liye",
                "explanation": "Keyboard ka use text, numbers aur commands enter karne ke liye kiya jata hai.",
                "difficulty": "Easy",
                "Category": "Computer"
            },

            {
                "question": "Operating System ka example kaunsa hai?",
                "options": ["Windows", "Python", "Google", "Keyboard"],
                "answer": "Windows",
                "explanation": "Windows ek operating system hai jo computer ke hardware aur software resources ko manage karta hai.",
                "difficulty": "Easy",
                "Category": "Computer"
},
]

total_questions= len(questions)
attempt = 0
best_score = 0


categories = ["Python", "Programming", "Computer", "Math"]

print("\n===== Quiz Categories =====")

for index, category in enumerate(categories, start=1):
    print(f"{index}. {category}")

while True:
    try: 
        category_choice = int (input("choose a category: "))

        if 1 <= category_choice <= len(categories):
            selected_category = categories[category_choice - 1]
            print(f"\nSelected Category: {selected_category}")

            category_questions = [
                quiz for quiz in questions
                if quiz["Category"] == selected_category 
            ]

            total_questions = len(category_questions)

            if total_questions == 0:
                print("No questions available in this category.")
            else:
                break
        else:
            print("Please choose a valid category.")

    except ValueError:
        print("Please enter a number.")

difficulties = ["Easy", "Medium", "Hard"]        

print("\n===== Quiz Difficulty =====")

for index, difficulty in enumerate(difficulties, start=1):
    print(f"{index}. {difficulty}")

while True:
    try:
        difficulty_choice = int(input("Choose difficulty: ")) 

        if 1 <= difficulty_choice <= len(difficulties):
            selected_difficulty = difficulties[difficulty_choice - 1]   
            print(f"\nSelected Difficulty: {selected_difficulty}")

            filtered_questions = [
                quiz for quiz in category_questions
                if quiz["difficulty"] == selected_difficulty
            ]        

            total_questions = len(filtered_questions)

            if total_questions == 0:
                print("NO questions available for this difficulty.")
            else:
                break

        else:
            print("Please choose a valid difficulty.")

    except ValueError:
        print("Please enter a number.")             
while True:

    attempt += 1
    score = 0
    correct_answers = 0
    wrong_answers = 0
    questions_attempted = 0

    print(f"\n===== Attempt Quiz {attempt} =====")

    random.shuffle(filtered_questions)

    for number, quiz in enumerate(filtered_questions, start=1):
        
        print(f"\nQuestion {number}/{total_questions}")
        print("difficulty:", quiz["difficulty"])
        print("Category:", quiz["Category"])
        print(quiz["question"])
        
        random.shuffle(quiz["options"])

        for index, option in enumerate(quiz["options"] , start=1):
            print(f"{index}. {option}")
           

        while True:
            try:
                user_input = input("Your Answer (1-4 or s to skip):").lower()

                if user_input == "s":
                    print("Question skipped. ⏭️")
                    break

                elif user_input in ["1", "2", "3", "4"]:
                    select_option = quiz["options"][int(user_input) - 1] 

                    if select_option == quiz["answer"]:
                        print (" Correct Anwere. ✅!")
                        print("Explanation:", quiz["explanation"])
                        score += 1
                        correct_answers += 1
                        questions_attempted += 1

                    else:
                        print(" Your Answer is wrong. ❌")    
                        print("Correct Answer:",quiz["answer"])
                        print("Explanation:", quiz["explanation"])
                        wrong_answers += 1
                        questions_attempted += 1
                    break

                else:
                    print("Please! choose the Input 1 to 4.")
                print()  
            except ValueError:
                print("Please enter a number.")        
             

    print("Quiz Complete!") 

    if score > best_score:
        best_score = score       
    
    percentage = (score / total_questions * 100)
    if percentage >= 80:
        print("Excellent! 🎉")
    elif percentage >= 50:
        print("Good job! 👍")
    else:
        print("Keep practicing! 💪")

    unanswered_questions = total_questions - questions_attempted   
   
    print("\n===== Score Summary =====")
    print(f"Attempt Number: {attempt}")
    print(f"Category: {selected_category}")
    print(f"Score: {score}/{total_questions}")
    print(f"Questions Attempted: {questions_attempted}")
    print(f"Correct Answers: {correct_answers}")
    print(f"Wrong Answers: {wrong_answers}")
    print(f"Unanswered Questions: {unanswered_questions}")
    print(f"Percentage: {percentage:.0f}%")
    print(f"Best Score: {best_score}/{total_questions}")

    while True:
        choose = input("continue? (yes/no):").lower()

        if choose == "yes":
            print("\nStarting a new quiz attempt... 🔄")
            break

        elif choose == "no":
            print("Quiz Game closed. ")
            exit()
                
        else:
            print(" Please! choose Input Yes or No")        
