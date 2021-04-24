import random

count = 0
source = 0
while count < 10:
    print(count)
    k1 = random.randint(0, 100)
    k2 = random.randint(0, 100)
    print("k1 is {}, k2 is {}\n".format(k1, k2))
    answer = ""
    while not isinstance(answer, int):
        answer = int(input("k1+k2 is ? input your answer"))
        if int(answer) == int(k1 + k2):
            print("True")
            count += 10
            print("total is {}".format(answer))
        else:
            print("Flase")
            print("答案是:{}".format(k1+k2))
