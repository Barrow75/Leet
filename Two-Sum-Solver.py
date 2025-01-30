
numbers = []

user_input = int(input("How many numbers: "))

for i in range(user_input):
    num = int(input("Enter a number "))
    numbers.append(num)
print(numbers)

target = int(input("What is the target sum you want to get? "))

for i in range(1, len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(f"{numbers[i]} and {numbers[j]} = {target}")

            
