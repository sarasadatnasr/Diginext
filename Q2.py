def counter(s):
    re = 0
    s = list(s)
    for i in range(len(s) - 1):
        if s[i] == 'A':
            if s[i + 1] != 'B':
                re += 1
        if s[i] == 'B':
            if s[i + 1] != 'A':
                re += 1
        print(i,s[i])
    return re
st = input()
print(st, counter(st))
