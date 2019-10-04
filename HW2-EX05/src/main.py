
def main():
    the_input = input("Enter a number\n>>")
    the_primes = find_primes_less_than(int(the_input))
    print(the_primes)


def find_primes_less_than(n):
    the_range = list(range(2, n))
    for i in the_range:
        for j in the_range:
            if j != i and j % i == 0:
                the_range.remove(j)
    return the_range


if __name__ == "__main__":
    main()
