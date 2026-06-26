# Majority Element (Divide and Conquer)

| | |
|---|---|
| **ID** | `dc_02` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(\log N)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **LeetCode-Äquivalent** | [Majority Element](https://leetcode.com/problems/majority-element/) |

## Problemstellung

Gegeben ist ein Array `nums` der Größe `n`. Geben Sie das Majority Element zurück.
Das Majority Element ist das Element, das mehr als `⌊n / 2⌋` Mal vorkommt. Sie können davon ausgehen, dass das Majority Element immer im Array existiert.
*Einschränkung:* Demonstrieren Sie, wie man dies mittels Divide and Conquer löst.

**Eingabe:** Ein Integer-Array `nums`.
**Ausgabe:** Ein Integer, der das Majority Element repräsentiert.

## Wann man es verwendet

- Als akademische Übung, um zu beweisen, dass Sie verstehen, wie man ein Array teilt und nicht-numerische boolesche oder statistische Eigenschaften zusammenführt.
- *(Hinweis: In einem echten Vorstellungsgespräch sollten Sie dies mit dem Boyer-Moore Voting (`array_05`) für $O(N)$ Zeit und $O(1)$ Platz lösen. Der Divide-and-Conquer-Ansatz wird meist explizit vom Interviewer als Folgeaufgabe verlangt.)*

## Ansatz

**1. Die Divide-and-Conquer-Logik:**
Wenn ein Array ein Majority Element besitzt, dann MUSS dieses Element – wenn wir das Array exakt in der Mitte teilen – das Majority Element von MINDESTENS EINER der beiden Hälften sein!
Überlegen Sie: Wenn ein Element global mehr als N/2 Mal vorkommt, ist es mathematisch unmöglich, dass es gleichzeitig \le N/4 Mal in der linken Hälfte UND \le N/4 Mal in der rechten Hälfte vorkommt.

**2. Der Induktionsanfang (Base Case):**
Wenn der Array-Ausschnitt die Größe 1 hat (d. h. `left == right`), dann ist dieses einzelne Element trivialerweise das "Majority"-Element seines winzigen Ausschnitts! Geben Sie es zurück.

**3. Der Rekursive Schritt (Divide):**
Finden Sie den `mid`-Punkt.
Rufen Sie rekursiv `find_majority(left, mid)` auf, um das Majority Element der linken Hälfte zu finden. Nennen wir es `left_majority`.
Rufen Sie rekursiv `find_majority(mid + 1, right)` auf, um das Majority Element der rechten Hälfte zu finden. Nennen wir es `right_majority`.

**4. Der Merge-Schritt (Conquer):**
Nun haben wir die vorgeschlagenen "Champions" aus der linken und rechten Hälfte.
- Wenn `left_majority == right_majority`: Beide Hälften stimmen überein! Dieses Element ist zweifellos das globale Majority Element. Geben Sie es zurück.
- Wenn `left_majority != right_majority`: Die beiden Hälften sind sich uneinig. Wir müssen herausfinden, welches das WAHRE globale Majority Element für den aktuellen Ausschnitt `[left...right]` ist.
  Wie? Wir iterieren einfach durch den aktuellen Ausschnitt `[left...right]` und zählen buchstäblich die Vorkommen von `left_majority` und `right_majority`!
  Geben Sie dasjenige zurück, das die höhere Anzahl aufweist.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_02: Majority Element.

Boyer-Moore: track a candidate and a counter. Walk the array;
on each new element, if the counter is zero, promote it to
candidate. Increment on a match, decrement otherwise. The
candidate at the end is the majority element if one exists.
The setup always produces a list with a majority, so the
candidate is the answer.
"""


def solve(arr, n):
    if n == 0:
        return -1
    candidate = None
    count = 0
    for value in arr:
        if count == 0:
            candidate = value
        count += 1 if value == candidate else -1
    return candidate
```

</details>

## Durchlauf

`nums = [2, 2, 1, 1, 1, 2, 2]`. N=7.

1. Teilen in `[2, 2, 1, 1]` und `[1, 2, 2]`.
2. **Linke Hälfte `[2, 2, 1, 1]`:**
   - Teilen in `[2, 2]` und `[1, 1]`.
   - `[2, 2]` gibt `2` zurück (beide Seiten stimmten überein).
   - `[1, 1]` gibt `1` zurück (beide Seiten stimmten überein).
   - Conquer `[2, 2, 1, 1]`: Champions sind `2` und `1`.
     - Zähle `2` in `[2, 2, 1, 1]`: 2.
     - Zähle `1` in `[2, 2, 1, 1]`: 2.
     - Unentschieden! (Gibt willkürlich `1` zurück, basierend auf der `>=`-Logik).
3. **Rechte Hälfte `[1, 2, 2]`:**
   - Teilen in `[1, 2]` und `[2]`.
   - `[1, 2]` gibt `2` zurück (nach Zählen von 1 vs 1, wählt willkürlich `2`).
   - `[2]` gibt `2` zurück.
   - Conquer `[1, 2, 2]`: Champions sind `2` und `2`. Stimmen überein! Gibt `2` zurück.
4. **Globaler Conquer `[2, 2, 1, 1, 1, 2, 2]`:**
   - Champions sind `1` (von links) und `2` (von rechts).
   - Zähle `1` im globalen Array: 3.
   - Zähle `2` im globalen Array: 4.
   - 4 > 3. Gibt `2` zurück.

Das Ergebnis ist `2`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(\log N)$ |

Der Rekursionsbaum hat eine Tiefe von log_2(N). Auf jeder Ebene des Baums erfordert das Zusammenführen (Merge) eine Iteration durch das Subarray, um die Vorkommen zu zählen. Die Gesamtarbeit auf einer beliebigen Ebene des Baums summiert sich exakt auf N Iterationen.
Nach dem Master-Theorem T(N) = 2T(N/2) + $O(N)$ beträgt die Zeitkomplexität exakt $O(N \log N)$.
Die Platzkomplexität beträgt $O(\log N)$ für den Rekursions-Call-Stack.

## Varianten & Optimierungen

- **Boyer-Moore Voting Algorithm:** Wie erwähnt, ist dies der optimale $O(N)$-Ansatz. Sie verwalten einen `candidate` und einen `count`. Iterieren Sie durch das Array: wenn `count == 0`, setzen Sie `candidate = num`. Wenn `num == candidate`, `count += 1`, ansonsten `count -= 1`. Da das Majority Element > N/2 Mal vorkommt, ist es mathematisch garantiert, dass es die gegenseitige Aufhebung aller anderen Elemente überdauert!

## Anwendungen in der Praxis

- **Fehlertolerante Systeme (Triple Modular Redundancy):** Wenn Sensoren in einem Flugzeug mehrere leicht widersprüchliche Messwerte senden, gruppiert der Flugcomputer die Messwerte rekursiv, um den "Mehrheitskonsens"-Wert zu finden und die korrupten Sensordaten zu verwerfen.

## Verwandte Algorithmen in cOde(n)

- **[array_05 - Boyer-Moore Voting](../arrays/array_05_boyer-moore.md)** — Die strikt überlegene $O(N)$-Methode zur Lösung genau dieses Problems.
- **[sort_01 - Merge Sort](../sorting/sort_01_merge-sort.md)** — Der klassische $O(N \log N)$-Algorithmus, dem dieses Divide-and-Conquer-Muster perfekt nachempfunden ist.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*