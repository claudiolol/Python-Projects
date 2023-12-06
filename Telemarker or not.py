def main():

    numbers = []
    for i in range(4):
        numbers.append(int(input("Print four numbers:")))
   # print(numbers)
    if(numbers[0] == 8 or numbers[0] == 9):
        print("Ignore")
    elif(numbers[3] == 8 or numbers[3] == 9):
        print("Ignore")
    elif(numbers[1] == numbers[2]):
        print("Ignore")
    else:
        print("Answer")
main()