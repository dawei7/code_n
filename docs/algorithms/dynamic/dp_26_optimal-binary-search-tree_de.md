# Optimaler Binary Search Tree

| | |
|---|---|
| **ID** | `dp_26` |
| **Kategorie** | dynamische_Programmierung |
| **Komplexität (erforderlich)** | $O(n^3)$ |
| **Schwierigkeitsgrad** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **Wikipedia** | [Optimaler Binary Search Tree](https://en.wikipedia.org/wiki/Optimal_binary_search_tree) |

## Aufgabenstellung

Gegeben sei ein sortiertes Array mit `n` Schlüsseln und ein Array `freq`, wobei `freq[i]` die Anzahl der Suchvorgänge für den Schlüssel `i` angibt.
Konstruiere einen Binary Search Tree (BST), der die **Gesamtsuchkosten** minimiert.
Die Suchkosten eines Schlüssels entsprechen genau seiner Tiefe im Baum multipliziert mit seiner Häufigkeit.

**Eingabe:** Zwei Arrays der Größe `n`: sortiert `keys` und deren `freq`.
**Ausgabe:** Eine ganze Zahl, die die minimalen Gesamtsuchkosten angibt.

**Beispiel:**
`keys = [10, 12, 20]`. `freq = [34, 8, 50]`.
Wenn wir 10 zur Wurzel machen: Kosten = `34*1 + 8*2 + 50*3 = 200`.
Wenn wir 20 zur Wurzel machen: Kosten = `50*1 + 12*2 + 34*3 = 176`.
Wenn wir 12 als Wurzel wählen: Kosten = `8*1 + 34*2 + 50*2 = 176`.
*(Tatsächlich ergibt sich, wenn man 20 als Wurzel und 10 als linkes Kind sowie 12 als rechtes Kind von 10 wählt: `50*1 + 34*2 + 8*3 = 142`)*.

## Wann man es verwendet

- Zum Erstellen statischer Wörterbücher oder Suchindizes, bei denen die Verteilung der Abfragen stark schief ist und im Voraus bekannt ist.

## Vorgehensweise

Dies ist ein weiteres klassisches **Intervall-DP**-Problem, dessen Struktur mit der Matrixkettenmultiplikation identisch ist.

Jeder Schlüssel `k` (zwischen `i` und `j`) kann die Wurzel des optimalen BST für das Teilarray `keys[i...j]` sein.
Wenn wir `k` zur Wurzel machen:
1. Bilden die Schlüssel von `i` bis `k-1` den linken Teilbaum.
2. Die Schlüssel von `k+1` bis `j` bilden den rechten Teilbaum.

Die Kosten dieses Teilbaums entsprechen den optimalen Kosten des linken Teilbaums plus den optimalen Kosten des rechten Teilbaums.
**Moment!** Da wir gerade beide Teilbäume um eine Ebene nach unten verschoben haben (indem wir sie unter die neue Wurzel `k` gesetzt haben), hat sich die Tiefe jedes einzelnen Knotens in beiden Teilbäumen um 1 erhöht!
Daher haben sich die Suchkosten für *jeden einzelnen Knoten* im Teilarray `i...j` gerade um `1 * freq[node]` erhöht.
Daher müssen wir die **Summe aller Häufigkeiten** von `i` bis `j` addieren, um diese Tiefenverschiebung zu berücksichtigen.

**DP-Zustand:**
`dp[i][j]` = minimale Suchkosten eines optimalen BST unter Verwendung der Schlüssel von `i` bis `j`.
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

## Schritt-für-Schritt-Anleitung

`freq = [34, 8, 50]`. (Schlüssel spielen keine Rolle, nur Häufigkeiten). `n=3`.

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

**L=3 (Endgültig):**
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

Genau wie bei der Matrixkettenmultiplikation bedingen die drei verschachtelten Schleifen (L, i, k) eine strenge $O(n^3)$ Zeitkomplexität.
Der Speicherbedarf für die DP-Tabelle beträgt $O(n^2)$.

## Varianten & Optimierungen

- **Knuths Optimierung $O(n^2)$:** Donald Knuth hat bewiesen, dass die optimale Wurzel K(i, j) für den Bereich `i...j` immer zwischen den optimalen Wurzeln der Teilbereiche liegt: K(i, j-1) \le K(i, j) \le K(i+1, j). Durch die Beschränkung der inneren `k`-Schleife auf dieses enge mathematische Fenster reduziert sich die Zeitkomplexität mathematisch von $O(n^3)$ auf $O(n^2)$!

## Praktische Anwendungen

- **Statische Parser:** Fest codierte Wörterbücher für Rechtschreibprüfungen oder Tokenizer für Schlüsselwörter in Programmiersprachen, bei denen die Häufigkeit von Wörtern (z. B. „if“, „while“) im Quellcode statistisch bekannt ist.

## Verwandte Algorithmen in cOde(n)

- **[dp_13 – Matrixkettenmultiplikation](dp_13_matrix-chain-multiplication.md)** — Die Engine hinter dieser Intervall-DP.
- **[greedy_01 – Huffman-Kodierung](../greedy/greedy_01_huffman-coding.md)** — Ein verwandtes optimales Baumproblem, aber Huffman-Bäume sind KEINE binären Suchbäume (die Schlüssel sind nicht von links nach rechts sortiert), was eine greedy $O(n log n)$-Lösung ermöglicht!

---

*Diese Dokumentation ist ein für cOde(n) verfasster Originalinhalt,
der sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
