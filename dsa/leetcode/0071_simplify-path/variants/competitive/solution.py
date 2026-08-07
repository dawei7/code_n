class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = []
        for component in path.split("/"):
            if component == "" or component == ".":
                continue
            if component == "..":
                if directories:
                    directories.pop()
            else:
                directories.append(component)
        return "/" + "/".join(directories)
