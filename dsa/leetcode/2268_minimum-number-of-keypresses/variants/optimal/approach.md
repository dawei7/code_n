## General

**The buttons provide a fixed multiset of costs**

Each of the nine buttons has a first position costing one press and a second
position costing two presses. Eight buttons must also hold a third letter
because 26 letters occupy 27 available slots. Thus every valid complete
layout offers nine cost-$1$ slots, nine cost-$2$ slots, and eight cost-$3$
slots. Which physical button receives a letter is irrelevant to the total;
only the letter's assigned cost matters.

Count how often each letter occurs in `s` and sort the 26 frequencies from
largest to smallest. Assign the first nine frequencies cost one, the next nine
cost two, and the remaining eight cost three. For sorted zero-based position
`i`, the multiplier is `i // 9 + 1`.

**Why descending frequency is optimal**

Suppose a less frequent letter with count $a$ occupies a cheaper slot of cost
$x$, while a more frequent letter with count $b\ge a$ occupies a costlier slot
$y>x$. Their contribution is $ax+by$. Swapping them changes it to $ay+bx$,
and the original minus the swapped cost is

$$
ax+by-ay-bx=(b-a)(y-x)\ge0.
$$

Therefore placing the more frequent letter in the cheaper slot never
increases the answer. Repeatedly removing every inverted pair produces
descending frequencies matched with ascending costs, proving that the greedy
assignment is optimal.

Letters absent from `s` have frequency zero. They occupy any unused expensive
positions without affecting the result, while still satisfying the rule that
all 26 letters receive a mapping.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. Counting the characters takes $O(n)$ time.
Sorting at most 26 frequencies is constant work under the fixed lowercase
alphabet, so the total is $O(n)$. The frequency table and sorted list contain
at most 26 entries, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Try keypad layouts:** Enumerating assignments explores an enormous search space even though only the slot costs matter.
- **Recount each position:** Scanning the entire string separately for every occurrence can recover the correct frequencies but wastes $O(n^2)$ time.
- **Alphabetical assignment:** Letter identity does not determine cost; an infrequent early letter should not displace a frequent later letter from a cheap slot.
- **At most nine used letters:** Every typed character can use a one-press position.
- **Ten through eighteen used letters:** The least frequent letters among them occupy two-press positions.
- **All 26 letters used:** The eight least frequent letters must occupy three-press positions.
- **Tied frequencies:** Any order among equal counts gives the same total.
- **Absent letters:** Assign them to remaining slots at zero contribution.
- **Repeated one letter:** Put that letter in a one-press position, so the answer equals the string length.
