key = 'my_var'
value = 1.234

formatted = f'{key} = {value}'
print(formatted)

formatted = f'{key!r:<10} = {value:.2f}'
print(formatted)

places = 3
number = 1.23456
print(f'My number is {number:.{places}f}')

