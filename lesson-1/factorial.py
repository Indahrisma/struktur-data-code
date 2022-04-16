
def tampilkanAngka(batas, i=10):
  print(f'Perulangan ke {i}')

  if (i > batas):
    tampilkanAngka(batas, i-1)


tampilkanAngka(0)

# #no 2
n = int(input('Masukkan nilai n: '))


def faktorial(n):
  if n == 1:
    return (n)
  else:
    return(n*faktorial(n-1))


print("%d!=%d" % (n, faktorial(n)))
