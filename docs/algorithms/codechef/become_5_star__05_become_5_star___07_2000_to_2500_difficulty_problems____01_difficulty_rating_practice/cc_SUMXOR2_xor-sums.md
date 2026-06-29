# XOR Sums

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUMXOR2 |
| Difficulty Rating | 2306 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SUMXOR2](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SUMXOR2) |

---

## Problem Statement

You are given a sequence of positive integers $A_1, A_2, \ldots, A_N$. You should answer $Q$ queries. In each query:
- You are given a positive integer $M$.
- Consider all non-empty subsequences of $A$ with length $\le M$. Recall that a subsequence is any sequence that can be created by deleting zero or more elements without changing the order of the remaining elements.
- For each of these subsequences, compute the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of its elements. Your task is to determine the sum of these values. Since this sum can be very large, compute it modulo $998,244,353$.

### Input
- The first line of the input contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- The third line contains a single integer $Q$.
- $Q$ lines follow. Each of these lines contains a single integer $M$ describing a query.

### Output
For each query, print a single line containing one integer ― the sum of bitwise XORs for all subsequences of $A$ with length $\le M$, modulo $998,244,353$.

### Constraints
- $1 \leq N, Q \leq 2 \cdot 10^5$
- $1 \leq A_i \lt 2^{30}$ for each valid $i$
- $1 \leq M \leq N$

### Subtask
**Subtask #1 (10 points):** $1 \leq N, Q \leq 1,000$

