import math
from itertools import combinations


def solve(n: int = 12) -> int:
    """Find F(n): sum of S(C_n)^4 over all n-card collections from the SET deck.

    SET Card Enumeration & Fourth Moment Computation.

    Each SET card has 4 attributes (shape, color, number, shading), each with 3 values.
    Cards are represented as 4-tuples from {0,1,2}^4, giving 81 total cards.
    Three cards form a SET if, for each attribute, the three values are all same or all different.

    S(C) = number of SETs in collection C. We compute F(n) = sum over all C(81,n) collections
    of S(C)^4.

    Using the linearity of expectation and moment expansion, S^4 can be expanded as
    a sum over 4-tuples of SETs. Each term equals the number of collections containing
    all four SETs.

    Time Complexity: O(T^4 / symmetry) where T = 1080 total SETs
    Space Complexity: O(T^2) for set pair intersection data
    """
    # Generate all 81 cards
    cards = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    cards.append((a, b, c, d))

    # Find all SETs (triples where each attribute sums to 0 mod 3)
    all_sets = []
    card_to_idx = {c: i for i, c in enumerate(cards)}

    for i in range(81):
        for j in range(i + 1, 81):
            # The third card completing the set is determined
            c3 = tuple((3 - cards[i][k] - cards[j][k]) % 3 for k in range(4))
            k_idx = card_to_idx[c3]
            if k_idx > j:
                all_sets.append((i, j, k_idx))

    T = len(all_sets)  # Should be 1080

    # Convert each SET to a frozenset of card indices for faster membership
    set_cards = [frozenset(s) for s in all_sets]

    # F(n) = sum_{C in C(81,n)} S(C)^4
    # = sum_{(s1,s2,s3,s4) in SETs^4} |{C : s1,s2,s3,s4 all in C}|
    # = sum_{(s1,s2,s3,s4)} C(81 - |s1 ∪ s2 ∪ s3 ∪ s4|, n - |s1 ∪ s2 ∪ s3 ∪ s4|)

    # For efficiency, group 4-tuples by their union size
    # Union of 4 SETs has between 3 (all same) and 12 (all disjoint) cards

    # Precompute C(81-u, n-u) for u = 3..12
    choose_cache = {}
    for u in range(3, 13):
        if n >= u:
            choose_cache[u] = math.comb(81 - u, n - u)
        else:
            choose_cache[u] = 0

    # For the 4th moment, enumerate all ordered 4-tuples of SETs
    # and compute the union size. This is T^4 = 1080^4 ≈ 1.36 * 10^12 — too large!

    # Instead, enumerate by union size using the multinomial structure.
    # Key insight: group the 4 SETs by their overlap pattern.

    # Faster approach: precompute pairwise intersections, then use
    # inclusion-exclusion over the 4 SETs.

    # For small T, enumerate pairs and use the moment formula:
    # E[S^4] = sum of 4th moments = sum over (s1,s2,s3,s4) of indicator products.

    # Alternative: compute M_k = sum_C S(C)^k using Newton's identities
    # from the power sums p_1, p_2, p_3, p_4 of the SET membership indicators.

    # p_r = sum_{(s_1,...,s_r)} C(81 - |union|, n - |union|)
    # where the sum is over ordered r-tuples of SETs.

    # p_1 = T * C(78, n-3)
    p1 = T * math.comb(78, n - 3)

    # p_2 = sum over ordered pairs (s1, s2) of C(81-|s1 ∪ s2|, n-|s1 ∪ s2|)
    # Enumerate all unordered pairs, compute union size, multiply by 2
    pair_counts = {}  # union_size -> count of unordered pairs
    for i in range(T):
        for j in range(i, T):
            u = len(set_cards[i] | set_cards[j])
            pair_counts[u] = pair_counts.get(u, 0) + (1 if i == j else 2)

    p2 = sum(cnt * math.comb(81 - u, n - u) for u, cnt in pair_counts.items() if n >= u)

    # p_3 = sum over ordered triples
    # This requires enumerating triples — T^3/6 ≈ 2*10^8, manageable
    triple_counts = {}
    for i in range(T):
        for j in range(i, T):
            uij = set_cards[i] | set_cards[j]
            for k in range(j, T):
                u = len(uij | set_cards[k])
                mult = 1
                if i == j == k:
                    mult = 1
                elif i == j or j == k:
                    mult = 3
                else:
                    mult = 6
                triple_counts[u] = triple_counts.get(u, 0) + mult

    p3 = sum(cnt * math.comb(81 - u, n - u) for u, cnt in triple_counts.items() if n >= u)

    # p_4 = sum over ordered quadruples
    # T^4/24 ≈ 5.6*10^10 — too large for brute force
    # Use: p_4 = sum_{i<=j<=k<=l} mult * C(81-u, n-u)
    # We can compute from the triple enumeration:
    quad_counts = {}
    for i in range(T):
        for j in range(i, T):
            uij = set_cards[i] | set_cards[j]
            for k in range(j, T):
                uijk = uij | set_cards[k]
                for l in range(k, T):
                    u = len(uijk | set_cards[l])
                    # Count ordered permutations
                    indices = [i, j, k, l]
                    distinct = len(set(indices))
                    if distinct == 4:
                        mult = 24
                    elif distinct == 3:
                        mult = 12
                    elif distinct == 2:
                        # Could be (a,a,b,b) or (a,a,a,b)
                        from collections import Counter
                        freq = Counter(indices)
                        vals = sorted(freq.values())
                        if vals == [1, 3]:
                            mult = 4
                        else:  # [2, 2]
                            mult = 6
                    else:
                        mult = 1
                    quad_counts[u] = quad_counts.get(u, 0) + mult

    p4 = sum(cnt * math.comb(81 - u, n - u) for u, cnt in quad_counts.items() if n >= u)

    # F(n) = sum S^4 = p4 (since S^4 = sum over ordered 4-tuples of indicators)
    return p4


if __name__ == "__main__":
    print(solve())
