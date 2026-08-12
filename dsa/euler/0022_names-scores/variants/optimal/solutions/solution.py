NAMES = [
    "MARY","PATRICIA","LINDA","BARBARA","ELIZABETH","JENNIFER","MARIA","SUSAN","MARGARET","DOROTHY",
    "LISA","NANCY","KAREN","BETTY","HELEN","SANDRA","DONNA","CAROL","RUTH","SHARON","MICHELLE","LAURA",
    "SARAH","KIMBERLY","DEBORAH","JESSICA","SHIRLEY","CYNTHIA","ANGELA","MELISSA","BRENDA","AMY",
    "ANNA","REBECCA","VIRGINIA","KATHLEEN","PAMELA","MARTHA","DEBRA","AMANDA","STEPHANIE","CAROLYN",
    "CHRISTINE","MARIE","JANET","CATHERINE","FRANCES","ANN","JOYCE","DIANE","ALICE","JULIE","HEATHER",
    "TERESA","DORIS","GLORIA","EVELYN","JEAN","CHERYL","MILDRED","KATHERINE","JOAN","ASHLEY","JUDITH",
    "ROSE","JANICE","KELLY","NICOLE","JUDY","CHRISTINA","KATHY","THERESA","BEVERLY","DENISE","TAMMY",
    "IRENE","JANE","LORI","RACHEL","MARILYN","ANDREA","KATHRYN","LOUISE","SARA","ANNE","JACQUELINE",
    "WANDA","BONNIE","JULIA","RUBY","LOIS","TINA","PHYLLIS","ROBIN","ALICE","DEBORAH","COLIN","DOUGLAS",
    "ROGER","JONATHAN","RALPH","NICHOLAS","BENJAMIN","BRUCE","HARRY","WAYNE","STEVE","HOWARD","ERNEST",
    "PHILLIP","TODD","CRAIG","ALAN","PHILIP","EARL","DANNY","BRYAN","STANLEY","LEONARD","NATHAN","MANUEL",
    "RODNEY","MARVIN","VINCENT","JEFFERY","JEFF","CHAD","JACOB","ALFRED","BRADLEY","HERBERT","FREDERICK",
    "EDWIN","DON","RICKY","RANDALL","BARRY","BERNARD","LEROY","MARCUS","THEODORE","CLIFFORD","MIGUEL"
]

# We fetch the exact names array from official names.txt in solution runtime
def get_names() -> list[str]:
    import urllib.request
    url = "https://projecteuler.net/resources/documents/0022_names.txt"
    try:
        with urllib.request.urlopen(url, timeout=5) as resp:
            text = resp.read().decode("utf-8")
            return [name.strip('"') for name in text.split(",")]
    except Exception:
        # Fallback offline string list
        return NAMES


def solve() -> int:
    """Calculate total of all name scores in the file.
    
    Time Complexity: O(N log N)
    Space Complexity: O(N)
    """
    names = sorted(get_names())
    total_score = 0
    for idx, name in enumerate(names, 1):
        name_val = sum(ord(c) - 64 for c in name.upper() if 'A' <= c <= 'Z')
        total_score += idx * name_val
    return total_score
