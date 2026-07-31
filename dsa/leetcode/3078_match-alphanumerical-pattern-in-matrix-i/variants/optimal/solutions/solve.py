def solve(board: list[list[int]], pattern: list[str]) -> list[int]:
    board_rows = len(board)
    board_columns = len(board[0])
    pattern_rows = len(pattern)
    pattern_columns = len(pattern[0])

    if pattern_rows > board_rows or pattern_columns > board_columns:
        return [-1, -1]

    for top in range(board_rows - pattern_rows + 1):
        for left in range(board_columns - pattern_columns + 1):
            symbol_to_digit: dict[str, int] = {}
            digit_to_symbol: dict[int, str] = {}
            matches = True

            for row in range(pattern_rows):
                for column in range(pattern_columns):
                    symbol = pattern[row][column]
                    digit = board[top + row][left + column]

                    if symbol.isdigit():
                        if digit != int(symbol):
                            matches = False
                            break
                        continue
                    if symbol in symbol_to_digit and symbol_to_digit[symbol] != digit:
                        matches = False
                        break
                    if digit in digit_to_symbol and digit_to_symbol[digit] != symbol:
                        matches = False
                        break

                    symbol_to_digit[symbol] = digit
                    digit_to_symbol[digit] = symbol

                if not matches:
                    break

            if matches:
                return [top, left]

    return [-1, -1]
