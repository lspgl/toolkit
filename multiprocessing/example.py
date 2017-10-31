from parmap import Parmap
import time


def function(x, fixed, print_string='None'):
    print(print_string)
    print('simulating long calculation...')
    time.sleep(1)
    return x**fixed


def main():
    a = [0, 1, 10, 15]
    exponent = 2
    t0 = time.time()
    b = Parmap(function, a, exponent, print_string='Im a process')
    print('computed b = ', end='')
    print(b)
    print('Time taken: ', str(round(time.time() - t0, 2)))


if __name__ == '__main__':
    main()
