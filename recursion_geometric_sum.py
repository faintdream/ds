def gsum(k):
    if k < 1:
        return True
    #output = gsum(k-1)
    return float(1+k/2**k) + gsum(k-1)
k = 3

print(str.format('{0:.5f}', gsum(k)))