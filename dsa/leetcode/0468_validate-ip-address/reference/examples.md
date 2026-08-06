## Examples

**Example 1**

- Input: `queryIP = "172.16.254.1"`
- Output: `"IPv4"`
- **Explanation:** The candidate satisfies every IPv4 rule, so return `"IPv4"`.

**Example 2**

- Input: `queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"`
- Output: `"IPv6"`
- **Explanation:** The candidate satisfies every IPv6 rule, so return `"IPv6"`.

**Example 3**

- Input: `queryIP = "256.256.256.256"`
- Output: `"Neither"`
- **Explanation:** The candidate is neither a valid IPv4 address nor a valid IPv6 address.
