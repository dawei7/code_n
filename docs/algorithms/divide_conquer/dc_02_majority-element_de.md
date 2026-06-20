# Mehrheitselement (Teile und herrsche)

| | |
|---|---|
| **ID** | `dc_02` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(\log N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **LeetCode-Äquivalent** | [Majority Element](https://leetcode.com/problems/majority-element/) |

## Aufgabenstellung

Gegeben sei ein Array `nums` der Größe `n`. Gib das häufigste Element zurück.
Das häufigste Element ist das Element, das mehr als `⌊n / 2⌋` Mal vorkommt. Es darf davon ausgegangen werden, dass das häufigste Element immer im Array vorhanden ist.
*Einschränkung:* Zeigen Sie, wie man diese Aufgabe mit der „Teile und herrsche“-Methode löst.

**Eingabe:** Ein Ganzzahl-Array `nums`.
**Ausgabe:** Eine Ganzzahl, die das häufigste Element darstellt.

## Wann man dies anwenden sollte

- Als akademische Übung, um zu beweisen, dass du verstehst, wie man ein Array aufteilt und nicht-numerische boolesche/statistische Eigenschaften zusammenführt.
- *(Hinweis: In einem echten Vorstellungsgespräch sollten Sie diese Aufgabe mit dem Boyer-Moore-Voting-Verfahren (`array_05`) in $O(N)$ Zeit und $O(1)$ Speicherplatz lösen. Der „Teile und herrsche“-Ansatz wird in der Regel vom Interviewer ausdrücklich als Folgeaufgabe verlangt).*

## Vorgehensweise

**1. Die „Divide-and-Conquer“-Logik:**
Wenn ein Array ein Mehrheitselement enthält, dann MUSS – wenn wir das Array perfekt in zwei Hälften teilen – genau dieses Element das Mehrheitselement von MINDESTENS EINER der beiden Hälften sein!
Denken Sie darüber nach: Wenn ein Element insgesamt mehr als N/2 Mal vorkommt, ist es mathematisch unmöglich, dass es gleichzeitig \le N/4 Mal in der linken Hälfte UND \le N/4 Mal in der rechten Hälfte vorkommt.

**2. Der Basisfall:**
Wenn der Array-Ausschnitt die Größe 1 hat (d. h. `left == right`), dann ist dieses einzelne Element trivialerweise das „häufigste“ Element seines winzigen Ausschnitts! Gib es zurück.

**3. Der rekursive Schritt (Teilen):**
Finde den Punkt `mid`.
Rufe rekursiv `find_majority(left, mid)` auf, um das Mehrheitselement der linken Hälfte zu finden. Nennen wir es `left_majority`.
Rufe rekursiv `find_majority(mid + 1, right)` auf, um das Mehrheitselement der rechten Hälfte zu finden. Nennen wir es `right_majority`.

**4. Der Zusammenführungsschritt (Conquer):**
Nun haben wir die vorgeschlagenen „Champions“ aus der linken und der rechten Hälfte.
- Wenn `left_majority == right_majority`: Beide Hälften stimmen überein! Dieses Element ist unbestreitbar die globale Mehrheit. Gib es zurück.
- Wenn `left_majority != right_majority`: Die beiden Hälften stimmen nicht überein. Wir müssen herausfinden, welches Element die WAHRE globale Mehrheit für den aktuellen Ausschnitt `[left...right]` ist.
  Wie? Wir durchlaufen einfach den aktuellen Ausschnitt `[left...right]` und zählen buchstäblich die Vorkommen von `left_majority` und `right_majority`!
  Gib dasjenige zurück, das die höhere Anzahl aufweist.

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

## Schritt-für-Schritt-Anleitung

`nums = [2, 2, 1, 1, 1, 2, 2]`. N = 7.

1. Aufteilen in `[2, 2, 1, 1]` und `[1, 2, 2]`.
2. **Linke Hälfte `[2, 2, 1, 1]`:**
   - Aufteilen in `[2, 2]` und `[1, 1]`.
   - `[2, 2]` ergibt `2` (Beide Seiten waren sich einig).
   - `[1, 1]` ergibt `1` (Beide Seiten waren sich einig).
   - Eroberung von `[2, 2, 1, 1]`: Die Sieger sind `2` und `1`.
 - Anzahl von `2` in `[2, 2, 1, 1]`: 2.
     - Anzahl `1` in `[2, 2, 1, 1]`: 2.
 - Unentschieden! (Gibt `1` willkürlich basierend auf der `>=`-Logik zurück).
3. **Rechte Hälfte `[1, 2, 2]`:**
   - Aufteilung in `[1, 2]` und `[2]`.
   - `[1, 2]` gibt `2` zurück (nach dem 1-gegen-1-Zählen wählt es willkürlich `2` aus).
   - `[2]` gibt `2` zurück.
   - Eroberung `[1, 2, 2]`: Die Champions sind `2` und `2`. Einverstanden! Gibt `2` zurück.
4. **Globale Eroberung `[2, 2, 1, 1, 1, 2, 2]`:**
   - Die Champions sind `1` (von links) und `2` (von rechts).
   - Anzahl von `1` im globalen Array: 3.
   - Anzahl von `2` im globalen Array: 4.
   - 4 > 3. Gibt `2` zurück.

Das Ergebnis ist `2`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(\log N)$ |
| **Schlechteste** | $O(N \log N)$ | $O(\log N)$ |

Der Rekursionsbaum hat eine Tiefe von log₂(N). Auf jeder Ebene des Baums erfordert das Zusammenführen eine Iteration durch das Teilarray, um die Vorkommen zu zählen. Der Gesamtaufwand auf einer bestimmten Ebene des Baums beläuft sich auf genau N Iterationen.
Nach dem Master-Theorem T(N) = 2T(N/2) + $O(N)$ beträgt die Zeitkomplexität genau $O(N \log N)$.
Die Platzkomplexität beträgt $O(\log N)$ für den Rekursionsaufrufstapel.

## Varianten & Optimierungen

- **Boyer-Moore-Voting-Algorithmus:** Wie bereits erwähnt, ist dies der $O(N)$ optimale Ansatz. Man verwaltet ein `candidate` und ein `count`. Durchlaufe das Array: Wenn `count == 0`, setze `candidate = num`. Wenn `num == candidate`, `count += 1`, sonst `count -= 1`. Da das Mehrheitselement mehr als N/2 Mal auftritt, ist es mathematisch garantiert, dass es die Streichungen aller anderen Elemente zusammen überdauert!

## Anwendungen in der Praxis

- **Fehlertolerante Systeme (Triple Modular Redundancy):** Wenn Sensoren in einem Flugzeug mehrere leicht widersprüchliche Messwerte senden, gruppiert der Flugcomputer die Messwerte rekursiv, um den „Mehrheitskonsens“-Wert zu ermitteln und die fehlerhaften Sensordaten zu verwerfen.

## Verwandte Algorithmen in cOde(n)

- **[array_05 – Boyer-Moore-Voting](../arrays/array_05_boyer-moore.md)** — Die dieser Methode $O(N)$ streng überlegene Methode zur Lösung genau dieses Problems.
- **[sort_01 – Merge-Sort](../sorting/sort_01_merge-sort.md)** — Der klassische $O(N \log N)$-Algorithmus, an dem sich dieses „Teile und herrsche“-Muster perfekt orientiert.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
