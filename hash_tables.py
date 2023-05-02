voted = {}


def check_voter(name):
    value = voted.get(name)
    if voted.get(name):
        return f'Kick them out!'
    else:
        voted[name] = True
        return f'Let them vote!'


print(check_voter('Tom'))
print(check_voter('Mike'))
print(check_voter('Tom'))
