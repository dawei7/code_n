# cook your dish here


def solve():
    for T in range(int(input())):

        # "N" is the desired length
        # "K" is the current length
        # "A" is the current array
        N,K = map(int,input().split())
        A = list(map(int,input().split()))

        # Set the first subarray in P,
        # so the conditions within the loop can be possible
        final_list = [A[0]] + [i for i in range(1,A[0])]

        # Append the rest of the subarraies
        for i in range(1,K):
            final_list.append(A[i])
            final_list += [j for j in range(A[i-1]+1,A[i])]

        # Print
        print(*final_list)


if __name__ == "__main__":
    solve()
