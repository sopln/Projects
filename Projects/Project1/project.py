def myStrategy(myscore, theirscore, last):
    if myscore == 0:
        return 32
    if myscore >= 50 and myscore <= 55:
        return 18
    if myscore > 55 and myscore <= 60:
        return 16
    if myscore > 60 and myscore <= 65:
        return 14
    if myscore > 65 and myscore <= 70:
        return 12
    if myscore > 70 and myscore <= 75:
        return 10
    if myscore > 75 and myscore <= 80:
        return 8
    if myscore > 80 and myscore <= 85:
        return 6
    if myscore > 85 and myscore <= 90:
        return 4
    if myscore > 90 and myscore <= 93:
        return 3
    if myscore > 93 and myscore <= 97:
        return 2
    if myscore >= 98:
        return 0