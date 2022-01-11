import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj2:
    numbers2 = json.load(f_obj2)

numbers2.append(3)
print(numbers2)


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj3:
            username = json.load(f_obj3)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input('What is your name? ')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back," + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + '!')


greet_user()
