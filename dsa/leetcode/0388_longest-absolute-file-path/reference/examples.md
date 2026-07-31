## Examples

**Example 1**

- Input: `input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"`
- Output: `20`
- Explanation: The only file has absolute path `"dir/subdir2/file.ext"`, whose length is `20`.

The first example's source image is represented by this tree:

```text
dir
├── subdir1
└── subdir2
    └── file.ext
```

**Example 2**

- Input: `input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"`
- Output: `32`
- Explanation: The two file paths are `"dir/subdir1/file1.ext"` of length `21` and `"dir/subdir2/subsubdir2/file2.ext"` of length `32`, so the longer length is returned.

The second example's source image expands both branches:

```text
dir
├── subdir1
│   ├── file1.ext
│   └── subsubdir1
└── subdir2
    └── subsubdir2
        └── file2.ext
```

**Example 3**

- Input: `input = "a"`
- Output: `0`
- Explanation: The representation contains one directory named `"a"` and no file.
