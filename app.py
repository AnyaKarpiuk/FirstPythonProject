# request a name
name = input('Print your name: ')

# compare name's length
if len(name) <= 3:
    print('We are sorry!')
    print('Name must be at least 4 characters')
    print(f'Name {name} has {len(name)} characters')
elif len(name) > 15:
    print('We are sorry!')
    print('Name must be maximum 15 characters')
    print(f'Name {name} has {len(name)} characters')
else:
    print(f'Thank you, {name}')



