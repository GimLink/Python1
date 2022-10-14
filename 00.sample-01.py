import random 

random_number = random.randint(1,100)

#print(random_number)

gamecount = 1

while True:

    try:
        

        mynumber = int(input("1~100 사이 숫자를 입력하시오."))

        if mynumber > random_number:
            print('Down')
        elif mynumber < random_number:
            print('Up')
        else:
            print('축하합니다. {gamecount}번 만에 맞추셨습니다.')
            break

        gamecount += 1