# Day 10 Math Fuctions ............................................................................................

# x = 2.9
# print(round(x))
# print(abs(-2.9)) # ALWAYS RETURN POSITIVE NUMBER

# import math

# print(math.ceil(2.9))
# print(math.floor(2.9))

""""
Write a Python program to sum all amicable numbers from 1 to specified numbers.
Note: Amicable numbers are two different numbers so related that the sum of the proper divisors of each is equal to the other number. (A proper divisor of a number is a positive factor of that number other than the number itself. For example, the proper divisors of 6 are 1, 2, and 3.)

Sample Solution :-

Python Code :

def amicable_numbers_sum(limit):
    if not isinstance(limit, int):
        return "Input is not an integer!"

    if limit < 1:
        return "Input must be bigger than 0!"

    amicables = set()

    for num in range(2, limit+1):
        if num in amicables:
            continue

        sum_fact = sum([fact for fact in range(1, num) if num % fact == 0])
        sum_fact2 = sum([fact for fact in range(1, sum_fact) if sum_fact % fact == 0])
        if num == sum_fact2 and num != sum_fact:
            amicables.add(num)
            amicables.add(sum_fact2)

    return sum(amicables)


print(amicable_numbers_sum(9999))
print(amicable_numbers_sum(999))
print(amicable_numbers_sum(9)) 

"""