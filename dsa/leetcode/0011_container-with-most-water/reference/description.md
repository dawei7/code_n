## Description

An integer array `height` of length $n$ defines $n$ vertical lines. Line $i$ extends from $(i,0)$ to $(i,\texttt{height[i]})$.

Choose two lines that, together with the x-axis between them, form a container. Return the largest amount of water any such container can hold. The sides must remain vertical; slanting the container is not allowed.

For the first source example, the diagram's data and highlighted maximum container are represented accessibly here:

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Height | 1 | 8 | 6 | 2 | 5 | 4 | 8 | 3 | 7 |

The selected sides are indices 1 and 8. Their width is 7, their limiting height is 7, and the enclosed area is $7 \times 7 = 49$.
