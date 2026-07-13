from bisect import bisect_left


def solve(products, search_word):
    products.sort()
    answer = []
    prefix = ""
    for ch in search_word:
        prefix += ch
        start = bisect_left(products, prefix)
        suggestions = []
        for product in products[start:start + 3]:
            if product.startswith(prefix):
                suggestions.append(product)
        answer.append(suggestions)
    return answer
