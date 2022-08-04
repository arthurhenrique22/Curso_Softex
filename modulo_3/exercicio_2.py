def insertionSort(lista):

    for passn in range(1, len(lista)):
        chave = lista[passn]
        i = passn - 1

        while i >= 0 and chave < lista[i]:
            lista[i + 1] = lista[i]
            i = i - 1

        lista[i + 1] = chave


vetor = [61, 59, 57, 55, 53, 51, 49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
insertionSort(vetor)
print(vetor)