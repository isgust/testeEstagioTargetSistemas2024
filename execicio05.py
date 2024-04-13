def inverterString(string):
    # Inicializar uma string vazia para armazenar a string invertida
    stringInvertida = ""
    
    # Percorrer toda string
    for i in range(len(string) - 1, -1, -1):
        # Adicionar cada caractere à string invertida
        stringInvertida += string[i]
    
    # Retornar a string invertida
    return stringInvertida

#Entrada de dados e Saída
textoOriginal = input("Digite uma string para inverter: ")
textoInvertido = inverterString(textoOriginal) #Aplicando a função inverterString e adicionando textoOriginal ao parametro
print("String original:", textoOriginal)
print("String invertida:", textoInvertido)
