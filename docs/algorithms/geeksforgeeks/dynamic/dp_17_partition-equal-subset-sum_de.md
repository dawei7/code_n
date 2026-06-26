# Partition Equal Subset Sum

| | |
|---|---|
| **ID** | `dp_17` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(N * S)$ Zeit, $O(S)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) |

## Problemstellung

Gegeben ist ein nicht leeres Array `nums`, das nur positive Ganzzahlen enthält. Es soll festgestellt werden, ob das Array in zwei Teilmengen partitioniert werden kann, sodass die Summe der Elemente in beiden Teilmengen gleich ist.

**Eingabe:** Ein Array `nums` aus positiven Ganzzahlen.
**Ausgabe:** Ein Boolean: `True`, falls eine gültige Partitionierung existiert, andernfalls `False`.

## Wann ist es anzuwenden?

- Sie sollten dies sofort als eine leicht verschleierte Variante des **Subset Sum** (`dp_06`) oder **0/1 Knapsack** (`dp_03`) Problems erkennen!
- Nutzen Sie es, um Ihre Fähigkeit zu demonstrieren, ein scheinbar komplexes Partitionierungsproblem auf eine Standard-Algorithmus-Vorlage zu reduzieren.

## Ansatz

**1. Die mathematische Reduktion:**
Wenn wir das Array in zwei Teilmengen A und B unterteilen, sodass \text{Sum}(A) == \text{Sum}(B), dann muss mathematisch gelten: \text{Sum}(A) + \text{Sum}(B) = \text{TotalSum}.
Daraus folgt: 2 x \text{Sum}(A) = \text{TotalSum}.
Dies impliziert zwei absolute Fakten:
1. Wenn die `TotalSum` UNGERADE ist, ist es physikalisch unmöglich, das Array mit Ganzzahlen gleichmäßig zu partitionieren. Geben Sie sofort `False` zurück.
2. Wenn die `TotalSum` GERADE ist, ist das Problem exakt identisch mit der Frage: "Existiert IRGENDEINE Teilmenge A, deren Summe exakt \frac{\text{TotalSum}}{2} beträgt?"

Wir haben das Problem nun perfekt auf `dp_06 - Subset Sum` mit `target = TotalSum // 2` reduziert!

**2. Definition des Zustands:**
Sei `dp[s]` ein Boolean, der angibt, ob eine Teilmenge existiert, deren Summe exakt `s` ergibt.

**3. Finden des Übergangs (Die Rekursionsgleichung):**
Für jede Zahl `num` im Array iterieren wir rückwärts durch das DP-Array von `target` bis `num`.
Wir aktualisieren `dp[s]` auf `True`, wenn es bereits `True` war (wir benötigen `num` nicht), ODER wenn `dp[s - num]` `True` war (wir verwenden `num`, um `s` zu erreichen).
`dp[s] = dp[s] OR dp[s - num]`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_17: Partition Equal Subset Sum.

True iff arr can be split into two equal-sum subsets.
"""


def solve(arr):
    total = sum(arr)
    if total % 2 != 0:
        return False
    target = total // 2
    reachable = {0}
    for v in arr:
        reachable = reachable | {s + v for s in reachable}
    return target in reachable
```

</details>

## Durchlauf

`nums = [1, 5, 11, 5]`.
`TotalSum` = 22. `target` = 11.
`dp` der Größe 12 wird initialisiert mit `[T, F, F, F, F, F, F, F, F, F, F, F]`.

1. **num = 1:**
   - Schleife `s` von 11 bis 1.
   - `dp[1] = dp[1] or dp[0] = T`.
   - Zustand: `[T, T, F, F, F, F, F, F, F, F, F, F]`.
2. **num = 5:**
   - Schleife `s` von 11 bis 5.
   - `dp[6] = dp[6] or dp[1] = T`.
   - `dp[5] = dp[5] or dp[0] = T`.
   - Zustand: Summen `{0, 1, 5, 6}` sind `True`.
3. **num = 11:**
   - Schleife `s` von 11 bis 11.
   - `dp[11] = dp[11] or dp[0] = T`.
   - `dp[target]` ist nun `True`! Vorzeitiger Abbruch wird ausgelöst.

Das Ergebnis ist `True`. ✓ (Die Teilmengen sind `[11]` und `[1, 5, 5]`).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(S)$ |
| **Durchschnittlicher Fall** | $O(N * S)$ | $O(S)$ |
| **Schlechtester Fall** | $O(N * S)$ | $O(S)$ |

*Wobei N die Länge von `nums` und S die Hälfte der Gesamtsumme ist.*
Die äußere Schleife läuft N-mal, die innere Schleife bis zu S-mal. Die gesamte Zeitkomplexität im schlechtesten Fall ist strikt $O(N x S)$.
Da S durch N x 100 begrenzt ist (unter der Annahme der Standard-LeetCode-Beschränkungen, bei denen `nums[i] <= 100`), ist dieser Algorithmus extrem schnell. Die Optimierung durch vorzeitigen Abbruch reduziert die Zeit im Bestfall oft auf nahezu $O(N)$.
Der Platzbedarf beträgt exakt $O(S)$ unter Verwendung der 1D-Rolling-Array-Optimierung.

## Varianten & Optimierungen

- **Partition to K Equal Sum Subsets:** Was ist, wenn Sie das Array in K gleiche Teilmengen statt in 2 partitionieren müssen? Dies zerstört den Standard-DP-Ansatz vollständig! Wenn K > 2, ist 1D-DP mathematisch unzureichend. Sie müssen Bitmask-DP ($O(K x 2^N)$) oder reines DFS-Backtracking mit starkem Pruning verwenden.
- **Bitset-Optimierung:** In C++ erlaubt `std::bitset` die Ausführung der inneren Schleife als eine einzige $O(1)$ bitweise Verschiebeoperation (`dp |= (dp << num)`). Dies ist ein phänomenal mächtiger Trick in der wettbewerbsorientierten Programmierung, um TLE-Limits zu umgehen.

## Anwendungen in der Praxis

- **Gerechte Aufteilung:** Die perfekte Aufteilung eines Erbes oder einer Sammlung diskreter, unteilbarer Vermögenswerte zwischen zwei Parteien.
- **Prozess-Scheduling:** Lastverteilung von Jobs mit unterschiedlichen Bearbeitungszeiten gleichmäßig auf genau zwei CPU-Kerne, um die Gesamtausführungszeit (Makespan) zu minimieren.

## Verwandte Algorithmen in cOde(n)

- **[dp_06 - Subset Sum](dp_06_subset-sum.md)** — Buchstäblich derselbe Algorithmus. Diese Datei dient dazu, die mathematische Reduktion zu verdeutlichen.
- **[bb_06 - Subset Sum (Branch & Bound)](../branch_and_bound/bb_06_subset-sum.md)** — Wie man dies löst, wenn S astronomisch groß und N klein ist.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für wettbewerbsorientierte Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*