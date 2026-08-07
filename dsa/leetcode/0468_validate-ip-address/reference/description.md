### 1. Description

Given a string `queryIP`, return `"IPv4"` if IP is a valid IPv4 address, `"IPv6"` if IP is a valid IPv6 address or `"Neither"` if IP is not a correct IP of any type.

**A valid IPv4** address is an IP in the form $"x_{1}.x_{2}.x_{3}.x_{4}"$ where $0 \le x_{i} \le 255$ and $x_{i}$ **cannot contain** leading zeros. For example, `"192.168.1.1"` and `"192.168.1.0"` are valid IPv4 addresses while `"192.168.01.1"`, `"192.168.1.00"`, and `"192.168@1.1"` are invalid IPv4 addresses.

**A valid IPv6** address is an IP in the form $"x_{1}:x_{2}:x_{3}:x_{4}:x_{5}:x_{6}:x_{7}:x_{8}"$ where:

- $1 \le x_{i}.length \le 4$

- $x_{i}$ is a **hexadecimal string** which may contain digits, lowercase English letter (`'a'` to `'f'`) and upper-case English letters (`'A'` to `'F'`).

- Leading zeros are allowed in $x_{i}$.

For example, "`2001:0db8:85a3:0000:0000:8a2e:0370:7334"` and "`2001:db8:85a3:0:0:8A2E:0370:7334"` are valid IPv6 addresses, while "`2001:0db8:85a3::8A2E:037j:7334"` and "`02001:0db8:85a3:0000:0000:8a2e:0370:7334"` are invalid IPv6 addresses.

### 2. Function Contract

**Inputs**

- `queryIP`: The candidate address string.

**Return value**

- Return exactly `"IPv4"`, `"IPv6"`, or `"Neither"` according to the full-form grammars in the description.

IPv6 compression such as `::` is not part of the accepted grammar because all eight fields must be present and nonempty.

### 3. Examples

#### Example 1

- **Input:** $queryIP = "172.16.254.1"$
- **Output:** `"IPv4"`
- **Explanation:** This is a valid IPv4 address, return "IPv4".
#### Example 2

- **Input:** $queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"$
- **Output:** `"IPv6"`
- **Explanation:** This is a valid IPv6 address, return "IPv6".
#### Example 3

- **Input:** $queryIP = "256.256.256.256"$
- **Output:** `"Neither"`
- **Explanation:** This is neither a IPv4 address nor a IPv6 address.

### 4. Constraints

- `queryIP` consists only of English letters, digits and the characters `'.'` and `':'`.