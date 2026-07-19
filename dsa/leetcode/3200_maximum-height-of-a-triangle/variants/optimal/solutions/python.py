def solve(red: int, blue: int) -> int:
    def get_max_height(first_color: int, second_color: int) -> int:
        height = 0
        row = 1
        while True:
            if row % 2 == 1:
                if first_color >= row:
                    first_color -= row
                else:
                    break
            else:
                if second_color >= row:
                    second_color -= row
                else:
                    break
            height += 1
            row += 1
        return height

    # Try starting with red, then try starting with blue
    return max(get_max_height(red, blue), get_max_height(blue, red))
