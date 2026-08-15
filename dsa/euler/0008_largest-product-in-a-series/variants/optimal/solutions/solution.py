import math


def solve(k: int = 13) -> int:
    """Find the k adjacent digits in the 1000-digit number with the greatest product.

    Mathematical Principles Applied:
    1. Sliding Window Multiplication:
       Given a string of N = 1000 decimal digits, we evaluate the product of contiguous
       blocks of size k = 13:
       P_i = d_i * d_{i+1} * ... * d_{i+k-1} for 0 <= i <= N - k.

    2. Zero-Segment Skipping:
       If any digit within the 13-digit window is '0', the product is 0.
       We skip window evaluations containing '0' to avoid redundant multiplications.

    Time Complexity: O(N * k) where N = 1000 and k = 13 (988 window checks).
    Space Complexity: O(N) to store digit sequence.
    """
    # The 1000-digit number represented as a contiguous string
    series = (
        "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843"
        "8586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557"
        "6689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749"
        "3035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776"
        "6572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397"
        "5369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474"
        "8216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586"
        "1786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408"
        "0719840385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717606"
        "0588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    )

    # Track maximum product found across all 13-digit windows
    max_product = 0

    # Slide window of size k from index 0 to N - k
    for i in range(len(series) - k + 1):
        window_str = series[i : i + k]

        # Skip windows containing digit '0' (product is trivially 0)
        if "0" in window_str:
            continue

        # Multiply all 13 digits in the current window
        prod = math.prod(int(d) for d in window_str)

        # Update maximum product if current window product is larger
        if prod > max_product:
            max_product = prod

    # Return the maximum 13-digit product
    return max_product


if __name__ == "__main__":
    print(solve())
