# Optimal Binary Search Tree

| | |
|---|---|
| **ID** | `dp_26` |
| **Kategorie** | dynamic_programming |
| **Komplexität (erforderlich)** | $O(n^3)$ |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **Wikipedia** | [Optimal binary search tree](https://en.wikipedia.org/wiki/Optimal_binary_search_tree) |

## Problemstellung

Gegeben ist ein sortiertes Array von `n` Schlüsseln sowie ein Array `freq`, wobei `freq[i]` die Häufigkeit angibt, mit der der Schlüssel `i` gesucht wird.
Konstruiere einen Binary Search Tree (BST), der die **Gesamtsuchkosten** minimiert.
Die Suchkosten eines Schlüssels entsprechen exakt seiner Tiefe im Baum multipliziert mit seiner Häufigkeit.

**Eingabe:** Zwei Arrays der Größe `n`: sortierte `keys` und deren `freq`.
**Ausgabe:** Eine Ganzzahl, die die minimalen Gesamtsuchkosten repräsentiert.

**Beispiel:**
`keys = [10, 12, 20]`. `freq = [34, 8, 50]`.
Wenn wir 10 zur Wurzel machen: Kosten = `34*1 + 8*2 + 50*3 = 200`.
Wenn wir 20 zur Wurzel machen: Kosten = `50*1 + 12*2 + 34*3 = 176`.
Wenn wir 12 zur Wurzel machen: Kosten = `8*1 + 34*2 + 50*2 = 176`.
*(Tatsächlich ergibt die Wahl von 20 als Wurzel, 10 als linkes Kind und 12 als rechtes Kind von 10: `50*1 + 34*2 + 8*3 = 142`)*.

## Anwendung

- Zum Aufbau statischer Wörterbücher oder Suchindizes, bei denen die Abfrageverteilung stark verzerrt und im Voraus bekannt ist.

## Ansatz

Dies ist ein weiteres klassisches **Interval DP**-Problem, das in seiner Struktur identisch mit der Matrix Chain Multiplication ist.

Jeder Schlüssel `k` (zwischen `i` und `j`) kann die Wurzel des optimalen BST für das Teil-Array `keys[i...j]` sein.
Wenn wir `k` zur Wurzel machen:
1. Bilden die Schlüssel von `i` bis `k-1` den linken Teilbaum.
2. Bilden die Schlüssel von `k+1` bis `j` den rechten Teilbaum.

Die Kosten dieses Teilbaums sind die optimalen Kosten des linken Teilbaums + die optimalen Kosten des rechten Teilbaums.
**Moment!** Da wir beide Teilbäume um eine Ebene nach unten verschoben haben (indem wir sie unter die neue Wurzel `k` platziert haben), hat sich die Tiefe jedes einzelnen Knotens in beiden Teilbäumen um 1 erhöht!
Daher müssen die Suchkosten *jedes einzelnen Knotens* im Teil-Array `i...j` um `1 * freq[node]` erhöht werden.
Wir müssen also die **Summe aller Häufigkeiten** von `i` bis `j` addieren, um diese Verschiebung der Tiefe zu berücksichtigen.

**DP-Zustand:**
`dp[i][j]` = minimale Kosten eines optimalen BST unter Verwendung der Schlüssel von `i` bis `j`.
`dp[i][j] = min( dp[i][k-1] + dp[k+1][j] ) + sum(freq[i...j])` für alle i \le k \le j.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_26: Optimal Binary Search Tree.

opt[i][j] = min cost over BSTs containing keys[i..j].
Recurrence: try k in [i, j] as the root. Cost of putting
a subtree at depth+1 adds the total probability.
"""


def solve(keys, probs, n):
    if n == 0:
        return 0
    INF = float("inf")
    prefix = [0.0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + probs[i]
    opt = [[0.0] * n for _ in range(n)]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            best = INF
            for k in range(i, j + 1):
                left = opt[i][k - 1] if k > i else 0
                right = opt[k + 1][j] if k < j else 0
                c = left + right + prefix[j + 1] - prefix[i]
                if c < best:
                    best = c
            opt[i][j] = best
    return opt[0][n - 1]
```

</details>

## Durchlauf

`freq = [34, 8, 50]`. (Die Schlüssel spielen keine Rolle, nur die Häufigkeiten). `n=3`.

**L=1:**
`dp[0][0] = 34`
`dp[1][1] = 8`
`dp[2][2] = 50`

**L=2:**
- `i=0, j=1`. `sum = 34+8 = 42`.
  - Wurzel `k=0`: links=0, rechts=`dp[1][1]=8`. Gesamt = `0 + 8 + 42 = 50`.
  - Wurzel `k=1`: links=`dp[0][0]=34`, rechts=0. Gesamt = `34 + 0 + 42 = 76`.
  - `dp[0][1] = 50`.
- `i=1, j=2`. `sum = 8+50 = 58`.
  - Wurzel `k=1`: links=0, rechts=`50`. Gesamt = `50 + 58 = 108`.
  - Wurzel `k=2`: links=`8`, rechts=0. Gesamt = `8 + 58 = 66`.
  - `dp[1][2] = 66`.

**L=3 (Abschluss):**
- `i=0, j=2`. `sum = 34+8+50 = 92`.
  - Wurzel `k=0`: links=0, rechts=`dp[1][2]=66`. Gesamt = `66 + 92 = 158`.
  - Wurzel `k=1`: links=`dp[0][0]=34`, rechts=`dp[2][2]=50`. Gesamt = `34 + 50 + 92 = 176`.
  - Wurzel `k=2`: links=`dp[0][1]=50`, rechts=0. Gesamt = `50 + 92 = 142`.
  - Das Minimum ist `142`.

Ausgabe: `142`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n^3)$ | $O(n^2)$ |
| **Durchschnittlicher Fall** | $O(n^3)$ | $O(n^2)$ |
| **Schlechtester Fall** | $O(n^3)$ | $O(n^2)$ |

Genau wie bei der Matrix Chain Multiplication erzwingen die 3 verschachtelten Schleifen (L, i, k) eine strikte $O(n^3)$ Zeitkomplexität.
Der Platzbedarf beträgt $O(n^2)$ für die DP-Tabelle.

## Varianten & Optimierungen

- **Knuth-Optimierung $O(n^2)$:** Donald Knuth bewies, dass die optimale Wurzel K(i, j) für den Bereich `i...j` immer zwischen den optimalen Wurzeln der Teilbereiche liegt: K(i, j-1) \le K(i, j) \le K(i+1, j). Durch die Einschränkung der inneren `k`-Schleife auf dieses enge mathematische Fenster reduziert sich die Zeitkomplexität mathematisch von $O(n^3)$ auf $O(n^2)$!

## Praxisanwendungen

- **Statische Parser:** Hardcodierte Wörterbücher für Rechtschreibprüfungen oder Tokenizer für Programmiersprachen-Schlüsselwörter, bei denen die Häufigkeit von Wörtern (z. B. "if", "while") im Quellcode statistisch bekannt ist.

## Verwandte Algorithmen in cOde(n)

- **[dp_13 - Matrix Chain Multiplication](dp_13_matrix-chain-multiplication.md)** — Die Engine hinter dieser Interval DP.
- **[greedy_01 - Huffman Coding](../greedy/greedy_01_huffman-coding.md)** — Ein verwandtes Problem für optimale Bäume, jedoch sind Huffman-Bäume KEINE Binary Search Trees (Schlüssel sind nicht von links nach rechts sortiert), was eine gierige $O(n log n)$ Lösung ermöglicht!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den enzyklopädischen Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*