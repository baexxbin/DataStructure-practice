import random

min, max = 0, 99
answer = random.randint(0,99)

for i in range (1,10):
    # print("범위: %d~%d" %(min,max))
    guess = int(input("숫자를 입력하세요 (범위: %d~%d): " % (min,max)))
    if guess == answer:
        print("딩동댕, 정답입니다! %d번 만에 맞췄습니다!" % i)
        break
    elif guess < answer:
        print("땡, 더 큰 숫자입니다!")
        min = guess
    elif guess > answer:
        print("땡, 더 작은 숫자입니다!")
        max = guess

print("게임이 끝났습니다 :)")
