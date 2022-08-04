def bubbleSort(alista):
    for passnum in range(len(alista)-1, 0, -1):
        for i in range(passnum):
            if alista[i]>alista[i+1]:
                tempo = alista[i]
                alista[i] = alista[i+1]
                alista[i+1] = tempo

alista = [2, 5, 8, 12, 6, 4, 3, 20, 17, 19 ]
bubbleSort(alista)
print(alista)