## Function Contract

**Inputs**

- `workers`: a non-empty array of two-coordinate worker locations.
- `bikes`: a non-empty array of two-coordinate bike locations.

Let $n=\lvert\texttt{workers}\rvert$ and $m=\lvert\texttt{bikes}\rvert$. The input guarantees $n \le m$, so every worker can receive a different bike. Coordinate pairs and array indices remain distinct concepts: the worker or bike index identifies an entity, while its pair identifies the entity's grid location.

**Return value**

- The minimum sum of Manhattan distances obtained by assigning a distinct bike to every worker.
