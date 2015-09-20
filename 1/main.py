__author__ = 'Eddie'

UPPER_BOUND = 1000

def solve():
    """
    Solves the problem
    :return: Int
    """

    total = 0
    # Do 5's first
    cur_num = 5
    while cur_num < UPPER_BOUND:
        total += cur_num
        cur_num += 5

    # Now 3's
    cur_num = 3
    while cur_num < UPPER_BOUND:
        # Ignore multiples of 5 since we have already added them
        if cur_num % 5 != 0:
            total += cur_num
        cur_num += 3

    return total

if __name__ == "__main__":
    answer = solve()
    print "The answer is: {0}".format(answer)