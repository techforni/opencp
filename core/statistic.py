def average(tDataMatrix):
    s = 0
    for i in range(len(tDataMatrix)):
        s += tDataMatrix[i]
    s / len(tDataMatrix)