class Solution:
    def numberOfWays(self, corridor: str) -> int:
        modulo = 1_000_000_007
        seat_count = 0
        previous_second_seat = -1
        ways = 1

        for index, cell in enumerate(corridor):
            if cell != "S":
                continue

            seat_count += 1
            if seat_count > 2 and seat_count % 2 == 1:
                ways = ways * (index - previous_second_seat) % modulo
            if seat_count % 2 == 0:
                previous_second_seat = index

        return ways if seat_count > 0 and seat_count % 2 == 0 else 0
