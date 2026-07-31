def solve(favoriteCompanies):
    company_sets = [set(companies) for companies in favoriteCompanies]
    result = []

    for index, current in enumerate(company_sets):
        contained = any(
            index != other_index and len(current) < len(candidate) and current.issubset(candidate)
            for other_index, candidate in enumerate(company_sets)
        )
        if not contained:
            result.append(index)

    return result
