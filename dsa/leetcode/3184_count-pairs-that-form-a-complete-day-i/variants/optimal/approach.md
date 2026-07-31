## General

**Reduce durations to one day.** Whether two durations sum to a multiple of 24 depends only on their remainders modulo 24. If the current duration has remainder $r$, a previous duration must have remainder $(24-r)\bmod24$. The second modulo is important for $r=0$, whose complement is also 0.

**Count earlier complements.** Maintain a 24-slot frequency array for remainders of durations already scanned. Before recording the current remainder, add the frequency of its complement to the answer. Every such earlier entry forms exactly one pair whose earlier index is smaller, so the scan enforces $i<j$ without storing indices or revisiting pairs.

After processing any prefix, each frequency slot equals the number of processed durations with that remainder, and the accumulated answer counts exactly the qualifying pairs entirely inside the prefix. For the next duration, the complement lookup adds every new qualifying pair ending at its index and no nonqualifying pair. Updating its own slot restores the invariant. Therefore the final answer is precisely the number requested.

## Complexity detail

Let $n$ be the length of `hours`. The scan performs constant work for each duration, giving $O(n)$ time. The frequency array always has exactly 24 slots, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Brute-force pair enumeration:** Check every $i<j$ directly in $O(n^2)$ time and $O(1)$ space. This fits the small I-version constraint but does unnecessary repeated work.
- **Hash map of full values:** Exact values are not the relevant identity; values differing by a multiple of 24 belong to the same remainder class.
- **Remainder zero:** Multiples of 24 complement other multiples of 24, so the complement formula must map 0 back to 0.
- **Remainder twelve:** Two remainder-12 durations complement each other, including repeated equal values.
- **Duplicate durations:** Equal entries at different indices form distinct pairs and must each be counted.
- **Single duration:** With no possible $i<j$, the answer is zero.
- **Large durations:** Reduce values modulo 24 before matching; their absolute size does not change pair validity.
