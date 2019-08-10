def question(prompt, hint, answer):
    '''
    prompt - string
    hint - string
    answer - string
    '''
    while True: 
        response = input(prompt)
        if response is "?":
            print(hint)
        elif response is not None:
            print(answer)
            break

##### Quiz: Stats edition #####

print("For each question, type your response, then press ENTER to proceed; this triggers the answer to each open-ended quesiton. Type '?' to trigger a hint.\n\n")

q1 = question("Question", "Hint", "Answer")

q2 = question("Question", "Hint", "Answer")

q3 = question("Question", "Hint", "Answer")

q4 = question("Question", "Hint", "Answer")

q5 = question("Question", "Hint", "Answer")

