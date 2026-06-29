# cook your dish here


def solve():
    for T in range(int(input())):

        R,C = map(int, input().strip().split())

        Rows = []
        for i in range(R):
            Rows.append(input().strip())

        count = 0
        for i in range(2,R-2):
            for j in range(2,C-2):

                if Rows[i][j] == '#':
                    continue

                To = False
                if Rows[i-1][j] == '^' and Rows[i-2][j] == '^':
                    To = True

                Bo = False
                if Rows[i+1][j] == '^' and Rows[i+2][j] == '^':
                    Bo = True

                Le = False
                if Rows[i][j-1] == '^' and Rows[i][j-2] == '^':
                    Le = True

                Ri = False
                if Rows[i][j+1] == '^' and Rows[i][j+2] == '^':
                    Ri = True


                if Le and Ri and To and Bo:
                    count += 1

        print(count)


if __name__ == "__main__":
    solve()
