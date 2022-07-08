# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

itens = int(sys.stdin.readline())

chances = []

for item in range(0, itens):
    chances.append(int(sys.stdin.readline())*3)
    print(chances[item])