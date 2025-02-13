# Write a function that accepts a list of numbers as an argument
# And returns list with squares for each number
def squares(numbers):
    sq = []
    for num in numbers:
        sq.append(num ** 2)
    return sq


x = [1, 2, 3, 4, 5]
# print(squares(x))

# Write a function that accepts a list of numbers
# And returns a tuple with two numbers, amount of odd and even numbers
# Example: input -> [1, 2, 3, 4, 5] output (3, 2)
# Where 3 is amount of Odds and 2 is amount of evens
def count_odds_and_evens(numbers):
    odds, evens = 0, 0
    for num in numbers:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    return odds, evens


print(count_odds_and_evens(x))


# Write a function that accepts a list of numbers
# and returns largest number
def max_number(numbers):
    return max(numbers)


print(max_number(x))


# Write a function that accepts a start number and end number
# Create a FizzBuzz for given range
# (If number divided by 3 has no remainder, print number + FIZZ
# If number divided by 5 has no remainder, print number + BUZZ
# If number divided by 5 and 3 has no remainder, print number + FIZZBUZZ)

def fizzbuzz(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print(num, 'FIZZBUZZ')
        elif num % 5 == 0:
            print(num, 'BUZZ')
        elif num % 3 == 0:
            print(num, 'FIZZ')


fizzbuzz(809, 1543)