#DAY 5 How about a nice game of chess?
import hashlib

def findPassword(id):
    password = ''
    count = 0
    for _ in range(0,8):
        hashhex = ''
        while hashhex[0:5] != '00000':
            hashhex = hashlib.md5(bytes(id+str(count), 'utf-8')).hexdigest()
            count += 1

        password+=hashhex[5]
        # print(hashhex)

    return password

def findPasswordUpdated(id):
    password = [''] * 8
    valids = [str(i) for i in range(0,8)]
    count = 0
    while '' in password:
        hashhex = ''
        while hashhex[0:5] != '00000':
            hashhex = hashlib.md5(bytes(id+str(count), 'utf-8')).hexdigest()
            count += 1

        if hashhex[5] in valids:
            if password[ int(hashhex[5]) ] == '':
                password[ int(hashhex[5]) ] = hashhex[6]
                # print(hashhex)

    password = cat(password)
    return password