import sys
input = sys.stdin.readline

def solution (arr):
    count = 0
    result = ""
    for type in arr:
        if type == "BOOL":
            result += "#"
            count += 1
        elif type == "SHORT":
            if (count % 8) % 2 == 1:
                result += ".##"
                count += 3
            else:
                result += "##"
                count += 2
        elif type == "FLOAT":
            if count % 8 == 1 or count % 8 == 5:
                result += "...####"
                count += 7
            elif count % 8 == 2 or count % 8 == 6:
                result += "..####"
                count += 6
            elif count % 8 == 3 or count % 8 == 7:
                result += ".####"
                count += 5
            else:
                result += "####"
                count += 4
        elif type == "INT":
            if count % 8 == 0:
                result += "########"
            else:
                result += "." * (8 - (count % 8)) + "########"
                count += (8 - (count % 8)) + 8
        elif type == "LONG":
            if count % 8 == 0:
                result += "#" * 16
            else:
                result += "." * (8 - (count % 8)) + "#" * 16
                count += (8 - (count % 8)) + 8
    if count % 8 != 0:
        result += (8 - (count % 8)) * "."
    return result

a = ["BOOL", "SHORT"]
b = ["BOOL", "BOOL"]
c = ["BOOL", "SHORT", "FLOAT"]
d = ["BOOL", "INT"]
e = ["SHORT", "BOOL"]
f = ["FLOAT", "SHORT"]

l = [a, b, c, d, e, f]
for i in l:
    print(solution(i))