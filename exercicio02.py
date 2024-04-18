# imprimir operacoes matematicas usando todos os numeros inteiros Reais
# numero natural {1, 2, 3 ...} numero inteiro {-1, -2, -3, 0, 1, 2, 3} numeros racionais {1, 1.01, 1.2 ...}

valor_um = 12
valor_dois = 28.12
valor_tres = 100
valor_quatro = -3
valor_cinco = 3.1415

print(valor_um + valor_dois)
print(valor_cinco - valor_dois)
print(valor_tres * valor_um)
print(valor_um / valor_cinco)

#-----------------------------------------------------------------

valor_novo = valor_cinco
print(id(valor_novo))
print(id(valor_cinco))

#------------------------------------------------------------------
print(type(valor_um))
print(type(valor_quatro))
print(type(valor_cinco))

#------------------------------------------------------------------
valor_seis = "100"
valor_sete = "abacaxi"
valor_oito = "2"

print(valor_seis + valor_oito)
print(valor_seis + valor_sete)
