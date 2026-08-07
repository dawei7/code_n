## Description

Design an algorithm to encode **a list of strings** to **a string**. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

```cpp
string encode(vector<string> strs) {
{{ ... }}
  //... your code
  return strs;
}
```

So Machine 1 does:

```cpp
string encoded_string = encode(strs);
```

and Machine 2 does:

```cpp
vector<string> strs2 = decode(encoded_string);
```

`strs2` in Machine 2 should be the same as `strs` in Machine 1.

Implement the `encode` and `decode` methods.

You are not allowed to solve the problem using any serialize methods (such as `eval`).
