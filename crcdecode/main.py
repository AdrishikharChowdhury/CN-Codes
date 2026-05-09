def findXor(a, b):
    n = len(b)
    result = ""
    for i in range(1, n):  # Skip first bit
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result


def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = findXor(divisor, tmp) + dividend[pick]
        else:
            tmp = findXor('0' * pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = findXor(divisor, tmp)
    else:
        tmp = findXor('0' * pick, tmp)

    return tmp

def decodeData(data, key):
    if mod2div(data, key) == 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    code = input("Enter CRC Code: ")
    key = input(" Generator (binary): ")   

    print("\nerror:",decodeData(code,key))
