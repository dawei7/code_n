## Function Contract

**Inputs**

- `workers`: an array of $W$ distinct coordinate pairs, where index $i$ identifies worker $i$.
- `bikes`: an array of $B$ distinct coordinate pairs, where index $j$ identifies bike $j$.

Each assignment consumes one currently available worker and one currently available bike. The comparison key for every available pair is `(Manhattan distance, worker index, bike index)`, in that order.

Let $D$ denote the largest possible Manhattan distance between two legal coordinates. Under the stated coordinate bounds, $D=1998$.

**Return value**

- An integer array `answer` of length $W$, where `answer[i]` is the 0-indexed bike assigned to worker `i`.
