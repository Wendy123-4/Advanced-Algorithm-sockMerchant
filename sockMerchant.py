import random


# Main function for pairing up socks
def sockMerchant(n, ar):
    counter = {}
    pairs = []

    # Creates a dictionary of the color and the number available
    for item in ar:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    # Stores count of pairs of each color
    for x in list(counter.values()):
        pairs.append(int(x / 2))

    # Returns total of pairs in the pile
    return sum(pairs)


# Test function with 30 elements in array and returns 10 pairs
def test_array1():
    return sockMerchant(30, random.sample(range(30, 50), 10) + (random.sample(range(0, 20), 10) * 2))


print("Pairs returned:",test_array1())


# Test function with 80 elements in array and returns 36 pairs
def test_array2():
    return sockMerchant(80, random.sample(range(50, 100), 10) + (random.sample(range(0, 40), 18) * 4))


print("Pairs returned:",test_array2())
