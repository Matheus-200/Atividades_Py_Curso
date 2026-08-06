# Analisando uma string 
# Ultilizando o len (Ele conta quantos caracteres dentro da string, contando também os espaços)
frase = 'Meu nome é matheus gabriel'
print (len(frase))


#Ultilizando o count 
n2 = frase.count('a',0,13) 
print(n2)
#  Aqui eu pedi para ele contar quantas vezes aparece a letra 'a' dentro da da string,
#  eu armazenei o resutado dentro da variável 'oi', e exibi ele com um print. 
# Adicionei também '0' e '13', que faz o fatiamento, então ele vai contar somente o que está dentro desses dois valores.


#Ultilizando o find
n3 = frase.find('eus')
print(n3)
# A função find, conta a partir de qual caratere começa a frase, o resultado aqui irá ser 15.

#Utilizando o in
n4 = 'matheus' in frase
print (n4)
# Ele vai me dizer se existe uma palavra dentro da string (true ou false)

#ultilzando o replace (trocar)
n5 = frase.replace('matheus gabriel','xaolin-matador-de-porco')
print(n5) 
# Essa função serve para trocar uma informação por outra.

#Ultilizando upper() / lower()
n6 = frase.upper()
print(n6)
#Ele deixa tudo em maiusculo
n7 = frase.lower()
print(n7) 
#Tudo em minúsculo
n8 = frase.capitalize()
print(n8)
#Ele coloca todas as letras minúsculas, e coloca somente a primeira como maiúscula.
n9 = frase.title()
print(n9)
# Ele coloca em maiusculo a inicial de cada palavra, ele faz a partir do espaço entre cada uma.