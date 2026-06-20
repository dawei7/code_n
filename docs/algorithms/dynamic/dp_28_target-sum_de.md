# Zielsumme

| | |
|---|---|
| **ID** | `dp_28` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(N * S)$ Zeit, $O(S)$ Speicherplatz |
| **Schwierigkeitsgrad** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Target Sum](https://leetcode.com/problems/target-sum/) |

## Aufgabenstellung

Gegeben sind ein Array aus ganzen Zahlen `nums` und eine ganze Zahl `target`.
Sie möchten aus `nums` einen Ausdruck bilden, indem Sie vor jeder Ganzzahl in `nums` eines der Symbole `+` und `-` einfügen und anschließend alle Ganzzahlen verketten.
Gib die Anzahl der verschiedenen Ausdrücke zurück, die du bilden kannst und deren Ergebnis `target` ist.

**Eingabe:** Ein Ganzzahl-Array `nums` und eine Ganzzahl `target`.
**Ausgabe:** Eine Ganzzahl, die die Gesamtzahl der Möglichkeiten angibt, das Ziel zu erreichen.

## Wann man es verwenden sollte

- Um Ihre Fähigkeit zu demonstrieren, ein scheinbar einzigartiges kombinatorisches Problem mathematisch direkt auf das kanonische **0/1-Rucksackproblem** (`dp_03`) oder das **Teilmenge-Summen-Problem** (`dp_06`) zu reduzieren.

## Vorgehensweise

**1. Die mathematische Reduktion:**
Teilen wir alle Zahlen in zwei Mengen auf:
- Menge P: Die Zahlen, denen wir ein `+`-Vorzeichen zugewiesen haben.
- Menge N: Die Zahlen, denen wir ein `-`-Vorzeichen zugewiesen haben.

Die Summe unseres Ausdrucks lautet: \text{Sum}(P) - \text{Sum}(N) = \text{Zielwert}.
Außerdem wissen wir mit Sicherheit: \text{Summe}(P) + \text{Summe}(N) = \text{Gesamtsumme} (die Summe aller Elemente im Array).

Wenn wir diese beiden Gleichungen addieren, erhalten wir:
2 × \text{Summe}(P) = \text{Zielwert} + \text{Gesamtsumme}
\text{Summe}(P) = (\text{Zielwert} + \text{Gesamtsumme}) / 2

Das ist eine unglaubliche Erkenntnis! Das Problem ist mathematisch identisch mit der Frage: **„Wie viele Teilmengen von `nums` ergeben in der Summe genau `(target + TotalSum) / 2`?“**
Wir haben dies perfekt auf das `dp_06 - Subset Sum`-Problem reduziert!

**Grenzfälle, die sofort zu beachten sind:**
- Wenn `(target + TotalSum)` eine ungerade Zahl ist, ist es mathematisch unmöglich, das Ziel mit ganzen Zahlen zu erreichen. Gib 0 zurück.
- Wenn `abs(target) > TotalSum`, ist es unmöglich, das Ziel zu erreichen. Gib 0 zurück.

**2. Definiere den Zustand:**
Sei `dp[s]` die Anzahl der Möglichkeiten, eine Teilmenge von Zahlen auszuwählen, deren Summe genau `s` beträgt.
Unser neues Ziel ist S = (\text{Ziel} + \text{Gesamtsumme}) / 2.

**3. Den Basisfall ermitteln:**
`dp[0] = 1`. Es gibt genau eine Möglichkeit, eine Summe von 0 zu erreichen: keine Elemente auswählen! (Hinweis: Wenn `nums` Nullen enthält, verdoppeln diese später natürlich die Anzahl der Möglichkeiten).

**4. Bestimme den Übergang (die Rekursionsbeziehung):**
Für jede Zahl `num` im Array durchlaufen wir das DP-Array rückwärts von S bis hinunter zu `num`.
Die Anzahl der Möglichkeiten, die Summe `s` zu erreichen, ist einfach die Anzahl der Möglichkeiten, die wir BEREITS hatten, um `s` zu erreichen (ohne `num` zu verwenden), ZUZÜGLICH der Anzahl der Möglichkeiten, `s - num` zu erreichen (was bedeutet, dass wir uns für die Verwendung von `num` entschieden haben)!
`dp[s] = dp[s] + dp[s - num]`

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_28: Target Sum.

Reduce to subset-sum: find number of subsets with sum
equal to (target + total_sum) // 2. Classic 0/1 knapsack
counting DP with 1D backward iteration.
"""


def solve(nums, n, target):
    total = sum(nums)
    if (target + total) % 2 != 0 or abs(target) > total:
        return 0
    s = (target + total) // 2
    dp = [0] * (s + 1)
    dp[0] = 1
    for num in nums:
        for j in range(s, num - 1, -1):
            dp[j] += dp[j - num]
    return dp[s]
```

</details>

## Schritt-für-Schritt-Anleitung

`nums = [1, 1, 1, 1, 1]`, `target = 3`.
`total_sum` = 5.
`subset_target` = (3 + 5) / 2 = 4.
`dp` Größe 5, initialisiert auf `[1, 0, 0, 0, 0]`.

1. **num = 1 (1.):**
   - `s=4..1`: `dp[1] += dp[0]`.
   - `dp`-Zustand: `[1, 1, 0, 0, 0]`.
2. **num = 1 (2.):**
   - `s=4..1`: `dp[2] += dp[1]`, `dp[1] += dp[0]`.
   - `dp` Zustand: `[1, 2, 1, 0, 0]`.
3. **num = 1 (3.):**
   - `s=4..1`: `dp[3]+=dp[2]`, `dp[2]+=dp[1]`, `dp[1]+=dp[0]`.
   - `dp` Zustand: `[1, 3, 3, 1, 0]`. (Das ist das Pascalsche Dreieck!).
4. **num = 1 (4.):**
   - `s=4..1`: `dp[4]+=1`, `dp[3]+=3`, `dp[2]+=3`, `dp[1]+=1`.
   - `dp` Zustand: `[1, 4, 6, 4, 1]`.
5. **num = 1 (5.):**
   - `s=4`: `dp[4] += dp[3] = 1 + 4 = 5`.
   - `dp` Zustand: `[1, 5, 10, 10, 5]`.

Das Ergebnis `dp[4]` ist 5. ✓ (Die Teilmengen der Größe 4 aus 5 Elementen sind genau 5!).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(S)$ |
| **Durchschnittlicher Fall** | $O(N * S)$ | $O(S)$ |
| **Schlechtester Fall** | $O(N * S)$ | $O(S)$ |

*Dabei ist N die Anzahl der Elemente und S ist `subset_target`.*
Die äußere Schleife wird N-mal durchlaufen. Die innere Schleife wird bis zu S-mal durchlaufen. Die Gesamtzeit beträgt $O(N x S)$.
Die Platzkomplexität beträgt für das 1D-Rolling-Array streng $O(S)$.

## Varianten & Optimierungen

- **Top-Down-Memoisation mit echtem Zielwert:** Falls dir der mathematische Trick während eines Vorstellungsgesprächs nicht einfallen sollte, kannst du das Problem direkt mit Top-Down-Memoisation lösen! Dein Zustand ist `solve(index, current_sum)`. Da `current_sum` negativ sein kann, musst du ihn beim Speichern in einem 2D-Cache-Array um `TotalSum` verschieben oder einfach eine Hash-Map `cache[(index, current_sum)]` verwenden. Die Zeitkomplexität bleibt $O(N x \text{TotalSum})$.

## Anwendungen in der Praxis

- **Signalverarbeitung / Fehlerkorrektur:** Ermittlung der Gesamtzahl der Permutationen, bei denen ein BPSK-Signal (Binary Phase-Shift Keying) seine Vorzeichen umkehren könnte und dennoch dieselbe endgültige integrierte Amplitude ergeben würde.

## Verwandte Algorithmen in cOde(n)

- **[dp_17 – Partition Equal Subset Sum](dp_17_partition-equal-subset-sum.md)** — Ein weiteres Problem, das eine mathematische Reduktion auf die Teilmengen-Summe erfordert.
- **[dp_06 – Teilmenge-Summe](dp_06_subset-sum.md)** — Der grundlegende Algorithmus, auf den sich dieses Problem reduzieren lässt.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
