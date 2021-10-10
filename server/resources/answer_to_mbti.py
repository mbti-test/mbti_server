def answer_to_mbti(answer):
    # 0: I T S J  1: E F N P

    mbti = ""
    if (int(answer[0]) + int(answer[3]) + int(answer[6])) > 1:
        mbti += "E"
    else:
        mbti += "I"

    if (int(answer[4]) + int(answer[5]) + int(answer[10])) > 1:
        mbti += "N"
    else:
        mbti += "S"

    if (int(answer[1]) + int(answer[2]) + int(answer[7])) > 1:
        mbti += "F"
    else:
        mbti += "T"

    if (int(answer[8]) + int(answer[9]) + int(answer[11])) > 1:
        mbti += "P"
    else:
        mbti += "J"

    return mbti
