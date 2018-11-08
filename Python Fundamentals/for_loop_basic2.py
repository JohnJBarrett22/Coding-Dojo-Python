#1
def biggie_size(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr

#2
def count_positives(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count += 1
    arr[-1] = count
    return arr

#3
def sum_total(arr):
    count = 0
    for i in range(len(arr)):
        count = count + arr[i]
    return count

#4
def average(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    return sum / len(arr)

#5
def length(arr):
    return len(arr)

#6
def minimum(arr):
    min = arr[0]
    if len(arr) == 0:
        return False
    for i in arr:
        if i < min:
            min = i
    return min

#7
def maximum(arr):
    max = arr[0]
    if len(arr) == 0:
        return False
    for i in arr:
        if i > max:
            max = i
    return max

#8
def ultimate_analyze(arr):
    dict = {
        'sumtotal' : sum_total(arr),
        'avg' : average(arr),
        'min' : minimum(arr),
        'max' : maximum(arr),
        'len' : length(arr)
    }
    return dict
        
#9
def reversed(arr):
    arr = arr[::-1]
    return arr