def myStrategy(myscore, theirscore, last):
    k = myscore - theirscore
    l = theirscore - myscore
    x = 100 - myscore
    if myscore == 0:
        return 32
    if theirscore == 100 and myscore!= 100:
        return 1
    if myscore == 99 or myscore == 100:
        return 0
    if k >= 10:
        if myscore == 97 or myscore == 98:
            return 0
        if myscore >92 and myscore <= 96:
            return 1
        if myscore >= 91 and myscore <= 92:
            return 2
    if k >= 20:
        if myscore >= 80:
            return x// 3.
        if myscore >= 72:
            return x//3.40
    if k >= 1 and k <= 2 and (myscore == 97): 
         return 1 
    if k==0:
        if myscore == 98 or myscore == 1:
            return 1
    if l >= 1 and l <=3 :
            if theirscore >= 95:
                if myscore >= 91 and myscore <= 94:
                    return 2
                if myscore >= 95 and myscore <= 98:
                    return 1 
    if l >= 8:
        if theirscore >= 85:
            return x//3.1
    if l >= 4:
        if theirscore >= 92:
            if myscore == 96 or myscore == 97 or myscore == 95 or myscore == 98:
                return 1
            if myscore == 94 or myscore == 93:
                return 2
            if myscore == 91:
                return 3
        else:
            return x//3.30
    if myscore == 98:
        return 0
    if x >= 40:
        return x//2.8
    if x >= 30:
        return x//2.92
    if x >= 20:
        return x//3.06
    if x >= 10:
        return x//3.2
    if x >= 4:
        return x//3.35
    if x == 3:
        return 1