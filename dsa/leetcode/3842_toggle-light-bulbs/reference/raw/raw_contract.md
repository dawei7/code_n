## Function Contract

**Inputs**

- `bulbs`: The sequence of bulb numbers to toggle, in operation order.

For each bulb number $b\in\{1,\ldots,100\}$, define its occurrence count

$$
C(b)=\left\lvert\left\{i\mid\texttt{bulbs}[i]=b\right\}\right\rvert.
$$

All bulbs begin off, and each occurrence reverses exactly one bulb's state. Consequently, bulb $b$ is on at the end exactly when $C(b)$ is odd.

**Return value**

Return every $b$ with odd $C(b)$ in ascending numeric order. If no such bulb exists, return `[]`.
