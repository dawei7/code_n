# Chef Is Just Throwing Random Words

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SSO |
| Difficulty Rating | 2181 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SSO](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SSO) |

---

## Problem Statement

Chef once had a deep epiphany and ended up saying: Given a sequence of positive integers $a_1, a_2, \ldots, a_N$, if you take each of its $2^N$ subsequences and write down the sum of elements of this subsequence, what will the bitwise OR of the written integers be?

Yes, you read it right, but can you solve it?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $a_1, a_2, \ldots, a_N$.

### Output
For each test case, print a single line containing one integer ― the bitwise OR of sums of all subsequences.

### Constraints
- $1 \le T \le 5$
- $1 \le N \le 10^5$
- $1 \le a_i \lt 2^{30}$ for each valid $i$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
2
1 1
3
1 9 8
```

**Output**

```text
3
27
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 1
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3
1 9 8
```

**Output for this case**

```text
27
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SSO)

[Contest](https://www.codechef.com/LTIME89B/problems/SSO)

**Setter:** [Mohammed Ehab](https://www.codechef.com/users/mohammed200218)

**Tester:** [Ramazan Rakhmatullin](https://www.codechef.com/users/grumpy_gordon)

**Editorialist:** [Ishmeet Singh Saggu](https://www.codechef.com/users/psychik)

# DIFFICULTY:

Easy

# PREREQUISITES:

Bitwise Operation and Maths

# PROBLEM:

Given a sequence of positive integers a_1,a_2,…,a_N, if you take each of its 2^N subsequences and write down the sum of elements of this subsequence, Output the bitwise OR of the written integers.

# EXPLANATION:

Let the sequence formed by writing down the sum of elements of each 2^N subsequences of the sequence a is : b_1, b_2, ... b_{2^N}. Note the maximum element in the sequence b is the sum of all elements in the sequence a, so the final answer which we have to compute by doing bitwise OR of all the elements of the sequence b will have the same number of bits in its binary representation as of the maximum number in sequence b.

So this observation gives us a hint that if for each bit position, if we can find out that is it possible to make it 1 by summing some or all elements of sequence a then we can compute the answer. Now let’s see how to check it.

- We will start from the lowest bit i.e. the bit-0 which represents 2^0 and go till the maximum bit.

- We will count the number of elements in the sequence a which have bit-0 equals to 1 in its binary representation and it will be the final count of bit-0 let us represent it as dp[0]. If dp[0] \geq 1 then we can make the bit-0 equals to 1 in the answer else bit-0 will be 0, then we will go to the next bit i.e. the bit-1 then again we will count as we did for the bit-0 but to the count of bit-1 we will add the floor(dp[0]/2), hence for bit-1, dp[1] = count in sequence + floor(dp[0]/2).

- So for bit-i, dp[i] = count in sequence + floor(dp[i-1]/2), where i > 0

- To construct the answer, if dp[i]>0 then the bit-i in the answer will be 1 else it will be 0 because if dp[i] > 0 then it is always possible to select a subsequence such that bit-i is 1 when all the numbers in the subsequence are added.

To give you an intuition about why the above process works. Suppose we consider a bit-i, and if there is at least one element in the sequence a which have 1 at bit-i in its binary representation then, as it is the subsequence(where we will select only this element) then we will have 1 at bit-i in the binary representation of the final answer. Suppose we don’t have elements with bit-i equals 1, but we have 2 numbers whose bit-(i-1) is 1 or 4 numbers whose bit-(i-2) is 1 , then we can make 1 at bit-i by selecting these numbers as subsequence. Similarly, you can think of many other possible constructions. One more example is if you have 2 numbers with bit-(i-2) equals 1 and 1 number with bit-(i-1) equals 1 `(and for simplicity consider rest all bits are 0 in these 3 numbers)` then if we add these 3 numbers together we will get a number with bit-i equals 1.

# TIME COMPLEXITY:

- Time complexity per test case is O(N * log(max(a_i))).

# SOLUTIONS:

Setter's Solution
``
``

Tester's Solution
``#include <bits/stdc++.h>

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunused-const-variable"
#define popcnt(x) __builtin_popcount(x)

#define fr first

#define sc second

#define m_p make_pair

#define low_bo(a, x) lower_bound(a.begin(), a.end(), x) - a.begin()

#define up_bo(a, x) upper_bound(a.begin(), a.end(), x) - a.begin()

#define unique(a) a.resize(unique(a.begin(), a.end()) - a.begin())

#define popcnt(x) __builtin_popcount(x)

//#include <ext/pb_ds/assoc_container.hpp>

//using namespace __gnu_pbds;

//gp_hash_table<int, int> table;

//#pragma GCC optimize("O3")
//#pragma GCC optimize("Ofast,no-stack-protector")
//#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx")
//#pragma GCC target("avx,tune=native")
//float __attribute__((aligned(32)))

/*char memory[(int)1e8];
char memorypos;

inline void * operator new(size_t n){
    char * ret = memory + memorypos;
    memorypos += n;
    return (void *)ret;
}

inline void operator delete(void *){}
*/

using namespace std;

typedef long long ll;

typedef unsigned long long ull;

typedef long double ld;

typedef unsigned int uint;

template<typename T>
class Modular {
public:
    using Type = typename decay<decltype(T::value)>::type;

    constexpr Modular() : value() {}

    template<typename U>
    Modular(const U &x) {
        value = normalize(x);
    }

    static Type inverse(Type a, Type mod) {
        Type b = mod, x = 0, y = 1;
        while (a != 0) {
            Type t = b / a;
            b -= a * t;
            x -= t * y;
            swap(a, b);
            swap(x, y);
        }
        if (x < 0)
            x += mod;
        return x;
    }

    template<typename U>
    static Type normalize(const U &x) {
        Type v;
        if (-mod() <= x && x < mod()) v = static_cast<Type>(x);
        else v = static_cast<Type>(x % mod());
        if (v < 0) v += mod();
        return v;
    }

    const Type &operator()() const { return value; }

    template<typename U>
    explicit operator U() const { return static_cast<U>(value); }

    constexpr static Type mod() { return T::value; }

    Modular &operator+=(const Modular &other) {
        if ((value += other.value) >= mod()) value -= mod();
        return *this;
    }

    Modular &operator-=(const Modular &other) {
        if ((value -= other.value) < 0) value += mod();
        return *this;
    }

    template<typename U>
    Modular &operator+=(const U &other) { return *this += Modular(other); }

    template<typename U>
    Modular &operator-=(const U &other) { return *this -= Modular(other); }

    Modular &operator++() { return *this += 1; }

    Modular &operator--() { return *this -= 1; }

    Modular operator++(int) {
        Modular result(*this);
        *this += 1;
        return result;
    }

    Modular operator--(int) {
        Modular result(*this);
        *this -= 1;
        return result;
    }

    Modular operator-() const { return Modular(-value); }

    template<typename U = T>
    typename enable_if<is_same<typename Modular<U>::Type, int>::value, Modular>::type &operator*=(const Modular &rhs) {
#ifdef _WIN32
        uint64_t x = static_cast<int64_t>(value) * static_cast<int64_t>(rhs.value);
        uint32_t xh = static_cast<uint32_t>(x >> 32), xl = static_cast<uint32_t>(x), d, m;
        asm(
        "divl %4; \n\t"
        : "=a" (d), "=d" (m)
        : "d" (xh), "a" (xl), "r" (mod())
        );
        value = m;
#else
        value = normalize(static_cast<int64_t>(value) * static_cast<int64_t>(rhs.value));
#endif
        return *this;
    }

    template<typename U = T>
    typename enable_if<is_same<typename Modular<U>::Type, int64_t>::value, Modular>::type &
    operator*=(const Modular &rhs) {
        int64_t q = static_cast<int64_t>(static_cast<long double>(value) * rhs.value / mod());
        value = normalize(value * rhs.value - q * mod());
        return *this;
    }

    template<typename U = T>
    typename enable_if<!is_integral<typename Modular<U>::Type>::value, Modular>::type &operator*=(const Modular &rhs) {
        value = normalize(value * rhs.value);
        return *this;
    }

    Modular &operator/=(const Modular &other) { return *this *= Modular(inverse(other.value, mod())); }

    template<typename U>
    friend const Modular<U> &abs(const Modular<U> &v) { return v; }

    template<typename U>
    friend bool operator==(const Modular<U> &lhs, const Modular<U> &rhs);

    template<typename U>
    friend bool operator<(const Modular<U> &lhs, const Modular<U> &rhs);

    template<typename U>
    friend std::istream &operator>>(std::istream &stream, Modular<U> &number);

private:
    Type value;
};

template<typename T>
bool operator==(const Modular<T> &lhs, const Modular<T> &rhs) { return lhs.value == rhs.value; }

template<typename T, typename U>
bool operator==(const Modular<T> &lhs, U rhs) { return lhs == Modular<T>(rhs); }

template<typename T, typename U>
bool operator==(U lhs, const Modular<T> &rhs) { return Modular<T>(lhs) == rhs; }

template<typename T>
bool operator!=(const Modular<T> &lhs, const Modular<T> &rhs) { return !(lhs == rhs); }

template<typename T, typename U>
bool operator!=(const Modular<T> &lhs, U rhs) { return !(lhs == rhs); }

template<typename T, typename U>
bool operator!=(U lhs, const Modular<T> &rhs) { return !(lhs == rhs); }

template<typename T>
bool operator<(const Modular<T> &lhs, const Modular<T> &rhs) { return lhs.value < rhs.value; }

template<typename T>
Modular<T> operator+(const Modular<T> &lhs, const Modular<T> &rhs) { return Modular<T>(lhs) += rhs; }

template<typename T, typename U>
Modular<T> operator+(const Modular<T> &lhs, U rhs) { return Modular<T>(lhs) += rhs; }

template<typename T, typename U>
Modular<T> operator+(U lhs, const Modular<T> &rhs) { return Modular<T>(lhs) += rhs; }

template<typename T>
Modular<T> operator-(const Modular<T> &lhs, const Modular<T> &rhs) { return Modular<T>(lhs) -= rhs; }

template<typename T, typename U>
Modular<T> operator-(const Modular<T> &lhs, U rhs) { return Modular<T>(lhs) -= rhs; }

template<typename T, typename U>
Modular<T> operator-(U lhs, const Modular<T> &rhs) { return Modular<T>(lhs) -= rhs; }

template<typename T>
Modular<T> operator*(const Modular<T> &lhs, const Modular<T> &rhs) { return Modular<T>(lhs) *= rhs; }

template<typename T, typename U>
Modular<T> operator*(const Modular<T> &lhs, U rhs) { return Modular<T>(lhs) *= rhs; }

template<typename T, typename U>
Modular<T> operator*(U lhs, const Modular<T> &rhs) { return Modular<T>(lhs) *= rhs; }

template<typename T>
Modular<T> operator/(const Modular<T> &lhs, const Modular<T> &rhs) { return Modular<T>(lhs) /= rhs; }

template<typename T, typename U>
Modular<T> operator/(const Modular<T> &lhs, U rhs) { return Modular<T>(lhs) /= rhs; }

template<typename T, typename U>
Modular<T> operator/(U lhs, const Modular<T> &rhs) { return Modular<T>(lhs) /= rhs; }

template<typename T, typename U>
Modular<T> power(const Modular<T> &a, const U &b) {
    assert(b >= 0);
    Modular<T> x = a, res = 1;
    U p = b;
    while (p > 0) {
        if (p & 1) res *= x;
        x *= x;
        p >>= 1;
    }
    return res;
}

template<typename T>
bool IsZero(const Modular<T> &number) {
    return number() == 0;
}

template<typename T>
string to_string(const Modular<T> &number) {
    return to_string(number());
}

template<typename T>
std::ostream &operator<<(std::ostream &stream, const Modular<T> &number) {
    return stream << number();
}

template<typename T>
std::istream &operator>>(std::istream &stream, Modular<T> &number) {
    typename common_type<typename Modular<T>::Type, int64_t>::type x;
    stream >> x;
    number.value = Modular<T>::normalize(x);
    return stream;
}

const int md = 1e9 + 7;

using Mint = Modular<std::integral_constant<decay<decltype(md)>::type, md>>;

ll sqr(ll x) {
    return x * x;
}

int mysqrt(ll x) {
    int l = 0, r = 1e9 + 1;
    while (r - l > 1) {
        int m = (l + r) / 2;
        if (m * (ll) m <= x)
            l = m;
        else
            r = m;
    }
    return l;
}

#ifdef ONPC
mt19937 rnd(513);
mt19937_64 rndll(231);
#else
mt19937 rnd(chrono::high_resolution_clock::now().time_since_epoch().count());
    mt19937_64 rndll(chrono::high_resolution_clock::now().time_since_epoch().count());
#endif

template<typename T>
T gcd(T a, T b) {
    return a ? gcd(b % a, a) : b;
}

int gcdex(int a, int b, int &x, int &y) {
    if (a == 0) {
        x = 0;
        y = 1;
        return b;
    }
    int x1, y1;
    int ret = gcdex(b % a, a, x1, y1);
    x = y1 - (b / a) * x1;
    y = x1;
    return ret;
}

void setmin(int &x, int y) {
    x = min(x, y);
}

void setmax(int &x, int y) {
    x = max(x, y);
}

void setmin(ll &x, ll y) {
    x = min(x, y);
}

void setmax(ll &x, ll y) {
    x = max(x, y);
}

const ll llinf = 4e18 + 100;

const ld eps = 1e-9, PI = atan2(0, -1);

const int maxn = 1e5 + 100, maxw = 2e6 + 1111, inf = 1e9 + 100, sq = 450, LG = 18, mod = 1e9 + 933, mod1 = 1e9 + 993;

int main() {
#ifdef ONPC
    freopen("../a.in", "r", stdin);
    freopen("../a.out", "w", stdout);
#else
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
#endif // ONPC
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        ll ans = 0;
        ll sum = 0;
        for (int i = 0; i < n; i++) {
            ll w;
            cin >> w;
            ans |= w;
            sum += w;
            ans |= sum;
        }
        cout << ans << '\n';
    }
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

void Solve() {
	int n;
	cin >> n;
	vector<int> a(n);
	for(int i = 0; i < n; i ++) {
		cin >> a[i];
	}
	vector<int> dp(50, 0);
	for(int i = 0; i < n; i ++) {
		for(int j = 0; j < 30; j ++) {
			dp[j] += a[i] % 2;
			a[i] /= 2;
		}
	}
	long long num = 0;
	long long mul = 1;
	for(int i = 0; i < 50; i ++) {
		if(i) {
			dp[i] += (dp[i-1]/2);
		}
		if(dp[i]) num += mul;
		mul *= 2LL;
	}
	cout << num << "\n";
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int test_case = 1;
	cin >> test_case;
	for(int i = 1; i <= test_case; i ++) {
		Solve();
	}

	return 0;
}
``

# VIDEO EDITORIAL:

Feel free to share your approach. In case of any doubt or anything is unclear please ask it in the comment section. Any suggestions are welcomed.

</details>
