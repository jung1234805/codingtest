'''
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
'''


def solution(s):
    answer = ''
    index = 0
    if len(s) % 2 != 0:
        index = (len(s) // 2) + 1
        answer = s[index - 1]
    else:
        index = len(s) // 2
        answer = s[index - 1] + s[index]

    return answer