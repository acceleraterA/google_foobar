def solution(i):
    string = ""
    for num in range(2, 30007):
        if all(num % j != 0 for j in range(2, num)):
            string += str(num)
    return string[i : i + 5]
