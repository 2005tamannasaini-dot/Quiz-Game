# Quiz Game Project

import random
questions = [
            {"question" : "Python kis type ki language hai?",
             "options" : ["Programming language", "Markup language", "Database", "Operating system"] ,
             "answer"  : "Programming language",
             "explanation": "Python ek high-level programming language hai.",
             "difficulty": "Easy",
              "Category"  : "Python"},

            {"question" : "Python me function banane ke liye kaunsa keyword use hota hai?",
             "options" : ["func", "def", "function", "define"],
             "answer"  : "def",
             "explanation": "Python me function define karne ke liye def keyword use hota hai.",
             "difficulty": "Easy",
              "Category"  : "Programming"},

             {"question" : "Python me list kaunse brackets me banti hai?",
              "options" : ["()", "{}", "[]", "<>"],
              "answer"  : "[]",
              "explanation": "Python me list square brackets [] ke andar banayi jati hai.",
              "difficulty": "Easy",
               "Category"  : "Programming"},

             {"question" : "10 + 5 kitna hota hai?",
              "options" : ["20", "10", "25", "15"],
              "answer"  : "15",
              "explanation": "10 me 5 add karne par result 15 hota hai.",
              "difficulty": "Easy",
              "Category"  : "Mathmatics" },

             {"question" : "Computer me RAM ka full form kya hai?",
              "options" : ["Random Access Memory", "Read Access Memory","Rapid Access Machine", "Random Application Memory"],
              "answer"  : "Random Access Memory",
              "explanation": "RAM ka full form Random Access Memory hai. Ye computer ki temporary memory hoti hai.",
              "difficulty": "Easy",
               "Category" : "Computer Basic"}
]

total_questions= len(questions)
attempt = 0
best_score = 0

while True:

    attempt += 1
    score = 0
    correct_answers = 0
    wrong_answers = 0

    print(f"\n===== Attempt Quiz {attempt} =====")

    random.shuffle(questions)

    for number, quiz in enumerate(questions, start=1):
        
        print(f"\nQuestion {number}/{total_questions}")
        print("difficulty:", quiz["difficulty"])
        print("Category:", quiz["Category"])
        print(quiz["question"])
        
        random.shuffle(quiz["options"])

        for index, option in enumerate(quiz["options"] , start=1):
            print(f"{index}. {option}")
           

        while True:
            try:
                user_input = input("Your Answer:")

                if user_input in ["1", "2", "3", "4"]:
                    select_option = quiz["options"][int(user_input) - 1] 

                    if select_option == quiz["answer"]:
                        print (" Correct Anwere. ✅!")
                        print("Explanation:", quiz["explanation"])
                        score += 1
                        correct_answers += 1

                    else:
                        print(" Your Answer is wrong. ❌")    
                        print("Correct Answer:",quiz["answer"])
                        print("Explanation:", quiz["explanation"])
                        wrong_answers += 1
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
   
    print("\n===== Score Summary =====")
    print(f"Attempt Number: {attempt}")
    print(f"Score: {score}/{total_questions}")
    print(f"Correct Answers: {correct_answers}")
    print(f"Wrong Answers: {wrong_answers}")
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
