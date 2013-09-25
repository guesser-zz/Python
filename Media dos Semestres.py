n = 1
soma = 0
semestre = 0
while semestre < 4:
    x = int(input("Digite as Nota:"))
    soma = soma + x
    semestre = semestre + 1
print ("Média dos 4 semestres é: %5.2f" %(soma/4))
