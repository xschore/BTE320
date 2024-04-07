# def recursive_factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*recursive_factorial(n-1)

# print(recursive_factorial(10))

def strRev(n):
    if len(n)==1:
        return n
    else:
        return n[-1]+strRev(n[:-1])

print(strRev('Miami'))