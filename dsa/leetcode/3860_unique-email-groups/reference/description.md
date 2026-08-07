## Description

You are given an array of strings `emails`, where each string is a valid email address.

Two email addresses belong to the same group if **both** their **normalized** local names and **normalized** domain names are **identical**.

The normalization rules are as follows:

- The local name is the part **before** the `'@'` symbol.

		<li>Ignore all dots `'.'`.

- Ignore everything after the first `'+'`, if present.

- Convert to lowercase.

	</li>
- The domain name is the part **after** the `'@'` symbol.

		<li>Convert to lowercase.

	</li>

Return an integer denoting the number of **unique** email groups after normalization.
### Function Contract

**Inputs**

- `emails`: A nonempty array of valid email-address strings.

Each address has exactly one `@`, separating a nonempty local name from a
nonempty domain name. Define the total character count

$S = \sum_{e \in \texttt{emails}} \lvert e \rvert.$

Normalization is case-insensitive in both parts, but the dot-removal and
plus-suffix rules apply only to the local name.

**Return value**

Return the number of distinct normalized addresses, which is the number of
unique email groups.

### Examples

#### Example 1

<div class="example-block">
**Input:** emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]

**Output:** 2

**Explanation:**

</div>

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Email</th>
			<th style="border: 1px solid black;">Local</th>
			<th style="border: 1px solid black;">Normalized Local</th>
			<th style="border: 1px solid black;">Domain</th>
			<th style="border: 1px solid black;">Normalized Domain</th>
			<th style="border: 1px solid black;">Final Email</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">test.email+alex@leetcode.com</td>
			<td style="border: 1px solid black;">test.email+alex</td>
			<td style="border: 1px solid black;">testemail</td>
			<td style="border: 1px solid black;">leetcode.com</td>
			<td style="border: 1px solid black;">leetcode.com</td>
			<td style="border: 1px solid black;">testemail@leetcode.com</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">test.e.mail+bob.cathy@leetcode.com</td>
			<td style="border: 1px solid black;">test.e.mail+bob.cathy</td>
			<td style="border: 1px solid black;">testemail</td>
			<td style="border: 1px solid black;">leetcode.com</td>
			<td style="border: 1px solid black;">leetcode.com</td>
			<td style="border: 1px solid black;">testemail@leetcode.com</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">testemail+david@lee.tcode.com</td>
			<td style="border: 1px solid black;">testemail+david</td>
			<td style="border: 1px solid black;">testemail</td>
			<td style="border: 1px solid black;">lee.tcode.com</td>
			<td style="border: 1px solid black;">lee.tcode.com</td>
			<td style="border: 1px solid black;">testemail@lee.tcode.com</td>
		</tr>
	</tbody>
</table>

Unique emails are [`"testemail@leetcode.com"`, `"testemail@lee.tcode.com"`]. Thus, the answer is 2.
#### Example 2

<div class="example-block">
**Input:** emails = ["A@B.com", "a@b.com", "ab+xy@b.com", "a.b@b.com"]

**Output:** 2

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Email</th>
			<th style="border: 1px solid black;">Local</th>
			<th style="border: 1px solid black;">Normalized Local</th>
			<th style="border: 1px solid black;">Domain</th>
			<th style="border: 1px solid black;">Normalized Domain</th>
			<th style="border: 1px solid black;">Final Email</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">A@B.com</td>
			<td style="border: 1px solid black;">A</td>
			<td style="border: 1px solid black;">a</td>
			<td style="border: 1px solid black;">B.com</td>
			<td style="border: 1px solid black;">b.com</td>
			<td style="border: 1px solid black;">a@b.com</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">a@b.com</td>
			<td style="border: 1px solid black;">a</td>
			<td style="border: 1px solid black;">a</td>
			<td style="border: 1px solid black;">b.com</td>
			<td style="border: 1px solid black;">b.com</td>
			<td style="border: 1px solid black;">a@b.com</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">ab+xy@b.com</td>
			<td style="border: 1px solid black;">ab+xy</td>
			<td style="border: 1px solid black;">ab</td>
			<td style="border: 1px solid black;">b.com</td>
			<td style="border: 1px solid black;">b.com</td>
			<td style="border: 1px solid black;">ab@b.com</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">a.b@b.com</td>
			<td style="border: 1px solid black;">a.b</td>
			<td style="border: 1px solid black;">ab</td>
			<td style="border: 1px solid black;">b.com</td>
			<td style="border: 1px solid black;">b.com</td>
			<td style="border: 1px solid black;">ab@b.com</td>
		</tr>
	</tbody>
</table>

Unique emails are [`"a@b.com"`, `"ab@b.com"`]. Thus, the answer is 2.

</div>
#### Example 3

<div class="example-block">
**Input:** emails = ["a.b+c.d+e@DoMain.com", "ab+xyz@domain.com", "ab@domain.com"]

**Output:** 1

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Email</th>
			<th style="border: 1px solid black;">Local</th>
			<th style="border: 1px solid black;">Normalized Local</th>
			<th style="border: 1px solid black;">Domain</th>
			<th style="border: 1px solid black;">Normalized Domain</th>
			<th style="border: 1px solid black;">Final Email</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">a.b+c.d+e@DoMain.com</td>
			<td style="border: 1px solid black;">a.b+c.d+e</td>
			<td style="border: 1px solid black;">ab</td>
			<td style="border: 1px solid black;">DoMain.com</td>
			<td style="border: 1px solid black;">domain.com</td>
			<td style="border: 1px solid black;">ab@domain.com</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">ab+xyz@domain.com</td>
			<td style="border: 1px solid black;">ab+xyz</td>
			<td style="border: 1px solid black;">ab</td>
			<td style="border: 1px solid black;">domain.com</td>
			<td style="border: 1px solid black;">domain.com</td>
			<td style="border: 1px solid black;">ab@domain.com</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">ab@domain.com</td>
			<td style="border: 1px solid black;">ab</td>
			<td style="border: 1px solid black;">ab</td>
			<td style="border: 1px solid black;">domain.com</td>
			<td style="border: 1px solid black;">domain.com</td>
			<td style="border: 1px solid black;">ab@domain.com</td>
		</tr>
	</tbody>
</table>

All emails normalize to `"ab@domain.com"`. Thus, the answer is 1.

</div>
### Constraints

- $1 \le \text{emails.length} \le 1000$

- $1 \le \text{emails}[i].length \le 100$

- $\text{emails}[i]$ consists of lowercase and uppercase English letters, digits, and the characters `'.'`, `'+'`, and `'@'`.

- Each $\text{emails}[i]$ contains **exactly** one `'@'` character.

- All local and domain names are non-empty; local names do not start with `'+'`.

- Domain names end with the `".com"` suffix and contain at least one character before `".com"`.