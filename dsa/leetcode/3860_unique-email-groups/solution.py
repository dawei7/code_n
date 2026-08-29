class Solution:
    def uniqueEmailGroups(self, emails: list[str]) -> int:
        st = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "").lower()
            domain = domain.lower()
            st.add((local, domain))
        return len(st)
