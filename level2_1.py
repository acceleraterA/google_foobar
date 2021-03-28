def solution(l):

    #'1.2.1' -> [1, 2 ,1]

    l.sort(key=lambda s: list(map(int, s.split('.'))))
    return l
l=["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]
solution(l)
print(solution(l))