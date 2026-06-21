# Hamiltonian Path Existence

| | |
|---|---|
| **ID** | `graph_21` |
| **Kategorie** | graphs |
| **Komplexität (erforderlich)** | $O(V!)$ Zeit, $O(V)$ Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **GeeksForGeeks Äquivalent** | [Hamiltonian Cycle](https://www.geeksforgeeks.org/hamiltonian-cycle/) |

## Problemstellung

Gegeben ist ein ungewichteter Graph (entweder gerichtet oder ungerichtet). Bestimmen Sie, ob ein Hamiltonpfad existiert.
Ein Hamiltonpfad ist ein Pfad, der jeden einzelnen Knoten im Graphen genau einmal besucht.
(Ein Hamiltonkreis ist ein Hamiltonpfad, der zusätzlich eine Kante enthält, die den letzten Knoten wieder mit dem Startknoten verbindet).

**Eingabe:** Anzahl der Knoten `V` und eine Adjacency List `adj`.
**Ausgabe:** Ein Boolean. `True`, falls ein Hamiltonpfad existiert, andernfalls `False`.

## Wann man es verwendet

- Zur Lösung der ungewichteten Entscheidungsvariante des Travelling Salesperson Problems.
- Wie das Graph Coloring ist dies **NP-vollständig**. Da uns der *kürzeste* Pfad nicht interessiert (keine Kantengewichte), ist eine DP-Optimierung (Held-Karp) übertrieben, es sei denn, man möchte alle Pfade prüfen. Im Allgemeinen verwenden wir hierfür reines Backtracking.

## Ansatz

**1. Der Backtracking-Zustand:**
Wir führen ein Array `path[]`, das die geordnete Sequenz der besuchten Knoten speichert.
Zusätzlich führen wir ein `visited`-Set, um sicherzustellen, dass wir keinen Knoten zweimal besuchen (was die Definition eines Hamiltonpfads verletzen würde).

**2. Der rekursive Schritt:**
Unsere rekursive Funktion `backtrack(curr, path_length)` versucht, den Pfad zu erweitern.
Wenn `path_length == V`, haben wir es geschafft! Wir haben erfolgreich jeden Knoten genau einmal berührt! Gib `True` zurück.
Andernfalls iterieren wir über alle `neighbors` von `curr`.
Wenn ein `neighbor` NICHT in `visited` enthalten ist:
- Füge ihn zu `visited` hinzu und hänge ihn an `path` an.
- Rekursion: `if backtrack(neighbor, path_length + 1) == True: return True`.
- Backtrack: Entferne ihn aus `visited` und führe ein `pop` auf `path` aus.

**3. Die globale Schleife:**
Da wir nicht wissen, von *welchem* Knoten aus der Hamiltonpfad starten könnte, müssen wir unsere Backtracking-Funktion in eine globale Schleife einbetten, die versucht, den Pfad bei `0` zu starten, dann bei `1`, dann bei `2` usw., bis einer erfolgreich ist.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_21: Hamiltonian Path Existence.

DFS from 0. Stop at n-1 when count == n.
"""


def solve(n, edges):
    if n <= 1:
        return n == 1
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    visited = [False] * n
    visited[0] = True

    def dfs(u, count):
        if count == n:
            return u == n - 1
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if dfs(v, count + 1):
                    return True
                visited[v] = False
        return False

    return dfs(0, 1)
```

</details>

## Durchlauf

`V = 4`. `adj = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2]}`. (Ein Quadrat `0-1-3-2-0`).

1. **Start `0`:** `visited={0}`, `path=[0]`.
   - `backtrack(0, 1)`:
     - Probiere Nachbar `1`. `visited={0,1}`.
     - `backtrack(1, 2)`:
       - Probiere Nachbar `3`. `visited={0,1,3}`.
       - `backtrack(3, 3)`:
         - Probiere Nachbar `2`. `visited={0,1,3,2}`.
         - `backtrack(2, 4)`:
           - `length == 4 == V`. RETURN `True`!
2. Erfolg wird nach oben weitergegeben. Der Pfad ist `[0, 1, 3, 2]`. ✓

*Hinweis: Wenn wir auf einen Hamiltonkreis prüfen wollten, würden wir ganz am Ende, wenn `length == V`, eine zusätzliche Prüfung hinzufügen: `if path[0] in adj[curr]: return True`.*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V)$ | $O(V)$ |
| **Durchschnittlicher Fall** | $O(V!)$ | $O(V)$ |
| **Schlechtester Fall** | $O(V!)$ | $O(V)$ |

Im schlimmsten Fall (einem sehr dichten Graphen, in dem KEIN Hamiltonpfad existiert) untersucht der Algorithmus jede einzelne gültige Permutation der Knoten, bevor er fehlschlägt. Die Anzahl der Permutationen von V Knoten ist V!. Die Zeitkomplexität ist mathematisch durch $O(V!)$ begrenzt.
Die Platzkomplexität beträgt strikt $O(V)$ für das `visited`-Set, das `path`-Array und die maximale Tiefe des Rekursions-Stacks.

## Varianten & Optimierungen

- **Satz von Dirac (Mathematische Abkürzung):** Wenn der Graph einfach ist und V \ge 3 Knoten besitzt, und JEDER einzelne Knoten einen Grad \ge \frac{V}{2} aufweist, dann ist mathematisch garantiert, dass der Graph einen Hamiltonkreis enthält! Man muss nicht einmal einen Algorithmus ausführen, um `True` zu erhalten!
- **Held-Karp DP:** Sie können exakt dasselbe DP-Bitmasking wie beim TSP (`graph_20`) anwenden. `dp(mask, curr)` gibt einen Boolean zurück. Der Übergang lautet `dp(mask, curr) = ANY(dp(mask | (1 << nxt), nxt))`. Dies löst das Hamiltonpfad-Problem in $O(V^2 2^V)$ Zeit anstelle von $O(V!)$, wodurch V=20 in Millisekunden lösbar wird!

## Anwendungen in der Praxis

- **Springerproblem (Knight's Tour):** Kann ein Schachspringer jedes Feld auf einem 8 x 8 Schachbrett genau einmal besuchen? Dies ist exakt das Hamiltonpfad-Problem angewendet auf einen Graphen mit 64 Knoten, bei dem die Kanten gültige L-förmige Sprünge darstellen!

## Verwandte Algorithmen in cOde(n)

- **[graph_20 - Travelling Salesperson](graph_20_travelling-salesman-held-karp-dp.md)** — Die gewichtete (Optimierungs-) Variante genau dieses Problems.
- **[graph_19 - M-Coloring Problem](graph_19_m-coloring-problem.md)** — Ein weiterer klassischer NP-vollständiger Graph-Algorithmus, der rein durch Backtracking lösbar ist.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*