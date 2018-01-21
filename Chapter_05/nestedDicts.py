allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}

numBrought = {}
def totalBrought(guests):
    for v in guests.values():
        for k, v2 in v.items():
            numBrought.setdefault(k, 0)
            numBrought[k] += v2
    return numBrought

print('Number of things being brought:')
for k, v in totalBrought(allGuests).items():
    print(k + ': ' + str(v))
