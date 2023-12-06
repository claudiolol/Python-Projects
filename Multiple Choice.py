def main():
    num = int(input())
    responses = []
    answers = []
    for i in range(num):
        answers.append(input())
    for i in range(num):
        responses.append(input())
   # print(answers)
  #  print(responses)
    correct = 0
    for j in range(len(responses)):
        if(responses[j] == answers[j]):
            correct += 1
    print(correct)
main()