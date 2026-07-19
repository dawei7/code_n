class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        login_hour, login_minute = map(int, loginTime.split(":"))
        logout_hour, logout_minute = map(int, logoutTime.split(":"))
        start = 60 * login_hour + login_minute
        end = 60 * logout_hour + logout_minute
        if end < start:
            end += 24 * 60

        first_round_start = ((start + 14) // 15) * 15
        last_round_end = (end // 15) * 15
        return max(0, (last_round_end - first_round_start) // 15)
