class Solution:
    def countTime(self, time: str) -> int:
        if time[0] == "?" and time[1] == "?":
            hours = 24
        elif time[0] == "?":
            hours = 3 if time[1] <= "3" else 2
        elif time[1] == "?":
            hours = 10 if time[0] <= "1" else 4
        else:
            hours = 1

        if time[3] == "?" and time[4] == "?":
            minutes = 60
        elif time[3] == "?":
            minutes = 6
        elif time[4] == "?":
            minutes = 10
        else:
            minutes = 1

        return hours * minutes
