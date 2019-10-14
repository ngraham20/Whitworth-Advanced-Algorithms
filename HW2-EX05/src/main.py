
def main():
    the_input = input("Enter a number\n>>")
    the_primes = find_primes_less_than(int(the_input))
    the_sieve = sieve(int(the_input))
    print(the_sieve)


def find_primes_less_than(n):
    the_range = list(range(2, n))
    for i in the_range:
        for j in the_range:
            if j != i and j % i == 0:
                the_range.remove(j)
    return the_range

def sieve(n):
    the_range = list(range(n))  # initialize the list of numbers ranging from 0 to n-1
    for i in the_range:  # for every number from 0 to n-1
        for j in range(i*i, n, i): # from i^2 to n, in increments of i
            the_range[0] = 0  # set to 0

    the_range = filter(lambda a: a != 0, the_range)  # filter out all 0s from the final list
    return the_range

if __name__ == "__main__":
    main()
