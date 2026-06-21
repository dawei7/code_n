# Count Distinct Substrings

| | |
|---|---|
| **ID** | `suffix_04` |
| **Kategorie** | suffix_array |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **GeeksForGeeks Äquivalent** | [Count of distinct substrings of a string using Suffix Array](https://www.geeksforgeeks.org/count-distinct-substrings-string-using-suffix-array/) |

## Problemstellung

Gegeben ist ein String `s` der Länge N. Berechnen Sie die Gesamtzahl der mathematisch verschiedenen (eindeutigen) Teilstrings innerhalb des Strings.
Zum Beispiel erscheint bei `s = "ababa"` der Teilstring `"aba"` zweimal, sollte aber nur einmal gezählt werden.

**Eingabe:** Ein String `s`.
**Ausgabe:** Eine Ganzzahl, die die Anzahl der verschiedenen Teilstrings repräsentiert.

## Wann man es verwendet

- Zur Messung der exakten Entropie oder Komplexität eines Strings.
- Dies ist das kanonische Lehrbuchbeispiel dafür, warum das LCP Array erfunden wurde.

## Ansatz

**1. Das mathematische Maximum:**
Wie viele Teilstrings existieren insgesamt in einem String der Länge N?
Ein String der Länge 5 hat:
- 5 Teilstrings der Länge 1
- 4 Teilstrings der Länge 2
- 3 Teilstrings der Länge 3
- 2 Teilstrings der Länge 4
- 1 Teilstring der Länge 5
Die Gesamtzahl der Teilstrings ist die Summe der ersten N Ganzzahlen: N(N+1)/2.
Für N = 5 ist die maximal mögliche Anzahl an Teilstrings 5 x 6 / 2 = 15.

**2. Subtraktion der Duplikate:**
Wenn alle Zeichen im String eindeutig sind (z. B. `"abcde"`), ist die Antwort exakt N(N+1)/2.
Wenn es jedoch wiederholte Zeichen gibt, werden einige Teilstrings mehrfach generiert.
Wir müssen die exakte Anzahl der Duplikate von unserem Maximum abziehen.
Wie finden wir mathematisch jeden einzelnen duplizierten Teilstring, ohne sie alle zu hashen?

**3. Die Erkenntnis durch das LCP Array:**
Das Suffix Array sortiert alle Suffixe perfekt alphabetisch. Dies erzwingt, dass alle identischen Präfixe sequenziell gruppiert werden!
Das LCP (Longest Common Prefix) Array sagt uns exakt, wie viele Zeichen ein Suffix mit dem Suffix teilt, das ihm im sortierten Array unmittelbar vorausgeht.
Wenn `lcp[i] = 3` ist (z. B. teilen sich `"anana"` und `"ana"` den Präfix `"ana"`), bedeutet dies mathematisch, dass die 3 Teilstrings `"a"`, `"an"` und `"ana"` BEREITS durch das vorherige Suffix generiert wurden! Sie sind Duplikate!
Daher ist die Gesamtzahl der duplizierten Teilstrings, die über den gesamten String hinweg generiert werden, EXAKT die Summe aller Elemente im LCP Array!

**4. Die finale Formel:**
`Distinct Substrings = Total Substrings - Sum(LCP Array)`
\text{Distinct} = \frac{N(N+1)}{2} - \sum_{i=0}^{N-1} \text{LCP}[i]

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for suffix_04: Count Distinct Substrings.

Count the number of distinct non-empty substrings
"""


def solve(s, n):
    """Count distinct non-empty substrings via suffix array."""
    if n == 0:
        return 0
    # Build the suffix array naively.
    sa = sorted(range(n), key=lambda i: s[i:])
    # Build the LCP array (Kasai-style, but the naive
    # version suffices for small n).
    rank = [0] * n
    for i, idx in enumerate(sa):
        rank[idx] = i
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    # Sum of (n - sa[i] - lcp[i]) for i in 0..n-1.
    total = 0
    for i in range(n):
        total += n - sa[i] - lcp[i]
    return total
```

</details>

## Durchlauf

`s = "banana"`, N = 6.
Theoretisches Maximum an Teilstrings: 6 x 7 / 2 = 21.

1. Suffix Array erstellen: `[5, 3, 1, 0, 4, 2]`
   - `0: "a"`
   - `1: "ana"`
   - `2: "anana"`
   - `3: "banana"`
   - `4: "na"`
   - `5: "nana"`
2. LCP Array erstellen durch Vergleich jedes Suffixes mit dem darüber liegenden:
   - `LCP[0] = 0` (Kein Nachbar über `"a"`)
   - `LCP[1] = 1` (`"ana"` teilt `"a"` mit `"a"`)
   - `LCP[2] = 3` (`"anana"` teilt `"ana"` mit `"ana"`)
   - `LCP[3] = 0` (`"banana"` teilt nichts mit `"anana"`)
   - `LCP[4] = 0` (`"na"` teilt nichts mit `"banana"`)
   - `LCP[5] = 2` (`"nana"` teilt `"na"` mit `"na"`)
   LCP Array: `[0, 1, 3, 0, 0, 2]`.
3. Summe des LCP Arrays: 0 + 1 + 3 + 0 + 0 + 2 = 6.
4. Gesamtzahl der verschiedenen Teilstrings: 21 - 6 = 15.

Rückgabe `15`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(N)$ |

Das Erstellen des Suffix Arrays benötigt $O(N log^2 N)$ oder $O(N \log N)$, abhängig von der gewählten Sortierimplementierung.
Das Erstellen des LCP Arrays mittels Kasai-Algorithmus benötigt $O(N)$.
Das Summieren des Arrays benötigt $O(N)$.
Die Zeitkomplexität wird vollständig durch die Generierung des Suffix Arrays begrenzt: $O(N \log N)$.
Die Platzkomplexität beträgt $O(N)$ für das Suffix- und LCP Array.

## Varianten & Optimierungen

- **Suffix Tree ($O(N)$):** Ein Suffix Tree fasst duplizierte Präfixe auf natürliche Weise in gemeinsamen Kanten zusammen. Um verschiedene Teilstrings mit einem Suffix Tree zu zählen, summiert man buchstäblich die Längen aller Kanten im Baum! Dies benötigt $O(N)$ Zeit, wenn es mit dem Ukkonen-Algorithmus erstellt wird, aber der Code ist unendlich viel schwieriger zu schreiben als diese Formel.
- **Trie ($O(N^2)$):** Wenn der String kurz ist (< 1000 Zeichen), kann man einfach alle $O(N^2)$ Teilstrings in einen Standard-Trie einfügen. Ein Trie kollabiert identische Präfixe nativ in dieselben Knoten! Die Anzahl der verschiedenen Teilstrings entspricht exakt der Gesamtzahl der Knoten im Trie (abzüglich der Wurzel).

## Anwendungen in der Praxis

- **Informationstheorie:** Bei Grenzwerten der Datenkompression beweist die mathematische Analyse des exakten Verhältnisses von verschiedenen Teilstrings zu Gesamtzahl der Teilstrings das theoretisch maximal erreichbare Kompressionsverhältnis für eine spezifische Datei (z. B. um zu bestimmen, ob eine Datei hochgradig komprimierbar oder im Wesentlichen zufälliges Rauschen ist).

## Verwandte Algorithmen in cOde(n)

- **[suffix_03 - LCP Array](suffix_03_lcp-array-kasai-s-algorithm.md)** — Die Engine, die diesen $O(1)$ mathematischen Trick ermöglicht.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*