## Examples

**Example 1**

- Input: `["FileSystem","createPath","get"], [[],["/a",1],["/a"]]`
- Output: `[null,true,1]`
- Explanation: Construct an empty system, create `"/a"` with value `1`, and then retrieve that value.

**Example 2**

- Input: `["FileSystem","createPath","createPath","get","createPath","get"], [[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]`
- Output: `[null,true,true,2,false,-1]`
- Explanation: `"/leet/code"` can be created after `"/leet"` exists. Creating `"/c/d"` fails because its parent `"/c"` is absent, and looking up that missing parent returns `-1`.
