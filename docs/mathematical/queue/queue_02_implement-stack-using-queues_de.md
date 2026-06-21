# Formale mathematische Spezifikation: Implementierung eines Stack mittels Queues

## 1. Definitionen und Notation

Sei $\mathcal{Q}$ eine FIFO (First-In, First-Out) Queue, definiert als eine geordnete Sequenz von Elementen $q = (e_1, e_2, \dots, e_n)$, wobei $e_1$ das vordere Ende (front) und $e_n$ das hintere Ende (back) ist. Wir definieren die folgenden primitiven Operationen auf $\mathcal{Q}$:
*   $\text{enqueue}(x)$: Bildet $\mathcal{Q} \to \mathcal{Q}'$ ab, sodass $\mathcal{Q}' = (e_1, \dots, e_n, x)$.
*   $\text{dequeue}()$: Bildet $\mathcal{Q} \to \mathcal{Q}'$ ab, sodass $\mathcal{Q}' = (e_2, \dots, e_n)$, und gibt $e_1$ zurück.
*   $\text{size}(\mathcal{Q}) = n$.
*   $\text{peek}(\mathcal{Q}) = e_1$.

Sei $\mathcal{S}$ ein LIFO (Last-In, First-Out) Stack, definiert als eine geordnete Sequenz $s = (a_1, a_2, \dots, a_n)$, wobei $a_n$ das oberste Element (top, das zuletzt hinzugefügte Element) ist. Wir definieren die Stack-Operationen:
*   $\text{push}(x)$: Bildet $\mathcal{S} \to \mathcal{S}'$ ab, sodass $\mathcal{S}' = (a_1, \dots, a_n, x)$.
*   $\text{pop}()$: Bildet $\mathcal{S} \to \mathcal{S}'$ ab, sodass $\mathcal{S}' = (a_1, \dots, a_{n-1})$, und gibt $a_n$ zurück.
*   $\text{top}()$: Gibt $a_n$ zurück.

Das Ziel ist es, eine Abbildung $f: \mathcal{S} \to \mathcal{Q}$ zu definieren, sodass die LIFO-Eigenschaft von $\mathcal{S}$ durch die FIFO-Operationen von $\mathcal{Q}$ gewahrt bleibt.

## 2. Algebraische Charakterisierung

Um die Stack-Invariante aufrechtzuerhalten, bei der das zuletzt mittels $\text{push}(x)$ hinzugefügte Element die vordere Position der Queue einnimmt, definieren wir den Zustandsübergang für $\text{push}(x)$ wie folgt:

Gegeben sei eine Queue $\mathcal{Q}$ der Größe $n$, sei $\mathcal{Q}_0 = (e_1, e_2, \dots, e_n)$.
1.  Führe $\text{enqueue}(x)$ aus, was zu $\mathcal{Q}_1 = (e_1, e_2, \dots, e_n, x)$ führt.
2.  Für $i = 1$ bis $n$:
    *   Sei $y = \text{dequeue}(\mathcal{Q}_i)$.
    *   Führe $\text{enqueue}(y)$ aus.
    *   $\mathcal{Q}_{i+1} = (e_2, \dots, e_n, x, e_1, \dots, e_i)$.

Nach $n$ Rotationen ist der Zustand $\mathcal{Q}_{n+1} = (x, e_1, e_2, \dots, e_n)$. 

**Invariante:** Nach Abschluss jeder $\text{push}(x)$-Operation ist die Queue $\mathcal{Q}$ eine Permutation des Stacks $\mathcal{S}$, sodass $\text{peek}(\mathcal{Q}) = \text{top}(\mathcal{S})$ gilt. Speziell gilt: Wenn $\mathcal{S} = (a_1, a_2, \dots, a_n)$, dann ist $\mathcal{Q} = (a_n, a_{n-1}, \dots, a_1)$.

Die Korrektheit der Stack-Operationen ist somit trivial:
*   $\text{top}(\mathcal{S}) \equiv \text{peek}(\mathcal{Q})$
*   $\text{pop}(\mathcal{S}) \equiv \text{dequeue}(\mathcal{Q})$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $N$ die Anzahl der aktuell im Stack befindlichen Elemente.

*   **Push-Operation:** Der Algorithmus führt eine $\text{enqueue}$-Operation gefolgt von $N$ $\text{dequeue}$- und $\text{enqueue}$-Operationen aus. Die Gesamtzahl der primitiven Queue-Operationen beträgt $1 + 2N$. Da jede primitive Operation $O(1)$ ist, ergibt sich die Zeitkomplexität zu:
    $$T_{\text{push}}(N) = \sum_{i=1}^{N} O(1) = O(N)$$
*   **Pop/Top-Operationen:** Diese Operationen bestehen jeweils aus einer einzelnen $\text{dequeue}$- bzw. $\text{peek}$-Operation.
    $$T_{\text{pop}}(N) = O(1), \quad T_{\text{top}}(N) = O(1)$$

Die Zeitkomplexität im schlechtesten Fall für eine Sequenz von $M$ Operationen, wobei $K$ davon $\text{push}$-Operationen sind, beträgt $O(M \cdot K)$, was sich für $N$ Gesamtoperationen zu $O(N^2)$ vereinfacht.

### Platzkomplexität
Der Algorithmus verwendet eine einzelne Queue, um $N$ Elemente zu speichern. Es werden keine zusätzlichen Datenstrukturen über den Speicherplatz für die Elemente selbst hinaus benötigt.
*   **Zusätzlicher Speicherplatz (Auxiliary Space):** $O(1)$ (exklusive des Speicherplatzes, der für die Speicherung der $N$ Elemente erforderlich ist).
*   **Gesamter Speicherplatz:** $O(N)$, wobei $N$ die maximale Anzahl der Elemente im Stack zu einem beliebigen Zeitpunkt ist.