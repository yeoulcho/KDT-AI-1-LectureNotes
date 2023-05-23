def bigger_than_20(num):
    return num > 20 # 20보다 큰 수만

def add_10(num):
    return num + 10

def times(num1, num2):
    return num1 * num2

def intersect(preList, postList):
    retList = []
    for x in preList:
        if x in postList:
            retList.append(x)

    return retList

#원본 파괴하지 않을때 사용하면 된다 (+영상 처리할때도 가능)
# 두개의 x 주소가 다름 (복사),
# x[:] 는 데이터만 복사하는데 별개의 데이터가 만들어진다. 별도의 객체를 만들어줌 (new를 만든거랑 같음)
def change(x):
    x = x[:]
    x[0] = 'H'
    print("in function =", x)

def change2(x):
    x[0] = 'H'

glob = 1

def xChgScope(num):
    global glob
    glob = 7
    return glob + num

import random
import math # 수학라이브러리

def functions_test():
    numList = [res for res in range(10, 31, 5)]
    filteredNumList = filter(bigger_than_20, numList)

    for num in filteredNumList:
        print("element: {0}".format(num))

    print(filteredNumList)
    print(type(filteredNumList))

    print(list(filter(bigger_than_20, numList)))
    print(list(filter(lambda i: i > 20, numList)))

    for i in map(add_10, numList):
        print("num: {0}".format(i))

    print(list(map((lambda i: i + 10), numList)))
    print(times)
    print(times(10, 10))

    functions_address = times
    print(functions_address(10, 10))

    list1 = "apple"
    list2 = "grape"
    list3 = "banana"

    print(intersect(list1, list2))
    print(intersect(list1, list3))

    wordList = ['J', 'A', 'M']
    print(wordList)

    change(wordList)
    print(wordList)

    change2(wordList)
    print(wordList)

    print(glob)
    print(xChgScope(3))
    print(glob) # 전역 변수 값을 7로 바꿈

    for _ in range(5):
        print(random.randrange(3, 7)) # 3 ~ 6

    print(math.pow(3, 4))
    print(3 ** 4)

    print(math.sqrt(9))