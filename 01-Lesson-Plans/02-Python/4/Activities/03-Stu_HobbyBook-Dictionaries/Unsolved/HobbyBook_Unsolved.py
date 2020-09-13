# @TODO: Your code here
# * Create a dictionary to store the following:

#   * Your name
#   * Your age
#   * A list of a few of your hobbies
#   * A dictionary of a few times you wake up during the week


michael = {
    'name': 'Michael',
    'age': 26,
    'hobbies': ['cooking', 'baking', 'running'],
    'wake-up': {
        'Monday': '6 AM',
        'Tuesday': '6 AM',
        'Saturday': '7 AM'
    }
}

print(michael['name'])
print(michael['age'])
print(michael['hobbies'])

print(michael['wake-up']['Saturday'])