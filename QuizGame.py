# Quiz Game Project

import random
questions = [
            {"question" : "Python kis type ki language hai?",
             "options" : ["Programming language", "Markup language", "Database", "Operating system"] ,
             "answer"  : "Programming language"},

            {"question" : "Python me function banane ke liye kaunsa keyword use hota hai?",
             "options" : ["func", "def", "function", "define"],
             "answer"  : "def"},

             {"question" : "Python me list kaunse brackets me banti hai?",
              "options" : ["()", "{}", "[]", "<>"],
              "answer"  : "[]"},

             {"question" : "10 + 5 kitna hota hai?",
              "options" : ["20", "10", "25", "15"],
              "answer"  : "15"},

             {"question" : "Computer me RAM ka full form kya hai?",
              "options" : ["Random Access Memory", "Read Access Memory","Rapid Access Machine", "Random Application Memory"],
              "answer"  : "Random Access Memory"}
]

attempt = 0

while True:

    attempt += 1
    score = 0

    print(f"\n===== Attempt Quiz {attempt} =====")

    random.shuffle(questions)

    for number, quiz in enumerate(questions, start=1):
        
        print(f"\nQuestion {number}/{len(questions)}")
        print(quiz["question"])

        for index, option in enumerate(quiz["options"] , start=1):
            print(f"{index}. {option}")
           

        while True:
            user_input = input("Your Answer:")

            if user_input in ["1", "2", "3", "4"]:
                select_option = quiz["options"][int(user_input) - 1] 

                if select_option == quiz["answer"]:
                    print (" Correct Anwere. ✅!")
                    score += 1

                else:
                    print(" Your Answer is wrong. ❌")    
                    print("Correct Answer:",quiz["answer"])
                break

            else:
                print("Please! choose the Input 1 to 4.")
            print()    

    print("Quiz Complete!")        
    print("Your final score:", score)
    print("Total questions:", len(questions))

    percentage = (score / len(questions) * 100)
    if percentage >= 80:
        print("Excellent! 🎉")
    elif percentage >= 50:
        print("Good job! 👍")
    else:
        print("Keep practicing! 💪")
    print(f"Your percentage: {percentage:.0f}% ")

    while True:
        choose = input("continue? (yes/no):").lower()

        if choose == "yes":
            break

        elif choose == "no":
                print("Quiz Game closed. ")
                exit()
                
        else:
            print(" Please! choose Input Yes or No")        
