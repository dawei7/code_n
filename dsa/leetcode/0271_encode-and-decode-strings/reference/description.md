## Description

Design an algorithm to encode **a list of strings** to **a string**. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

```
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
```

Machine 2 (receiver) has the function:

```
vector<string> decode(string s) {
  //... your code
  return strs;
}
```

So Machine 1 does:

```
string encoded_string = encode(strs);
```

and Machine 2 does:

```
vector<string> strs2 = decode(encoded_string);
```

`strs2` in Machine 2 should be the same as `strs` in Machine 1.

Implement the `encode` and `decode` methods.

You are not allowed to solve the problem using any serialize methods (such as `eval`).
### Function Contract

**Inputs**

- `operation`: Either `"encode"` or `"decode"` in the offline app adapter.
- `value`: A list of strings for encoding, or a previously encoded string for decoding.

For encoding, let $c$ include all payload characters and decimal length-header characters. For decoding, let $c$ be
the encoded string's length.

**Return value**

For `"encode"`, return the codec's transport string. For `"decode"`, return the represented list of strings. The native interface exposes `Codec.encode(strs)` and `Codec.decode(s)` directly.

### Examples

#### Example 1

- **Input:** $\text{dummy}_{input} = ["Hello","World"]$
- **Output:** `["Hello","World"]`
- **Explanation:**
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2
Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
#### Example 2

- **Input:** $\text{dummy}_{input} = [""]$
- **Output:** `[""]`
### Constraints

- $1 \le \text{strs.length} \le 200$

- $0 \le \text{strs}[i].length \le 200$

- $\text{strs}[i]$ contains any possible characters out of `256` valid ASCII characters.

**Follow up: **Could you write a generalized algorithm to work on any possible set of characters?