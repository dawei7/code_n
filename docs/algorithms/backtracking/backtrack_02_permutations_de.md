# Permutationen

| | |
|---|---|
| **ID** | `backtrack_02` |
| **Kategorie** | Backtracking |
| **Komplexität (erforderlich)** | $O(N * N!)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Permutations](https://leetcode.com/problems/permutations/) |

## Problemstellung

Gegeben ist ein Array `nums` mit verschiedenen Ganzzahlen. Geben Sie alle möglichen Permutationen zurück. Sie können das Ergebnis in einer beliebigen Reihenfolge zurückgeben.
Eine Permutation ist eine Neuanordnung aller Elemente in einer spezifischen sequenziellen Reihenfolge.

**Eingabe:** Ein Ganzzahl-Array `nums` mit verschiedenen Zahlen.
**Ausgabe:** Eine Liste von Listen, wobei jede innere Liste eine gültige Permutation darstellt.

## Wann man es verwendet

- Um jede mögliche Anordnung von Elementen zu generieren.
- Im Gegensatz zu Subsets ist bei Permutationen die Reihenfolge wichtig (`[1, 2]` ist etwas anderes als `[2, 1]`) und Permutationen müssen immer JEDES Element aus dem ursprünglichen Array enthalten.

## Ansatz

**1. Der Entscheidungsbaum:**
An der allerersten Position unserer Permutation können wir JEDE der N Zahlen wählen.
Für die zweite Position können wir JEDE der verbleibenden N-1 Zahlen wählen.
Dies erzeugt einen Baum mit genau N! (N-Fakultät) Blättern!

**2. Der Backtracking-Zustand:**
Wir definieren eine rekursive Funktion `backtrack(current_perm)`:
- `current_perm`: Eine Liste, die die Zahlen sammelt, die wir der Reihe nach ausgewählt haben.
Da die Reihenfolge wichtig ist, verwenden wir KEINEN `index`-Parameter, um uns zu zwingen, nur nach vorne zu schauen (wie wir es bei Subsets getan haben). Bei Permutationen durchlaufen wir immer das GESAMTE Array `nums`, um nach verfügbaren Zahlen zu suchen!

**3. Basisfall:**
Wenn `len(current_perm) == len(nums)`, ist unsere Permutation vollständig!
Wir fügen eine Kopie zum globalen Ergebnis hinzu und kehren zurück.

**4. Der rekursive Schritt (Backtracking):**
Wir durchlaufen jede Zahl in `nums`.
Wenn die Zahl BEREITS in `current_perm` enthalten ist, überspringen wir sie (da wir dasselbe Element nicht zweimal verwenden können).
Wenn sie verfügbar ist:
- Wir fügen sie zu `current_perm` hinzu.
- Wir gehen tiefer in die Rekursion.
- Backtrack: Wir entfernen sie wieder mittels `pop` aus `current_perm`, damit die nächste Iteration der Schleife versuchen kann, eine andere Zahl für diese Position zu wählen.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for backtrack_02: Permutations.

Return every ordering of ``arr`` as a list of lists. Standard
backtracking: pick each unused element in turn, recurse, then
unpick. The output list of permutations is sorted so the
verify can do a plain equality check.
"""


def solve(arr, n):
    if n == 0:
        return [[]]
    result = []
    used = [False] * n

    def helper(path):
        if len(path) == n:
            result.append(list(path))
            return
        for i in range(n):
            if not used[i]:
                used[i] = True
                path.append(arr[i])
                helper(path)
                path.pop()
                used[i] = False

    helper([])
    result.sort()
    return result
```

</details>

## Durchlauf

`nums = [1, 2]`. N=2.

1. `backtrack([])`:
   - Schleife `num = 1`: nicht in `[]`. Hinzufügen. `perm = [1]`.
     - `backtrack([1])`:
       - Schleife `num = 1`: in `[1]`. Überspringen.
       - Schleife `num = 2`: nicht in `[1]`. Hinzufügen. `perm = [1, 2]`.
         - `backtrack([1, 2])`: Basisfall! `[1, 2]` zum Ergebnis hinzufügen.
       - Backtrack: `2` entfernen. `perm = [1]`.
   - Backtrack: `1` entfernen. `perm = []`.
   - Schleife `num = 2`: nicht in `[]`. Hinzufügen. `perm = [2]`.
     - `backtrack([2])`:
       - Schleife `num = 1`: nicht in `[2]`. Hinzufügen. `perm = [2, 1]`.
         - `backtrack([2, 1])`: Basisfall! `[2, 1]` zum Ergebnis hinzufügen.
       - Backtrack: `1` entfernen. `perm = [2]`.
       - Schleife `num = 2`: in `[2]`. Überspringen.
   - Backtrack: `2` entfernen. `perm = []`.

Ergebnis: `[[1, 2], [2, 1]]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N * N!)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N * N!)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N * N!)$ | $O(N)$ |

Es gibt genau N! Blätter. An jedem Blatt benötigt das Kopieren des Arrays $O(N)$ Zeit. Die Gesamtzeit beträgt strikt $O(N * N!)$.
*(Hinweis: Die Suche `num in current_perm` benötigt $O(N)$ Zeit, was die theoretische Zeit auf $O(N^2 * N!)$ erhöht. Wir können dies jedoch durch ein Hash Set oder ein boolesches Array auf $O(1)$ optimieren).*
Die Platzkomplexität beträgt $O(N)$ für den Rekursions-Stack und die Zustandsliste.

## Varianten & Optimierungen

- **Permutations II (Mit Duplikaten):** Was ist, wenn `nums = [1, 1, 2]`? Der grundlegende Algorithmus würde doppelte Permutationen erzeugen.
  1. Verwenden Sie ein boolesches `used[]`-Array anstelle von `num in current_perm` (da die beiden `1`en unterschiedliche Objekte an verschiedenen Indizes sind).
  2. Sortieren Sie das Array zuerst.
  3. Überspringen Sie innerhalb der Schleife identische Nachbarn, WENN ihr identischer Zwilling in der aktuellen Rekursionstiefe NICHT verwendet wurde: `if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue`.
- **In-Place Swapping Optimierung:** Anstatt eine separate `current_perm`-Liste zu verwalten, können Sie das `nums`-Array direkt manipulieren! Übergeben Sie einen `index`, der die Grenze der fixierten Elemente darstellt. Für den aktuellen `index` durchlaufen Sie `j` von `index` bis `N`, tauschen `nums[index]` und `nums[j]`, gehen rekursiv zu `index+1` und tauschen sie zum Backtracking wieder zurück!

## Anwendungen in der Praxis

- **Traveling Salesperson Problem (Brute Force):** Berechnung der Gesamtdistanz für jede einzelne mögliche Permutation der zu besuchenden Städte, um den absolut kürzesten Pfad zu finden.
- **Kryptographie:** Brute-Force-Angriffe auf alle möglichen Transpositionschiffren oder Schlüsselpermutationen.

## Verwandte Algorithmen in cOde(n)

- **[backtrack_01 - Subsets](backtrack_01_subset-sum-decision.md)** — Das $O(2^N)$-Grundlagenproblem, bei dem die Reihenfolge keine Rolle spielt.
- **[backtrack_03 - Combination Sum](backtrack_03_combination-sum.md)** — Ein Hybrid, bei dem die Reihenfolge keine Rolle spielt, aber Elemente unbegrenzt wiederverwendet werden können!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*