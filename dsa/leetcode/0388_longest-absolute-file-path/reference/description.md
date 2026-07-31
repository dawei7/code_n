## Description

Consider an abstract file system containing directories and files. One representative hierarchy has root directory `dir`; it contains `subdir1` and `subdir2`. The first contains `file1.ext` and `subsubdir1`, while the second contains `subsubdir2`, which in turn contains `file2.ext`.

The source hierarchy and its indentation encoding can be represented together as follows. Each `\t` indicates one leading tab and each `\n` separates entries.

```text
dir
├─ \t subdir1
│  ├─ \t\t file1.ext
│  └─ \t\t subsubdir1
└─ \t subdir2
   └─ \t\t subsubdir2
      └─ \t\t\t file2.ext
```

Thus the serialized form is `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"`.

An absolute path lists the directories traversed to reach an entry and joins their names with `/`. For example, the path to `file2.ext` above is `"dir/subdir2/subsubdir2/file2.ext"`. Directory names contain letters, digits, or spaces. File names have the form `name.extension`, with letters, digits, or spaces in both parts.

Given a valid serialized file system string `input`, return the length of its longest absolute path ending at a file. Return `0` when the system contains no file. Every file and directory name is nonempty.
