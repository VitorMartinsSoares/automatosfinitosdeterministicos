def afd(listaFuncao, estadoinicial, estadosfinais,palavra):
    qA = estadoinicial
    retorno = 'Rejeita!'
    for p in palavra:
        qA = geraFuncaoTransicao(listaFuncao,qA,p)
    for ef in estadosfinais:
        if qA == ef:
            retorno = 'Aceita!'
    return retorno

def geraFuncaoTransicao(listafuncao,qA,letraPalavra):
    for j in listafuncao:
        if(j[0]==qA):
            if(letraPalavra==j[1]):
                qA = j[2]
                return qA
    return qA

arquivo = open('funcoes.txt','r')
lista = []
lista2 = []
print("leia o readme para entender como inserir os valores!")
#Exemplo: q0
inicial = input("Informe o estado inicial:")
#Exemplo: q3,q4
finais = input("Informe os estados finais:")
#Exemplo: aaabbb
palavra = input("Informe a palavra:")
for i in arquivo:
    i=i.rstrip('\n')
    i2=i.split(',')
    lista.append(i2)
finais=finais.split(',')
resultado = afd(lista,inicial,finais,palavra)
print(resultado)