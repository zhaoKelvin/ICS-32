def sumUp(num):
    if num <= 0:
        return 0
    return sumUp(num // 10) + num % 10

def sum_digit(n):
    if n > 0:
        return sum_digit(n // 10) + n % 10
    else:
        return 0
    
print(sum_digit(1234))
print(sumUp(1234))