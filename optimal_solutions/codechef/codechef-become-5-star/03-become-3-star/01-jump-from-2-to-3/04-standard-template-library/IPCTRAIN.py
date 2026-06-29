import sys
import bisect

def solve():
    num_participants, max_days = map(int, input().split())
    days = [0] * num_participants
    trials = [0] * num_participants
    score = [0] * num_participants
    participants = []
    total_score = 0
    for i in range(num_participants):
        days[i], trials[i], score[i] = map(int, input().split())
        participants.append((score[i], i))
        total_score += score[i] * trials[i]
    participants.sort(reverse=True, key=lambda x: x[0])
    available_days = list(range(1, max_days + 1))
    for score_val, participant_index in participants:
        while trials[participant_index] > 0:
            pos = bisect.bisect_left(available_days, days[participant_index])
            if pos == len(available_days):
                break
            available_days.pop(pos)
            total_score -= score[participant_index]
            trials[participant_index] -= 1
    print(total_score)

def main():
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    assert 1 <= t <= 10
    idx = 1
    for _ in range(t):
        num_participants, max_days = map(int, data[idx].split())
        participants_info = data[idx + 1:idx + 1 + num_participants]
        days, trials, score = ([], [], [])
        total_score = 0
        participants = []
        for i in range(num_participants):
            d, tr, sc = map(int, participants_info[i].split())
            days.append(d)
            trials.append(tr)
            score.append(sc)
            participants.append((sc, i))
            total_score += sc * tr
        participants.sort(reverse=True, key=lambda x: x[0])
        available_days = list(range(1, max_days + 1))
        for score_val, participant_index in participants:
            while trials[participant_index] > 0:
                pos = bisect.bisect_left(available_days, days[participant_index])
                if pos == len(available_days):
                    break
                available_days.pop(pos)
                total_score -= score[participant_index]
                trials[participant_index] -= 1
        print(total_score)
        idx += num_participants + 1


if __name__ == "__main__":
    solve()
