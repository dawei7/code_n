## General

Scan `rolls` and collect distinct faces in the current block. Whenever all
`k` faces have appeared, finish that block, increment a counter, and begin a
new empty block. These are the earliest possible consecutive blocks that each
contain every face.

**Why complete blocks determine the answer**

If $c$ complete blocks are found, every sequence of length $c$ occurs: choose
its first requested face from block one, its second from block two, and so on.
The chosen positions necessarily increase.

Conversely, in each complete block record the face whose first appearance
finished that block. After the last complete block, choose a face missing from
the incomplete suffix. The sequence formed by the $c$ recorded finishing faces
followed by that missing face cannot occur. Matching each finishing face in
order consumes at least through the end of its block, leaving only the final
incomplete suffix for the last face. Therefore some length-$(c+1)$ sequence is
impossible, while all shorter lengths are possible, so the answer is $c+1$.

## Complexity detail

Every roll is processed once, giving $O(n)$ time. The current block stores at
most all $k$ faces and uses $O(k)$ space.

## Alternatives and edge cases

- **Search for each face per block:** Repeatedly locating every face after the
  current boundary finds the same greedy blocks, but can take $O(nk)$ time.
- **Enumerate candidate sequences:** This is a useful tiny-input oracle, but
  the number of candidates grows exponentially with the length.
- **Missing face initially:** No complete block exists, so the answer is 1.
- **Incomplete suffix:** It never increments the block count, but supplies the
  missing final face in the impossibility construction.
- **One-sided die:** Every completed roll forms a block, so $n$ rolls yield
  answer $n+1$.
