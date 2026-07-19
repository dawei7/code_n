def solve(accounts: list[list[str]]) -> list[list[str]]:
    parent = {}
    size = {}
    email_to_name = {}

    def add(email: str) -> None:
        if email not in parent:
            parent[email] = email
            size[email] = 1

    def find(email: str) -> str:
        while parent[email] != email:
            parent[email] = parent[parent[email]]
            email = parent[email]
        return email

    def union(left: str, right: str) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root == right_root:
            return
        if size[left_root] < size[right_root]:
            left_root, right_root = right_root, left_root
        parent[right_root] = left_root
        size[left_root] += size[right_root]

    for account in accounts:
        name = account[0]
        first_email = account[1]
        add(first_email)
        email_to_name[first_email] = name
        for email in account[2:]:
            add(email)
            email_to_name[email] = name
            union(first_email, email)

    groups = {}
    for email in parent:
        groups.setdefault(find(email), []).append(email)

    merged = []
    for emails in groups.values():
        emails.sort()
        merged.append([email_to_name[emails[0]], *emails])

    merged.sort()
    return merged
