# cook your dish here


def solve():
    for i in range(int(input())):
        u_initial_speed, v_end_speed, a_accelaration, s_distance = map(int,input().split())
        measure_v = (u_initial_speed**2)-(2*a_accelaration*s_distance)
        if measure_v>(v_end_speed**2):
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    solve()
