'''
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

제한 사항
arr은 길이 1이상, 15이하인 배열입니다.
arr의 원소는 100 이하인 자연수입니다.
'''


def solution(arr):
    answer = 1
    stack = []
    tmp = [0] * 100
    count = [0] * 100
    arr_acc = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in arr:
        stack = []
        while i > 1:
            if i % 2 == 0:
                i = i // 2
                stack.append(2)
            elif i % 3 == 0:
                i = i // 3
                stack.append(3)
            elif i % 5 == 0:
                i = i // 5
                stack.append(5)
            elif i % 7 == 0:
                i = i // 7
                stack.append(7)
            elif i % 11 == 0:
                i = i // 11
                stack.append(11)
            elif i % 13 == 0:
                i = i // 13
                stack.append(13)
            elif i % 17 == 0:
                i = i // 17
                stack.append(17)
            elif i % 19 == 0:
                i = i // 19
                stack.append(19)
            elif i % 23 == 0:
                i = i // 23
                stack.append(23)
            elif i % 29 == 0:
                i = i // 29
                stack.append(29)
            elif i % 31 == 0:
                i = i // 31
                stack.append(31)
            elif i % 37 == 0:
                i = i // 37
                stack.append(37)
            elif i % 41 == 0:
                i = i // 41
                stack.append(41)
            elif i % 43 == 0:
                i = i // 43
                stack.append(43)
            elif i % 47 == 0:
                i = i // 47
                stack.append(47)
            elif i % 53 == 0:
                i = i // 53
                stack.append(53)
            elif i % 59 == 0:
                i = i // 59
                stack.append(59)
            elif i % 61 == 0:
                i = i // 61
                stack.append(61)
            elif i % 67 == 0:
                i = i // 67
                stack.append(67)
            elif i % 71 == 0:
                i = i // 71
                stack.append(71)
            elif i % 73 == 0:
                i = i // 73
                stack.append(73)
            elif i % 79 == 0:
                i = i // 79
                stack.append(79)
            elif i % 83 == 0:
                i = i // 83
                stack.append(83)
            elif i % 89 == 0:
                i = i // 89
                stack.append(89)
            elif i % 97 == 0:
                i = i // 97
                stack.append(97)

        uni = list(set(stack))
        for i in uni:
            m = stack.count(i)
            k = max(count[i], m)
            count[i] = k

    for l in range(len(count)):
        if count[l] != 0:
            answer = answer * (l ** count[l])

    return answer