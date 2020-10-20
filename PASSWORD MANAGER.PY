# PASSWORD MANAGER

mainpassword = 'ahmed20@'
passowrd = input('please enter your password: ')
if passowrd == mainpassword:
    print('log in succeeded')

tries = 3

while passowrd != mainpassword and tries > 1:
    tries -= 1
    print(f'sorry wrong password,please try agin..{tries} cahnce left')
    passowrd = input('please enter your password: ')
    print('sorry, wait for 20 seconds')
