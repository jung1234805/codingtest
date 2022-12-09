'''
신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.

각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.
'''


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    tmp_answer = {}
    tmp = {}
    stop = {}
    ban = []
    for j in id_list:
        stop[j] = 0

    for i in report:
        s = i.split(' ')
        if (s[0] in tmp) == True and s[1] not in tmp[s[0]]:
            tmp[s[0]].append(s[1])
            stop[s[1]] += 1
        elif (s[0] in tmp) == True and s[1] in tmp[s[0]]:
            continue
        elif (s[0] in tmp) == False:
            tmp[s[0]] = [s[1]]
            stop[s[1]] += 1

    for s in stop:
        if stop[s] >= k:
            ban.append(s)

    for l in tmp:
        count = 0
        count = len(list(set(tmp[l]) & set(ban)))
        tmp_answer[l] = count

    p = 0
    for o in id_list:
        if o not in tmp_answer:
            answer[p] = 0
            p += 1
        else:
            answer[p] = tmp_answer[o]
            p += 1

    return answer