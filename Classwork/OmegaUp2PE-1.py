def sieve():
    primes = [1] * 1_000_001
    primes[0] = primes[1] = 0
    for i in range(2, 1_000_001):
        for j in range(i+i, 1_000_001, i):
            if primes[j]:
                primes[j] = 0

    return primes

letters = dict()
listLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#for i in range(0, 26):
#    letters[chr(i + 97)] = i+1
#
#for i in range(0, 26):
#    letters[chr(i + 65)] = i+27

for i in range(len(listLetters)):
    letters[listLetters[i]] = i+1

#print(letters.keys())

primes = sieve()

A = input()
while A != '0':

    val = 0
    for i in A:
        val += letters[i]

    if primes[val]:
        print("Codificación prima")
    else:
        print("Codificación normal")
    A = input()