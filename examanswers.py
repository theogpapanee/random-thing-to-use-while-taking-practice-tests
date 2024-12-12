econ302exam1answers = {
    1: "C",
    2: "C",
    3: "C",
    4: "B",
    5: "D",
    6: "B",
    7: "C",
    8: "A",
    9: "A",
    10: "D",
    11: "D",
    12: "B",
    13: "D",
    14: "A",
    15: "A",
    16: "C",
    17: "A",
    18: "C",
    19: "C",
    20: "D",
    21: "A",
    22: "A"
}

econ302exam2answers = {
    1: "D",
    2: "C",
    3: "A",
    4: "A",
    5: "D",
    6: "D",
    7: "B",
    8: "C",
    9: "C",
    10: "E",
    11: "B",
    12: "D",
    13: "A",
    14: "B",
    15: "C",
    16: "C",
    17: "D",
    18: "D",
    19: "B",
    20: "C",
    21: "A",
    22: "D",
    23: "B",
    24: "D"
}

# # Iterator for the dictionary
# answers_iterator = iter(answers.items())

# def next_answer():
#     try:
#         question, answer = next(answers_iterator)
#         print(f"The answer for {question} is {answer}")
#     except StopIteration:
#         print("No more questions!")

# Simulating terminal input
answers = econ302exam2answers
correct = 0
wrong = []
while True:
    command = input("Type question + answer (or 'quit' to exit): ").strip().lower().split()
    try:
        if int(command[0]) in answers:
            if int(command[1].lower() == answers[int(command[0])].lower()):
                correct += 1
                print(f"correct! answer for {command[0]} is indeed {command[1]}")
            else:
                wrong.append(command[0])
                print(f"WRONG!!! answer for {command[0]} is {answers[int(command[0])]}")
    except:
        print("do something breh")
        if command[0] == "quit":
            print(f"final score = {(correct)/(correct + len(wrong)) * 100}%")
            print("wrong answers were", wrong)
            print("Exiting.")
            break
    # elif command != "quit":
    #     next_answer()
    # elif command == "quit":
    #     print("Exiting.")
    #     break
    # else:
    #     print("Invalid command. Type 'next' or 'quit'.")
