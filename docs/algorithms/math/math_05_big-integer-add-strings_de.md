# Add Strings (Big Integer Addition)

| | |
|---|---|
| **ID** | `math_05` |
| **Kategorie** | math |
| **Komplexität (erforderlich)** | $O(max(N, M)$) Zeit, $O(max(N, M)$) Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Add Strings](https://leetcode.com/problems/add-strings/) |

## Problemstellung

Gegeben sind zwei nicht-negative Ganzzahlen `num1` und `num2`, die als Strings repräsentiert werden.
Geben Sie die Summe von `num1` und `num2` als String zurück.
Sie dürfen keine integrierte BigInteger-Bibliothek verwenden oder die Eingaben direkt in Ganzzahlen umwandeln (z. B. ist `return str(int(num1) + int(num2))` nicht erlaubt).

**Eingabe:** Zwei Strings `num1` und `num2`.
**Ausgabe:** Ein String, der deren Summe repräsentiert.

## Wann man es verwendet

- Um mathematische Überlaufgrenzen in Sprachen mit strikten 32-Bit- oder 64-Bit-Ganzzahlbegrenzungen (wie C++, Java oder Go) zu handhaben.
- Eine äußerst häufige Aufwärm- oder Screening-Frage in Vorstellungsgesprächen, um grundlegende Array-Iteration und den Umgang mit Randfällen zu testen.

## Ansatz

**1. Die Logik der schriftlichen Addition:**
Wir müssen simulieren, wie wir Zahlen auf Papier addieren: vertikal, beginnend bei der rechtesten Ziffer (Einerstelle), nach links wandernd und jeden Übertrag zur nächsten Spalte mitnehmend.

**2. Zwei Pointer und ein Übertrag:**
Setzen Sie zwei Pointer `p1` und `p2` auf die letzten Indizes von `num1` und `num2`.
Initialisieren Sie einen `carry = 0`.
Solange einer der Pointer $\ge 0$ ist oder der `carry` $> 0$ ist:
1. Extrahieren Sie die Ziffer aus `num1[p1]`. (Wenn `p1 < 0`, behandeln Sie sie als `0`).
2. Extrahieren Sie die Ziffer aus `num2[p2]`. (Wenn `p2 < 0`, behandeln Sie sie als `0`).
3. Addieren Sie diese: `total = digit1 + digit2 + carry`.
4. Die Ziffer, die an unser Ergebnis angehängt wird, ist `total % 10`.
5. Der neue Übertrag für die nächste Schleife ist `total // 10`.
6. Dekrementieren Sie beide Pointer.

**3. String-Konstruktion:**
Da Strings in den meisten Sprachen unveränderlich (immutable) sind, benötigt das ständige Voranstellen an einen String `result = char + result` eine Zeitkomplexität von $O(N)$ pro Zeichen, was den Algorithmus auf $O(N^2)$ verschlechtert!
Hängen Sie die Zeichen immer an ein Array/eine Liste an und führen Sie am Ende `reverse()` auf dem Array aus und `join()` es, um eine Zeitkomplexität von $O(N)$ beizubehalten.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for math_05: Big Integer Add (Strings).

Add two non-negative integers given as digit strings.
"""


def solve(a, b):
    if not a:
        return b
    if not b:
        return a
    a_rev = a[::-1]
    b_rev = b[::-1]
    n = max(len(a_rev), len(b_rev))
    carry = 0
    out = []
    for i in range(n):
        da = int(a_rev[i]) if i < len(a_rev) else 0
        db = int(b_rev[i]) if i < len(b_rev) else 0
        s = da + db + carry
        out.append(str(s % 10))
        carry = s // 10
    if carry:
        out.append(str(carry))
    return "".join(reversed(out))
```

</details>

## Durchlauf

`num1 = "456"`, `num2 = "77"`.
`p1 = 2 ('6')`, `p2 = 1 ('7')`. `carry = 0`.

1. `digit1 = 6`, `digit2 = 7`.
   - `sum = 6 + 7 + 0 = 13`.
   - `curr = 13 % 10 = 3`. `carry = 1`.
   - `res = ['3']`.
   - `p1 = 1`, `p2 = 0`.
2. `digit1 = 5`, `digit2 = 7`.
   - `sum = 5 + 7 + 1 = 13`.
   - `curr = 13 % 10 = 3`. `carry = 1`.
   - `res = ['3', '3']`.
   - `p1 = 0`, `p2 = -1`.
3. `digit1 = 4`, `digit2 = 0` (Außerhalb der Grenzen!).
   - `sum = 4 + 0 + 1 = 5`.
   - `curr = 5 % 10 = 5`. `carry = 0`.
   - `res = ['3', '3', '5']`.
   - `p1 = -1`, `p2 = -2`.
4. `p1 < 0` UND `p2 < 0` UND `carry == 0`. Die Schleife endet.

`res` umkehren: `['5', '3', '3']`.
`join`: `"533"`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(\max(N, M)$) | $O(\max(N, M)$) |
| **Durchschnittlicher Fall** | $O(\max(N, M)$) | $O(\max(N, M)$) |
| **Schlechtester Fall** | $O(\max(N, M)$) | $O(\max(N, M)$) |

Seien N und M die Längen der beiden Strings.
Wir iterieren genau so oft, wie die Länge des längsten Strings vorgibt, plus maximal eine zusätzliche Iteration für einen finalen Übertrag. Die Zeitkomplexität ist strikt linear $O(\max(N, M)$).
Die Platzkomplexität beträgt $O(\max(N, M)$), um das Ergebnis-Array der Zeichen vor dem Zusammenfügen zu speichern.

## Varianten & Optimierungen

- **Multiply Strings:** Eine schwierigere Variante! Sie erstellen ein Ergebnis-Array der Größe `N + M`, das mit Nullen initialisiert ist. Sie führen eine verschachtelte Schleife aus, die jede Ziffer in `num1` mit jeder Ziffer in `num2` multipliziert. Das Produkt von `num1[i]` und `num2[j]` addiert seinen Wert IMMER zu `result[i + j + 1]` und seinen Übertrag zu `result[i + j]`.
- **Add Binary:** Der exakt gleiche Algorithmus, aber anstelle von `% 10` und `// 10` verwenden Sie `% 2` und `// 2`.

## Anwendungen in der Praxis

- **Arithmetik mit beliebiger Genauigkeit:** Standardimplementierung in Standardbibliotheken (wie Javas `BigInteger` oder C++ GNU MP Bibliothek), um Zahlen zu verarbeiten, die die physischen CPU-Registergrenzen überschreiten.

## Verwandte Algorithmen in cOde(n)

- **[math_04 - Karatsuba Multiplication](math_04_karatsuba-multiplication.md)** — Der fortgeschrittene Algorithmus zur extrem schnellen Multiplikation großer Ganzzahlen, der intern auf diesem Additionsalgorithmus basiert.
- **[linked_list_03 - Add Two Numbers](../linked_list/ll_03_add-two-numbers.md)** — Die exakt gleiche Logik, jedoch werden die Ziffern als Knoten in einer Linked List anstatt als Zeichen in einem String gespeichert.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*