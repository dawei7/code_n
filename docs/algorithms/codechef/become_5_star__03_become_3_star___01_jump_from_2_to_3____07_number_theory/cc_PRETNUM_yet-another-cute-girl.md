# Yet Another Cute Girl

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PRETNUM |
| Difficulty Rating | 1850 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Number Theory |
| Official Link | [PRETNUM](https://www.codechef.com/practice/course/2to3stars/LP2TO307/problems/PRETNUM) |

---

## Problem Statement

Chef doesn't love math anymore. He loves Sasha. Sashen'ka is cute.

Chef goes on a date with her. Flowers are boring, while numbers are not. He knows that most of all this girl loves numbers, that's why he is going to bring ribbon with numbers **L, L+1, L+2, ..., R** written on it.

Sasha thinks that numbers with prime number of divisors are special. That's why she is going to kiss boy for each such number he will bring.

Now Chef wonder how many times he will be kissed by Sashen'ka ?

### Input
The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.
The first line of each test case contains two number **L, R**.

### Output
For each test case, output a single line containing answer for corresponding test case.

### Constraints

- **1** ≤ **T** ≤ **5**

- **1** ≤ **L** ≤ **R** ≤ **1012**

- **0** ≤ **R-L** ≤ **106**

---

## Examples

**Example 1**

**Input**

```text
1
1 10
```

**Output**

```text
6
```

**Explanation**

**Example case 1.** Numbers 2,3,4,5,7,9 are special.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/PRETNUM)

[Contest](http://www.codechef.com/NOV13/problems/PRETNUM)

### DIFFICULTY:

EASY

### PREREQUISITES:

Prime factorization, [Sieve](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

### PROBLEM:

Find the number of integers in the given range which have prime number of divisors.

### QUICK EXPLANATION:

Although L and R can be as high as 10^12 but R-L is <= 10^6, this allows us to iterate through the complete range and count the number of divisors of each number in the range.

### EXPLANATION:

**Approach 1:**

If a number N is divisible by D then either it has 2 factors(D and N/D) or it is square of D. Another thing to note is that if a number has 2 divisors x and y such that x < y, then x < sqrt(N) and y > sqrt(N). Using these 2 facts we can iterate through all the numbers in range [1, sqrt®] and count the number of factors for each of the number.

Working commented solution follows:

``bool isPrime[10000];
void init()
{
	// Since range is very small so not used Sieve
	for (int i = 2; i < sizeof(isPrime); ++i) {
		int j = 2;
		for (; j * j <= i; ++j) {
			if (i % j == 0) {
				break;
			}
		}
		if (j * j > i) isPrime[i] = true;
	}
}
``
``main()
{
	init();
	int testCases, divisors[1000005];
	scanf("%d", &testCases);
	while(testCases--) {
		long long L, R;
		scanf("%lld%lld", &L, &R);
		for(long long i=L; i<=R; i++) divisors[i-L] = 0; //Initialize divisors of all numbers to 0
		for(long long i=1; i*i <= R; i++) { // Iterate through 1 to sqrt(R)
			long long square = i*i;
			// j starts with first number in range [L, R] which is multiple of i
			for(long long j=( (L-1) / i + 1) * i; j <= R; j += i) {
				// Factors under consideration are i and j / i
				if (j < square) continue; // Already counted because of 2 in else condition below
				if( square == j ) // Just 1 factor
					divisors[j-L] += 1;
				else divisors[j-L] += 2; // Counting factors i and j / i
			}
		}
		int ans = 0;
		for(long long i = L; i <= R; i++) if(isPrime[divisors[i-L]]) ans++;
		printf("%d\n",ans);
	}
}
``

**Approach 2:**

This approach is taken by more coders including tester.

This is based on **prime factorization** of a number and then counting the total number of divisors.

Lets take an example:

Consider prime factors breakdown of 18 (2^1 * 3^2) so total number of factors are (1+1) * (2 + 1) = 6 [Factors: 1, 2, 3, 6, 9, 18]. Similarly if a number is p1^x1 * p2^x2 * p3^x3 * … then total number of factors is (x1+1) * (x2+1) * (x3+1) * …

Now if we generate all primes <= 10^6 using [sieve](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) and later use them to find out how many times it goes into each number in the given range, we know the number of divisors composed of primes <= 10^6. We may have missed 1 prime number > 10^6 which might have fallen in the range as range goes as high as 10^12. But we are sure that there is only 1 such prime! So if we detect this case we can simply multiply our number of factors calculated so far by (1+1). See tester’s solution for working code.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution will be uploaded soon

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/2013/November/Tester1/PRETNUM.cpp) and [here](http://www.codechef.com/download/Solutions/2013/November/Tester2/PRETNUM.cpp)

</details>
