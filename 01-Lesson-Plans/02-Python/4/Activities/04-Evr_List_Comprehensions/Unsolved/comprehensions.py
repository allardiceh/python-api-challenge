# @TODO: Your code here
# numbers = [1, 2, 3, 4, 5]

# newNumberList = []
# for num in numbers:
#     newNumberList.append(num + 1)

# print(numbers)
# print(newNumberList)

# compNumbers = [num + 1 for num in numbers]

# print('compNumber', compNumbers)

temperatures = [40, 54, 69, 28, 90, 99]

hotDays = []
for temp in temperatures:
    if temp > 80:
        hotDays.append(temp)

print('hot days', hotDays)

hotDaysComp = [temp for temp in temperatures if temp > 80]
floatHotdays = [float(temp) for temp in hotDaysComp]

print('hot days comp', floatHotdays)