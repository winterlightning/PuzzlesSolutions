#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#solution comment: simplest solution is you can sum from 3 -> 999 and 5 -> 995, the key is adding the multiples of 3 and 5 only once

#calculate the sum of the multiples of 3 and 5 up till the limit
def calculate_multiple_sum(limit):
    return sum(range(3, limit, 3) ) + sum ( range(5, limit, 5) ) - sum (range(15, limit, 15))
