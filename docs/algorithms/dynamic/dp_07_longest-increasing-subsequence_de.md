# Longest Increasing Subsequence (LIS)

| | |
|---|---|
| **ID** | `dp_07` |
| **Category** | dynamic |
| **Complexity (required)** | $O(n log n)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **Wikipedia** | [Longest increasing subsequence](https://en.wikipedia.org/wiki/Longest_increasing_subsequence) |

## Problem statement

Gegeben ist eine Zahlenfolge `a[0..n-1]`. Gesucht ist die Länge der längsten **streng monoton steigenden Teilfolge** (nicht notwendigerweise zusammenhängend). Eine Teilfolge ist eine Untermenge, die die ursprüngliche Reihenfolge beibehält; "steigend" bedeutet, dass jedes Element streng größer als das vorherige ist.

**Input:** ein Array vergleichbarer Elemente.
**Output:** die Länge der LIS.

**Beispiel:**

| Input | LIS | Länge |
|---|---|---:|
| `[10, 9, 2, 5, 3, 7, 101, 18]` | `[2, 3, 7, 18]` oder `[2, 3, 7, 101]` | 4 |
| `[0, 1, 0, 3, 2, 3]` | `[0, 1, 2, 3]` | 4 |
| `[7, 7, 7, 7]` | (keine streng steigende) | 1 |
| `[]` | (leer) | 0 |

## Wann man es verwendet

- Das kanonische Problem der "**$O(n²)$ DP, die durch einen Patience-Sorting-Trick zu $O(n log n)$ wird**". Die $O(n log n)$-Version wird bei jedem Top-Unternehmen abgefragt.
- Immer wenn Sie eine **reihenfolgeerhaltende Untermenge** finden müssen, die eine Monotonie-Bedingung erfüllt, ist LIS oder eine Variante anwendbar.
- Grundlage für die **Patience-Sorting-basierten Sortieralgorithmen** und die Zerlegung in die **minimale Anzahl an steigenden Teilfolgen** (Dilworths Theorem).

## Ansatz

Es gibt zwei kanonische Ansätze. Die Engine von cOde(n) prüft gegen die $O(n log n)$-Variante, daher konzentrieren wir uns darauf.

### Der $O(n log n)$ Patience-Sorting-Ansatz

Wir führen ein Array `tails[]`, wobei `tails[i]` den **kleinstmöglichen Endwert** einer beliebigen steigenden Teilfolge der Länge `i+1` darstellt, die bisher gesehen wurde. Dieses Array ist immer sortiert.

Für jedes Element `x` im Input:
- Finde die **linkeste Position** in `tails`, die `>= x` ist (mittels binärer Suche).
- Ersetze `tails[pos]` durch `x`.
- Wenn `x` größer als jedes existierende Ende ist, verlängert es die längste Teilfolge — hänge es an.

Die Länge von `tails` am Ende entspricht der LIS-Länge.

**Warum es funktioniert:** Das Array `tails` ist eine nach Länge abnehmende Zusammenfassung aller Kandidaten-Teilfolgen. Für jede Länge behalten wir nur das "kleinstmögliche Ende", da ein kleineres Ende immer mindestens so gut ist wie ein größeres (da mehr Elemente darauf folgen können).

### Der $O(n²)$ DP-Ansatz (zum Verständnis)

`dp[i]` = Länge der LIS, die bei `a[i]` endet. Rekursionsgleichung:
`dp[i] = 1 + max(dp[j])` über alle `j < i` mit `a[j] < a[i]`.
Antwort: `max(dp)`. Die oben genannte $O(n log n)$-Version ist eine strikte Verbesserung und diejenige, die man auswendig lernen sollte.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_07: Longest Increasing Subsequence.

Patience sorting with binary search — O(n log n).
"""


def solve(arr):
    import bisect
    tails = []
    for v in arr:
        i = bisect.bisect_left(tails, v)
        if i == len(tails):
            tails.append(v)
        else:
            tails[i] = v
    return len(tails)
```

</details>

## Ablauf

`a = [10, 9, 2, 5, 3, 7, 101, 18]`.

| x | lower_bound(tails, x) | tails danach |
|---:|---:|---|
| 10 | 0 | `[10]` |
| 9 | 0 | `[9]` (ersetzt 10) |
| 2 | 0 | `[2]` (ersetzt 9) |
| 5 | 1 | `[2, 5]` |
| 3 | 1 | `[2, 3]` (ersetzt 5) |
| 7 | 2 | `[2, 3, 7]` |
| 101 | 3 | `[2, 3, 7, 101]` |
| 18 | 3 | `[2, 3, 7, 18]` (ersetzt 101) |

`len(tails) = 4`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n log n)$ | $O(n)$ |
| **Durchschnittlicher Fall** | $O(n log n)$ | $O(n)$ |
| **Schlechtester Fall** | $O(n log n)$ | $O(n)$ |

Die binäre Suche ist $O(log n)$ pro Element, und wir führen sie n-mal aus. Das `tails`-Array enthält maximal n Elemente.

Für den Fall eines streng absteigenden Inputs wird bei `tails` nie ein Ende ersetzt, daher führt die binäre Suche bei jedem Schritt die volle $O(log n)$-Operation aus — insgesamt bleibt es bei $O(n log n)$.

## Varianten & Optimierungen

- **Streng steigend → nicht-fallend** — ändere `lower_bound` (erstes `>=`) zu `upper_bound` (erstes `>`). Dies behandelt gleiche Elemente korrekt.
- **Rekonstruktion der tatsächlichen Folge** — speichere ein paralleles `parent[i]`-Array (den Index `j`, der ersetzt wurde, als wir `tails[pos]` aktualisierten). Gehe dann vom letzten Element rückwärts, um die LIS in umgekehrter Reihenfolge zu rekonstruieren. $O(n)$ zusätzlicher Platz und $O(n)$ Rekonstruktionszeit.
- **Längste nicht-fallende Teilfolge von 2D-Punkten** — sortiere nach x, dann wende LIS auf y an. Wird beim "Russian Doll Envelopes"-Problem verwendet.
- **Patience Sort** — dieser Algorithmus ist exakt Patience Sorting; die Anzahl der Stapel ist die LIS-Länge, und das vollständige Patience Sort erzeugt eine stabile Sortierung in $O(n log n)$.

## Anwendungen in der Praxis

- **Diff- und Merge-Tools** — finden den längsten übereinstimmenden Block von Zeilen zwischen zwei Dateiversionen. Der Diff-Algorithmus reduziert sich auf LCS (verwandt), aber eine ähnliche DP tritt auf.
- **Molekularbiologie** — Finden konservierter Teilfolgen in DNA- / Proteinsequenzen.
- **Finanzanalyse** — Finden der längsten Serie steigender Aktienkurse, verwendet in der Trendanalyse.
- **Patience Sorting** — der obige Algorithmus IST Patience Sorting; die Stapelanzahl ist die LIS-Länge. Patience Sort ist $O(n log n)$ und stabil.

## Verwandte Algorithmen in cOde(n)

- **[dp_29 — LIS (Patience Sort)](dp_29_lis-patience-sort.md)** —
  derselbe Algorithmus, gerahmt als Sortierergebnis statt als reine DP. (d=5/10, r=9/10)
- **[dp_04 — Longest Common Subsequence](dp_04_longest-common-subsequence.md)** —
  ähnliche Struktur, aber auf zwei Folgen statt einer.
  (d=5/10, r=9/10)
- **[stack_02 — Next Greater Element](stack_02_next-greater-element.md)** —
  ein weiteres klassisches "längste-steigende-ähnliches" Problem, gelöst mit einem monotonen Stack in $O(n)$. (d=4/10, r=7/10)

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*