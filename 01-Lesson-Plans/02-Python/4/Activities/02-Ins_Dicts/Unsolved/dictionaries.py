me = {
    "firstName": "Michael",
    "lastName": "Dinh",
    "age": 26,
    "isHungry": True,
    "hobbies": ['cooking', 'baking', 'sleep'],
    "address": {
        "state": 'NC',
        "zip": 27006
    }
}



me['favoriteFood'] = ['Pizza']

# key = input('What do you want to know? ')

me['favoriteFood'].append('Fried Chicken')

for key in me:
    print(key, me[key])
