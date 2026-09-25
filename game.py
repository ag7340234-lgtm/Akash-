import random

print("🎮 NUMBER GUESSING GAME")
print("1 se 10 ke beech number guess karo!")

secret = random.randint(1, 10)

guess = int(input("Tumhara guess: "))

if guess == secret:
    print("🎉 Wah! Sahi guess!")
else:
    print("❌ Galat!")
    print("Sahi number tha:", secret)