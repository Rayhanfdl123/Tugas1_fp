# Nomor 1
def sum_squares(*numbers) :
    arr = [*numbers]
    temp = 0
    for num in arr:
        temp += num**2
    return temp

print("Sum Squares dari (1, 2, 3) = " + str(sum_squares(1, 2, 3)))

# Nomor 2
def triangular(n):
    temp = 0
    for i in range(n):
        temp += n
        n -= 1
    return temp
print("Hasil dari triangular 5 = " + str(triangular(5)))

# Nomor 3
def pangkat(num, power):
    temp = num
    if num < 0 or power < 0:
        return "only accept positive number"
    counter = 0
    if power == 0:
        return 1
    while counter < power - 1:
        num = num * temp
        counter += 1
    return num

print("Hasi dari pangkat 3 dengan power 9 = " + str(pangkat(3, 9)))

# Nomor 4
def is_palindrome(x):
    arr = str()
    for i in reversed(x):
        arr += i
    if arr == x:
        return True
    else:
        return False

print("rotator merupakan palindrome = " + str(is_palindrome("rotator")))