# Formale mathematische Spezifikation: Längstes gemeinsames Präfix (Trie-Methode)

## 1. Definitionen und Notation

Sei $\Sigma$ ein endliches Alphabet. Sei $S = \{s_1, s_2, \dots, s_n\}$ eine Menge von $n$ Strings, wobei jedes $s_i \in \Sigma^*$ ist. Sei $M = \max_{i} |s_i|$ die Länge des längsten Strings in $S$.

Ein **Trie** ist definiert als ein gewurzelter Baum $T = (V, E, \text{root}, \text{label}, \text{is\_end})$, wobei:
*   $V$ die Menge der Knoten ist.
*   $E \subseteq V \times V$ die Menge der gerichteten Kanten ist.
*   $\text{root} \in V$ der eindeutige Startknoten ist.
*   $\text{label}: E \to \Sigma$ eine Funktion ist, die jede Kante auf ein Zeichen im Alphabet abbildet.
*   $\text{is\_end}: V \to \{0, 1\}$ ein Prädikat ist, das angibt, ob ein Knoten das Ende eines Strings $s_i \in S$ repräsentiert.

Für jeden Knoten $u \in V$ bezeichne $\text{children}(u) = \{v \in V \mid (u, v) \in E\}$ die Menge der Nachfolgerknoten. Die Größe der Kindknotenmenge wird mit $\text{deg}^+(u) = |\text{children}(u)|$ bezeichnet.

Das **Längste gemeinsame Präfix (LCP)** von $S$ ist der längste String $p \in \Sigma^*$, sodass $p$ ein Präfix von jedem $s_i \in S$ ist.

## 2. Algebraische Charakterisierung

Das LCP entspricht dem eindeutigen Pfad, der an der Wurzel beginnt und bestimmte strukturelle Einschränkungen innerhalb des Tries erfüllt. Sei $P = (v_0, v_1, \dots, v_k)$ ein Pfad in $T$, sodass $v_0 = \text{root}$ ist. Der durch diesen Pfad repräsentierte String ist $\mathcal{L}(P) = \text{label}(v_0, v_1) \cdot \text{label}(v_1, v_2) \dots \text{label}(v_{k-1}, v_k)$.

Das LCP ist die Zeichenkette $\mathcal{L}(P)$, wobei $P$ der maximale Pfad ist, der für alle $0 \le i < k$ die folgenden Bedingungen erfüllt:
1.  **Eindeutigkeit:** $\text{deg}^+(v_i) = 1$. Dies stellt sicher, dass alle Strings in $S$ an dieser Position das gleiche Zeichen teilen.
2.  **Kontinuität:** $\text{is\_end}(v_i) = 0$. Dies stellt sicher, dass kein String in $S$ vor diesem Punkt geendet hat, da ein terminierter String kein Präfix teilen kann, das länger als er selbst ist.

Formal ist das LCP die Sequenz von Kantenbeschriftungen entlang des Pfades $P$, sodass gilt:
$$k = \min \{ i \in \mathbb{N} \mid \text{deg}^+(v_i) \neq 1 \lor \text{is\_end}(v_i) = 1 \}$$
Das resultierende LCP ist die Konkatenation der Beschriftungen:
$$\text{LCP}(S) = \bigoplus_{i=0}^{k-1} \text{label}(v_i, v_{i+1})$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus besteht aus zwei unterschiedlichen Phasen:
1.  **Aufbauphase:** Wir fügen $n$ Strings in den Trie ein. Für jeden String $s_i$ durchlaufen wir höchstens $|s_i|$ Knoten. Die Gesamtzeit beträgt:
    $$T_{\text{build}} = \sum_{i=1}^{n} O(|s_i|) \le O(n \cdot M)$$
2.  **Traversierungsphase:** Wir durchlaufen den in Abschnitt 2 definierten Pfad $P$. Da die Pfadlänge $k$ durch $M$ beschränkt ist, benötigt die Traversierung $O(k) = O(M)$ Zeit.

Die Gesamtzeitkomplexität beträgt $T(n, M) = O(n \cdot M) + O(M) = O(n \cdot M)$.

### Platzkomplexität
Die Platzkomplexität wird durch die Anzahl der Knoten $|V|$ im Trie bestimmt. 
*   Im schlechtesten Fall, in dem alle Strings verschieden sind und keine gemeinsamen Präfixe teilen, beträgt die Anzahl der Knoten $\sum_{i=1}^n |s_i| + 1$.
*   Da $|s_i| \le M$ gilt, ist die obere Schranke für die Anzahl der Knoten $O(n \cdot M)$.
*   Jeder Knoten speichert eine Map der Größe von maximal $|\Sigma|$. Somit beträgt die gesamte Platzkomplexität $O(n \cdot M \cdot |\Sigma|)$. Unter der Annahme, dass $|\Sigma|$ eine Konstante ist (z. B. 26 für englische Kleinbuchstaben), beträgt die Platzkomplexität $O(n \cdot M)$.
