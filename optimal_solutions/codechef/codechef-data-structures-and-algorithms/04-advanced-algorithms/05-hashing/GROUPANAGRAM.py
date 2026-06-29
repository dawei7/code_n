from collections import defaultdict


def solve():
    def group_anagrams(strings):
        anagram_map = defaultdict(list)
        for s in strings:
            key = ''.join(sorted(s))
            anagram_map[key].append(s)
        return list(anagram_map.values())


if __name__ == "__main__":
    solve()
