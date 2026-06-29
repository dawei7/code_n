# Cute Chef Gift

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COPAR |
| Difficulty Rating | 2235 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [COPAR](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/COPAR) |

---

## Problem Statement

Chef wants to give a gift to Chefina to celebrate their anniversary. Of course, he has a sequence $a_1, a_2, \ldots, a_N$ ready for this occasion. Since the half-heart necklace is kind of cliche, he decided to cut his sequence into two pieces and give her a piece instead. Formally, he wants to choose an integer $l$ ($1 \le l \lt N$) and split the sequence into its prefix with length $l$ and its suffix with length $N-l$.

Chef wants his gift to be *cute*; he thinks that it will be cute if the product of the elements in Chefina's piece is coprime with the product of the elements in his piece. Can you tell him where to cut the sequence? Find the smallest valid $l$ such that Chef's gift would be cute.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains the integer $N$.
- The second line contains $N$ space-separated integers $a_1, a_2, \ldots, a_N$.

### Output
For each test case, print a single line containing one integer $l$ where Chef should cut the sequence.

It is guaranteed that a solution exists for the given test data.

### Constraints
- $1 \le T \le 20$
- $2 \le N \le 10^5$
- $2 \le a_i \le 10^5$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $3 \cdot 10^5$

### Subtasks
**Subtask #1 (25 points):**
- $N \le 200$
- the sum of $N$ over all test cases does not exceed $600$

**Subtask #2 (40 points):**
- $N \le 2,000$
- the sum of $N$ over all test cases does not exceed $6,000$

**Subtask #3 (35 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
4
2 3 4 5
```

**Output**

```text
3
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/COPAR)

[Contest](https://www.codechef.com/LTIME89A/problems/COPAR)

**Setter:** [Mohammed Ehab](https://www.codechef.com/users/mohammed200218)

**Tester:** [Ramazan Rakhmatullin](https://www.codechef.com/users/grumpy_gordon)

**Editorialist:** [Ishmeet Singh Saggu](https://www.codechef.com/users/psychik)

# DIFFICULTY:

Easy

# PREREQUISITES:

[Difference Array](https://www.geeksforgeeks.org/difference-array-range-update-query-o1/) and Sieve of Eratosthenes

# PROBLEM:

Given a sequence a_1, a_2, ..., a_N, you have to find the smallest index l such that the product of elements from index 1 to l and product of elements from index l+1 to N is coprime with each other.

# EXPLANATION:

Two numbers x and y are said to be coprime if gcd(x, y) = 1.

let us make a list of all prime numbers P, such that for every prime number P_i, there exist at least one number in the sequence a which has P_i as its prime factor.

Now to satisfy the condition for the partition, we have to make sure that for every prime number P_i, the numbers in the sequence a which have P_i as a prime factor are one side of the partition. Why? because if they are present in both prefix and suffix, then when we multiply the numbers together in prefix and in the suffix, we will have at least P_i which is present in both numbers making their gcd \neq 1.

So using the sieve(using SPF, smallest prime factor) we will prime factorize all the numbers in the sequence a and make their list. For each prime number P_i, we will find out the minimum and maximum index of the number in the sequence a which has P_i as their prime factor. Suppose for a P_i it is L and R, then all the indexes from L to R-1 can’t be the answer `(because then the prime number` P_i `will be present in both the partition)`. So all the indexes from L to R-1 are bad indexes and can’t be the answer. So we can mark these bad indexes for all prime numbers P_i efficiently using the [difference array](https://www.geeksforgeeks.org/difference-array-range-update-query-o1/) and after marking indexes for all prime number P_i we will find out the smallest index which is not marked and it will be our answer.

# TIME COMPLEXITY:

- We can precompute the SPF(smallest prime factor) for factorization.

- Time complexity per test case is O(N * log(max(a_i))).

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;
#define MX 100000
int f[MX+5],l[MX+5],cum[MX+5];
int main()
{
	int t;
	scanf("%d",&t);
	while (t--)
	{
		int n;
		scanf("%d",&n);
		for (int i=2;i<=MX;i++)
		{
			f[i]=0;
			l[i]=0;
		}
		for (int i=1;i<=n;i++)
		{
			int a;
			scanf("%d",&a);
			for (int j=2;j*j<=a;j++)
			{
				if (a%j==0)
				{
					if (!f[j])
					f[j]=i;
					l[j]=i;
					while (a%j==0)
					a/=j;
				}
			}
			if (a!=1)
			{
				if (!f[a])
				f[a]=i;
				l[a]=i;
			}
			cum[i]=0;
		}
		for (int i=2;i<=MX;i++)
		{
			cum[f[i]]++;
			cum[l[i]]--;
		}
		for (int i=1;i<n;i++)
		{
			cum[i]+=cum[i-1];
			if (!cum[i])
			{
				printf("%d\n",i);
				break;
			}
		}
	}
}
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

int p[maxn], tot[maxn], cs[maxn];

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
    for (int i = 2; i < maxn; i++)
        if (p[i] == 0) {
            for (int j = i; j < maxn; j += i)
                if (p[j] == 0)
                    p[j] = i;
        }
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<vector<int>> a(n);
        vector<int> all;
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            while (x > 1) {
                int w = p[x];
                while (x % w == 0)
                    x /= w;
                a[i].push_back(w);
                all.push_back(w);
                tot[w]++;
            }
        }
        int cur = 0;
        for (int i = 0; i < n; i++) {
            for (int j : a[i]) {
                if (cs[j] == 0)
                    cs[j] = 1, cur++;
                tot[j]--;
                if (tot[j] == 0)
                    cur--;
            }
            if (cur == 0) {
                cout << i + 1 << '\n';
                break;
            }
        }
        for (int i : all)
            tot[i] = 0, cs[i] = 0;
    }
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

const int maxA = 1e5+1;

vector<int> spf(maxA, -1);

void computeSPF() {
	spf[1] = 1;
	for(int i = 2; i < maxA; i ++) {
		if(spf[i] == -1) {
			for(int j = i; j < maxA; j += i) {
				if(spf[j] == -1) spf[j] = i;
			}
		}
	}
}

void Solve() {
	int N;
	cin >> N;
	vector<int> marking(N, 0); // difference array, for marking restricted index.
	vector<pair<int, int>> prime_range(maxA, {-1, -1});
	for(int i = 0; i < N; i ++) {
		int x;
		cin >> x;
		while(x > 1) {
			int prime = spf[x];
			if(prime_range[prime].first != -1) {
				prime_range[prime].second = i;
			}
			else prime_range[prime] = {i, i};
			x /= prime;
		}
	}

	// Now marking the indexes with difference array which can't be answer;
	for(int i = 2; i < maxA; i ++) {
		if(prime_range[i].first == -1) continue;
		int L = prime_range[i].first;
		int R = prime_range[i].second;
		// All the index from [L, R-1] can't be the "l" as the answer
		marking[L] ++;
		marking[R] --;
	}
	for(int i = 1; i < N; i ++) {
		marking[i] += marking[i-1];
	}
	for(int i = 0; i < N; i ++) {
		if(marking[i]) continue;
		cout << i+1 << "\n";
		return;
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	computeSPF();

	int test_case;
	cin >> test_case;
	for(int i = 1; i <= test_case; i ++) {
		Solve();
	}
}
``

# VIDEO EDITORIAL:

Feel free to share your approach. In case of any doubt or anything is unclear please ask it in the comment section. Any suggestions are welcomed.

</details>
