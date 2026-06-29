# cook your dish here
from collections import Counter


def solve():
    for _ in range(int(input())):
        n = int(input())
        s = list(map(int, list(input())))
        t = list(map(int, list(input())))

        c = Counter(zip(s, t))
        allrounders = c[(1,1)]
        if allrounders >= n // 2:
            teams = n // 2
        else:
            beginners = c[(0,0)]
            knows_p_lang = c[(1,0)]
            knows_e_lang = c[(0,1)]
            teams = 0
            if allrounders > 0:
                part_1 = min(allrounders, beginners)
                allrounders -= part_1
                teams += part_1
            part_3 = min(knows_p_lang, knows_e_lang)
            teams += part_3
            if allrounders > 0:
                part_2 = min(allrounders, 
                             max(knows_p_lang, knows_e_lang) - part_3)
                teams += part_2
                allrounders -= part_2
            if allrounders > 1:
                part_4 = allrounders // 2
                teams += part_4
        print(teams)


if __name__ == "__main__":
    solve()
