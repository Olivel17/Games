# def print_valid_cities(all_cities, used_cities):
#     diff = all_cities.difference(used_cities)
#     for city in diff:
#         print(city)
#
# def add_cities(all_cities, new_cities):
#     for city in new_cities:
#         all_cities.add(city)
#
# new_cities = [
#     'Екатеринбург',
#     'Выборг' ,
#     'Владивосток',
#     'Казань',
#     'Why',
#     'Йезд'
# ]
#
# all_cities = {
#     'Абакан',
#     'Астрахань',
#     'Бобруйск',
#     'Калуга',
#     'Караганда',
#     'Кострома',
#     'Липецк',
#     'Новосибирск'
# }
#
# used_cities = {
#     'Калуга',
#     'Абакан' ,
#     'Новосибирск'
# }
#
#
#
# add_cities(all_cities, new_cities)
# print_valid_cities(all_cities, used_cities)
# print()

def get_together_games(anfisa_games, alisa_games):
    together = anfisa_games.union(alisa_games)
    return together

anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]

together_games = get_together_games
for game in together_games:
    print(game)