def solve(favorite_companies):
    sets = []
    for companies in favorite_companies:
        if isinstance(companies, list):
            sets.append(set(companies))
        else:
            sets.append({companies})
    result = []
    for index, companies in enumerate(sets):
        if not any(index != other and companies <= other_companies for other, other_companies in enumerate(sets)):
            result.append(index)
    return result
