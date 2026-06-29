# cook your dish here


def solve():
    T = int(input().strip())  # Number of test cases

    for _ in range(T):
        N, R = map(int, input().strip().split())  # Number of sweets and amount of money Chef has
        A = list(map(int, input().strip().split()))  # Cost of each sweet
        B = list(map(int, input().strip().split()))  # Cashback for each sweet

        # Create a list of (cost, cashback) pairs and sort it by effective cost
        sweets = sorted(zip(A, B), key=lambda x: x[0] - x[1])

        cnt = 0  # Counter for the number of sweets bought

        for a, b in sweets:
            effective_cost = a - b
            if R >= a:
                # Calculate how many of this sweet can be bought in one go
                n_sweets = (R - b) // effective_cost


                R -= n_sweets * effective_cost
                cnt += n_sweets


        print(cnt)


if __name__ == "__main__":
    solve()
