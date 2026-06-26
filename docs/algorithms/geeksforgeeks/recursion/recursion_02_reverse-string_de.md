# Reverse String (Rekursiv)

| | |
|---|---|
| **ID** | `recursion_02` |
| **Kategorie** | Rekursion |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 1/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **LeetCode-Äquivalent** | [Reverse String](https://leetcode.com/problems/reverse-string/) |

## Problemstellung

Schreiben Sie eine Funktion, die einen String umkehrt. Der Eingabestring ist als Array von Zeichen `s` gegeben.
Sie müssen dies durch eine In-Place-Modifikation des Eingabearrays erreichen.
*Einschränkung:* Sie müssen dieses Problem mittels **Rekursion** lösen. (Verwenden Sie keine `while`- oder `for`-Schleifen).

**Eingabe:** Ein Array von Zeichen `s`.
**Ausgabe:** Keine (das Array wird In-Place modifiziert).

## Wann sollte man dies verwenden?

- Ausschließlich als pädagogische Übung, um zu vermitteln, wie Variablen und Speicher über den Recursive Call Stack weitergegeben und modifiziert werden.
- Verwenden Sie dies niemals in der Produktion. Ein iterativer Two-Pointer-Ansatz benötigt $O(1)$ Platz, während dieser rekursive Ansatz $O(N)$ Platz benötigt und das Risiko eines Stack Overflow birgt!

## Ansatz

**1. Die rekursive Analogie (Two Pointers):**
Um einen String iterativ umzukehren, platzieren wir einen `left`-Pointer am Index 0 und einen `right`-Pointer am letzten Index. Wir tauschen die Zeichen an diesen beiden Pointern. Dann inkrementieren wir `left` und dekrementieren `right`. Dies führen wir so lange fort, bis `left >= right` gilt.

Wie setzen wir dies rekursiv um?
Anstatt die Pointer in einer `while`-Schleife zu aktualisieren, übergeben wir die aktualisierten Pointer einfach als Argumente an den nächsten rekursiven Funktionsaufruf!

**2. Die Struktur der rekursiven Funktion:**
Wir benötigen eine Hilfsfunktion `recurse(left, right)`.
- **Induktionsanfang (Base Case):** Wenn `left >= right`, wurden alle Paare getauscht! Die Mitte des Strings ist erreicht. Beenden Sie die Rekursion und führen Sie ein `return` aus.
- **Rekursionsschritt:**
  1. Tauschen Sie die Zeichen an `s[left]` und `s[right]`.
  2. Führen Sie den rekursiven Aufruf aus: `recurse(left + 1, right - 1)`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for recursion_02: Reverse String.

Two-pointer swap; swap s[left] and s[right] in place, recurse
on the inner substring. Stop when left >= right. O(n) time,
O(n) recursion stack space.
"""


def solve(s, n):
    chars = list(s)

    def helper(left, right):
        if left >= right:
            return
        chars[left], chars[right] = chars[right], chars[left]
        helper(left + 1, right - 1)

    helper(0, n - 1)
    return "".join(chars)
```

</details>

## Ablauf

`s = ['h', 'e', 'l', 'l', 'o']`. Länge 5.
Start: `recurse(0, 4)`.

1. **`recurse(0, 4)`**:
   - `0 >= 4` ist False.
   - Tausche `s[0]` ('h') und `s[4]` ('o').
   - Das Array ist nun: `['o', 'e', 'l', 'l', 'h']`.
   - Aufruf von `recurse(0 + 1, 4 - 1)` -> `recurse(1, 3)`.
2. **`recurse(1, 3)`**:
   - `1 >= 3` ist False.
   - Tausche `s[1]` ('e') und `s[3]` ('l').
   - Das Array ist nun: `['o', 'l', 'l', 'e', 'h']`.
   - Aufruf von `recurse(1 + 1, 3 - 1)` -> `recurse(2, 2)`.
3. **`recurse(2, 2)`**:
   - `2 >= 2` ist TRUE! Induktionsanfang erreicht!
   - `return`.
4. Der Call Stack wird abgebaut. `recurse(1, 3)` endet. `recurse(0, 4)` endet.

Finales Array: `['o', 'l', 'l', 'e', 'h']`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Die Pointer starten an den Rändern und bewegen sich bei jedem Schritt um 1 nach innen. Sie treffen sich exakt in der Mitte. Daher werden genau N/2 rekursive Aufrufe getätigt. Die Zeitkomplexität ist linear durch $O(N)$ beschränkt.
Jeder rekursive Aufruf wird auf dem Call Stack des Systems im Speicher abgelegt. Da N/2 Aufrufe gleichzeitig aktiv sind, bevor der Induktionsanfang erreicht wird, ist die Platzkomplexität strikt $O(N)$.
*(In Sprachen ohne Tail-Call Optimization führt eine Eingabe von 100.000 Zeichen sofort zum Programmabsturz durch einen Stack Overflow Error!)*

## Varianten & Optimierungen

- **Iterative Two-Pointer (`two_pointers_02`):** Indem man die Rekursion vollständig entfernt und die Tauschlogik einfach in eine `while (left < right)`-Schleife setzt, sinkt die Platzkomplexität sofort von $O(N)$ auf $O(1)$ konstanten Platz!
- **Tail-Call Optimization (TCO):** In Sprachen wie C++ oder Scheme (aber NICHT in Python oder Java) optimiert der Compiler den Call Stack vollständig weg, wenn der rekursive Aufruf die absolut letzte Anweisung in der Funktion ist. Dadurch läuft der rekursive Code in $O(1)$ Platz, genau wie eine `while`-Schleife!

## Anwendungen in der Praxis

- **Funktionale Programmiersprachen:** Reine funktionale Sprachen (wie Haskell oder Erlang) besitzen buchstäblich keine `for`- oder `while`-Schleifen! JEDE Iteration muss als Rekursion wie diese geschrieben werden, wobei man sich vollständig auf die Tail-Call Optimization des Compilers verlässt, um Speicherabstürze zu verhindern.

## Verwandte Algorithmen in cOde(n)

- **[two_pointers_02 - Valid Palindrome](../two_pointers/two_pointers_02_valid-palindrome.md)** — Verwendet exakt dieselbe Two-Pointer-Logik an den String-Rändern, jedoch iterativ.
- **[linked_list_01 - Reverse Linked List](../linked_list/ll_01_reverse-linked-list.md)** — Der iterative rekursive Ansatz angewendet auf Knoten anstelle von Array-Indizes.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*