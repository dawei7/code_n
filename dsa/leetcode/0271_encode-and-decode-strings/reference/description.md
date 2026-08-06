## Description

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

```cpp
string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
```

Machine 2 (receiver) has the function:

```cpp
vector<string> decode(string s) {
  //... your code
  return strs;
}
```

So Machine 2 should be able to decode the output of Machine 1's encode.

```cpp
string encoded_string = encode(strs);
vector<string> strs2 = decode(encoded_string);
```

`strs2` should be equal to `strs`.

Implement the `encode` and `decode` methods.

