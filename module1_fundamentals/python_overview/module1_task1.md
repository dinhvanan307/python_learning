# FUNDAMENTALS

## 1. What is coding and overview of Python Language

### What is coding?
Coding is using a programming language to make a program, website, or game, etc., that helps simplify the way users interact with laptops or connect easily with other electronic devices.

### Python Programming Language Overview for DE
**Why Python is a perfect companion for Data Engineering (DE)?**
It has three main reasons: **Vast Ecosystem**, **Speed Of Coding** (due to its easily readable syntax), and being a **Glue Language**.

* **Vast Ecosystem:** Python supports users with a wide range of libraries which are perfect for DE, such as:
    * **Pandas** (Data Manipulation)
    * **PySpark** (Big Data Processing)
    * **Airflow** (Workflow Orchestration)

* **Speed Of Coding:** Python syntax is easy to write and read.
    * *Example:* When you code an algorithm in C++ or Java, it may contain 50 lines of code, but in Python, you might only have to write 5 or 10 lines.
    * This allows you to build a pipeline faster and with less complexity.

* **Glue Language:** It can connect disconnected systems easily (APIs, Databases, Cloud Services, etc.).

---

## 2. Decomposition (Phân Chia Bài Toán)

**Meaning:** Decomposition is the process of breaking down a complex problem into smaller, sequential, and logical steps that a computer can understand and execute exactly.

### Example: Collect Data base on (E-T-L)
Dividing to 3 independent parts:

1.  **Extract (Trích xuất):** Only focus on collecting data.
2.  **Transform (Chuyển đổi):** Only focus on cleaning and fining data.
3.  **Load (Nạp):** Only focus on pushing data into storage(Data Warehouse).