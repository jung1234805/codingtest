import math


def solution(fees, records):
    answer = []
    enter = {}
    cal = {}
    for i in records:
        s = i.split(' ')
        time = s[0].split(':')
        hour = time[0]
        minu = time[1]
        total = (int(hour) * 60) + int(minu)
        cost = 0
        if s[2] == 'IN':
            enter[s[1]] = total
        else:
            in_time = enter[s[1]]
            del enter[s[1]]
            spend_t = total - in_time
            if s[1] in cal:
                cal[s[1]] += spend_t
            else:
                cal[s[1]] = spend_t

    if len(enter) != 0:
        for i in enter:
            spend_t = 1439 - enter[i]
            if i in cal:
                cal[i] += spend_t
            else:
                cal[i] = spend_t

    cal = dict(sorted(cal.items()))
    for i in cal:
        if cal[i] <= fees[0]:
            answer.append(fees[1])
        else:
            fee = fees[1] + (math.ceil((cal[i] - fees[0]) / fees[2])) * fees[3]
            answer.append(fee)

    return answer