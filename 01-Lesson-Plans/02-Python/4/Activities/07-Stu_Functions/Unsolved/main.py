# @TODO: Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0
    for number in numbers:
        # total = total + number
        total += number

    # [total := total + number for number in numbers]
    

    return total / length

# Test your function with the following:
print(average([1, 5.5, 9.0]))
# print(average(range(20)))
