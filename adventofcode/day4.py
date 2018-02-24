#DAY 4 Security through obscurity
file = [i.strip('\n') for i in open('/Users/cloudlife/Desktop/input4.txt').readlines()]

def checkSummer(counts):
    checkSumList = []
    temp = ''
    priorNum = counts[0][1]
    for ele in counts:
        char = ele[0]
        num = ele[1]

        if priorNum == num:
            temp += char

        if priorNum != num:
            checkSumList.append(''.join(sorted(temp)))
            temp = ''
            priorNum = num
            temp+=char

    checkSumList.append(''.join(sorted(temp)))

    return ''.join(checkSumList)[0:5]

def checkRoomName(name):
    matches = re.match( r'([a-z\-]+)(\d+)(\[.+\])', name)

    dashedName = matches.group(1)
    encryptName = dashedName.replace('-', '')
    sectorId = int(matches.group(2))
    checkSum = matches.group(3)[1:-1]

    nameCounts = collections.Counter(encryptName).most_common()
    nameCheckSum = checkSummer(nameCounts)
    if checkSum == nameCheckSum:
        return dashedName, sectorId
    else:
        return '', 0

# assert checkRoomName('aaaaa-bbb-z-y-x-123[abxyz]') == 123
# assert checkRoomName('a-b-c-d-e-f-g-h-987[abcde]') == 987
# assert checkRoomName('not-a-real-room-404[oarel]') == 404

# total = 0
# realRooms = []
# for room in file:
#     dashedName, sectorId = checkRoomName(room)
#     if sectorId != 0:
#         realRooms.append({'roomName': dashedName, 'sectorId':sectorId})
#         total += sectorId
# print(total)

def cap(num):
    if num > 25:
        return num-25-1
    else:
        return num

def shiftChar(char, num):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = num % 26
    charIdx = alphabet.index(char)
    newIdx = cap(charIdx + shift)
    return alphabet[newIdx]

def decryptName(name, sectorId):
    temp = ''
    for char in name:
        if char == '-':
            temp+= ' '
        else:
            temp += shiftChar(char, sectorId)

    return temp

# assert decryptName('qzmt-zixmtkozy-ivhz-', 343) == 'very encrypted name '

# decryptNames = []
# for room in realRooms:
#     name = decryptName(room['roomName'], room['sectorId'])
#     decryptNames.append([name,room['sectorId']])
#     print(decryptNames[-1])
