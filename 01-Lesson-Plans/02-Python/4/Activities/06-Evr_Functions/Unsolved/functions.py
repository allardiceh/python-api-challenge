def hello(name, role):
    print(f"Hello {name}. You are a {role}")

def square(number):
    squared = int(number) * int(number)
    return squared

result = square("6")
# print(result)

def sum(numbers):
    total = 0
    for num in numbers:
        print('current total', total)
        total = total + num
        print('new total', total)

    return total

# def sum(numbers ,offset):
#     total = 0
#     for num in numbers:
#         total = total + num

#     return total

result = sum([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(result)