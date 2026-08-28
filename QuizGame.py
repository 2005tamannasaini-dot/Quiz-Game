# Quiz Game Project

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

score = 0
for quiz in questions:
    print(quiz["question"])

    for index, option in enumerate(quiz["options"] , start=1):
        print(f"{index}. {option}")

    user_input = input("Your Answer:")

    select_option = quiz["options"][int(user_input) - 1] 

    if select_option == quiz["answer"]:
        print (" Correct Anwere. ✅!")
        score += 1

    else:
        print(" Your Answer is wrong. ❌")    
        print("Correct Answer:",quiz["answer"])

    print()        
