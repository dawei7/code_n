## General

Two independent upper bounds determine the answer.

The square deck contains exactly $n^2$ cells, and each cell can hold at most one container. Therefore no loading plan can use more than $n^2$ containers.

If $k$ containers are loaded, their combined weight is $kw$. The capacity condition $kw\le\texttt{maxWeight}$ permits at most

$$
\left\lfloor\frac{\texttt{maxWeight}}{w}\right\rfloor
$$

whole containers. Because all containers are identical and every deck cell is interchangeable, any number satisfying both upper bounds is attainable: choose that many distinct cells and place one container in each. The maximum feasible count is consequently the smaller bound.

## Complexity detail

The algorithm performs one multiplication, one integer division, and one minimum operation. Under the problem's fixed-width integer model, this is $O(1)$ time and $O(1)$ auxiliary space.

The benchmark size is $C=n^2$, the number of deck cells. Its capacity is deliberately nonbinding. The optimal formula has constant work at every tier, while the calibrated slower implementation increments the loaded count one container at a time and therefore requires $\Theta(C)$ time.

## Alternatives and edge cases

- **Load containers one by one:** Simulation is correct but wastes $O(\min(n^2,\lfloor\texttt{maxWeight}/w\rfloor))$ time on a result available by arithmetic.
- **Binary search the count:** Feasibility is monotone, but binary search takes $O(\log n)$ checks despite the direct closed form.
- **No container fits:** When `maxWeight < w`, floor division gives zero even though the deck has cells.
- **Deck limit binds:** Extra weight capacity cannot create more than $n^2$ physical positions.
- **Weight limit binds:** Empty deck cells do not help once another container would exceed `maxWeight`.
- **Exact equality:** When both limits are equal, that shared value is feasible and returned.
- **Overflow in fixed-width languages:** Compute `n * n` in a sufficiently wide integer type; the Python implementation has arbitrary-precision integers.
