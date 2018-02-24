#DAY 7 Internet Protocol Version 7
def parse(string):
    start = re.match(r'(\w+)\[.*', string).groups()[0]
    outer = [ele.strip('[]') for ele in re.findall(r'\][a-z]*\[', string)]
    end = re.match(r'.*\]([\w]+)', string).groups()[0]
    inner = [ele.strip('[]') for ele in re.findall(r'\[[a-z]*\]', string)]
    return [start]+outer+[end], inner

def scan(string):
    for idx in range(len(string)-4+1):
        firstHalf = string[idx:idx+2]
        secondHalf = string[idx+2:idx+4]
        # print(firstHalf, secondHalf)
        if firstHalf[0] != firstHalf[1] and firstHalf == secondHalf[::-1]:
            return True
    return False

def checkTLS(data):
    count = 0
    for line in data:
        outer, inner = parse(line)
        if any(map(scan, outer)) == True and any(map(scan, inner)) != True:
            count+=1
    return count

data = fileImport('input7')

def scanABA(string):
    return [string[idx:idx+3] for idx in range(len(string)-3+1) if string[idx] == string[idx+2] and string[idx] != string[idx+1]]

def flipABA(string):
    return string[1] + string[0] + string[1]

def checkSSL(data):
    count = 0
    for line in data:
        outer, inner = parse(line)
        outerABA = set( [flipABA(ele) for ele in mapCombine(scanABA, outer)] )
        innerBAB = set(mapCombine(scanABA, inner))
        if len(outerABA.intersection(innerBAB)) >=1:
            count+=1
    return count