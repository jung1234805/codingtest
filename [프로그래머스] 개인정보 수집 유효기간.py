'''
고객의 약관 동의를 얻어서 수집된 1~n번으로 분류되는 개인정보 n개가 있습니다. 약관 종류는 여러 가지 있으며 각 약관마다 개인정보 보관 유효기간이 정해져 있습니다. 당신은 각 개인정보가 어떤 약관으로 수집됐는지 알고 있습니다. 수집된 개인정보는 유효기간 전까지만 보관 가능하며, 유효기간이 지났다면 반드시 파기해야 합니다.

예를 들어, A라는 약관의 유효기간이 12 달이고, 2021년 1월 5일에 수집된 개인정보가 A약관으로 수집되었다면 해당 개인정보는 2022년 1월 4일까지 보관 가능하며 2022년 1월 5일부터 파기해야 할 개인정보입니다.
당신은 오늘 날짜로 파기해야 할 개인정보 번호들을 구하려 합니다.

모든 달은 28일까지 있다고 가정합니다.

다음은 오늘 날짜가 2022.05.19일 때의 예시입니다.
'''


def solution(today, terms, privacies):
    answer = []
    dic = {}

    day = int(today.replace('.', ''))

    for j in terms:
        tmp = j.split(' ')
        k = tmp[0]
        e = tmp[1]
        dic[k] = e

    for i in range(len(privacies)):
        tmp = privacies[i].split('.')
        y = int(tmp[0])
        m = int(tmp[1])
        t = tmp[2]
        u = t.split(' ')
        d = u[0]
        term = u[1]

        due = int(dic[term])

        if m + due > 12:
            new_year = (m + due) // 12
            new_month = (m + due) % 12
            m = (m + due) - 12 * new_year
            y = y + new_year
        else:
            m = m + due

        y = str(y)

        if m < 10:
            m = '0' + str(m)
        else:
            m = str(m)
        db = str(y) + m + d

        if int(db) <= day:
            answer.append(i + 1)

    return answer