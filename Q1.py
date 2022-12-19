def generator(number, string):
    n = len(string)
    while n < num:
        string += string
        n = len(string)
    return string[:number]


def counter(s):
     return s.count('a')


num = int(input())
st = input()
word = generator(num, st)
print(word, counter(word))