import itertools


def solve() -> int:
    """Find the maximum 16-digit string for a magic 5-gon ring using numbers 1 to 10.
    
    Time Complexity: O(10!)
    Space Complexity: O(1)
    """
    max_string = 0

    for perm in itertools.permutations(range(1, 11)):
        o0, o1, o2, o3, o4, i0, i1, i2, i3, i4 = perm

        # Canonical starting node condition: lowest external node
        if o0 != min(o0, o1, o2, o3, o4):
            continue

        s0 = o0 + i0 + i1
        s1 = o1 + i1 + i2
        s2 = o2 + i2 + i3
        s3 = o3 + i3 + i4
        s4 = o4 + i4 + i0

        if s0 == s1 == s2 == s3 == s4:
            s_concat = f"{o0}{i0}{i1}{o1}{i1}{i2}{o2}{i2}{i3}{o3}{i3}{i4}{o4}{i4}{i0}"
            if len(s_concat) == 16:
                max_string = max(max_string, int(s_concat))

    return max_string
