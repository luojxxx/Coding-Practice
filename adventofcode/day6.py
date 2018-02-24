#DAY 6 Signals and Noise
data = [i.strip('\n') for i in open('/Users/cloudlife/Desktop/input6.txt').readlines()]

def recover(data):
    msg = ''
    msgLen = len(data[0])
    for i in range(msgLen):
        temp = []
        for row in data:
            temp.append(row[i])

        msg += Counter(temp).most_common(1)[0][0]

    return msg

def recoverLeastCommon(data):
    msg = ''
    msgLen = len(data[0])
    for i in range(msgLen):
        temp = []
        for row in data:
            temp.append(row[i])

        msg += Counter(temp).most_common()[-1][0]

    return msg