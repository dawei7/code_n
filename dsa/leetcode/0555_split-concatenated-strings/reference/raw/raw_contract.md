## Function Contract

**Inputs**

- `strs`: a nonempty list of nonempty lowercase English strings.

Let $m = \lvert\texttt{strs}\rvert$ and let

$$
L = \sum_{w \in \texttt{strs}} \lvert w \rvert.
$$

Every legal result contains exactly $L$ characters. Reversal changes the order inside a block but not the circular
order of the $m$ blocks.

**Return value**

Return the lexicographically largest length-$L$ string obtainable after choosing all block orientations and opening
the resulting loop at one character boundary.
