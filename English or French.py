def EnglishorFrench(s):
    tCount = 0
    sCount = 0
    for i in s.lower():
        if(i == "t"):
            tCount += 1
        if(i == "s"):
            sCount += 1
    if(sCount > tCount):
        print("French")
    if(tCount > sCount):
        print("English")
    if(tCount == sCount):
        print("French")
def main():
    num = int(input("num"))
    s = ""
    for i in range(num):
        s += input("sentence")
    EnglishorFrench(s)
main()