
def all_variants(text):
    a = []
    b = []
    for i in range(len(text)):
        for y in range(1, len(text)+1):
            a.append(text[i: i+y])
    a.sort()
    b = list(set(a))
    b.sort(key=len)

    yield b




z = all_variants('abc')
for i in z :
    print(*i, sep='\n')