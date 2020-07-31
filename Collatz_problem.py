print("Problem Collatza")
import random
try:
    number = int(input())
except ValueError:
    print("Należy podawać tylko liczby całkowite")
#number = random.randint(1,20000)
#print(number)

def collatz(number):
    if number %2 == 0:
        print(number // 2)
        return number // 2

    elif number %2 == 1:
        result = 3 * number + 1
        print(result)
        return result

while number != 1:
    number = collatz(int(number))
#collatz(number)