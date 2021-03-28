def solution(l):
    l.sort(reverse=True)
    new_l=[]
    j=1
    i=len(l)
    while i>=0:
        if sum(l)==0:
            break
        if sum(l) % 3 == 0:
            return "".join(map(str, l))
        i-=1
        for k in reversed(range(len(l))):
            new_l.append(l[:k] + l[k+1:])
        l = new_l[0]
        for com in new_l:
            if sum(com)%3==0:
                l=com
                break
    return 0


print(solution([3,1,1]))