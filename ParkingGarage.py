for i in range(1,9,1):
    fee=(5+2.5*i)
    if fee<10:
        print (f'{i} {float(10)}')
    elif fee<20:
        print(f'{i} {fee}')
    else:
        print(f'{i} {float(20)}')