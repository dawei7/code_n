# Formale mathematische Spezifikation: Linear Search

## 1. Definitionen und Notation

Sei $A$ ein Array (oder eine Sequenz) der Länge $N \in \mathbb{N}_0$, wobei $N$ die Kardinalität der Indexmenge $I = \{0, 1, \dots, N-1\}$ bezeichnet. Die Elemente des Arrays stammen aus einer Menge $\mathcal{D}$ (der Datendomäne), sodass $A: I \to \mathcal{D}$ gilt.

Wir definieren Folgendes:
*   **Eingabe:** Eine Sequenz $A = (a_0, a_1, \dots, a_{N-1})$ und ein Zielwert $\tau \in \mathcal{D}$.
*   **Ausgabe:** Ein Index $k \in I \cup \{-1\}$, wobei $k$ durch die folgende Abbildung definiert ist:
    $$f(A, \tau) = \begin{cases} \min \{i \in I \mid a_i = \tau\} & \text{falls } \exists i \in I : a_i = \tau \\ -1 & \text{sonst} \end{cases}$$
*   **Zustandsraum:** Der Algorithmus verwaltet eine Zustandsvariable $i \in \{0, 1, \dots, N\}$, die den aktuell untersuchten Index repräsentiert.

## 2. Algebraische Charakterisierung

Die Korrektheit des Linear Search Algorithmus wird durch eine Schleifeninvariante begründet. Sei $i$ der Schleifenzähler.

**Schleifeninvariante:** Zu Beginn jeder Iteration $i$ gilt für alle $j$ mit $0 \le j < i$, dass $a_j \neq \tau$.

*   **Initialisierung:** Vor der ersten Iteration ist $i = 0$. Die Menge $\{j \in \mathbb{N} \mid 0 \le j < 0\}$ ist leer; daher ist die Bedingung trivialerweise erfüllt.
*   **Aufrechterhaltung:** Angenommen, die Invariante gilt für $i$. In der aktuellen Iteration untersuchen wir $a_i$.
    *   Falls $a_i = \tau$, terminiert der Algorithmus und gibt $i$ zurück, was der kleinste Index ist, der die Bedingung erfüllt.
    *   Falls $a_i \neq \tau$, gilt die Invariante für $i+1$, da die Menge der geprüften Indizes nun $\{0, \dots, i\}$ umfasst, für die alle $a_j \neq \tau$ gilt.
*   **Terminierung:** Die Schleife terminiert, wenn $i = N$ (Fehlschlag) oder wenn $a_i = \tau$ (Erfolg). Wenn $i = N$, impliziert die Invariante $\forall j \in I, a_j \neq \tau$, was den Rückgabewert $-1$ rechtfertigt.

Der Algorithmus kann als Komposition einer Suchfunktion über der Indexmenge $I$ ausgedrückt werden:
$$\text{Search}(A, \tau) = \text{if } (\exists i \in I : a_i = \tau) \text{ then } \text{argmin}_{i \in I} \{i \mid a_i = \tau\} \text{ else } -1$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität $T(N)$ wird durch die Anzahl der durchgeführten Vergleiche bestimmt. Sei $c$ die Kosten eines einzelnen Vergleichs $a_i = \tau$.

*   **Schlechtester Fall:** Tritt ein, wenn $\tau \notin A$ oder $\tau = a_{N-1}$. Der Algorithmus führt $N$ Vergleiche durch.
    $$T_{worst}(N) = \sum_{i=0}^{N-1} c = c \cdot N \implies O(N)$$
*   **Bestfall:** Tritt ein, wenn $\tau = a_0$. Der Algorithmus führt genau 1 Vergleich durch.
    $$T_{best}(N) = c \implies \Omega(1)$$
*   **Durchschnittlicher Fall:** Unter der Annahme, dass $\tau$ in $A$ an einem gleichverteilten zufälligen Index $k \in \{0, \dots, N-1\}$ vorhanden ist, ergibt sich die erwartete Anzahl an Vergleichen $E[T]$ zu:
    $$E[T] = \frac{1}{N} \sum_{i=1}^{N} i = \frac{1}{N} \frac{N(N+1)}{2} = \frac{N+1}{2} \implies \Theta(N)$$

### Platzkomplexität
Der Algorithmus benötigt eine konstante Menge an zusätzlichem Speicherplatz, um den Schleifenindex $i$ und die Eingabereferenzen zu speichern.
*   Sei $S_{aux}$ der für Variablen benötigte Speicherplatz. Da $i$ ein skalarer Integer ist, gilt $S_{aux} = O(1)$.
*   Das Eingabe-Array $A$ belegt $O(N)$ Speicherplatz, aber der Algorithmus arbeitet in-place und benötigt keine zusätzlichen Datenstrukturen, die proportional zur Eingabegröße sind.
*   Daher beträgt die zusätzliche Platzkomplexität $O(1)$.