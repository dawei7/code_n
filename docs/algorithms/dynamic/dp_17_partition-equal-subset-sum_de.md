# Summe der Teilmengen bei gleicher Partition

| | |
|---|---|
| **ID** | `dp_17` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(N * S)$ Zeit, $O(S)$ Speicherplatz |
| **Schwierigkeitsgrad** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) |

## Aufgabenstellung

Gegeben ist ein nichtleeres Array `nums`, das ausschließlich positive ganze Zahlen enthält. Stelle fest, ob das Array in zwei Teilmengen partitioniert werden kann, sodass die Summe der Elemente in beiden Teilmengen gleich ist.

**Eingabe:** Ein Array `nums` mit positiven ganzen Zahlen.
**Ausgabe:** Ein boolescher Wert: `True`, wenn eine gültige Partition existiert, andernfalls `False`.

## Wann man es verwenden sollte

- Du solltest sofort erkennen, dass es sich hierbei um eine leicht getarnte Variante des **Subset-Sum**-Problems (`dp_06`) oder des **0/1-Knapsack**-Problems (`dp_03`) handelt!
- Nutze es, um deine Fähigkeit zu demonstrieren, ein scheinbar komplexes Partitionierungsproblem auf eine standardmäßige algorithmische Vorlage zu reduzieren.

## Vorgehensweise

**1. Die mathematische Reduktion:**
Wenn wir das Array in zwei Teilmengen A und B so aufteilen, dass \text{Sum}(A) == \text{Sum}(B) gilt, dann muss mathematisch zwingend gelten, dass \text{Sum}(A) + \text{Sum}(B) = \text{TotalSum} ist.
Daher gilt: 2 × \text{Summe}(A) = \text{Gesamtsumme}.
Daraus ergeben sich zwei unumstößliche Tatsachen:
1. Ist `TotalSum` UNGERADE, ist es physikalisch unmöglich, das Array mithilfe von ganzen Zahlen gleichmäßig zu partitionieren. Gib sofort `False` zurück.
2. Ist `TotalSum` GERADE, ist das Problem genau dasselbe wie die Frage: „Gibt es IRGENDEINE Teilmenge A, deren Summe genau \frac{\text{Gesamtsumme}}{2} beträgt?“

Wir haben das Problem nun vollständig auf `dp_06 - Subset Sum` mit `target = TotalSum // 2` reduziert!

**2. Definition des Zustands:**
Sei `dp[s]` ein Boolescher Wert, der angibt, ob eine Teilmenge existiert, deren Summe genau `s` beträgt.

**3. Finde den Übergang (die Rekursionsbeziehung):**
Für jede Zahl `num` im Array durchlaufen wir das DP-Array rückwärts von `target` bis hinunter zu `num`.
Wir aktualisieren `dp[s]` auf `True`, wenn es bereits `True` war (wir benötigen `num`), ODER wenn `dp[s - num]` `True` war (wir verwenden `num`, um `s` zu erreichen).
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

## Schritt-für-Schritt-Anleitung

`nums = [1, 5, 11, 5]`.
`TotalSum` = 22. `target` = 11.
`dp` Größe 12, initialisiert auf `[T, F, F, F, F, F, F, F, F, F, F, F]`.

1. **num = 1:**
   - Schleife `s` von 11 bis 1.
   - `dp[1] = dp[1] or dp[0] = T`.
   - Zustand: `[T, T, F, F, F, F, F, F, F, F, F, F]`.
2. **num = 5:**
   - Schleife `s` von 11 bis 5.
   - `dp[6] = dp[6] or dp[1] = T`.
   - `dp[5] = dp[5] or dp[0] = T`.
   - Zustand: Die Summen `{0, 1, 5, 6}` betragen `True`.
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

*Dabei ist N die Länge von `nums` und S die Hälfte der Gesamtsumme.*
Die äußere Schleife wird N-mal durchlaufen, die innere Schleife bis zu S-mal. Die Gesamtlaufzeit im schlimmsten Fall beträgt streng genommen $O(N x S)$.
Da S durch N × 100 begrenzt ist (unter den gegebenen Standard-LeetCode-Einschränkungen, bei denen `nums[i] <= 100`), ist dieser Algorithmus außerordentlich schnell. Die Optimierung durch vorzeitiges Beenden senkt die Laufzeit im besten Fall oft auf nahezu $O(N)$.
Der Speicherbedarf beträgt unter Verwendung der 1D-Rolling-Array-Optimierung genau $O(S)$.

## Varianten & Optimierungen

- **Aufteilung in K Teilmengen mit gleicher Summe:** Was ist, wenn man das Array statt in 2 in K gleich große Teilmengen aufteilen muss? Dies macht den Standard-DP-Ansatz völlig zunichte! Wenn K > 2 ist, reicht 1D-DP mathematisch nicht aus. Man muss Bitmask-DP ($O(K x 2^N)$) oder reines DFS-Backtracking mit starkem Pruning verwenden.
- **Bitset-Optimierung:** In C++ ermöglicht `std::bitset` es dir, die innere Schleife als eine einzige $O(1)$ bitweise Verschiebungsoperation (`dp |= (dp << num)`) auszuführen. Dies ist ein außerordentlich wirkungsvoller Trick in der Wettbewerbsprogrammierung, um TLE-Grenzen zu umgehen.

## Anwendungen in der Praxis

- **Gerechte Aufteilung:** Die perfekte gleichmäßige Aufteilung eines Erbes oder einer Sammlung diskreter, unteilbarer Vermögenswerte zwischen zwei Parteien.
- **Prozessplanung:** Gleichmäßige Lastverteilung von Aufgaben mit unterschiedlichen Verarbeitungszeiten auf genau zwei CPU-Kerne, um die Gesamtlaufzeit (Makespan) zu minimieren.

## Verwandte Algorithmen in cOde(n)

- **[dp_06 – Subset Sum](dp_06_subset-sum.md)** — Der buchstäblich exakt gleiche Algorithmus. Diese Datei dient dazu, die mathematische Reduktion zu veranschaulichen.
- **[bb_06 – Teilmenge-Summe (Branch & Bound)](../branch_and_bound/bb_06_subset-sum.md)** — Wie man dieses Problem löst, wenn S astronomisch groß und N klein ist.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
