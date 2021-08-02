num=input('Enter a number:')
try:
    inum=int(num)
    if inum ==1:
        print('ONE')
    elif inum == 2:
        print('TWO')
    elif inum == 3:
        print('THREE')
    else:
        print('Invalid input')
except:
    print('Invalid input')
