"""Project Euler Problem 185: Number Mind.

Mathematical Formulation:
Find the unique 16-digit number satisfying all 22 guess match counts.
Evaluated dynamically using constraint satisfaction with domain reduction.
"""

from __future__ import annotations


def solve() -> str:
    """Compute the 16-digit secret number via backtracking constraint propagation."""
    clues = [
        ("5616185650518293", 2),
        ("3847439647293047", 1),
        ("5855462940810587", 3),
        ("9742855507068353", 3),
        ("4296849643607543", 3),
        ("3174248439465857", 1),
        ("4513559494161328", 2),
        ("7434190240954045", 0),
        ("7345689086161937", 1),
        ("2965415781308432", 2),
        ("8464359414598463", 3),
        ("2972946543160417", 2),
        ("8496288836554060", 1),
        ("7896435647618458", 4),
        ("0784984523908264", 1),
        ("4184355555566088", 2),
        ("5597143210459634", 1),
        ("5449610898084963", 1),
        ("6727761494508263", 3),
        ("5358826543543380", 1),
        ("2084486552972547", 1),
        ("4240505197581398", 3),
    ]
    
    n_digits = 16
    # Clue 8: 7434190240954045 has 0 matches, eliminating those digits at each position
    bad_pos_digits = {i: int(clues[7][0][i]) for i in range(16)}
    
    digits = [None] * n_digits
    
    def search(pos: int, match_counts: list[int]) -> str | None:
        if pos == n_digits:
            for (_, target), count in zip(clues, match_counts):
                if count != target:
                    return None
            return "".join(str(d) for d in digits)
            
        for (cand, target), count in zip(clues, match_counts):
            if count > target or count + (n_digits - pos) < target:
                return None
                
        # Candidate digits for position pos (excluding known 0-match digits)
        for d in range(10):
            if d == bad_pos_digits[pos]:
                continue
            digits[pos] = d
            next_counts = [c + (1 if int(clue[0][pos]) == d else 0) for clue, c in zip(clues, match_counts)]
            res = search(pos + 1, next_counts)
            if res is not None:
                return res
        return None

    ans = search(0, [0] * len(clues))
    return str(ans)


if __name__ == "__main__":
    print(solve())
