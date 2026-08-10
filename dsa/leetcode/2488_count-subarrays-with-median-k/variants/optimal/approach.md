## General

**Turn values into a balance around `k`**

The array contains distinct integers, so every value other than `k` is unambiguously smaller or greater than `k`. Give a value greater than `k` contribution $+1$ and a value smaller than `k` contribution $-1$.

For a subarray that contains `k`, let $G$ be the count of values greater than `k` and $L$ the count smaller than `k`. Its balance is $G-L$.

If the subarray has odd length, `k` is its middle sorted element exactly when $G=L$, giving balance zero. If it has even length, the problem chooses the left middle element. For `k` to occupy that position, there must be one more greater value than smaller value, so $G=L+1$ and the balance is one.

Therefore, a subarray containing `k` has median `k` exactly when its comparison balance is either zero or one.

**Every valid subarray must cross the unique position of `k`**

The code locates `k` at index `i` with `nums.index(k)`. Because values are distinct, this occurrence is unique. A subarray whose median equals `k` must contain that value, so every candidate has a left endpoint at or before `i` and a right endpoint at or after `i`.

This lets the method describe a candidate by two independent extensions from `k`:

- a suffix of the elements left of `i`, scanned outward from `i-1`;
- a prefix of the elements right of `i`, scanned from `i+1` onward.

The center `[k]` alone is always valid, so `ans` starts at one.

**Collect every right-side balance**

The first loop scans positions to the right of `k`. Variable `x` is the balance of the current right prefix. Each greater value adds one and each smaller value subtracts one.

The subarray consisting of `k` plus only that right prefix has total balance `x`. The Boolean expression `0 <= x <= 1` is true exactly when that subarray has median `k`. In Python, adding a Boolean to an integer adds one for `True` and zero for `False`.

The counter `cnt[x]` records how many non-empty right prefixes have each balance. Multiple prefixes can have the same balance, and each corresponds to a different right endpoint, so their multiplicities must be preserved.

Notice that the empty right extension is not put in `cnt`. Right-empty subarrays are counted separately during the left scan, just as left-empty ones are counted directly during the right scan. This organization avoids double counting.

**Match each left balance with compatible right balances**

The second loop moves leftward from `i-1`. Its `x` is the balance of the chosen left suffix. The subarray using no right extension is valid when this balance is zero or one, so the same Boolean condition is added.

For a subarray extending on both sides, let the left balance be $x$ and right balance be $y$. Their combined balance is $x+y$ because `k` itself contributes zero. Validity requires

$$
x+y\in\{0,1\}.
$$

If the total is zero, $y=-x$. If the total is one, $y=1-x=-x+1$. Therefore, the exact number of compatible non-empty right extensions is

`cnt[-x] + cnt[-x+1]`.

The counter returns zero for a key that has not appeared, so no special existence check is needed.

**Why every qualifying subarray is counted once**

Every subarray containing `k` falls into exactly one of four categories: center only, extends only right, extends only left, or extends on both sides. Initialization counts the first category. The right loop counts the second, the direct Boolean in the left loop counts the third, and counter lookups count the fourth.

Within the fourth category, a subarray has one definite left endpoint and one definite right endpoint. The left iteration reaches its left balance once, and the counter entry includes its right prefix once. The balance equation accepts it exactly when its median is `k`.

No subarray can belong to two categories, so there is no overlap. The balance characterization also proves that no invalid median is counted.

**A small trace**

For `nums=[3,2,1,4,5]` and `k=4`, the right side contains 5, giving right balance one. This counts `[4,5]` and stores `cnt[1]=1`. Scanning left, value 1 gives balance $-1$. The left-only subarray is invalid, but `cnt[-(-1)+1]=cnt[2]` is zero while `cnt[-(-1)]=cnt[1]` is one, counting `[1,4,5]`. Further left extensions do not form a valid balance. Together with `[4]`, the answer is three.

## Complexity detail

Finding `k` takes $O(n)$ time. The right and left scans together visit every remaining value once, and expected-time counter operations are $O(1)$. Total expected time is $O(n)$.

The counter may store $O(n)$ distinct balances. In addition, `nums[i+1:]` creates a Python slice containing up to $O(n)$ references. Thus auxiliary space is $O(n)$.

All balances lie between $-n$ and $n$, and the answer can be quadratic in the number of endpoints; Python integers represent it safely.

## Alternatives and edge cases

- **Prefix-balance map over the whole array:** Count compatible prefix states while enforcing inclusion of `k`. It is equivalent but often harder to organize without counting subarrays that omit `k`.
- **Brute-force sorting:** Enumerating subarrays and sorting each one is far too slow.
- **Distinct values:** They ensure every non-`k` value contributes exactly $+1$ or $-1$ and that `k` has one center position.
- **Even-length median:** Because the left middle is used, valid balance is one as well as zero.
- **Center only:** `[k]` is counted by the initial answer of one.
- **Empty extension:** It is handled directly rather than inserted into `cnt`.
- **All useful extensions on one side:** The Boolean additions count them without needing a pair from the opposite side.
- **Repeated balances:** Counter frequencies, not mere membership, are required because different endpoints define different subarrays.
- **Negative balance keys:** Python's counter accepts them normally.
- **Boolean arithmetic:** `True` contributes one and `False` contributes zero in the exact implementation.
