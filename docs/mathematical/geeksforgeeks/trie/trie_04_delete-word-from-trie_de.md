# Formale mathematische Spezifikation: Wort aus Trie löschen

## 1. Definitionen und Notation

Sei $\mathcal{T} = (V, E, \Sigma, \text{root}, \text{is\_end}, \text{children})$ eine Trie-Datenstruktur, wobei:
*   $V$ die Menge der Knoten ist.
*   $\Sigma$ das endliche Alphabet von Zeichen ist.
*   $\text{root} \in V$ der designierte Wurzelknoten ist.
*   $\text{children}: V \times \Sigma \to V \cup \{\perp\}$ eine partielle Funktion ist, die einen Knoten und ein Zeichen auf einen Nachfolgerknoten abbildet.
*   $\text{is\_end}: V \to \{0, 1\}$ ein Prädikat ist, das angibt, ob ein Knoten das Ende eines gültigen Wortes repräsentiert.
*   $S = \{s_1, s_2, \dots, s_M\}$ die zu löschende Zeichenkette der Länge $M$ ist, wobei $s_i \in \Sigma$ ist.

Wir definieren den Pfad, welcher $S$ entspricht, als eine Sequenz von Knoten $(v_0, v_1, \dots, v_M)$, sodass $v_0 = \text{root}$ und $v_i = \text{children}(v_{i-1}, s_i)$ für $1 \le i \le M$ gilt. Der Algorithmus setzt die Existenz dieses Pfades voraus, sodass $\text{is\_end}(v_M) = 1$ ist.

## 2. Algebraische Charakterisierung

Der Löschvorgang wird durch eine Postorder-Traversierungsfunktion $f(v, i)$ definiert, wobei $v$ der aktuelle Knoten und $i$ der Index des verarbeiteten Zeichens in $S$ ist. Der Zustandsübergang wird durch die folgende rekursive Logik gesteuert:

**Basis:**
Für $i = M$:
$$\text{is\_end}(v_M) \leftarrow 0$$
Gib $\mathbb{1}(\text{degree}(v_M) = 0)$ zurück, wobei $\text{degree}(v) = |\{c \in \Sigma \mid \text{children}(v, c) \neq \perp\}|$ ist.

**Rekursionsschritt:**
Für $0 \le i < M$:
Sei $v_{i+1} = \text{children}(v_i, s_{i+1})$.
Sei $\text{delete\_child} = f(v_{i+1}, i+1)$.
Falls $\text{delete\_child} = 1$:
1. $\text{children}(v_i, s_{i+1}) \leftarrow \perp$
2. Gib $\mathbb{1}(\text{degree}(v_i) = 0 \land \text{is\_end}(v_i) = 0)$ zurück.
Andernfalls:
Gib $0$ zurück.

**Korrektheitsinvariante:**
Ein Knoten $v$ wird genau dann aus $V$ entfernt, wenn gilt:
$$\forall v' \in \text{descendants}(v) \cup \{v\}, \text{is\_end}(v') = 0 \land \text{degree}(v') = 0$$
Dies stellt sicher, dass das Löschen von $v$ nicht die Integrität eines Pfades verletzt, der ein Wort $W \in \mathcal{L}(\mathcal{T}) \setminus \{S\}$ repräsentiert.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus führt eine Tiefensuche (DFS) entlang des Pfades der Länge $M$ durch. 
Sei $T(M)$ die Zeitkomplexität. Die Rekursionsgleichung lautet:
$$T(M) = T(M-1) + \Theta(1)$$
wobei $\Theta(1)$ für die Wörterbuch-Suchoperation, die Aktualisierung des `is_end`-Flags und das eventuelle Löschen eines Zeigers auf ein Kindelement steht. Unter Berücksichtigung des Basisfalls $T(0) = \Theta(1)$ ergibt sich die geschlossene Form:
$$T(M) = \sum_{i=1}^{M} \Theta(1) = \Theta(M)$$
Die Zeitkomplexität beträgt somit $O(M)$, da wir jeden Knoten auf dem Pfad genau einmal besuchen und bei jedem Schritt Operationen mit konstantem Zeitaufwand ausführen.

### Platzkomplexität
Die Platzkomplexität wird durch den für die rekursiven Aufrufe erforderlichen Hilfs-Stack-Speicher dominiert.
*   **Hilffsspeicher:** Die Rekursionstiefe beträgt exakt $M$, was der Länge der Zeichenkette $S$ entspricht. Jeder Stack-Frame verbraucht $O(1)$ Speicherplatz. Somit beträgt der Hilfsspeicher $O(M)$.
*   **Gesamtspeicher:** Der Algorithmus modifiziert den Trie in-place. Die gesamte Platzkomplexität beträgt im schlechtesten Fall (wenn der gesamte Pfad gelöscht wird) $O(M)$, was die Reduzierung der Knotenzahl $|V|$ darstellt. Da keine zusätzlichen Datenstrukturen proportional zur Eingabegröße erstellt werden, bleibt die Platzkomplexität bei $O(M)$.
