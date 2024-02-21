import random
random.randint(20,30)
jackpot = random.randint(20,30)
guess = int(input("chal guess kar :"))
counter = 1
while guess !=jackpot:
    if guess < jackpot:
        print("Guess Lower")
    guess = int(input("Chal Guess kar"))
    counter +=1
print("Sahi Jawab")
print("You took",counter,"attempt")