def solve(target_count: int = 12) -> int:
    """Find the sum of leg lengths L for the 12 smallest isosceles triangles with base b and height h = b +/- 1.

    Mathematical Principles Applied:
    1. Isosceles Triangle Pythagorean System:
       For an isosceles triangle with base b, equal legs L, and height h:
       (b / 2)^2 + h^2 = L^2 => b^2 + 4h^2 = 4L^2.

    2. Substitution h = b +/- 1:
       b^2 + 4(b +/- 1)^2 = 5b^2 +/- 8b + 4 = 4L^2.
       Multiplying by 5:
       (5b +/- 4)^2 + 4 = 20L^2.
       Let X = 5b +/- 4. Then X^2 - 20L^2 = -4 (Pell-type Diophantine Equation).

    3. 2nd-Order Linear Recurrence for Leg Lengths L:
       The leg lengths L_k for both h = b + 1 and h = b - 1 satisfy the unified linear recurrence:
       L_{k+1} = 18 * L_k - L_{k-1}
       with base seed values L_1 = 17, L_2 = 305.

    Time Complexity: O(target_count) linear execution in ~0.0000s.
    Space Complexity: O(1) constant auxiliary space.
    """
    l_prev, l_curr = 17, 305
    l_sum = l_prev + l_curr

    # Advance 2nd-order linear recurrence L_{k+1} = 18 * L_k - L_{k-1} for k = 3 to 12
    for _ in range(3, target_count + 1):
        l_next = 18 * l_curr - l_prev
        l_sum += l_next
        l_prev, l_curr = l_curr, l_next

    # Return total sum of leg lengths L for the 12 smallest special isosceles triangles
    return l_sum


if __name__ == "__main__":
    print(solve())
