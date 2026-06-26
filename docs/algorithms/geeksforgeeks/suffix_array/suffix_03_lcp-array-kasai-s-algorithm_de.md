# LCP Array (Kasai-Algorithmus)

| | |
|---|---|
| **ID** | `suffix_03` |
| **Kategorie** | suffix_array |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **GeeksForGeeks Äquivalent** | [Kasai’s Algorithm for Construction of LCP array from Suffix Array](https://www.geeksforgeeks.org/%C2%AD%C2%ADkasais-algorithm-for-construction-of-lcp-array-from-suffix-array/) |

## Problemstellung

Gegeben sei ein String `s` der Länge N und dessen vorab berechnetes Suffix Array `suffix_arr`. Konstruieren Sie das **Longest Common Prefix (LCP) Array**.
Das LCP Array ist ein Array der Größe N, wobei `lcp[i]` die Länge des längsten gemeinsamen Präfixes zwischen dem i-ten Suffix und dem (i-1)-ten Suffix im sortierten Suffix Array speichert.
Sie müssen dieses Array in mathematisch garantierter $O(N)$ linearer Zeit generieren.

**Eingabe:** Ein String `s` und ein Integer-Array `suffix_arr`.
**Ausgabe:** Ein Integer-Array `lcp`.

## Wann man es verwendet

- Ein Suffix Array allein ist lediglich eine sortierte Liste. Erst die Kombination aus Suffix Array **UND** LCP Array ermöglicht es, einige der schwierigsten String-Probleme der Informatik (längster wiederholter Teilstring, Anzahl distinkter Teilstrings) in $O(N)$ Zeit zu lösen!

## Ansatz

**1. Der naive $O(N^2)$ Vergleich:**
Wenn wir über das Suffix Array iterieren und `suffix_arr[i]` mit `suffix_arr[i-1]` Zeichen für Zeichen vergleichen, benötigt dies $O(N)$ Zeit pro Vergleich. Über N Elemente hinweg ergibt das $O(N^2)$. Das ist zu langsam.

**2. Kasais magische Erkenntnis:**
Anstatt das LCP Array in der sortierten Reihenfolge des Suffix Arrays zu berechnen, was wäre, wenn wir es in der **ursprünglichen Reihenfolge** des Strings berechnen würden?
Finden wir zuerst das LCP des längsten Suffixes (`s[0...]`), dann das des zweitlängsten (`s[1...]`), dann `s[2...]`.

Angenommen, das Suffix `s[i...]` befindet sich an der Position `rank` im Suffix Array. Sein Nachbar darüber ist `rank - 1`. Nehmen wir an, ihr LCP ist K.
Beispiel: Der Nachbar ist `"banana"` und unser Suffix ist `"banjo"`. K = 3 (`"ban"`).
Gehen wir nun zum nächsten Suffix im ursprünglichen String: `s[i+1...]`. Dies schneidet physisch das erste Zeichen ab!
Unser neues Suffix ist `"anjo"`. Der Nachbar schrumpft mathematisch zu `"anana"`.
Da das erste Zeichen bei BEIDEN Strings abgeschnitten wurde, MUSS das verbleibende übereinstimmende Präfix exakt K - 1 sein! (z. B. `"an"`).
Daher WISSEN wir bereits, dass das LCP unseres neuen Suffixes mit seinem Nachbarn **mindestens** K - 1 ist!
Wir müssen die ersten K - 1 Zeichen nicht vergleichen! Wir setzen unseren Zeichenvergleich einfach ab Index K - 1 fort!

**3. Das Rank Array:**
Um Suffixe in ihrer ursprünglichen String-Reihenfolge zu verarbeiten, aber ihre "Nachbarn" im sortierten Suffix Array leicht zu finden, benötigen wir eine Rückwärtssuche. Wir erstellen ein $O(N)$ `rank` Array, wobei `rank[i]` uns die sortierte Position des Suffixes angibt, das am String-Index `i` beginnt.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for suffix_03: LCP Array (Kasai's Algorithm).

Given a string s, return its suffix array sa and
"""


def solve(s, n):
    """Return (suffix_array, lcp_array) of s.

    Build the suffix array naively (sort suffixes), then run
    Kasai's algorithm to build the LCP array in O(n).
    """
    if n == 0:
        return [], []
    # Build the suffix array naively.
    sa = sorted(range(n), key=lambda i: s[i:])
    # Inverse SA: rank[i] = position of suffix i in sa.
    rank = [0] * n
    for i, idx in enumerate(sa):
        rank[idx] = i
    # Kasai's algorithm.
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            # j is the previous suffix in the suffix array.
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
        # If rank[i] == 0 (it's the smallest suffix), lcp[0] = 0
        # (already initialized).
    return sa, lcp
```

</details>

## Durchlauf

`s = "banana"`, `suffix_arr = [5, 3, 1, 0, 4, 2]`.
*Sortierte Suffixe:*
`0: "a" (idx 5)`
`1: "ana" (idx 3)`
`2: "anana" (idx 1)`
`3: "banana" (idx 0)`
`4: "na" (idx 4)`
`5: "nana" (idx 2)`

1. **`rank` Array erstellen:**
   `rank[5]=0, rank[3]=1, rank[1]=2, rank[0]=3, rank[4]=4, rank[2]=5`.
2. **`i = 0` (Suffix `"banana"`):**
   - `rank[0] = 3`. Nachbar ist `rank 2` (Suffix `"anana"` bei `idx 1`).
   - Vergleiche `"banana"` mit `"anana"`. `b != a`. `k = 0`.
   - `lcp[3] = 0`.
3. **`i = 1` (Suffix `"anana"`):**
   - `rank[1] = 2`. Nachbar ist `rank 1` (Suffix `"ana"` bei `idx 3`).
   - Vergleiche `"anana"` mit `"ana"`. 3 Zeichen stimmen überein! `k = 3`.
   - `lcp[2] = 3`.
   - **Kasai-Schrumpfung:** Im nächsten Schritt wird `k` zu 3 - 1 = 2. Wir überspringen garantiert 2 Vergleiche!
4. **`i = 2` (Suffix `"nana"`):**
   - `rank[2] = 5`. Nachbar ist `rank 4` (Suffix `"na"` bei `idx 4`).
   - Wir überspringen sofort die ersten `k=2` Zeichen!
   - Wir prüfen nur `s[2 + 2]` mit `s[4 + 2]`. `s[4]` ist `'n'`, `s[6]` ist außerhalb der Grenzen. Mismatch!
   - `k = 2`. `lcp[5] = 2`.
   - **Kasai-Schrumpfung:** Im nächsten Schritt wird `k` zu 2 - 1 = 1.

Das LCP Array ist vollständig in linearer Zeit erstellt: `[0, 1, 3, 0, 0, 2]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Das Erstellen des Rank Arrays benötigt $O(N)$ Zeit.
In der Hauptschleife führen wir eine `while`-Schleife aus, die `k` inkrementiert.
Obwohl `k` theoretisch bis zu N-mal inkrementiert werden kann, beachten Sie, dass `k` am Ende jeder Iteration um exakt 1 dekrementiert wird.
Da `k` niemals N überschreiten kann und es höchstens N-mal dekrementiert wird, ist die Gesamtzahl der Inkrementierungen von `k` über den GESAMTEN Algorithmus mathematisch auf 2N begrenzt.
Daher führt die innere `while`-Schleife global höchstens 2N Operationen aus. Die gesamte Zeitkomplexität ist strikt $O(N)$.
Die Platzkomplexität beträgt $O(N)$, um das `rank` Array und das `lcp` Array zu speichern.

## Varianten & Optimierungen

- **Direkte Berechnung bei der Suffix Array Generierung:** Hochmoderne Suffix Array Generierungsalgorithmen (wie DC3) können das LCP Array tatsächlich direkt während des Sortiervorgangs berechnen, wodurch ein separater Kasai-Durchlauf entfällt.

## Anwendungen in der Praxis

- **Bioinformatik / Kürzester eindeutiger Teilstring:** Finden der kürzesten DNA-Sequenz, die einen spezifischen Virusstamm eindeutig identifiziert, indem der Teilstring mit der minimalen Länge gesucht wird, der ein LCP von 0 mit seinen sortierten Nachbarn hat.

## Verwandte Algorithmen in cOde(n)

- **[suffix_05 - Longest Repeated Substring](suffix_05_longest-repeated-substring.md)** — Ein komplexes Problem, das durch das LCP Array trivialisiert wird (es ist einfach der Maximalwert im LCP Array!).
- **[suffix_04 - Count Distinct Substrings](suffix_04_count-distinct-substrings.md)** — Ein weiteres Problem, das durch das LCP Array trivialisiert wird (N(N+1)/2 - \sum LCP[i]).

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*