**Subtask #2 (90 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
4
1 3 5 2
2
1
2
```

**Output**

```text
11
34
```

**Explanation**

In the first query, the answer is just the sum of elements of $A$ (modulo $998,244,353$), which is $1+3+5+2 = 11$.

In the second query, the answer is the sum of bitwise XORs for all subsequences with length $1$ or $2$, which is $1+3+5+2 + (1 \oplus 3) + (1 \oplus 5) + (1 \oplus 2) + (3 \oplus 5) + (3 \oplus 2) + (5 \oplus 2) = 34$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Div-1 Contest](https://www.codechef.com/FEB21A/problems/SUMXOR2/)

[Div-2 Contest](https://www.codechef.com/FEB21B/problems/SUMXOR2/)

[Div-3 Contest](https://www.codechef.com/FEB21C/problems/SUMXOR2/)

[Practice](https://www.codechef.com/problems/SUMXOR2)

**Author & Editorialist:** [Samarth Gupta](https://www.codechef.com/users/samarth2017)

**Tester:** [ Felipe Mota](https://www.codechef.com/users/fmota)

# DIFFICULTY:

MEDIUM

# PREREQUISITES:

Bitwise XOR, [FFT/NTT](https://cp-algorithms.com/algebra/fft.html)

# PROBLEM:

Given an array A, you need to compute sum of bitwise XOR of all subsequences of A of length less than equal to M.

# QUICK EXPLANATION:

Let’s precompute the answer for every M. Consider the i^{th} bit. Let there be n_1 ones and n_0 zeros. The answer for subsequences of size M is \sum\limits_{i=1,i+=2}^{n_1} {n_1 \choose i}{n_0 \choose M-i}.  This is clearly a convolution and so we can use FFT/NTT to evaluate it for every M and answer the queries in O(1).

# EXPLANATION:

We know that in bitwise xor, bits i and j(i != j) are independent and so we can solve the problem for each bit independently. Consider the i^{th} bit from right. Suppose we need to select subsequences of size M. Assuming there are n_1 ones and n_0 zeros, the number of ways to select subsequences of size M such that bitwise XOR is 1 can be written as:

S_{M,i} = \sum\limits_{j=1,j+=2}^{n_1}{n_1 \choose j}{n_0 \choose M-j}

because in the subsequence we need to select odd number of 1's and remaining bits as 0.

The sum of subsequences of size M can be found using:

\sum\limits_{i=0}^{\lfloor log(max(A_i))\rfloor} S_{M,i} \times 2^i

Clearly we can pre-compute the answer for every M and answer the queries in O(1) using prefix sum arrays. The complexity of this approach is O(N^2*log(max(A_i))+ Q) which is sufficient for subtask 1.

**Constructing the Polynomials**

Consider the expression for S_{M,i}. We can see this as a convolution and can think of polynomials which would give us the same expression when multiplied.

Consider P(x) = \sum\limits_{i=1,i+=2}^{n_1}{n_1 \choose i}x^i and Q(x) = \sum\limits_{i=0}^{n_0}{n_0 \choose i}x^i. What happens when we multiply P(x) and Q(x)?

Let’s try to find the coefficient of x^M in the polynomial R(x) = P(x)Q(x). We take x^i from P(x) and x^{M-i} from Q(x) for all valid **odd** i and add them up. We can then see the coefficient of x^M in R(x) is S_{M, i}.

**Polynomial multiplication**

Naive Multiplication of polynomials P(x) and Q(x) is O(N^2) for a particular bit and so O(N^2*log(max(A_i))) overall which has room for improvement if we do polynomial multiplication using FFT/NTT. Answering the queries is O(1) since we just need to maintain a prefix-sum array.

Overall Complexity: O(N*log(N)*log(max(A_i)) + Q)

# SOLUTIONS:

Setter's & Editorialist Solution
``#include<bits/stdc++.h>
#define ll long long
#define ull unsigned ll
#define For(i,j,k) for (int i=(int)(j);i<=(int)(k);i++)
#define Rep(i,j,k) for (int i=(int)(j);i>=(int)(k);i--)
using namespace std;
const int mo=998244353;
const int FFTN=1<<18;
#define poly vector<int>
namespace FFT{
	int w[FFTN+5],W[FFTN+5],R[FFTN+5];
	int power(int x,int y){
		int s=1;
		for (;y;y/=2,x=1ll*x*x%mo)
			if (y&1) s=1ll*s*x%mo;
		return s;
	}
	void FFTinit(){
		W[0]=1;
		W[1]=power(3,(mo-1)/FFTN);
		For(i,2,FFTN) W[i]=1ll*W[i-1]*W[1]%mo;
	}
	int FFTinit(int n){
		int L=1;
		for (;L<=n;L<<=1);
		For(i,0,L-1) R[i]=(R[i>>1]>>1)|((i&1)?(L>>1):0);
		return L;
	}
	int A[FFTN+5],B[FFTN+5];
	ull p[FFTN+5];
	void DFT(int *a,int n){
		For(i,0,n-1) p[R[i]]=a[i];
		for (int d=1;d<n;d<<=1){
			int len=FFTN/(d<<1);
			for (int i=0,j=0;i<d;i++,j+=len) w[i]=W[j];
			for (int i=0;i<n;i+=(d<<1))
				for (int j=0;j<d;j++){
					int y=p[i+j+d]*w[j]%mo;
					p[i+j+d]=p[i+j]+mo-y;
					p[i+j]+=y;
				}
			if (d==1<<15)
				For(i,0,n-1) p[i]%=mo;
		}
		For(i,0,n-1) a[i]=p[i]%mo;
	}
	void IDFT(int *a,int n){
		For(i,0,n-1) p[R[i]]=a[i];
		for (int d=1;d<n;d<<=1){
			int len=FFTN/(d<<1);
			for (int i=0,j=FFTN;i<d;i++,j-=len) w[i]=W[j];
			for (int i=0;i<n;i+=(d<<1))
				for (int j=0;j<d;j++){
					int y=p[i+j+d]*w[j]%mo;
					p[i+j+d]=p[i+j]+mo-y;
					p[i+j]+=y;
				}
			if (d==1<<15)
				For(i,0,n-1) p[i]%=mo;
		}
		int val=power(n,mo-2);
		For(i,0,n-1) a[i]=p[i]*val%mo;
	}
	poly Mul(const poly &a,const poly &b){
		int sza=a.size()-1,szb=b.size()-1;
		poly ans(sza+szb+1);
		if (sza<=30||szb<=30){
			For(i,0,sza) For(j,0,szb)
				ans[i+j]=(ans[i+j]+1ll*a[i]*b[j])%mo;
			return ans;
		}
		int L=FFTinit(sza+szb);
		For(i,0,L-1) A[i]=(i<=sza?a[i]:0);
		For(i,0,L-1) B[i]=(i<=szb?b[i]:0);
		DFT(A,L); DFT(B,L);
		For(i,0,L-1) A[i]=1ll*A[i]*B[i]%mo;
		IDFT(A,L);
		For(i,0,sza+szb) ans[i]=A[i];
		return ans;
	}
}
using FFT::Mul;
using FFT::power;
#define mxn 200005
int fact[mxn];
int inv[mxn];

void pre()
{
    fact[0] = 1;
    int i;
    For(i,1,mxn-1)
        fact[i] = fact[i-1]*1ll*i%mo;
    inv[mxn-1] = power(fact[mxn-1], mo-2);
    Rep(i, mxn-2, 0)
        inv[i] = inv[i+1]*1ll*(i+1)%mo;
}
int nCr(int n, int r)
{
    if(n < 0 || r < 0 || n < r)
        return 0;
    int ans = fact[n]*1ll*inv[r]%mo;
    ans = ans*1ll*inv[n-r]%mo;
    return ans;
}
poly compute(int n, poly &arr)
{
    poly ans(n+1);
    For(bit, 0, 29)
    {
        int k = 0;
        For(i, 0, n-1)
            if((arr[i] >> bit)&1)
                k++;
        poly ones(k+1), zero_odd(n-k+1);
        for(int i=1;i<=k;i+=2) // ones(x) = C(k, 1)*x + C(k, 3)*x^3 + C(k, 5)*x^5....
            ones[i] = nCr(k, i);

        For(i, 0, (n-k))  // zero_odd(x) = C(n-k, 0) + C(n-k, 1)*x+....
            zero_odd[i] = nCr(n-k, i);
        poly odd = Mul(ones, zero_odd);
        For(i, 1, n)
            ans[i] = (ans[i] + odd[i]*1ll*(1 << bit)%mo)%mo;
    }
    return ans;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
	FFT::FFTinit();
    pre();
    int n;
	cin >> n;
	poly arr(n);
	For(i, 0 ,n-1)
	    cin >> arr[i];
	poly ans = compute(n, arr);
	For(i, 1, n)
	    ans[i] = (ans[i] + ans[i-1])%mo;
	int q;
	cin >> q;
	while(q--)
	{
	    int m;
	    cin >> m;
	    cout << ans[m] << '\n';
	}
}
``

Tester's Solution
``#include <bits/stdc++.h>

#include <cassert>
#include <numeric>
#include <type_traits>

#ifdef _MSC_VER
#include <intrin.h>
#endif

#include <utility>

#ifdef _MSC_VER
#include <intrin.h>
#endif

namespace atcoder {

namespace internal {

constexpr long long safe_mod(long long x, long long m) {
    x %= m;
    if (x < 0) x += m;
    return x;
}

struct barrett {
    unsigned int _m;
    unsigned long long im;

    barrett(unsigned int m) : _m(m), im((unsigned long long)(-1) / m + 1) {}

    unsigned int umod() const { return _m; }

    unsigned int mul(unsigned int a, unsigned int b) const {

        unsigned long long z = a;
        z *= b;
#ifdef _MSC_VER
        unsigned long long x;
        _umul128(z, im, &x);
#else
        unsigned long long x =
            (unsigned long long)(((unsigned __int128)(z)*im) >> 64);
#endif
        unsigned int v = (unsigned int)(z - x * _m);
        if (_m <= v) v += _m;
        return v;
    }
};

constexpr long long pow_mod_constexpr(long long x, long long n, int m) {
    if (m == 1) return 0;
    unsigned int _m = (unsigned int)(m);
    unsigned long long r = 1;
    unsigned long long y = safe_mod(x, m);
    while (n) {
        if (n & 1) r = (r * y) % _m;
        y = (y * y) % _m;
        n >>= 1;
    }
    return r;
}

constexpr bool is_prime_constexpr(int n) {
    if (n <= 1) return false;
    if (n == 2 || n == 7 || n == 61) return true;
    if (n % 2 == 0) return false;
    long long d = n - 1;
    while (d % 2 == 0) d /= 2;
    constexpr long long bases[3] = {2, 7, 61};
    for (long long a : bases) {
        long long t = d;
        long long y = pow_mod_constexpr(a, t, n);
        while (t != n - 1 && y != 1 && y != n - 1) {
            y = y * y % n;
            t <<= 1;
        }
        if (y != n - 1 && t % 2 == 0) {
            return false;
        }
    }
    return true;
}
template <int n> constexpr bool is_prime = is_prime_constexpr(n);

constexpr std::pair<long long, long long> inv_gcd(long long a, long long b) {
    a = safe_mod(a, b);
    if (a == 0) return {b, 0};

    long long s = b, t = a;
    long long m0 = 0, m1 = 1;

    while (t) {
        long long u = s / t;
        s -= t * u;
        m0 -= m1 * u;  // |m1 * u| <= |m1| * s <= b

        auto tmp = s;
        s = t;
        t = tmp;
        tmp = m0;
        m0 = m1;
        m1 = tmp;
    }
    if (m0 < 0) m0 += b / s;
    return {s, m0};
}

constexpr int primitive_root_constexpr(int m) {
    if (m == 2) return 1;
    if (m == 167772161) return 3;
    if (m == 469762049) return 3;
    if (m == 754974721) return 11;
    if (m == 998244353) return 3;
    int divs[20] = {};
    divs[0] = 2;
    int cnt = 1;
    int x = (m - 1) / 2;
    while (x % 2 == 0) x /= 2;
    for (int i = 3; (long long)(i)*i <= x; i += 2) {
        if (x % i == 0) {
            divs[cnt++] = i;
            while (x % i == 0) {
                x /= i;
            }
        }
    }
    if (x > 1) {
        divs[cnt++] = x;
    }
    for (int g = 2;; g++) {
        bool ok = true;
        for (int i = 0; i < cnt; i++) {
            if (pow_mod_constexpr(g, (m - 1) / divs[i], m) == 1) {
                ok = false;
                break;
            }
        }
        if (ok) return g;
    }
}
template <int m> constexpr int primitive_root = primitive_root_constexpr(m);

}  // namespace internal

}  // namespace atcoder

#include <cassert>
#include <numeric>
#include <type_traits>

namespace atcoder {

namespace internal {

#ifndef _MSC_VER
template <class T>
using is_signed_int128 =
    typename std::conditional<std::is_same<T, __int128_t>::value ||
                                  std::is_same<T, __int128>::value,
                              std::true_type,
                              std::false_type>::type;

template <class T>
using is_unsigned_int128 =
    typename std::conditional<std::is_same<T, __uint128_t>::value ||
                                  std::is_same<T, unsigned __int128>::value,
                              std::true_type,
                              std::false_type>::type;

template <class T>
using make_unsigned_int128 =
    typename std::conditional<std::is_same<T, __int128_t>::value,
                              __uint128_t,
                              unsigned __int128>;

template <class T>
using is_integral = typename std::conditional<std::is_integral<T>::value ||
                                                  is_signed_int128<T>::value ||
                                                  is_unsigned_int128<T>::value,
                                              std::true_type,
                                              std::false_type>::type;

template <class T>
using is_signed_int = typename std::conditional<(is_integral<T>::value &&
                                                 std::is_signed<T>::value) ||
                                                    is_signed_int128<T>::value,
                                                std::true_type,
                                                std::false_type>::type;

template <class T>
using is_unsigned_int =
    typename std::conditional<(is_integral<T>::value &&
                               std::is_unsigned<T>::value) ||
                                  is_unsigned_int128<T>::value,
                              std::true_type,
                              std::false_type>::type;

template <class T>
using to_unsigned = typename std::conditional<
    is_signed_int128<T>::value,
    make_unsigned_int128<T>,
    typename std::conditional<std::is_signed<T>::value,
                              std::make_unsigned<T>,
                              std::common_type<T>>::type>::type;

#else

template <class T> using is_integral = typename std::is_integral<T>;

template <class T>
using is_signed_int =
    typename std::conditional<is_integral<T>::value && std::is_signed<T>::value,
                              std::true_type,
                              std::false_type>::type;

template <class T>
using is_unsigned_int =
    typename std::conditional<is_integral<T>::value &&
                                  std::is_unsigned<T>::value,
                              std::true_type,
                              std::false_type>::type;

template <class T>
using to_unsigned = typename std::conditional<is_signed_int<T>::value,
                                              std::make_unsigned<T>,
                                              std::common_type<T>>::type;

#endif

template <class T>
using is_signed_int_t = std::enable_if_t<is_signed_int<T>::value>;

template <class T>
using is_unsigned_int_t = std::enable_if_t<is_unsigned_int<T>::value>;

template <class T> using to_unsigned_t = typename to_unsigned<T>::type;

}  // namespace internal

}  // namespace atcoder

namespace atcoder {

namespace internal {

struct modint_base {};
struct static_modint_base : modint_base {};

template <class T> using is_modint = std::is_base_of<modint_base, T>;
template <class T> using is_modint_t = std::enable_if_t<is_modint<T>::value>;

}  // namespace internal

template <int m, std::enable_if_t<(1 <= m)>* = nullptr>
struct static_modint : internal::static_modint_base {
    using mint = static_modint;

  public:
    static constexpr int mod() { return m; }
    static mint raw(int v) {
        mint x;
        x._v = v;
        return x;
    }

    static_modint() : _v(0) {}
    template <class T, internal::is_signed_int_t<T>* = nullptr>
    static_modint(T v) {
        long long x = (long long)(v % (long long)(umod()));
        if (x < 0) x += umod();
        _v = (unsigned int)(x);
    }
    template <class T, internal::is_unsigned_int_t<T>* = nullptr>
    static_modint(T v) {
        _v = (unsigned int)(v % umod());
    }

    unsigned int val() const { return _v; }

    mint& operator++() {
        _v++;
        if (_v == umod()) _v = 0;
        return *this;
    }
    mint& operator--() {
        if (_v == 0) _v = umod();
        _v--;
        return *this;
    }
    mint operator++(int) {
        mint result = *this;
        ++*this;
        return result;
    }
    mint operator--(int) {
        mint result = *this;
        --*this;
        return result;
    }

    mint& operator+=(const mint& rhs) {
        _v += rhs._v;
        if (_v >= umod()) _v -= umod();
        return *this;
    }
    mint& operator-=(const mint& rhs) {
        _v -= rhs._v;
        if (_v >= umod()) _v += umod();
        return *this;
    }
    mint& operator*=(const mint& rhs) {
        unsigned long long z = _v;
        z *= rhs._v;
        _v = (unsigned int)(z % umod());
        return *this;
    }
    mint& operator/=(const mint& rhs) { return *this = *this * rhs.inv(); }

    mint operator+() const { return *this; }
    mint operator-() const { return mint() - *this; }

    mint pow(long long n) const {
        assert(0 <= n);
        mint x = *this, r = 1;
        while (n) {
            if (n & 1) r *= x;
            x *= x;
            n >>= 1;
        }
        return r;
    }
    mint inv() const {
        if (prime) {
            assert(_v);
            return pow(umod() - 2);
        } else {
            auto eg = internal::inv_gcd(_v, m);
            assert(eg.first == 1);
            return eg.second;
        }
    }

    friend mint operator+(const mint& lhs, const mint& rhs) {
        return mint(lhs) += rhs;
    }
    friend mint operator-(const mint& lhs, const mint& rhs) {
        return mint(lhs) -= rhs;
    }
    friend mint operator*(const mint& lhs, const mint& rhs) {
        return mint(lhs) *= rhs;
    }
    friend mint operator/(const mint& lhs, const mint& rhs) {
        return mint(lhs) /= rhs;
    }
    friend bool operator==(const mint& lhs, const mint& rhs) {
        return lhs._v == rhs._v;
    }
    friend bool operator!=(const mint& lhs, const mint& rhs) {
        return lhs._v != rhs._v;
    }

  private:
    unsigned int _v;
    static constexpr unsigned int umod() { return m; }
    static constexpr bool prime = internal::is_prime<m>;
};

template <int id> struct dynamic_modint : internal::modint_base {
    using mint = dynamic_modint;

  public:
    static int mod() { return (int)(bt.umod()); }
    static void set_mod(int m) {
        assert(1 <= m);
        bt = internal::barrett(m);
    }
    static mint raw(int v) {
        mint x;
        x._v = v;
        return x;
    }

    dynamic_modint() : _v(0) {}
    template <class T, internal::is_signed_int_t<T>* = nullptr>
    dynamic_modint(T v) {
        long long x = (long long)(v % (long long)(mod()));
        if (x < 0) x += mod();
        _v = (unsigned int)(x);
    }
    template <class T, internal::is_unsigned_int_t<T>* = nullptr>
    dynamic_modint(T v) {
        _v = (unsigned int)(v % mod());
    }

    unsigned int val() const { return _v; }

    mint& operator++() {
        _v++;
        if (_v == umod()) _v = 0;
        return *this;
    }
    mint& operator--() {
        if (_v == 0) _v = umod();
        _v--;
        return *this;
    }
    mint operator++(int) {
        mint result = *this;
        ++*this;
        return result;
    }
    mint operator--(int) {
        mint result = *this;
        --*this;
        return result;
    }

    mint& operator+=(const mint& rhs) {
        _v += rhs._v;
        if (_v >= umod()) _v -= umod();
        return *this;
    }
    mint& operator-=(const mint& rhs) {
        _v += mod() - rhs._v;
        if (_v >= umod()) _v -= umod();
        return *this;
    }
    mint& operator*=(const mint& rhs) {
        _v = bt.mul(_v, rhs._v);
        return *this;
    }
    mint& operator/=(const mint& rhs) { return *this = *this * rhs.inv(); }

    mint operator+() const { return *this; }
    mint operator-() const { return mint() - *this; }

    mint pow(long long n) const {
        assert(0 <= n);
        mint x = *this, r = 1;
        while (n) {
            if (n & 1) r *= x;
            x *= x;
            n >>= 1;
        }
        return r;
    }
    mint inv() const {
        auto eg = internal::inv_gcd(_v, mod());
        assert(eg.first == 1);
        return eg.second;
    }

    friend mint operator+(const mint& lhs, const mint& rhs) {
        return mint(lhs) += rhs;
    }
    friend mint operator-(const mint& lhs, const mint& rhs) {
        return mint(lhs) -= rhs;
    }
    friend mint operator*(const mint& lhs, const mint& rhs) {
        return mint(lhs) *= rhs;
    }
    friend mint operator/(const mint& lhs, const mint& rhs) {
        return mint(lhs) /= rhs;
    }
    friend bool operator==(const mint& lhs, const mint& rhs) {
        return lhs._v == rhs._v;
    }
    friend bool operator!=(const mint& lhs, const mint& rhs) {
        return lhs._v != rhs._v;
    }

  private:
    unsigned int _v;
    static internal::barrett bt;
    static unsigned int umod() { return bt.umod(); }
};
template <int id> internal::barrett dynamic_modint<id>::bt = 998244353;

using modint998244353 = static_modint<998244353>;
using modint1000000007 = static_modint<1000000007>;
using modint = dynamic_modint<-1>;

namespace internal {

template <class T>
using is_static_modint = std::is_base_of<internal::static_modint_base, T>;

template <class T>
using is_static_modint_t = std::enable_if_t<is_static_modint<T>::value>;

template <class> struct is_dynamic_modint : public std::false_type {};
template <int id>
struct is_dynamic_modint<dynamic_modint<id>> : public std::true_type {};

template <class T>
using is_dynamic_modint_t = std::enable_if_t<is_dynamic_modint<T>::value>;

}  // namespace internal

}  // namespace atcoder

#include <algorithm>
#include <array>
#include <cassert>
#include <type_traits>
#include <vector>

#ifdef _MSC_VER
#include <intrin.h>
#endif

namespace atcoder {

namespace internal {

int ceil_pow2(int n) {
    int x = 0;
    while ((1U << x) < (unsigned int)(n)) x++;
    return x;
}

int bsf(unsigned int n) {
#ifdef _MSC_VER
    unsigned long index;
    _BitScanForward(&index, n);
    return index;
#else
    return __builtin_ctz(n);
#endif
}

}  // namespace internal

}  // namespace atcoder

namespace atcoder {

namespace internal {

template <class mint, internal::is_static_modint_t<mint>* = nullptr>
void butterfly(std::vector<mint>& a) {
    static constexpr int g = internal::primitive_root<mint::mod()>;
    int n = int(a.size());
    int h = internal::ceil_pow2(n);

    static bool first = true;
    static mint sum_e[30];  // sum_e[i] = ies[0] * ... * ies[i - 1] * es[i]
    if (first) {
        first = false;
        mint es[30], ies[30];  // es[i]^(2^(2+i)) == 1
        int cnt2 = bsf(mint::mod() - 1);
        mint e = mint(g).pow((mint::mod() - 1) >> cnt2), ie = e.inv();
        for (int i = cnt2; i >= 2; i--) {
            es[i - 2] = e;
            ies[i - 2] = ie;
            e *= e;
            ie *= ie;
        }
        mint now = 1;
        for (int i = 0; i <= cnt2 - 2; i++) {
            sum_e[i] = es[i] * now;
            now *= ies[i];
        }
    }
    for (int ph = 1; ph <= h; ph++) {
        int w = 1 << (ph - 1), p = 1 << (h - ph);
        mint now = 1;
        for (int s = 0; s < w; s++) {
            int offset = s << (h - ph + 1);
            for (int i = 0; i < p; i++) {
                auto l = a[i + offset];
                auto r = a[i + offset + p] * now;
                a[i + offset] = l + r;
                a[i + offset + p] = l - r;
            }
            now *= sum_e[bsf(~(unsigned int)(s))];
        }
    }
}

template <class mint, internal::is_static_modint_t<mint>* = nullptr>
void butterfly_inv(std::vector<mint>& a) {
    static constexpr int g = internal::primitive_root<mint::mod()>;
    int n = int(a.size());
    int h = internal::ceil_pow2(n);

    static bool first = true;
    static mint sum_ie[30];  // sum_ie[i] = es[0] * ... * es[i - 1] * ies[i]
    if (first) {
        first = false;
        mint es[30], ies[30];  // es[i]^(2^(2+i)) == 1
        int cnt2 = bsf(mint::mod() - 1);
        mint e = mint(g).pow((mint::mod() - 1) >> cnt2), ie = e.inv();
        for (int i = cnt2; i >= 2; i--) {
            es[i - 2] = e;
            ies[i - 2] = ie;
            e *= e;
            ie *= ie;
        }
        mint now = 1;
        for (int i = 0; i <= cnt2 - 2; i++) {
            sum_ie[i] = ies[i] * now;
            now *= es[i];
        }
    }

    for (int ph = h; ph >= 1; ph--) {
        int w = 1 << (ph - 1), p = 1 << (h - ph);
        mint inow = 1;
        for (int s = 0; s < w; s++) {
            int offset = s << (h - ph + 1);
            for (int i = 0; i < p; i++) {
                auto l = a[i + offset];
                auto r = a[i + offset + p];
                a[i + offset] = l + r;
                a[i + offset + p] =
                    (unsigned long long)(mint::mod() + l.val() - r.val()) *
                    inow.val();
            }
            inow *= sum_ie[bsf(~(unsigned int)(s))];
        }
    }
}

}  // namespace internal

template <class mint, internal::is_static_modint_t<mint>* = nullptr>
std::vector<mint> convolution(std::vector<mint> a, std::vector<mint> b) {
    int n = int(a.size()), m = int(b.size());
    if (!n || !m) return {};
    if (std::min(n, m) <= 60) {
        if (n < m) {
            std::swap(n, m);
            std::swap(a, b);
        }
        std::vector<mint> ans(n + m - 1);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                ans[i + j] += a[i] * b[j];
            }
        }
        return ans;
    }
    int z = 1 << internal::ceil_pow2(n + m - 1);
    a.resize(z);
    internal::butterfly(a);
    b.resize(z);
    internal::butterfly(b);
    for (int i = 0; i < z; i++) {
        a[i] *= b[i];
    }
    internal::butterfly_inv(a);
    a.resize(n + m - 1);
    mint iz = mint(z).inv();
    for (int i = 0; i < n + m - 1; i++) a[i] *= iz;
    return a;
}

template <unsigned int mod = 998244353,
          class T,
          std::enable_if_t<internal::is_integral<T>::value>* = nullptr>
std::vector<T> convolution(const std::vector<T>& a, const std::vector<T>& b) {
    int n = int(a.size()), m = int(b.size());
    if (!n || !m) return {};

    using mint = static_modint<mod>;
    std::vector<mint> a2(n), b2(m);
    for (int i = 0; i < n; i++) {
        a2[i] = mint(a[i]);
    }
    for (int i = 0; i < m; i++) {
        b2[i] = mint(b[i]);
    }
    auto c2 = convolution(move(a2), move(b2));
    std::vector<T> c(n + m - 1);
    for (int i = 0; i < n + m - 1; i++) {
        c[i] = c2[i].val();
    }
    return c;
}

std::vector<long long> convolution_ll(const std::vector<long long>& a,
                                      const std::vector<long long>& b) {
    int n = int(a.size()), m = int(b.size());
    if (!n || !m) return {};

    static constexpr unsigned long long MOD1 = 754974721;  // 2^24
    static constexpr unsigned long long MOD2 = 167772161;  // 2^25
    static constexpr unsigned long long MOD3 = 469762049;  // 2^26
    static constexpr unsigned long long M2M3 = MOD2 * MOD3;
    static constexpr unsigned long long M1M3 = MOD1 * MOD3;
    static constexpr unsigned long long M1M2 = MOD1 * MOD2;
    static constexpr unsigned long long M1M2M3 = MOD1 * MOD2 * MOD3;

    static constexpr unsigned long long i1 =
        internal::inv_gcd(MOD2 * MOD3, MOD1).second;
    static constexpr unsigned long long i2 =
        internal::inv_gcd(MOD1 * MOD3, MOD2).second;
    static constexpr unsigned long long i3 =
        internal::inv_gcd(MOD1 * MOD2, MOD3).second;

    auto c1 = convolution<MOD1>(a, b);
    auto c2 = convolution<MOD2>(a, b);
    auto c3 = convolution<MOD3>(a, b);

    std::vector<long long> c(n + m - 1);
    for (int i = 0; i < n + m - 1; i++) {
        unsigned long long x = 0;
        x += (c1[i] * i1) % MOD1 * M2M3;
        x += (c2[i] * i2) % MOD2 * M1M3;
        x += (c3[i] * i3) % MOD3 * M1M2;
        long long diff =
            c1[i] - internal::safe_mod((long long)(x), (long long)(MOD1));
        if (diff < 0) diff += MOD1;
        static constexpr unsigned long long offset[5] = {
            0, 0, M1M2M3, 2 * M1M2M3, 3 * M1M2M3};
        x -= offset[diff % 5];
        c[i] = x;
    }

    return c;
}

}  // namespace atcoder

using namespace std;
using mint = atcoder::modint998244353;
int main(){
  ios::sync_with_stdio(false);
  cin.tie(0);
  const int mod = 998244353;
  int n;
  cin >> n;
  vector<int> a(n);
  vector<mint> ans(n + 1);
  for(int i = 0; i < n; i++)
    cin >> a[i];
  vector<mint> fat(n + 1, 1), ifat(n + 1);
  for(int i = 1; i <= n; i++)
    fat[i] = fat[i - 1] * i;
  for(int i = 0; i <= n; i++)
    ifat[i] = mint(1) / fat[i];
  auto ncr = [&](int n, int r){
    if(n < r) return mint(0);
    return fat[n] * ifat[r] * ifat[n - r];
  };
  for(int b = 0; b < 30; b++){
    int c[2] = {};
    for(int i = 0; i < n; i++){
      c[(a[i]>>b)&1]++;
    }
    vector<int> A(n + 1, 0), B(n + 1, 0);
    for(int i = 0; i <= c[0]; i++) A[i] = ncr(c[0], i).val();
    for(int i = 1; i <= c[1]; i += 2) B[i] = ncr(c[1], i).val();
    auto res = atcoder::convolution(A, B);
    for(int i = 0; i <= n; i++){
      ans[i] += mint(2).pow(b) * res[i];
    }
  }
  for(int i = 1; i <= n; i++)
    ans[i] += ans[i - 1];
  int q;
  cin >> q;
  while(q--){
    int x;
    cin >> x;
    cout << ans[x].val() << '\n';
  }
  return 0;
}
``

# VIDEO EDITORIAL:

</details>
