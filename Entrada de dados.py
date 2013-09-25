nome = input("Seu nome:")
print ("Olá", nome)
resposta = (str(input("Tudo bem com você ?, S/N:")))

if resposta == 'N' or resposta == 'n':
    resposta2 = input("Porque você não se sente bem?:")
    print ("Vai ficar tudo bem, não se preocupe com ", resposta2)
else: print ("Que bom que você se sente bem,",nome)
