## Function Contract

**Inputs**

- `digitSum`: An array whose entry at index `i` is the required decimal digit sum of `arr[i]`.

Let $n=\lvert\texttt{digitSum}\rvert$, let $U=5001$ be the number of permitted values, and let $D(x)$ denote the sum of the decimal digits of $x$. A candidate array must satisfy $0\le\texttt{arr[i]}\le5000$, $\texttt{arr[i-1]}\le\texttt{arr[i]}$ whenever $i>0$, and $D(\texttt{arr[i]})=\texttt{digitSum[i]}$ at every index.

Arrays are distinct when they differ at one or more positions.

**Return value**

Return the number of distinct valid arrays, reduced modulo $1{,}000{,}000{,}007$.
