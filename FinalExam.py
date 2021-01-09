def get_cmax(c1, c2, c3):
    cmax = 0
    for i in range(16):
        (d1, d2, d3, d) = get_binary(i)
        num = abs(c1*d1 + c2*d2 + c3*d3 + d)
        if num > cmax:
            cmax = num
    return cmax


def get_binary(i):
    binary = "{:08b}".format(i)
    d = int(binary[-1])
    d3 = int(binary[-2])
    d2 = int(binary[-3])
    d1 = int(binary[-4])
    return (d1, d2, d3, d)


def get_KC(C):
    KC = 0
    if C>0:
        KC = len("{:b}".format(C))
    return KC


def get_bi(C, i):
    KC = get_KC(C)
    if i > KC+1:
        return False
    elif i == KC+1:
        return 0
    else:
        #print("{:0b}".format(C))
        return int("{:0b}".format(C)[-i])


def FA(c1=-1, c2=-1, c3=-1, c=3):
    print("c1=", c1, ", c2=", c2, ",c3=", c3, ",c=", c)
    cmake = get_cmax(c1, c2, c3)
    KC = get_KC(c)
    FA = []
    for carry in range(-cmake, cmake+1):
        for i in range(1, KC+2):
            for carry2 in range(-cmake, cmake+1):
                for i2 in range(1, KC+2):
                    for a1 in range(0, 2):
                        for a2 in range(0, 2):
                            for a3 in range(0, 2):
                                R = c1*a1 + c2*a2 + c3*a3 + get_bi(c, i) + carry
                                if R%2 == 0 and carry2==R/2:
                                    if i>KC and i2==i:
                                        FA.append([carry, i, carry2, i2, a1, a2, a3])
                                    if i<=KC and i2==i+1:
                                        FA.append([carry, i, carry2, i2, a1, a2, a3])

    return FA

''' type input here '''
FA1_c = 3
FA2_c = 3
FA1 = FA(c1=3, c2=-2, c3=-1, c=FA1_c)
FA2 = FA(c1=6, c2=-4, c3=1, c=FA2_c)
FA = []
for i in FA1:
    for j in FA2:
        if i[4]==j[4] and i[5]==j[5] and i[6]==j[6]:
            FA.append([i[0], i[1], i[2], i[3], j[0], j[1], j[2], j[3], j[4], j[5], j[6]])


stack = []
first = []
output = []
leaves = []
get = 0

for i in FA:
    if i[0] == 0 and i[1] == 1 and i[4] == 0 and i[5] == 1:
        first.append(i)

if len(first)==0:
    print("there is no solution")
else:
    count = 0
    node = first[0]
    del first[0]
    stack.append(node)

    while True:

        if len(stack) == 0:
            if len(first) == 0:
                print("run out but don't get a path")
                break
            else:
                node = first[0]
                del first[0]
                stack.append(node)
                leaves = []

        if node[2] == 0 and node[3] == (get_KC(FA1_c)+1) and node[6] == 0 and node[7] == (get_KC(FA2_c)+1):
            print("get a path")
            get = 1
            print(stack)
            break

        leave = 0
        for i in FA:
            if i[0] == node[2] and i[1] == node[3] and i[4] == node[6] and i[5] == node[7]:
                if i[0] != node[0] and i[1] != node[1] and i[4] != node[4] and i[5] != node[5]:
                    if i not in leaves:
                        stack.append(i)
                        leave = 1
                        node = stack[-1]
                        break

        if leave == 0:
            leaves.append(node)
            del stack[-1]
            if len(stack)!=0:
                node = stack[-1]

if get == 1:

    x1 = x2 = x3 = 0
    n = 1
    for i in stack:
        x1 = x1 + i[8]*n
        x2 = x2 + i[9]*n
        x3 = x3 + i[10]*n
        i*=2
    print("x1=", x1, ",x2=", x2, ",x3=", x3)