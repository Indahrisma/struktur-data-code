# def hello_world ():
#     print('Hello World')
#     hello_world()

# hello_world()

def tampilkanAngka(batas, i=1):
  print(f'Perulangan ke {i}')

  if (i < batas):
    tampilkanAngka(batas, i+1)


tampilkanAngka(10)
