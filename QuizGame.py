# Quiz Game Project

import random
questions = [
            {"question" : "Python kis type ki language hai?",
             "options" : ["Programming language", "Markup language", "Database", "Operating system"] ,
             "answer"  : "Programming language",
             "explanation": "Python ek high-level programming language hai."},

            {"question" : "Python me function banane ke liye kaunsa keyword use hota hai?",
             "options" : ["func", "def", "function", "define"],
             "answer"  : "def",
             "explanation": "Python me function define karne ke liye def keyword use hota hai."
},

             {"question" : "Python me list kaunse brackets me banti hai?",
              "options" : ["()", "{}", "[]", "<>"],
              "answer"  : "[]",
              "explanation": "Python me list square brackets [] ke andar banayi jati hai."},

             {"question" : "10 + 5 kitna hota hai?",
              "options" : ["20", "10", "25", "15"],
              "answer"  : "15",
              "explanation": "10 me 5 add karne par result 15 hota hai."},

             {"question" : "Computer me RAM ka full form kya hai?",
              "options" : ["Random Access Memory", "Read Access Memory","Rapid Access Machine", "Random Application Memory"],
              "answer"  : "Random Access Memory",
              "explanation": "RAM ka full form Random Access Memory hai. Ye computer ki temporary memory hoti hai."}
]

attempt = 0

while True:

    attempt += 1
    score = 0
    correct_answers = 0
    wrong_answers = 0

    print(f"\n===== Attempt Quiz {attempt} =====")

    random.shuffle(questions)

    for number, quiz in enumerate(questions, start=1):
        
        print(f"\nQuestion {number}/{len(questions)}")
        print(quiz["question"])

        random.shuffle(quiz["options"])

        for index, option in enumerate(quiz["options"] , start=1):
            print(f"{index}. {option}")
           

        while True:
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

    print("Quiz Complete!")        
    print("Your final score:", score)
    print("Total questions:", len(questions))
    print("Correct Question:", correct_answers)
    print("Wrong Question:", wrong_answers )

    percentage = (score / len(questions) * 100)
    if percentage >= 80:
        print("Excellent! 🎉")
    elif percentage >= 50:
        print("Good job! 👍")
    else:
        print("Keep practicing! 💪")
    print(f"Your percentage: {percentage:.0f}% ")

    correct_rate = (correct_answers / len(questions)*100)
    print(f"correct answer rate: {correct_rate:.0f}%")

    while True:
        choose = input("continue? (yes/no):").lower()

        if choose == "yes":
            break

        elif choose == "no":
                print("Quiz Game closed. ")
                exit()
                
        else:
            print(" Please! choose Input Yes or No")        
