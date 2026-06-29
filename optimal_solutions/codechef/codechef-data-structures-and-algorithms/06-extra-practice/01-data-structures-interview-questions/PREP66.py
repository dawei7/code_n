# cook your dish here


def solve():
    class treeNode:
        def __init__(self, data):
            self.data = data
            self.links = []

    T = int(input())

    def treeHeight(n, np):
        if not n:
            return 0 
        elif len(n.links) == 0 or (len(n.links) == 1 and n.links[0]==np):
            return 1
        else:
            return max([treeHeight(c, n) for c in n.links if c != np]) + 1

    for _ in range(T):
        N = int(input())
        nodes = {}
        for n in range(N-1):
            a, b = map(int, input().split())
            if not a in nodes:
                na = treeNode(a)
                nodes[a] = na
            else:
                na = nodes[a]
            nb = treeNode(b)
            nodes[b] = nb
            nodes[a].links.append(nb)
            nodes[b].links.append(na)
        root = nodes[1]
        print(treeHeight(root, None))


if __name__ == "__main__":
    solve()
