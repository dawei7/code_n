## Examples

**Example 1**

- Input: `emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]`
- Output: `2`
- Explanation:

| Email | Local | Normalized Local | Domain | Normalized Domain | Final Email |
|---|---|---|---|---|---|
| `test.email+alex@leetcode.com` | `test.email+alex` | `testemail` | `leetcode.com` | `leetcode.com` | `testemail@leetcode.com` |
| `test.e.mail+bob.cathy@leetcode.com` | `test.e.mail+bob.cathy` | `testemail` | `leetcode.com` | `leetcode.com` | `testemail@leetcode.com` |
| `testemail+david@lee.tcode.com` | `testemail+david` | `testemail` | `lee.tcode.com` | `lee.tcode.com` | `testemail@lee.tcode.com` |

  - The unique normalized addresses are `testemail@leetcode.com` and
    `testemail@lee.tcode.com`, so the answer is `2`.

**Example 2**

- Input: `emails = ["A@B.com", "a@b.com", "ab+xy@b.com", "a.b@b.com"]`
- Output: `2`
- Explanation:

| Email | Local | Normalized Local | Domain | Normalized Domain | Final Email |
|---|---|---|---|---|---|
| `A@B.com` | `A` | `a` | `B.com` | `b.com` | `a@b.com` |
| `a@b.com` | `a` | `a` | `b.com` | `b.com` | `a@b.com` |
| `ab+xy@b.com` | `ab+xy` | `ab` | `b.com` | `b.com` | `ab@b.com` |
| `a.b@b.com` | `a.b` | `ab` | `b.com` | `b.com` | `ab@b.com` |

  - The unique normalized addresses are `a@b.com` and `ab@b.com`, giving
    `2` groups.

**Example 3**

- Input: `emails = ["a.b+c.d+e@DoMain.com", "ab+xyz@domain.com", "ab@domain.com"]`
- Output: `1`
- Explanation:

| Email | Local | Normalized Local | Domain | Normalized Domain | Final Email |
|---|---|---|---|---|---|
| `a.b+c.d+e@DoMain.com` | `a.b+c.d+e` | `ab` | `DoMain.com` | `domain.com` | `ab@domain.com` |
| `ab+xyz@domain.com` | `ab+xyz` | `ab` | `domain.com` | `domain.com` | `ab@domain.com` |
| `ab@domain.com` | `ab` | `ab` | `domain.com` | `domain.com` | `ab@domain.com` |

  - All three addresses normalize to `ab@domain.com`; therefore the answer is
    `1`.
