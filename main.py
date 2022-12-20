from random import randint
mas = [randint(0, 100) for a in range(10)]

def merge_mas(a,b):
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c


def split_and_merge(a):
    n = len(a) // 2
    a1, a2 = a[:n], a[n:]

    if len(a1) > 1:
        a1 = split_and_merge(a1)
    if len(a2) > 1:
        a2 = split_and_merge(a2)

    return merge_mas(a1, a2)

print(mas)
arr = split_and_merge(mas)
print(arr)

'''
Сложность алгоритма будет одинакова во всех случаях и равняется O(n log n)
идея алгоритма заключается в разделении массива на 2 примерно равные(или равные) части, дальше сортируются 2 эти части 
раздельно и соединяются в единый массив обратно.
'''