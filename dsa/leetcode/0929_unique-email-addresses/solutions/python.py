"""Optimal app-local solution for LeetCode 929."""


def solve(emails):
    recipients = set()
    for email in emails:
        local, domain = email.split("@")
        local = local.split("+", 1)[0].replace(".", "")
        recipients.add(local + "@" + domain)
    return len(recipients)
