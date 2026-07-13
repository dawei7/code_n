def solve(s: str) -> int:
    previous_run = 0
    current_run = 1
    answer = 0

    for index in range(1, len(s)):
        if s[index] == s[index - 1]:
            current_run += 1
        else:
            answer += min(previous_run, current_run)
            previous_run = current_run
            current_run = 1

    return answer + min(previous_run, current_run)
