def a():
    result = []
    for i in range(10000):
        result.append(i)
    return result


def b():
    return [i for i in range(10000)]

# 직접 이 모듈을 실행한 경우만 실행(Entry point)
# 다른 모듈에서 import 하는경우는 실행이 안되고, 직접 실행하는 경우만 아래가 호출되고 실행한다.
# 여기서는 함수 실행에걸린 시간 체크하는 예시
if __name__ == '__main__':
    import timeit
    print(timeit.timeit("a()", number=100, globals=globals()))
    print(timeit.timeit("b()", number=100, globals=globals()))