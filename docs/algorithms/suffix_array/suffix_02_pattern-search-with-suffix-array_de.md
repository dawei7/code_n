# Mustersuche mit Suffix Array

| | |
|---|---|
| **ID** | `suffix_02` |
| **Kategorie** | suffix_array |
| **Komplexität (erforderlich)** | $O(M \log N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **GeeksForGeeks Äquivalent** | [Pattern Searching using Suffix Array](https://www.geeksforgeeks.org/pattern-searching-using-suffix-array/) |

## Problemstellung

Gegeben ist ein langer `text`-String der Länge N, sein vorab berechnetes Suffix Array `suffix_arr` sowie ein `pattern`-String der Länge M.
Ermitteln Sie, ob das `pattern` als zusammenhängender Teilstring innerhalb des `text` existiert.
Sie müssen das Suffix Array nutzen, um eine Suchzeit von $O(M \log N)$ zu erreichen und den $O(N)$-Scan von Algorithmen wie KMP oder Rabin-Karp zu vermeiden.

**Eingabe:** Ein String `text`, sein Suffix Array und ein String `pattern`.
**Ausgabe:** Ein boolescher Wert, der angibt, ob das Muster existiert.

## Anwendungsbereiche

- Wenn Sie ein massives, statisches Dokument haben (wie den gesamten Text eines Buches) und dieses tausende Male nach verschiedenen Mustern abfragen müssen. (Ein $O(N)$ KMP-Scan pro Abfrage wäre zu langsam).

## Ansatz

**1. Die alphabetische Garantie:**
Was ist ein Suffix Array? Es ist eine Liste ALLER möglichen Suffixe des Textes, perfekt in alphabetischer Reihenfolge sortiert.
Wenn das `pattern` irgendwo innerhalb des `text` existiert, MUSS es mathematisch gesehen das *Präfix* mindestens eines Suffixes sein!
Zum Beispiel: Wenn `text = "banana"` und `pattern = "nan"`. `"nan"` ist buchstäblich das Präfix des Suffixes `"nana"`.
Daher ist die Suche nach einem Muster mathematisch identisch mit der Suche nach einem String, der *mit dem Muster beginnt*, innerhalb eines perfekt alphabetisch sortierten Arrays!

**2. Standard-Binärsuche:**
Wie findet man einen String in einem sortierten Array? Man verwendet **Binärsuche (`search_02`)**!
Die Array-Größe ist N. Die Binärsuche benötigt $O(\log N)$ Schritte.
In jedem Schritt betrachten wir `suffix_arr[mid]`. Dies verweist auf ein spezifisches Suffix im Text.
Wir vergleichen unser `pattern` mit den Zeichen des Textes, beginnend an diesem Index.
Da der String-Vergleich $O(M)$ Zeit in Anspruch nimmt, beträgt die gesamte Suchzeit exakt $O(M \log N)$!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for suffix_02: Pattern Search with Suffix Array.

Build SA, then binary-search for the range of suffixes
that start with pattern.
"""


def solve(s, n, pattern, m):
    if m == 0 or n == 0:
        return []
    sa = sorted(range(n), key=lambda i: s[i:])
    out = []
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if s[sa[mid]:] < pattern:
            lo = mid + 1
        else:
            hi = mid
    lower = lo
    hi = n
    while lo < hi:
        mid = (lo + hi) // 2
        if s[sa[mid]:].startswith(pattern):
            lo = mid + 1
        elif s[sa[mid]:] < pattern:
            lo = mid + 1
        else:
            hi = mid
    upper = lo
    for i in range(lower, upper):
        out.append(sa[i])
    return sorted(out)
```

</details>

## Durchlauf

`text = "banana"`, `suffix_arr = [5, 3, 1, 0, 4, 2]`.
`pattern = "nan"`. M = 3.

*Suffixe in Array-Reihenfolge:*
0: `[5]` "a"
1: `[3]` "ana"
2: `[1]` "anana"
3: `[0]` "banana"
4: `[4]` "na"
5: `[2]` "nana"

1. `left = 0`, `right = 5`. `mid = 2`.
   - `suffix_arr[2]` ist Index `1`.
   - Das Suffix, das bei Index `1` beginnt, ist `"anana"`.
   - Extrahiere Länge 3: `"ana"`.
   - Vergleiche `"nan"` mit `"ana"`. `"nan" > "ana"` alphabetisch.
   - `left = mid + 1 = 3`.
2. `left = 3`, `right = 5`. `mid = 4`.
   - `suffix_arr[4]` ist Index `4`.
   - Das Suffix, das bei Index `4` beginnt, ist `"na"`.
   - Extrahiere Länge 3: `"na"`.
   - Vergleiche `"nan"` mit `"na"`. `"nan" > "na"` alphabetisch.
   - `left = mid + 1 = 5`.
3. `left = 5`, `right = 5`. `mid = 5`.
   - `suffix_arr[5]` ist Index `2`.
   - Das Suffix, das bei Index `2` beginnt, ist `"nana"`.
   - Extrahiere Länge 3: `"nan"`.
   - Vergleiche `"nan"` mit `"nan"`. TREFFER!

Rückgabe `True`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(M)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(M \log N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(M \log N)$ | $O(1)$ |

Die Binärsuche halbiert den Suchraum in jedem Schritt und erfordert exakt $\log_2 N$ Iterationen.
In jeder Iteration vergleichen wir zwei Strings der maximalen Länge M. Ein String-Vergleich benötigt im schlechtesten Fall $O(M)$ Zeit (wenn die Strings bis auf das letzte Zeichen nahezu identisch sind).
Die gesamte Zeitkomplexität beträgt strikt $O(M \log N)$.
Die Platzkomplexität beträgt $O(1)$ zusätzlichen Speicherplatz (abgesehen vom vorab berechneten Suffix Array selbst).

## Varianten & Optimierungen

- **LCP-beschleunigte Binärsuche ($O(M + \log N)$):** Wenn Sie zusätzlich das Longest Common Prefix (LCP) Array vorab berechnen, können Sie die Binärsuche optimieren! Wenn Sie während der Binärsuche wissen, dass Sie K Zeichen mit der linken Grenze und K Zeichen mit der rechten Grenze übereinstimmend haben, MUSS jedes Suffix dazwischen mathematisch ebenfalls mit diesen K Zeichen übereinstimmen! Sie können die ersten K Zeichen während des String-Vergleichs sicher überspringen, wodurch die Zeitkomplexität auf beeindruckende $O(M + \log N)$ sinkt!

## Anwendungen in der Praxis

- **Bioinformatik / Genom-Datenbanken:** Genome sind massive Strings (3 Milliarden Zeichen), die sich nie ändern. Sie werden über Nacht in Suffix Arrays vorverarbeitet. Wenn Wissenschaftler ein kurzes RNA-Muster abfragen, führt die Datenbank exakt diese $O(M \log N)$-Suche aus, um die Chromosomenpositionen sofort zurückzugeben.

## Verwandte Algorithmen in cOde(n)

- **[search_02 - Binary Search](../searching/search_02_binary-search.md)** — Die Engine, die diese Suche antreibt.
- **[suffix_01 - Build Suffix Array](suffix_01_build-suffix-array.md)** — Wie das Index-Array überhaupt generiert wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*