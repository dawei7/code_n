## Function Contract

**Inputs**

- `pid`: the unique process identifiers.
- `ppid`: the parallel parent identifiers, where `ppid[i]` is the parent of `pid[i]`.
- `kill`: an identifier present in `pid` whose entire subtree must be terminated.

Let $n = \lvert\texttt{pid}\rvert = \lvert\texttt{ppid}\rvert$.

**Return value**

Return a list containing `kill` and every direct or indirect descendant of that process. List order is unrestricted.
