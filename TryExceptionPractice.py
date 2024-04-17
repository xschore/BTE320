def avg(alist):
    try:
        print(sum(alist)/len(alist))
    except ZeroDivisionError:
        print('Cannot divide by zero.')
        return []
    except TypeError:
        print('Must input an integer or float.')
        return []
    except:
        print('Unknown error.')

avg([1,2])