def solve() -> int:
    """Find unique positive integer whose square has form 1_2_3_4_5_6_7_8_9_0.
    
    Time Complexity: O((sqrt(1.93e16) - sqrt(1.02e16)) / 10)
    Space Complexity: O(1)
    """
    min_y = 101010101
    max_y = 138902662

    for y in range(101010103, max_y + 1, 10):
        y2_str = str(y * y)
        if (
            y2_str[0] == '1'
            and y2_str[2] == '2'
            and y2_str[4] == '3'
            and y2_str[6] == '4'
            and y2_str[8] == '5'
            and y2_str[10] == '6'
            and y2_str[12] == '7'
            and y2_str[14] == '8'
        ):
            return y * 10

    for y in range(101010107, max_y + 1, 10):
        y2_str = str(y * y)
        if (
            y2_str[0] == '1'
            and y2_str[2] == '2'
            and y2_str[4] == '3'
            and y2_str[6] == '4'
            and y2_str[8] == '5'
            and y2_str[10] == '6'
            and y2_str[12] == '7'
            and y2_str[14] == '8'
        ):
            return y * 10

    return 0
