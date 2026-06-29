# cook your dish here


def solve():
    for _ in range(int(input())):
        seasons = int(input())
        intro_duration = list(map(int, input().split(" ")))
        watch_duration = 0
        for season in range(seasons):
            episode_info = list(map(int, input().split(" ")))
            no_of_episodes = episode_info[0]
            episode_durations = episode_info[1:]
            watch_duration += sum(episode_durations) - ((no_of_episodes - 1) * intro_duration[season])
        print(watch_duration)


if __name__ == "__main__":
    solve()
