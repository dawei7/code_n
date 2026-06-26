"""Optimal solution for linked_list_03: Merge Two Sorted Lists.

Two-pointer walk. On each step, attach the smaller of the two
heads to the merged tail and advance that head. Append the
remaining tail of the non-empty list. Return the merged
``(values, next)`` representation.
"""


def solve(values1, next1, head1, values2, next2, head2, n1, n2):
    if n1 == 0:
        merged = list(values2)
    elif n2 == 0:
        merged = list(values1)
    else:
        merged = []
        i, j = head1, head2
        while i != -1 and j != -1:
            if values1[i] <= values2[j]:
                merged.append(values1[i])
                i = next1[i]
            else:
                merged.append(values2[j])
                j = next2[j]
        while i != -1:
            merged.append(values1[i])
            i = next1[i]
        while j != -1:
            merged.append(values2[j])
            j = next2[j]
    n = len(merged)
    merged_nxt = [k + 1 for k in range(n - 1)] + [-1]
    return merged, merged_nxt
