#data = "54900 usec, 2480 usec 620 usec, 1240 usec 620 usec, 620 usec 620 usec, 1240 usec 620 usec, 600 usec 640 usec, 1220 usec 660 usec, 560 usec 640 usec, 600 usec 640 usec, 1240 usec 640 usec, 580 usec 640 usec, 600 usec 640 usec, 620 usec 620 usec, 620 usec 26000 usec, 2480 usec 620 usec, 1220 usec 640 usec, 620 usec 600 usec, 1240 usec 640 usec, 580 usec 640 usec, 1240 usec 620 usec, 620 usec 620 usec, 620 usec 620 usec, 1240 usec 620 usec, 620 usec 620 usec, 620 usec 620 usec, 620 usec 620 usec, 600 usec 26020 usec, 2480 usec 620 usec, 1240 usec 620 usec, 620 usec 620 usec, 1220 usec 640 usec, 580 usec 660 usec, 1220 usec 640 usec, 620 usec 600 usec, 620 usec 620 usec, 1240 usec 620 usec, 620 usec 620 usec, 620 usec 620 usec, 620 usec 620 usec, 620 usec 26000 usec, 2500 usec 600 usec, 1240 usec 620 usec, 620 usec 620 usec, 1240 usec 620 usec, 620 usec 620 usec, 1220 usec 640 usec, 620 usec 600 usec, 640 usec 600 usec, 1240 usec 640 usec, 600 usec 620 usec, 620 usec 620 usec, 620 usec 620 usec, 620 usec 26000 usec, 2480 usec 620 usec, 1240 usec 620 usec, 620 usec 620 usec, 1240 usec 620 usec, 620 usec 620 usec, 1220 usec 640 usec, 580 usec 640 usec, 600 usec 640 usec, 1240 usec 620 usec, 620 usec 620 usec, 600 usec 640 usec, 600 usec 640 usec, 620 usec 26020 usec, 2480 usec 600 usec, 1240 usec 620 usec, 620 usec 640 usec, 1180 usec 660 usec, 600 usec 640 usec, 1220 usec 640 usec, 600 usec 640 usec, 580 usec 660 usec, 1220 usec 640 usec, 580 usec 640 usec, 600 usec 640 usec, 600 usec 640 usec, 600 usec"
off = []
on = []
temp = []
def encode (String):
    i = 1
    inc = 0
    for x in range(0, len(data)):
        if(data[x].isdigit()):
            temp.extend(data[x])
            if(data[x+1].isalpha() or data[x+1].isspace()):
                num = int(''.join(map(str,temp)))
                del temp[:]
                if(i % 2 != 0):
                    off.append(num)
                    num = str(num)
                    print("delayMicroseconds("+ num + ");")
                    i += 1
                else:
                    on.append(num)
                    num = str(num)
                    print("pulseIR("+num+");")
                    i += 1
encode(data)
