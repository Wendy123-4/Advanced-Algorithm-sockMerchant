def sockMerchant(n, ar):
    # Write your code here
    counter = {}
    pairs = []

    for item in ar:
        if (item in counter):
            counter[item] += 1
        else:
            counter[item] = 1
    for x in list(counter.values()):
        pairs.append(int(x / 2))

    return sum(pairs)