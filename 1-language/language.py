# generators / yield
witness = [0]


def factors(n, _witness):               # generator that computes factors
    for k in range(1, n+1):
        if n % k == 0:        # divides evenly, thus k is a factor
            yield k           # yield this factor as next result
            _witness[0] += 1


list_factors = factors(10, witness)
# n = 10
# list_factors = (k for k in range(1, n+1) if n%k == 0)
print("The result is: \n")
for i in list_factors:
    print("witness =" + str(witness[0]))
    print(i)

###
print("R-1.1")


def is_multiple(n, m):
    return True if n % m == 0 else False


print(str(is_multiple(6, 4)))
###

print("R-1.2")


def is_even(k):
    even = ["0", "2", "4", "6", "8"]
    for i in even:
        if (str(k).endswith(i)) :
            return True
    return False


print(is_even(101))


print("R-1.7")


def square_odd(n):
    return sum(k*k for k in range(1, n + 1) if k%2 != 0)


print(square_odd(5))


print("C-1.14")
# Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.

def numbers_with_odd_product(series):
    for k in series:
        if k%2 == 1:
            yield k


input_series = [2, 4, 6, 9, 10]
n = 0
for i in numbers_with_odd_product(input_series):
    n += 1
    print(str(i))
if n < 2:
    print("No pair")


# C-1.15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).

def is_unique(input):
    for i in range (0, len(input)):
        for j in range (0, len(input)):
            if i!=j:
                if input[i] == input[j]:
                    return False
    return True


input_series = [0, 1, 3, 4, 7, 7]
print(is_unique(input_series))
