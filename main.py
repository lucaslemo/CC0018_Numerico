import numpy as np

DELTA = np.float64(2**-53)


def testa_onde(p, q, r):
    l1 = [np.float64(1)]
    l2 = [np.float64(1)]
    l3 = [np.float64(1)]
    l1.extend(p)
    l2.extend(q)
    l3.extend(r)
    mat = np.array([l1, l2, l3])
    det = np.linalg.det(mat)
    return np.sign(det)


def main():
    global DELTA
    o = [np.float64(0), DELTA*17]
    p = [np.float64(12), np.float64(12)]
    q = [np.float64(24), np.float64(24)]
    r = o
    while r[0] <= 34*DELTA:
        print("({} | {})".format(r[0]/DELTA, r[1]/DELTA))
        if testa_onde(p, q, [r[0] + DELTA, r[1]]) > 0:
            print("Rota 01")
            r[1] -= DELTA
            r[0] += DELTA
        else:
            print("Rota 02")
            r[1] += DELTA
            r[0] += DELTA


if __name__ == '__main__':
    main()
