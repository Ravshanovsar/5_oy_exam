alp = []
for i in range(ord('a'), ord('a') + 26):
    alp.append(chr(i))
alphabet = iter(alp)

try:
    while True:
        print(next(alphabet), end=" ")
except StopIteration:
    pass
