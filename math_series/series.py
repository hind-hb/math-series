def fibonacci(n):
    
    if n<0:
        return 'Pleas Enter a positive Number'
    if n ==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def lucas(n):
    
    if n<0:
        return 'Pleas Enter a positive Number'
    if n ==0:
        return 2
    if n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)


def other_values(n,first_value,second_value):

    if n<0:
        return 'Plz Enter a positive Number'
    if n ==0:
        return first_value
    if n==1:
        return second_value
    else:
        return other_values(n-1,first_value,second_value)+other_values(n-2,first_value,second_value)


def sum_series(n,first_value=0,second_value=1):
    if first_value ==0 and second_value ==1:
        return fibonacci(n)
    elif first_value ==2 and second_value ==1:
        return lucas(n)
    else:
        return other_values(n,first_value,second_value)



print(sum_series(5,5,3))
