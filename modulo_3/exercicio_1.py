def bubbleSort(alista):
    for passnum in range(len(alista)-1, 0, -1):
        for i in range(passnum):
            if alista[i]>alista[i+1]:
                tempo = alista[i]
                alista[i] = alista[i+1]
                alista[i+1] = tempo

alista = [10, 9, 8, 7, 6, 5, 4, 2, 3, 1]
bubbleSort(alista)
print(alista)