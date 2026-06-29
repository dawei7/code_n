import sys
from collections import deque

def bfs_transform(A, B, word_set):
    if A == B:
        return 1
    L = len(A)
    q = deque()
    q.append((A, 1))
    visited = set()
    visited.add(A)
    while q:
        word, steps = q.popleft()
        for i in range(L):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch == word[i]:
                    continue
                new_word = word[:i] + ch + word[i + 1:]
                if new_word == B:
                    return steps + 1
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    q.append((new_word, steps + 1))
    return -1

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    result = []
    for _ in range(t):
        A = data[index]
        B = data[index + 1]
        index += 2
        m = int(data[index])
        index += 1
        words = data[index:index + m]
        index += m
        word_set = set(words)
        res = bfs_transform(A, B, word_set)
        result.append(str(res))
    sys.stdout.write('\n'.join(result))


if __name__ == "__main__":
    solve()
