## General
**Track distinct letters**

Scan the sentence and insert each character into a set. A repeated character leaves the set unchanged, while the first occurrence of a new character increases its size by one.

Because the input contains only lowercase English letters, the set can contain no more than 26 values. After the scan, the sentence is a pangram exactly when the set size is 26.

**Why the size test is sufficient**

There are exactly 26 permitted characters. A set of 26 distinct characters drawn only from that alphabet must contain every one of them. Conversely, if any letter is missing, at most 25 distinct permitted characters can be present. Therefore comparing the final size with 26 is equivalent to checking each alphabet letter individually.

The method does not depend on order or frequency. It treats a sentence with one copy of each letter and a sentence with many duplicate copies identically, as the definition requires.

## Complexity detail
Building the set examines all $n$ characters once, so time is $O(n)$. The set holds at most 26 letters. Since the alphabet size is fixed independently of $n$, its space is $O(1)$.

## Alternatives and edge cases
- **Boolean array:** Mark an index from 0 through 25 for each character; this has the same $O(n)$ time and fixed space while making the alphabet bound explicit.
- **Bit mask:** Set one of 26 bits per character and compare the final mask with $(1 \ll 26)-1`; it avoids a set but requires careful index conversion.
- **Search once per alphabet letter:** Checking whether each letter occurs is simple, but it may rescan the sentence 26 times; this remains linear only because the alphabet is fixed.
- **Sort the sentence:** Equal letters become adjacent and can be deduplicated, but sorting does unnecessary $O(n\log n)$ work.
- **Length below 26:** The answer must be `false`, because fewer than 26 positions cannot cover 26 distinct letters.
- **Exactly 26 characters:** The answer is `true` only when every position holds a different alphabet letter.
- **Many duplicates:** Repetition cannot compensate for one missing letter.
- **Order:** Alphabetical order is irrelevant; only membership matters.
- **Last missing letter:** A character at the final position must still be included before evaluating the set size.
