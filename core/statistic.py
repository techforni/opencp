from statistics import StatisticsError, mode

def average(tDataMatrix):
    if len(tDataMatrix) == 0:
        return 0

    s = 0
    for i in range(len(tDataMatrix)):
        s += tDataMatrix[i]

    return s / len(tDataMatrix)

def trend(tDataMatrix):
    try:
        trend = mode(tDataMatrix)
        return trend
    except StatisticsError as e:
        print(f"Errore: {e}")
