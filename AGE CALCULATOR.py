age = int(input('please enter your age: '))
m = age * 12 
w = m * 4 
d = age * 365 
h = d * 24
months = 1 
weeks = 2 
days = 3 
hours = 4

print('choose the number of the unit time')
unit = int(input(f'{months}.months ,{weeks}.weeks ,{days}.days ,{hours}.hours: '))
if unit == 1:
    print(f'you lived for {m:,} months.')
elif unit == 2:
    print(f'you lived for {w:,} weeks.')
elif unit == 3:
    print(f'you lived for {d:,} days.')
elif unit == 4:
    print(f'you lived for {h:,} hours.')
else:
    print('sorry the answer is not defined')
