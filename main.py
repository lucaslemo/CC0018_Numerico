import numpy as np

DELTA = np.float64(2**-53)


def testa_onde(p, q, r):
    mat = np.array([p, q, r])
    det = np.linalg.det(mat)
    print(det)
    return np.sign(det)


def main():
    global DELTA
    o = [np.float64(1), np.float64(0), DELTA*17]
    p = (np.float64(1), np.float64(12), np.float64(12))
    q = (np.float64(1), np.float64(24), np.float64(24))
    r = o
    count = 0
    while r[1] <= DELTA*34:
        valida = testa_onde(p, q, r)
        # print(valida, count, r)
        r[1] += DELTA
        count += 1
        '''if valida == 1:
            pass
        else:
            print("O robo colidiu com a parede!")
            break'''


if __name__ == '__main__':
    main()
