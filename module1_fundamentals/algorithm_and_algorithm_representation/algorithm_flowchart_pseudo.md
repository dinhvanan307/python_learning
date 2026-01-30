# ALGORITHM AND REPRESENTATIONS

## 1. What is an algorithm?
**Algorithms** can be understood as the correct and detailed ways to solve a problem. In Coding and Data Science, Algorithms are a set of finite, well-defined steps or instructions designed to solve or perform a computation.

> **Flow:** Input $\to$ Process (using data based on algorithms) $\to$ Output

### What makes a good algorithm? (Requirements)
1.  **Determinacy (Tính xác định):** Every step needs to be accurate and unambiguous.
2.  **Finiteness (Tính hữu hạn):** The algorithm has to terminate after a limited number of steps.
3.  **Efficiency (Tính hiệu quả):** Use resources (time, memory) in a reasonable and effective way.
4.  **Generality (Tính tổng quát):** Can be applied to different cases/inputs, not just one.

---

## 2. How to write Pseudo-code

### Definition
**Pseudo-code** is a technique used to describe distinct steps of an algorithm in plain language that helps everyone understand the logic without worrying about specific programming syntax.

### Main Constructs
* **SEQUENCE (Tuần tự):** Execute linearly from the start to the end.
* **WHILE (Vòng lặp "Trong khi"):** Check the condition at the **beginning** of a loop.
* **REPEAT - UNTIL:** Check the condition at the **bottom** of a loop.
* **FOR:** Another way of looping (usually with a counter).
* **IF-THEN-ELSE:** Two-way decision making.
* **CASE:** A generalization of IF-THEN-ELSE, used when there are multiple potential paths.

### Keywords
Use standard capitalized keywords: `START`, `END`, `INPUT`, `PRINT`, `IF...THEN...ELSE`, `WHILE`.

---

## 3. How to draw a Flowchart

### Components of Flowchart
| Shape | English Name | Vietnamese Name | Function |
| :--- | :--- | :--- | :--- |
| 🟢 (Oval) | **Oval / Terminal** | Hình Elip | Start or End of a program. |
| ▱ (Slanted) | **Parallelogram** | Hình Bình Hành | Input or Output. |
| ▭ (Rect) | **Rectangle** | Hình Chữ Nhật | Process, computation. |
| ◇ (Diamond)| **Diamond** | Hình Thoi (Kim cương)| Condition or branching (Yes/No). |
| ➡️ | **Arrow** | Mũi tên | Flowline (Direction). |

---

## 4. PRACTICE: Quadratic Equation Solver

**Problem:** Solve $ax^2 + bx + c = 0$

### Decomposition (Phân rã bài toán)
1.  **Step 1:** Input variables `a`, `b`, `c`.
2.  **Step 2:** Check condition if `a` is 0. If it is, it becomes a linear equation $bx+c=0$.
3.  **Step 3:** If `a` is not 0, calculate Delta ($d = b^2 - 4ac$).
4.  **Step 4:** Determine result based on Delta:
    * If $d < 0$: No real roots.
    * If $d = 0$: Same roots (double root) $x = -b/(2a)$.
    * If $d > 0$: Two distinct roots $x = \frac{-b \pm \sqrt{d}}{2a}$.

### Pseudo-code (Final Version)

```text
BEGIN
    INPUT a, b, c

    IF a = 0 THEN
        // Case: Linear equation bx + c = 0
        IF b = 0 THEN
            IF c = 0 THEN
                PRINT "Many roots"
            ELSE 
                PRINT "No roots"
            ENDIF
        ELSE
            x = -c / b
            PRINT x
        ENDIF
    ELSE
        // Case: Quadratic equation
        d = b*b - 4*a*c
        
        IF d < 0 THEN
            PRINT "No real roots"
        ELSE IF d = 0 THEN
            x = -b / (2 * a)
            PRINT x
        ELSE
            x1 = (-b + sqrt(d)) / (2 * a)
            x2 = (-b - sqrt(d)) / (2 * a)
            PRINT "x1 = ", x1
            PRINT "x2 = ", x2
        ENDIF
    ENDIF   