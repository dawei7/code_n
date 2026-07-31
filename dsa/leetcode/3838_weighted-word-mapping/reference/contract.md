## Function Contract

**Inputs**

- `words`: The ordered array of lowercase English words to map.
- `weights`: The 26 letter weights, indexed from `'a'` through `'z'`.

Let $W=\lvert\texttt{words}\rvert$ and let the total character count be

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert.
$$

For a word $w$, define its numeric weight by

$$
V(w)=\sum_{c\in w}\texttt{weights}[\operatorname{index}(c)],
$$

where $\operatorname{index}(\texttt{'a'})=0$ and $\operatorname{index}(\texttt{'z'})=25$. If $r=V(w)\bmod 26$, the mapped character is the reverse-alphabet letter at residue $r$, equivalently `chr(ord('z') - r)`.

**Return value**

Return a length-$W$ string containing one mapped character per word, preserving the input order.
