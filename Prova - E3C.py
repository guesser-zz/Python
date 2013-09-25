# A prova exige a seguinte condição:
#   De [1..100] imprimir
#   "fla" quando divisor de 3 
#   "flu" quando divisor de 5
#   "flaflu" quando divisor de 3 e 5

contador = 0 # incrementador
d1 = 3       # Divisor 1
d2 = 5       # Divisor 2
m1 = "fla"   # Mensagem referente a MOD Divisor 1
m2 = "flu"   # Mensagem referente a MOD Divisor 2
while contador < 100:
  contador = contador + 1
  if contador % d1 == 0 and contador % d2 == 0:
    print(m1+m2)
  else:
      if contador % d1 == 0:
        print(m1)
      else:
        if contador % d2 == 0:
          print(m2)
        else:
              print(contador)

