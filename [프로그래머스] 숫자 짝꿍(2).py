'''
문제 설명
두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다(X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.
'''


def solution(X, Y):
    answer = ''
    tmp = [0] * 10
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    min_num = ''
    tmp_num = 0
    for i in number:
        if i in X and i in Y:
            x = X.count(i)
            y = Y.count(i)
            min_num = min(x, y)
            tmp[int(i)] = min_num
            tmp_num = tmp_num + 1

    if tmp_num == 0:
        answer = '-1'
    else:
        for j in range(9, -1, -1):
            answer = answer + (str(j) * tmp[j])
    if '1' in answer or '2' in answer or '3' in answer or '4' in answer or '5' in answer or '6' in answer or '7' in answer or '8' in answer or '9' in answer:
        answer = answer
    else:
        answer = '0'

    return answer