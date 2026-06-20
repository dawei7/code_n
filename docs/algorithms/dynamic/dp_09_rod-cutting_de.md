# Stangenschneiden

| | |
|---|---|
| **ID** | `dp_09` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Stabschneideproblem](https://en.wikipedia.org/wiki/Cutting_stock_problem) |

## Aufgabenstellung

Gegeben sei ein Stab der Länge `n` und eine Preistabelle `prices[i]` für einen
Stab der Länge `i + 1` (für `i = 0..n-1`), bestimme den
**maximalen Erlös**, der erzielt werden kann, wenn der Stab in Stücke geschnitten
und diese verkauft werden.

**Eingabe:** eine ganze Zahl `n` und ein Array `prices` der Länge `n`.
**Ausgabe:** der maximale Erlös.

**Beispiel:**

| Länge | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Preis | 1 | 5 | 8 | 9 | 10 | 17 | 17 | 20 |

`n = 8`. Optimal: Aufteilung in 2 + 2 + 2 + 2 (Erlös 5+5+5+5 = 20)
ODER 6 + 2 (17+5 = 22) ODER 1+2+5+... — das beste Ergebnis ist **22** (6+2).

## Wann man es anwendet

- Die klassische Einführungsaufgabe zur dynamischen Programmierung (DP) für „**Aufteilung in Teile
  zur Maximierung einer Größe**“ – in der Variante mit unbegrenztem Rucksack,
  bei der jeder Schnitt zwischen den Teilen erfolgt und sich Teile wiederholen dürfen.
- Eine kleine Variante („Einen Stab der Länge N zerbrechen“) wird manchmal
  in Telefon-Vorauswahlgesprächen als Aufwärmaufgabe gestellt.

## Herangehensweise

Sei `dp[i]` = der maximale Erlös für einen Stab der Länge `i`.

**Rekursion:** Betrachten wir den ersten Schnitt. Wenn wir ein Stück
der Länge `j` (für `j = 1..i`) abschneiden, behalten wir `prices[j-1]` und
haben einen verbleibenden Stab der Länge `i - j` im Wert von `dp[i - j]`.
Man berechne das Maximum über alle ersten Schnitte:

```
dp[i] = max(prices[j-1] + dp[i - j])  for j = 1..i
```

**Basisfall:** `dp[0] = 0` (kein Stab, kein Erlös).

**Ergebnis:** `dp[n]`.

Dies ist die Form des „unbegrenzten Rucksacks“ – wir wählen
„Stücke“ (Längen) mit Wiederholungen aus, um den Wert zu maximieren.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_09: Rod Cutting.

dp[length] = max revenue for a rod of that length. For each
length, try every first-cut size.
"""


def solve(prices, n):
    dp = [0] * (n + 1)
    for length in range(1, n + 1):
        for cut in range(1, length + 1):
            revenue = prices[cut - 1] + dp[length - cut]
            if revenue > dp[length]:
                dp[length] = revenue
    return dp[n]
```

</details>

## Schritt-für-Schritt-Anleitung

`prices = [1, 5, 8, 9, 10, 17, 17, 20]`, `n = 8`.

`dp = [0, 0, 0, 0, 0, 0, 0, 0, 0]`.

| i | versuche j=1 (1+dp[i-1]) | j=2 (5+dp[i-2]) | j=3 (8+dp[i-3]) | j=4 (9+dp[i-4]) | ... | dp[i] |
|---:|---:|---:|---:|---:|---|---:|
| 1 | 1+0=1 | — | — | — | — | 1 |
| 2 | 1+1=2 | 5+0=5 | — | — | — | 5 |
| 3 | 1+5=6 | 5+1=6 | 8+0=8 | — | — | 8 |
| 4 | 1+8=9 | 5+5=10 | 8+1=9 | 9+0=9 | — | 10 |
| 5 | 1+10=11 | 5+8=13 | 8+5=13 | 9+1=10 | 10+0=10 → **13** |
| 6 | 1+13=14 | 5+10=15 | 8+8=16 | 9+5=14 | 10+1=11, 17+0=17 → **17** |
| 7 | 1+17=18 | 5+13=18 | 8+10=18 | 9+8=17 | 10+5=15, 17+1=18, 17+0=17 → **18** |
| 8 | 1+18=19 | 5+17=22 | 8+13=21 | 9+10=19 | 10+8=18, 17+5=22, 17+1=18, 20+0=20 → **22** |

Antwort: `dp[8] = 22`. ✓ (Schnitte: 2 + 6, Erlös 5 + 17 = 22.)

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(n²)$ | $O(n)$ |
| **Durchschnittlicher Fall** | $O(n²)$ | $O(n)$ |
| **Schlechtester Fall** | $O(n²)$ | $O(n)$ |

Jedes `dp[i]` ist das Maximum über höchstens `i` Kandidaten, daher beträgt die
Doppelschleife $O(n²)$. Der Speicherbedarf beträgt $O(n)$ für das DP-Array.

## Varianten & Optimierungen

- **Die Schnitte rekonstruieren** — ein paralleles `cut_at[i]`
  Array führen, das aufzeichnet, welches `j` ausgewählt wurde; zurückgehen, um
  die Schnitte auszugeben.
- **Kosten des Schneidens** — Wenn jeder Schnitt `c` kostet, ziehe `c`
  vom Kandidaten ab. Manche Schnitte werden unwirtschaftlich.
- **Minimale Schnitte für einen Zielerlös** — Anstelle des maximalen
  Erlöses die minimale Stückzahl ermitteln, sodass
  der Erlös ≥ dem Zielwert ist. Erfordert eine andere DP-Struktur (beide
  Metriken verfolgen).
- **Verallgemeinertes Stabschneiden** — Stücke können sowohl eine *Breite*
  als auch eine Länge haben (z. B. 2D-Schneidgut). Die 1D-DP
  lässt sich zu einer 2D-DP verallgemeinern.

## Anwendungen in der Praxis

- **Materialzerlegungsproblem** — Zerschneiden von Rohstoffen (Stahl,
  Papier, Stoff, Bauholz) in verkaufsfähige Stücke, um
  Abfall zu minimieren. Im Allgemeinen NP-schwer; die einfache Version ist die
  Stabzerlegungs-DP.
- **Logistik** — „Wie lässt sich ein 40-Fuß-Container in
  Standardpaletten aufteilen, um den Wert zu maximieren?“
- **Druck** — die beste Methode, eine Papier- oder Stoffrolle
  für Druckaufträge zuzuschneiden.
- **Registerzuordnung beim Compiler** — „Aufteilung einer langlebigen
  Variablen auf Register, um Cache-Treffer zu maximieren.“
- **Produktionsplanung** — Aufteilung eines langen Produktionslaufs in
  Chargen, die der Nachfrage entsprechen.

## Verwandte Algorithmen in cOde(n)

- **[dp_03 — 0/1-Rucksackproblem](dp_03_knapsack.md)** — begrenzte
  Variante, Maximierung. (d=5/10, r=9/10)
- **[dp_05 — Münzwechsel](dp_05_coin-change.md)** — unbegrenzt,
  Anzahl minimieren. (d=5/10, r=9/10)
- **[dp_07 — LIS](dp_07_longest-increasing-subsequence.md)** —
  ein weiterer klassischer 1D-DP, der ebenfalls häufig in Vorstellungsgesprächen abgefragt wird.
  (d=5/10, r=9/10)

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag
finden Sie über den Wikipedia-Link oben auf der Seite.
Quell-Repository: <https://github.com/dawei7/code_n>.*
