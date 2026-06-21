# Subarray Sum Equals K

| | |
|---|---|
| **ID** | `hash_02` |
| **Kategorie** | Hashing |
| **Komplexität (erforderlich)** | $O(n)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Hash table](https://en.wikipedia.org/wiki/Hash_table) |

## Problemstellung

Gegeben ist ein Array von Integern `nums` (welches **negative Zahlen und Nullen** enthalten kann) sowie ein Integer `k`. Zähle die Anzahl der **zusammenhängenden Subarrays**, deren Summe gleich `k` ist.

**Eingabe:** ein Array `nums`, eine Zielsumme `k`.
**Ausgabe:** die Anzahl der zusammenhängenden Subarrays mit der Summe `k`.

**Beispiel:**

| nums | k | Antwort | Subarrays |
|---|---|---:|---|
| `[1, 1, 1]` | 2 | 2 | `[1,1]@0-1`, `[1,1]@1-2` |
| `[1, 2, 3]` | 3 | 2 | `[1,2]@0-1`, `[3]@2-2` |
| `[1, -1, 1, -1, 1, -1]` | 0 | 9 | (alle Subarrays gerader Länge) |
| `[3, 4, 7, 2, -3, 1, 4, 2]` | 7 | 4 | |

## Anwendung

- Die klassische "**Präfixsumme + Hash Map**"-Technik. Wird in irgendeiner Form bei fast jedem Unternehmen abgefragt; testet, ob man den $O(n)$-Trick beherrscht.
- Grundlage für viele "**Zähle Subarrays mit Eigenschaft X**"-Probleme, bei denen X summenbezogen ist.

## Ansatz

**Brute Force** ($O(n²)$): Probiere jedes `(start, end)`-Paar aus.

**Präfixsumme** (der Trick): Definiere `prefix[i]` = Summe von `nums[0..i-1]`. Die Summe von `nums[i..j-1]` ist `prefix[j] - prefix[i]`. Wir möchten, dass dies gleich `k` ist, d. h. `prefix[i] = prefix[j] - k`.

Iteriere `j` von `0` bis `n`:
- Zähle für jedes `j`, wie viele `i < j` existieren, für die `prefix[i] = prefix[j] - k` gilt.
- Diese Anzahl entspricht der Anzahl der Subarrays, die bei `j` enden und die Summe `k` haben.
- Verwalte eine Hash Map `count[value] = Anzahl der bisherigen Vorkommen dieser Präfixsumme`.

**Basisfall:** `count[0] = 1` (das leere Präfix; ein Subarray, das bei Index 0 beginnt und die Summe 0 hat, trägt eins zur Gesamtzahl bei).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for hash_02: Subarray Sum Equals K.

The number of subarrays with sum k equals the number of prefix
sums p_j such that p_j == p_i - k for some earlier prefix p_i.
Track running prefix sums and the count of each. O(n).
"""


def solve(arr, k, n):
    count = 0
    prefix = 0
    freq = {0: 1}
    for i in range(n):
        prefix += arr[i]
        count += freq.get(prefix - k, 0)
        freq[prefix] = freq.get(prefix, 0) + 1
    return count
```

</details>

## Durchlauf

`nums = [1, 1, 1]`, `k = 2`. Antwort: 2.

`count = {0: 1}`, `running = 0`, `result = 0`.

| x | running | running - k | count[running - k] | result | count after |
|---:|---:|---:|---:|---:|---|
| 1 | 1 | -1 | 0 | 0 | `{0:1, 1:1}` |
| 1 | 2 | 0 | 1 | **1** | `{0:1, 1:1, 2:1}` |
| 1 | 3 | 1 | 1 | **2** | `{0:1, 1:1, 2:1, 3:1}` |

Antwort: 2. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n)$ | $O(n)$ |
| **Durchschnittlicher Fall** | $O(n)$ | $O(n)$ |
| **Schlechtester Fall** | $O(n)$ | $O(n)$ |

Ein einziger Durchlauf durch das Array. Die Hash Map speichert maximal `n + 1` verschiedene Präfixsummen (einschließlich der anfänglichen 0).

## Varianten & Optimierungen

- **Subarray product equals k** — gleiche Struktur, aber mit Produkt statt Summe. Lässt sich nicht direkt auf eine einfache Hash Map reduzieren; benötigt ein Sliding Window bei ausschließlich positiven Zahlen oder einen Präfix-Suffix-Split-Trick bei gemischten Vorzeichen.
- **Maximum-length subarray with sum k** — speichere nicht nur die Anzahl, sondern auch das früheste Vorkommen jeder Präfixsumme.
- **Subarray sum divisible by k** — verwendet modulare Arithmetik auf den Präfixsummen und eine Hash Map der Moduloklassen.
- **Two-sum Variante auf einer laufenden Summe** — gegeben eine Liste von Banktransaktionen und einen Zielbetrag, zähle wie viele zusammenhängende Fenster sich zu diesem Betrag summieren.
- **Count subarrays with sum in [a, b]** — verwende ein 2D-BIT oder einen Fenwick Tree auf koordinatenkomprimierten Präfixsummen.

## Anwendungen in der Praxis

- **Umsatzsteuer- / Gebührenabgleich** — zähle, wie viele zusammenhängende Zeitfenster eines täglichen P&L sich zu einem Zielwert summieren (z. B. "Gewinn der Morgenschicht").
- **Genomanalyse** — finde die Anzahl der Subsequenzen (im zusammenhängenden Sinne) mit einer Zielsumme von Marker-Anzahlen.
- **Datenstrom-Anomalieerkennung** — verfolge Präfixsummen eines Sliding Windows und zähle, wie viele Teilfenster einen Schwellenwert erreichen.
- **Netzwerk-Paketanalyse** — gegeben eine Sequenz von Byte-Anzahlen, zähle zusammenhängende Streams, die sich zu einer Ziel-Payload-Größe summieren.
- **Finanzielles Backtesting** — zähle die Anzahl der zusammenhängenden Handelstage, die eine Zielrendite erbracht haben.

## Verwandte Algorithmen in cOde(n)

- **[hash_01 — Two Sum](hash_01_two-sum.md)** — die Version für Subarrays der Größe 2. (d=4/10, r=9/10)
- **[hash_03 — Longest Substring Without Repeating](hash_03_longest-substring-without-repeating.md)** — Sliding-Window + Hash-Set. (d=4/10, r=9/10)
- **[dp_06 — Subset Sum](dp_06_subset-sum.md)** — die Subset-Version (nicht zusammenhängend) mit einer anderen Struktur. (d=5/10, r=9/10)

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*