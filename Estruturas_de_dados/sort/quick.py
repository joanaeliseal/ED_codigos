def quickSort(array):
    _quick(array,0,len(array)-1)

def _quick(array,primeiro,ultimo):
    print(f"Ordenando {array[primeiro:ultimo+1]}")
    if primeiro<ultimo:
        splitpoint = particao(array,primeiro,ultimo)
        print(f"{array[primeiro:ultimo+1]}. Dividindo em {splitpoint}")
        print(f"Left={array[primeiro:splitpoint]}. Right={array[splitpoint+1:ultimo+1]}")
        _quick(array,primeiro,splitpoint-1)
        _quick(array,splitpoint+1,ultimo)


def particao(array,primeiro,ultimo):
    pivo = array[primeiro]

    a = primeiro+1
    b = ultimo
    # print(f"\t Array=[{array[primeiro:ultimo+1]}]. pivo={array[primeiro]}. A={array[a]}. B={array[b]}")

    terminado = False
    while not terminado:
        print("loop")
        print(f"  Array=[{array[primeiro:ultimo+1]}]. pivo={array[primeiro]}. A={array[a]}. B={array[b]}")

        while a <= b and array[a] <= pivo:
            print(f"  Array=[{array[primeiro:ultimo+1]}]. pivo={array[primeiro]}. A={array[a]}. B={array[b]}")
            a = a + 1

        while array[b] >= pivo and b >= a:
            print(f"  Array=[{array[primeiro:ultimo+1]}]. pivo={array[primeiro]}. A={array[a]}. B={array[b]}")
            b = b -1

        if b < a:
            terminado = True
        else:
            print(f"  Array=[{array[primeiro:ultimo+1]}]. pivo={array[primeiro]}. A={array[a]}. B={array[b]} <- Troca A por B")
            array[a], array[b] = array[b], array[a]

    print(f"  Array=[{array[primeiro:ultimo+1]}].  <- Troca {array[b]} por {array[primeiro]}")
    print(f"  Split={b} - {ultimo}")
    array[primeiro], array[b] = array[b], array[primeiro]
    return b


v = [7, 75, 77, 94, 60, 76, 9, 12]
quickSort(v)
print(v)
