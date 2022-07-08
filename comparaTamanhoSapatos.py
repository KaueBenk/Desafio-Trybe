# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

def comparaTamanhoSapatos():
  sapatoIsabela = int(sys.stdin.readline())
  sapatoLuisa = int(sys.stdin.readline())
  if sapatoIsabela > sapatoLuisa:
    print("Isabela calça mais")
  elif sapatoIsabela < sapatoLuisa:
    print("Luisa calça mais")
  else:
    print("Isabela e Luisa calçam o mesmo tamanho de sapato")

comparaTamanhoSapatos()