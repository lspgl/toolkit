from parmap import Parmap
import time


def function(x, fixed, print_string='None'):
    print(print_string)
    # simulating long calculation
    time.sleep(1)
    return x**fixed


def main():
    a = [0, 1, 10, 15]
    exponent = 2
    statement = 'Im a function call!'
    t0 = time.time()
    print('Computing parallel')
    # parallelize 'function' over array 'a' with fixed parameters 'exponent' and 'statement'
    b = Parmap(function, a, exponent, print_string=statement)
    t1 = time.time() - t0
    print('computed b = ', end='')
    print(b)
    print('Time taken: ', str(round(t1, 2)))
    print()

    t2 = time.time()
    print('Computing serial')
    b_s = [function(a_s, exponent, print_string=statement) for a_s in a]
    t3 = time.time() - t2
    print('computed b = ', end='')
    print(b_s)
    print('Time taken: ', str(round(t3, 2)))
    print()
    speedup = t3 / t1
    print('Speedup x' + str(round(speedup, 2)))


if __name__ == '__main__':
    main()
