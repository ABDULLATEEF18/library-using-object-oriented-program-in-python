import random
## a python program that randomly generates 10 math problems for the user to solve
## at the end it prints the ones missed with answers
## complex shit, lets go.
## no it should always be 10 questions
### continue to build and add more functionality
def main():  
    trials = 10
    level = get_level()
    while trials > 0:
        final_score = 0
        x, y, z = numbers(level)
        #x, y, z = same.split()
        final_answer = calculate_answer(x, y, z)
        #print(final_score)
        user_answer = int(input(f"{x} {y} {z} = "))
        #print(user_answer)
        if final_answer == user_answer:
            print("yes")
            final_score = final_score + 1
            print(final_score)
            trials -= 1
        else:
            trials -= 1
    print(f"your final score of the test is {final_score}/10")

def numbers(level):
    list = ['+','*']
    if level == 1:
        x = random.randint(1, 10)
        y = random.choice(list)
        z = random.randint(1, 10)
    elif level == 2:
        x = random.randint(10, 20)
        y = random.choice(list)
        z = random.randint(10, 20)
    elif level == 3:
        x = random.randint(20, 30)
        y = random.choice(list)
        y = random.randint(20, 30)
    return x, y, z
    
def calculate_answer(x, y, z):
    if y == '+':
        return x + z
    #elif y == '-':
        return x - z
    #elif y == '/':
        return x / z
    elif y == '*':
        return x * z
def get_level():
    while True:
        n = int(input("what level are you willing to play: "))
        if n >= 1 or n <= 3:
            return n
        

main()
