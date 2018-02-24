# https://www.hackerrank.com/challenges/ctci-lonely-integer
def lonely_integer(a):
    bitArray = 0b0
    for ele in a:
        bitArray = bitArray ^  ele
        # print(ele, bin(bitArray))

    return int(bitArray)