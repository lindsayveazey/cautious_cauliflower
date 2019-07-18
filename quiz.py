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

##### Quiz #####

print("For each question, type your response, then press ENTER to proceed; this triggers the answer to each open-ended quesiton. Type '?' to trigger a hint.\n\n")

q1 = question("Here is q1.", "Here is hint 1.", "Here is answer 1.")
q2 = question("Here is q2.", "Here is hint 2.", "Here is answer 2.")

