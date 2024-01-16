print("Welcome to this quiz game!")

playing = input("Do you want to play? ")

if playing.lower()!="yes":
    quit()
print("Good - let's go!")
score = 0

# Q1
answer = input("What is 1+1? ")
if answer == "2":
    print("Good - correct!")
    score = score + 1
else:
    print("Wrong!")

# Q2
answer = input("What is 3*3? ")
if answer == "9":
    print("Good - correct!")
    score = score + 1
else:
    print("Wrong!")

# Q3
answer = input("2*8? ")
if answer == "16":
    print("Good - correct!")
    score = score + 1
else:
    print("Wrong!")

# Q4
answer = input("9*9? ")
if answer == "81":
    print("Good - correct!")
    score = score + 1
else:
    print("Wrong!")

print("Your total score out of 4Qs was:")
print(score)
print("In % terms:")
print(score/4*100)

