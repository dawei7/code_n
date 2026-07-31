## General

**Treat each adjacent pair as one round.** The index guarantees align every even-indexed node with its following odd-indexed node. Because the list length is even, each current node has a partner whenever a round begins. Compare their values, award the round to Even when the first is larger and to Odd otherwise, then advance two links to the next round.

**Store only the score difference.** A positive integer represents Even's lead and a negative integer represents Odd's lead. Increment it after an Even win and decrement it after an Odd win. The parity guarantee also means the two values in a pair cannot be equal: one is even and the other is odd.

After processing any prefix of complete pairs, the stored difference equals the number of Even wins minus the number of Odd wins in exactly that prefix. Processing the next pair changes it by the point awarded in that round, so the relationship continues to hold. Once the traversal ends, its sign therefore identifies the overall winner, while zero identifies a tie.

## Complexity detail

Let $n$ be the number of nodes. The traversal visits each node once through $n/2$ constant-work pair comparisons, so the time complexity is $O(n)$. It keeps only a score difference and a traversal pointer, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Two separate counters:** Counting Even and Odd wins independently is correct, but their difference contains all information needed to determine the result and uses a simpler final comparison.
- **Copy values into an array:** Array indexing makes pair boundaries explicit, but requires $O(n)$ extra space without improving the linear running time.
- **Minimum list:** A two-node list is one complete round and immediately produces either `"Even"` or `"Odd"`.
- **No equal value within a pair:** An even integer can never equal an odd integer, so every pair awards exactly one point.
- **Tied game:** Equal numbers of pair wins must return `"Tie"`, regardless of the magnitudes of the node values.
- **Final pair:** The last comparison can decide the game, so traversal cannot stop merely because one team is currently ahead.
