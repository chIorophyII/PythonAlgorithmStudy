# 쿠키 구입

def solution(cookie):
    maximum = 0

    for i in range(len(cookie)-1):
        ob, yb = i, i+1
        ob_c, yb_c = cookie[ob], cookie[yb]

        while True:
            if ob_c == yb_c and ob_c > maximum:
                maximum = ob_c

            if ob_c <= yb_c and ob > 0:
                ob -= 1
                ob_c += cookie[ob]

            elif ob_c >= yb_c and yb < len(cookie)-1:
                yb += 1
                yb_c += cookie[yb]
                
            else:
                break

    return maximum