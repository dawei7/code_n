## Examples

**Example 1**

- **Input:** `object = {"y": 1, "x": 2}`
- **Output:** `{"y":1,"x":2}`
- **Explanation:** The output keeps the key order returned by `Object.keys(object)`.

**Example 2**

- **Input:** `object = {"a": "str", "b": -12, "c": true, "d": null}`
- **Output:** `{"a":"str","b":-12,"c":true,"d":null}`
- **Explanation:** Strings, numbers, booleans, and `null` use their JSON primitive forms.

**Example 3**

- **Input:** `object = {"key": {"a": 1, "b": [{}, null, "Hello"]}}`
- **Output:** `{"key":{"a":1,"b":[{},null,"Hello"]}}`
- **Explanation:** Recursive serialization handles objects and arrays nested inside one another.

**Example 4**

- **Input:** `object = true`
- **Output:** `true`
- **Explanation:** A primitive value is itself a complete valid JSON value.
