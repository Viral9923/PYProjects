import random;

WIN1 = 36;
WIN2 = 5;
NUM = 10;

for i in range(NUM):
    num = random.randint(10,40);
    if num==WIN1 or num== WIN2:
        print(num);
        print("You won 10$");
    
    