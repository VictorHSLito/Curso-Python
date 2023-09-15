maçã = ''
moeda = ''
bloco_vazio = ''
passo = ''
bloco = ''
pega = ''
pula = ''
while not object(maçã):
   if bloco:
      passo()
   if bloco_vazio:
      pula()
   if moeda:
      pega() 
pega()
    
c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')