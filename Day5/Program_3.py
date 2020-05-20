def stolen(houseValue):
    maxValue = []
    for i in range(0,len(houseValue),2):
        maxValue.append(houseValue[i])
    print(max(maxValue))

value = list(map(int, input().split()))
stolen(value)
