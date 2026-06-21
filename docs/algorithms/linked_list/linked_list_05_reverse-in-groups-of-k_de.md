# Reverse Nodes in k-Group

| | |
|---|---|
| **ID** | `linked_list_05` |
| **Kategorie** | linked_list |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) |

## Problemstellung

Gegeben ist der `head` einer Linked List. Die Knoten der Liste sollen in Gruppen der Größe `k` umgekehrt werden; geben Sie die modifizierte Liste zurück.
`k` ist eine positive Ganzzahl und kleiner oder gleich der Länge der Linked List.
Wenn die Anzahl der Knoten kein Vielfaches von `k` ist, sollen die verbleibenden Knoten am Ende in ihrer ursprünglichen Reihenfolge belassen werden.

Sie dürfen die Werte in den Knoten der Liste nicht verändern, nur die Knoten selbst dürfen umgehängt werden. Sie müssen das Problem mit $O(1)$ zusätzlichem Speicherplatz lösen.

**Eingabe:** Ein Node `head` einer einfach verketteten Liste und eine Ganzzahl `k`.
**Ausgabe:** Ein Node `head`, der den Anfang der modifizierten Liste repräsentiert.

**Beispiel 1:**
`head = [1, 2, 3, 4, 5]`, `k = 2`
Ausgabe: `[2, 1, 4, 3, 5]`. (1 und 2 tauschen, 3 und 4 tauschen, 5 bleibt unverändert).

**Beispiel 2:**
`head = [1, 2, 3, 4, 5]`, `k = 3`
Ausgabe: `[3, 2, 1, 4, 5]`. (1, 2 und 3 werden umgekehrt, 4 und 5 bleiben unverändert).

## Wann man es verwendet

- Um absolute Beherrschung der Pointer-Manipulation bei Linked Lists zu beweisen. Dies ist eines der konzeptionell anspruchsvollsten Pointer-Probleme, denen Sie in einem Vorstellungsgespräch begegnen können.

## Ansatz

Dieses Problem kombiniert das **Dummy Node**-Muster mit dem **In-Place Reversal**-Muster.

Wir verarbeiten die Liste in Blöcken der Größe `k`.
Für jeden Block:
1. Überprüfen Sie, ob tatsächlich noch `k` Knoten vorhanden sind. Wenn nicht, sind wir fertig! Brechen Sie die Schleife ab.
2. Wenn `k` Knoten vorhanden sind, markieren wir den Anfang und das Ende dieses Blocks.
3. Wir führen eine standardmäßige $O(1)$ Pointer-Umkehrung (aus `linked_list_01`) *strikt* auf diesem Block durch.
4. **Der schwierige Teil (Verknüpfung):** Nach dem Umkehren eines Blocks ist der ursprüngliche "Anfang" des Blocks nun das "Ende" des umgekehrten Blocks! Und das ursprüngliche "Ende" des Blocks ist nun der neue "Anfang"! Wir müssen manuell das Ende des vorherigen Blocks mit diesem neuen Anfang verknüpfen und unser neues Ende mit dem nachfolgenden, noch nicht umgekehrten Segment verbinden.

**Benötigte Pointer:**
- `dummy`: Um den absoluten Anfang der Liste sauber zu handhaben.
- `prev_group_tail`: Zeigt auf den Knoten unmittelbar vor dem aktuellen Block. Wir benötigen diesen, um den umgekehrten Block wieder an die Hauptliste anzuhängen.
- `kth`: Ein Läufer, um das Ende des aktuellen Blocks zu finden.
- `prev`, `curr`, `next_node`: Das Standard-Trio für die Umkehrung.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for linked_list_05: Reverse in Groups of K.

Walk the list in chunks of k; reverse each chunk. The trick is
to thread the previous chunk's tail to the current chunk's
new head. Return (new_values, new_next, new_head).
"""


def solve(values, next, head, k, n):
    if n == 0 or head == -1 or k <= 1:
        return list(values), list(next), head
    new_next = list(next)
    prev_tail_new = -1
    cur = head
    new_head = -1
    while cur != -1:
        chunk = []
        c = cur
        for _ in range(k):
            if c == -1:
                break
            chunk.append(c)
            c = new_next[c]
        if len(chunk) < k:
            if prev_tail_new != -1:
                new_next[prev_tail_new] = chunk[0]
            break
        for i in range(len(chunk) - 1, 0, -1):
            new_next[chunk[i]] = chunk[i - 1]
        new_next[chunk[0]] = c
        if prev_tail_new != -1:
            new_next[prev_tail_new] = chunk[-1]
        else:
            new_head = chunk[-1]
        prev_tail_new = chunk[0]
        cur = c
    if new_head == -1:
        new_head = head
    return list(values), new_next, new_head
```

</details>

## Durchlauf

`head = [1, 2, 3]`, `k = 2`.
`dummy -> 1 -> 2 -> 3`. `prev_group_tail = dummy`.

**Gruppe 1:**
- `get_kth_node(dummy, 2)` gibt `Node(2)` zurück.
- `kth` ist nicht None. `next_group_head = Node(3)`.
- Setup für Umkehrung: `prev = Node(3)`, `curr = Node(1)`.
- Umkehrschleife (bis `curr == Node(3)`):
  - `curr = 1`: `next_node = 2`. `1.next = 3`. `prev = 1`. `curr = 2`.
  - `curr = 2`: `next_node = 3`. `2.next = 1`. `prev = 2`. `curr = 3`.
- Schleife endet. Umgekehrte Gruppe: `2 -> 1 -> 3`.
- Verknüpfung:
  - `tmp = dummy.next` (was `Node(1)` ist).
  - `dummy.next = prev` (was `Node(2)` ist).
  - `prev_group_tail = tmp` (bewegt sich zu `Node(1)`).
Die Liste ist nun: `dummy -> 2 -> 1 -> 3`.

**Gruppe 2:**
- `get_kth_node(Node(1), 2)` gibt `None` zurück (nur noch 1 Knoten übrig).
- Schleife abbrechen!

Rückgabe von `dummy.next`: `[2, 1, 3]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Wir durchlaufen die Liste einmal, um die `kth`-Knoten zu finden, und ein zweites Mal, um die eigentlichen Pointer-Umkehrungen durchzuführen. Das bedeutet, wir verarbeiten jeden Knoten genau zweimal. Die Zeitkomplexität ist strikt $O(N)$.
Die Platzkomplexität ist strikt $O(1)$, da wir unabhängig von der Listen- oder Blockgröße nur eine feste Anzahl an Pointern verwalten.

## Varianten & Optimierungen

- **Rekursive $O(N)$ Platzkomplexität:** Sie können dies leicht rekursiv lösen, indem Sie die ersten `k` Knoten nehmen, den Rest der Liste an die rekursive Funktion übergeben und den zurückgegebenen `head` an Ihren umgekehrten Block anhängen. LeetCode verbietet dies jedoch strikt in der Problembeschreibung und erzwingt $O(1)$ Platz.

## Anwendungen in der Praxis

- **Netzwerk-Paket-Reassemblierung:** Beim Empfang von gestückelten Datenströmen über UDP können Pakete in umgekehrter Blockreihenfolge ankommen, die eine kontinuierliche, blockweise Zusammenfügung erfordern, bevor sie an die Anwendungsschicht weitergegeben werden.

## Verwandte Algorithmen in cOde(n)

- **[linked_list_01 - Reverse Linked List](ll_01_reverse-linked-list.md)** — Die absolute Voraussetzung für diesen Algorithmus.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Seiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*