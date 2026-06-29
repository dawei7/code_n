# cook your dish here
# cook your dish here
# cook your dish here


def solve():
    def maximal_moves(s):

        count = 0
        try:
            while "C" in s and "H" in s and "E" in s and "F" in s:
                c_index = s.index("C")
                h_index = s.index("H", c_index)
                e_index = s.index("E", h_index)
                f_index = s.index("F", e_index)

                s = s[:c_index] + s[c_index+1:h_index] + s[h_index+1:e_index] + s[e_index+1:f_index] + s[f_index+1:]
                count += 1
        except ValueError:
            pass  # Ignore ValueError if any of "C", "H", "E", "F" is not present in the string

        return count

    # Input processing
    s = input().strip()

    # Output the result
    result = maximal_moves(s)
    print(result)


if __name__ == "__main__":
    solve()
