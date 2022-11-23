'''
문제 설명
머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다. 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.
'''


def solution(babbling):
    answer = 0

    say = ['aya', 'ye', 'woo', 'ma']
    for i in babbling:
        tmp_i = i
        tmp = ''
        k = True
        if 'ayaaya' in i or 'yeye' in i or 'woowoo' in i or 'mama' in i:
            continue
        while k == True:
            if 'aya' in i:
                i = i.replace('aya', ' ', 1)
                tmp = tmp + 'aya'
            elif 'ye' in i:
                i = i.replace('ye', ' ', 1)
                tmp = tmp + 'ye'
            elif 'woo' in i:
                i = i.replace('woo', ' ', 1)
                tmp = tmp + 'woo'
            elif 'ma' in i:
                i = i.replace('ma', ' ', 1)
                tmp = tmp + 'ma'
            else:
                k = False

        if len(tmp) == len(tmp_i):
            answer = answer + 1

    return answer