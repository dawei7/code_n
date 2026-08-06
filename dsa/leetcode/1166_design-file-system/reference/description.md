## Description

Design a file system that can create paths and associate a different integer value with each successfully created path.

A path consists of one or more components. Every component starts with `/` and continues with one or more lowercase English letters. For example, `"/leetcode"` and `"/leetcode/problems"` are paths, whereas the empty string and `"/"` are not valid paths.

The system must reject a path that already exists or whose immediate parent has not been created. It must also support retrieving the value of an existing path and report when a requested path is absent.
