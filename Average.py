howManyEntered = 0
total = 0
average = 0
howMany = int(input('How many numers do you want to enter? '))

while howManyEntered < howMany:
    testscore = float(input('Enter test score: '))
    total= total +testscore
    howManyEntered = howManyEntered + 1

average = total/howMany
print("The average for the test scores you entered is:",average)

