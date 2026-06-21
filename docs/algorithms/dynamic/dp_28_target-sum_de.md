# Target Sum

| | |
|---|---|
| **ID** | `dp_28` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(N * S)$ Zeit, $O(S)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Target Sum](https://leetcode.com/problems/target-sum/) |

## Problemstellung

Gegeben ist ein Array von Ganzzahlen `nums` und eine Ganzzahl `target`.
Sie möchten einen Ausdruck aus `nums` bilden, indem Sie vor jede Ganzzahl in `nums` eines der Symbole `+` oder `-` setzen und anschließend alle Ganzzahlen verketten.
Geben Sie die Anzahl der verschiedenen Ausdrücke zurück, die Sie bilden können und die zu `target` ausgewertet werden.

**Eingabe:** Ein Array von Ganzzahlen `nums` und eine Ganzzahl `target`.
**Ausgabe:** Eine Ganzzahl, die die Gesamtzahl der Möglichkeiten darstellt, das Ziel zu erreichen.

## Wann man es verwendet

- Um Ihre Fähigkeit unter Beweis zu stellen, ein scheinbar einzigartiges kombinatorisches Problem direkt auf das kanonische **0/1 Knapsack** (`dp_03`) oder **Subset Sum** (`dp_06`) Framework zu reduzieren.

## Ansatz

**1. Die mathematische Reduktion:**
Teilen wir alle Zahlen in zwei Mengen auf:
- Menge P: Die Zahlen, denen wir ein `+`-Zeichen zugewiesen haben.
- Menge N: Die Zahlen, denen wir ein `-`-Zeichen zugewiesen haben.

Die Summe unseres Ausdrucks ist: \text{Sum}(P) - \text{Sum}(N) = \text{target}.
Wir wissen außerdem absolut sicher: \text{Sum}(P) + \text{Sum}(N) = \text{TotalSum} (die Summe aller Elemente im Array).

Wenn wir diese beiden Gleichungen addieren, erhalten wir:
2 x \text{Sum}(P) = \text{target} + \text{TotalSum}
\text{Sum}(P) = (\text{target} + \text{TotalSum}) / 2

Dies ist eine erstaunliche Erkenntnis! Das Problem ist mathematisch identisch mit der Frage: **"Wie viele Teilmengen von `nums` summieren sich exakt zu `(target + TotalSum) / 2`?"**
Wir haben dies perfekt auf das Problem `dp_06 - Subset Sum` reduziert!

**Spezialfälle, die sofort abgefangen werden müssen:**
- Wenn `(target + TotalSum)` eine ungerade Zahl ist, ist es mathematisch unmöglich, das Ziel mit Ganzzahlen zu erreichen. Geben Sie 0 zurück.
- Wenn `abs(target) > TotalSum`, ist es unmöglich, das Ziel zu erreichen. Geben Sie 0 zurück.

**2. Definition des Zustands:**
Sei `dp[s]` die Anzahl der Möglichkeiten, eine Teilmenge von Zahlen auszuwählen, die sich exakt zu `s` summieren.
Unser neues Ziel ist S = (\text{target} + \text{TotalSum}) / 2.

**3. Finden des Induktionsanfangs:**
`dp[0] = 1`. Es gibt genau 1 Möglichkeit, eine Summe von 0 zu erreichen: keine Elemente auswählen! (Hinweis: Falls es Nullen in `nums` gibt, werden diese die Anzahl der Möglichkeiten später natürlich verdoppeln).

**4. Finden des Übergangs (Die Rekurrenz):**
Für jede Zahl `num` im Array iterieren wir rückwärts durch das DP-Array von S bis `num`.
Die Anzahl der Möglichkeiten, die Summe `s` zu erreichen, ist einfach die Anzahl der Möglichkeiten, die wir BEREITS hatten, um `s` zu erreichen (ohne `num` zu verwenden), PLUS die Anzahl der Möglichkeiten, `s - num` zu erreichen (was bedeutet, dass wir uns entschieden haben, `num` zu verwenden)!
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

## Durchlauf

`nums = [1, 1, 1, 1, 1]`, `target = 3`.
`total_sum` = 5.
`subset_target` = (3 + 5) / 2 = 4.
`dp` der Größe 5 initialisiert mit `[1, 0, 0, 0, 0]`.

1. **num = 1 (1.):**
   - `s=4..1`: `dp[1] += dp[0]`.
   - `dp`-Zustand: `[1, 1, 0, 0, 0]`.
2. **num = 1 (2.):**
   - `s=4..1`: `dp[2] += dp[1]`, `dp[1] += dp[0]`.
   - `dp`-Zustand: `[1, 2, 1, 0, 0]`.
3. **num = 1 (3.):**
   - `s=4..1`: `dp[3]+=dp[2]`, `dp[2]+=dp[1]`, `dp[1]+=dp[0]`.
   - `dp`-Zustand: `[1, 3, 3, 1, 0]`. (Das ist das Pascalsche Dreieck!).
4. **num = 1 (4.):**
   - `s=4..1`: `dp[4]+=1`, `dp[3]+=3`, `dp[2]+=3`, `dp[1]+=1`.
   - `dp`-Zustand: `[1, 4, 6, 4, 1]`.
5. **num = 1 (5.):**
   - `s=4`: `dp[4] += dp[3] = 1 + 4 = 5`.
   - `dp`-Zustand: `[1, 5, 10, 10, 5]`.

Das Ergebnis `dp[4]` ist 5. ✓ (Die Anzahl der Teilmengen der Größe 4 aus 5 Elementen ist exakt 5!).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(S)$ |
| **Durchschnittlicher Fall** | $O(N * S)$ | $O(S)$ |
| **Schlechtester Fall** | $O(N * S)$ | $O(S)$ |

*Wobei N die Anzahl der Elemente und S `subset_target` ist.*
Die äußere Schleife läuft N-mal. Die innere Schleife läuft bis zu S-mal. Die Gesamtzeit beträgt $O(N x S)$.
Die Platzkomplexität beträgt strikt $O(S)$ für das 1D-Array.

## Varianten & Optimierungen

- **Top-Down Memoization mit echtem Ziel:** Wenn Ihnen der mathematische Trick während eines Vorstellungsgesprächs nicht einfällt, können Sie dies direkt mittels Top-Down Memoization lösen! Ihr Zustand ist `solve(index, current_sum)`. Da `current_sum` negativ sein kann, müssen Sie diese um `TotalSum` verschieben, wenn Sie sie in einem 2D-Cache-Array speichern, oder einfach eine Hash Map `cache[(index, current_sum)]` verwenden. Die Zeitkomplexität bleibt $O(N x \text{TotalSum})$.

## Anwendungen in der Praxis

- **Signalverarbeitung / Fehlerkorrektur:** Bestimmung der Gesamtzahl der Permutationen, bei denen ein BPSK-Signal (Binary Phase-Shift Keying) Vorzeichen umkehren könnte und dennoch dieselbe integrierte Endamplitude ergibt.

## Verwandte Algorithmen in cOde(n)

- **[dp_17 - Partition Equal Subset Sum](dp_17_partition-equal-subset-sum.md)** — Ein weiteres Problem, das eine mathematische Reduktion auf Subset Sum erfordert.
- **[dp_06 - Subset Sum](dp_06_subset-sum.md)** — Der grundlegende Algorithmus, auf den dieses Problem reduziert wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*