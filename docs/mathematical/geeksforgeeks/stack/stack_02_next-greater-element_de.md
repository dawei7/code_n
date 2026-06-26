# Formale mathematische Spezifikation: Next Greater Element (Monotoner Stack)

## 1. Definitionen und Notation

Sei $A = \langle a_0, a_1, \dots, a_{n-1} \rangle$ eine Sequenz von $n$ ganzen Zahlen, wobei $a_i \in \mathbb{Z}$. Wir definieren die Indexmenge als $I = \{0, 1, \dots, n-1\}$.

Die **Next Greater Element (NGE)**-Funktion, $f: I \to \mathbb{Z} \cup \{-1\}$, ist wie folgt definiert:
$$f(i) = \begin{cases} a_j & \text{where } j = \min \{k \in I \mid k > i \land a_k > a_i\} \\ -1 & \text{if } \{k \in I \mid k > i \land a_k > a_i\} = \emptyset \end{cases}$$

Der Algorithmus verwaltet einen Zustand, der durch einen Stack $S$ repräsentiert wird, welcher eine geordnete Sequenz von Indizes $\langle s_0, s_1, \dots, s_m \rangle$ ist, sodass $s_m$ das oberste Element (Top) des Stacks ist. Der Stack erfüllt die **Monotonie-Invariante**:
$$\forall j \in \{0, \dots, m-1\}, \quad a_{s_j} \ge a_{s_{j+1}}$$
Dies stellt sicher, dass die Werte, die den Indizes im Stack entsprechen, von unten nach oben nicht-steigend sind.

## 2. Algebraische Charakterisierung

Der Algorithmus verarbeitet die Sequenz $A$ in einem einzigen Durchlauf. Sei $S_i$ der Zustand des Stacks nach der Verarbeitung des Index $i$. Der Übergang von $S_{i-1}$ zu $S_i$ wird durch die folgenden Operationen bestimmt:

1. **Pop-Phase:** Sei $S_{i-1} = \langle s_0, \dots, s_m \rangle$. Wir entfernen iterativ Elemente vom oberen Ende des Stacks, solange die Bedingung $a_i > a_{s_m}$ gilt. Sei $k$ die Anzahl der per `pop` entfernten Elemente. Der neue Stack $S'$ ist $\langle s_0, \dots, s_{m-k} \rangle$. Für jeden entfernten Index $s_j$ (wobei $j \in \{m-k+1, \dots, m\}$) weisen wir zu:
   $$f(s_j) = a_i$$
2. **Push-Phase:** Der aktuelle Index $i$ wird an den Stack angehängt:
   $$S_i = S' \oplus \langle i \rangle$$

**Korrektheitsinvariante:**
Bei jedem Schritt $i$ ist für alle $j \in I$, für die $j < i$ gilt und $f(j)$ noch nicht zugewiesen wurde, $j$ im Stack $S_i$ enthalten. Darüber hinaus ist für jedes $j \in S_i$ der Wert $a_j$ der Wert des am kürzesten zurückliegenden Elements links von $i$, das noch kein NGE gefunden hat. Da der Stack monoton fallend ist, ist $a_i$, falls $a_i > a_{s_m}$ gilt, das *erste* Element rechts von $s_m$, das strikt größer als $a_{s_m}$ ist, was die Definition von $f(s_m)$ erfüllt.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Wir definieren die gesamte Zeitkomplexität $T(n)$ als die Summe der Kosten aller Operationen. Sei $P$ die Gesamtzahl der `push`-Operationen und $Q$ die Gesamtzahl der `pop`-Operationen.

*   Jeder Index $i \in \{0, \dots, n-1\}$ wird genau einmal auf den Stack gelegt. Somit gilt $P = n$.
*   Da ein Index nur per `pop` entfernt werden kann, wenn er zuvor per `push` hinzugefügt wurde, ist die Gesamtzahl der `pop`-Operationen durch die Anzahl der `push`-Operationen beschränkt: $Q \le P = n$.
*   Die in jeder Iteration $i$ geleistete Arbeit besteht aus einer `push`- und $k_i$ `pop`-Operationen, wobei $k_i$ die Anzahl der im Schritt $i$ entfernten Elemente ist. Die gesamte Zeitkomplexität beträgt:
    $$T(n) = \sum_{i=0}^{n-1} (1 + k_i) = n + \sum_{i=0}^{n-1} k_i$$
    Da $\sum k_i = Q \le n$ gilt, erhalten wir $T(n) \le 2n$. Folglich gilt $T(n) = O(n)$.

### Platzkomplexität
Die Platzkomplexität $S(n)$ wird durch den für den Stack und das Ergebnis-Array benötigten Hilfsspeicher bestimmt.
*   Das Ergebnis-Array benötigt $O(n)$ Platz, um die $n$ Werte von $f(i)$ zu speichern.
*   Im Schlechtesten Fall (z. B. bei einer streng monoton fallenden Eingabesequenz $a_0 > a_1 > \dots > a_{n-1}$) werden bis zum Ende keine Elemente per `pop` entfernt, und der Stack wächst auf die Größe $n$ an.
*   Somit beträgt die gesamte Platzkomplexität:
    $$S(n) = O(n) + O(n) = O(n)$$