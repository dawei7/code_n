import collections

def solve(ranks: list[int], suits: list[str]) -> str:
    """
    Determines the best poker hand among "Flush", "Three of a Kind", "Pair", or "High Card"
    given five card ranks and suits. The hierarchy is Flush > Three of a Kind > Pair > High Card.

    Args:
        ranks: A list of 5 integers representing the ranks of the cards (e.g., 1-13).
        suits: A list of 5 characters representing the suits of the cards (e.g., 'a', 'b', 'c', 'd').

    Returns:
        A string indicating the strongest hand: "Flush", "Three of a Kind", "Pair", or "High Card".
    """
    # 1. Check for Flush
    # A flush occurs if all five cards have the same suit.
    # We use a set to find the number of unique suits. If there's only one unique suit, it's a Flush.
    if len(set(suits)) == 1:
        return "Flush"

    # 2. Check for Three of a Kind, Pair, or High Card
    # If it's not a flush, we need to analyze the ranks.
    # Use a frequency counter (collections.Counter) to count occurrences of each rank.
    rank_counts = collections.Counter(ranks)

    # Check for Three of a Kind
    # Iterate through the counts of each rank. If any rank appears 3 or more times,
    # it's a Three of a Kind. This check comes before Pair because it's a stronger hand.
    for count in rank_counts.values():
        if count >= 3:
            return "Three of a Kind"

    # Check for Pair
    # If we reach here, it's not a Flush or Three of a Kind.
    # Now, check if any rank appears 2 or more times. If so, it's a Pair.
    for count in rank_counts.values():
        if count >= 2:
            return "Pair"

    # If none of the above conditions are met, it means there are no Flushes,
    # Three of a Kinds, or Pairs. All card ranks must be distinct.
    # Therefore, the hand is a High Card.
    return "High Card"
