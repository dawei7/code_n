from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        recipients = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+", 1)[0].replace(".", "")
            recipients.add(local + "@" + domain)
        return len(recipients)
