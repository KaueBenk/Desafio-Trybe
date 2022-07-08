# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

frase = sys.stdin.readline()
letra = sys.stdin.readline()

def vezesLetraAparece(frase, letra):
    return frase.count(letra)

print(vezesLetraAparece(frase, letra))