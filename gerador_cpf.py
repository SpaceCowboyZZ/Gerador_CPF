import random

multiplicador = 10
i = 0
lista_resultados = []
lista_resultados2 = []
cpf = []
cpf = [random.randint(0,9) for i in range(9)]
while multiplicador > 1 and i < 10:
    resultado_parcial = multiplicador * cpf[i]
    lista_resultados.append(resultado_parcial)
    multiplicador -= 1
    i += 1
    continue
resultado = (sum(lista_resultados) * 10) % 11
if resultado > 9:
    resultado = 0
cpf.append(resultado)
multiplicador = 11
i = 0
while multiplicador > 1 and i < 11:
    resultado_parcial2 = multiplicador * cpf[i]
    lista_resultados2.append(resultado_parcial2)
    multiplicador -= 1
    i += 1
    continue
resultado2 = (sum(lista_resultados2) * 10) % 11
if resultado2 > 9:
    resultado2 = 0
cpf.append(resultado2)
cpf = [str(i) for i in cpf]# transforma de int para str(pra falar a vdd eu ainda não entendi bem como isso funciona
print(''.join(cpf))