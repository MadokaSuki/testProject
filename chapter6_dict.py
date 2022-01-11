import time

alien_list = [{'color': 'red', 'points': 5},
              {'color': 'green', 'points': 10},
              {'color': 'yellow', 'points': 20}]
kill_list = [{'color': 'red', 'numbers': 3},
             {'color': 'green', 'numbers': 4},
             {'color': 'blue', 'numbers': 1},
             {'color': 'yellow', 'numbers': 5}]

start = time.perf_counter()
score = 0
for kill in kill_list:
    for alien in alien_list:
        if kill['color'] == alien['color']:
            score += alien['points'] * kill['numbers']
        continue
print(score)
end = time.perf_counter()
print(end - start)

# 一个计算击杀外星人获得分数的案例

favorite_languages = {
    'jen': ['C', 'python'],
    'nico': ['C++'],
    'maki': ['go'],
    'Richard': ['java', 'c', 'python'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is:" + "\n\t" + languages[0].title())
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())

cities = {
    'Dalian': {
        "country": 'China',
        "population": 5000000,
        "feature": 'beautiful seaside and delicious seafood'
    },
    'Tokyo': {
        "country": 'Japan',
        "population": 35000000,
        "feature": 'fully developed with all kinds of devices'
    },
}

for cityname, city_info in cities.items():
    print('\nCityname :' + cityname)
    countries = city_info['country'];
    populations = city_info['population']
    features = city_info['feature']
    print('\tCountry : ' + countries)
    print('\tPopulation : ' + str(populations))
    print('\tFeature : ' + features)

active = True
while active:
    message = input('请输入： ')

    if message == 'quit':
        active = False
    else:
        print(message)

# 使用布尔变量作为标志

unconfirmed_users = ['piglet', 'pray', 'bang', 'ruler', 'jackeylove', 'lwx']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)
print(confirmed_users)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'rat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)


