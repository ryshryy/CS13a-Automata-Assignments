# Automata Theory & Formal Language Projects

This repository contains implementations of automata concepts for CS13a, including an NFA validator in C and a DFA minimizer in Python.

---

## Part 1: C-Style Comment NFA Validator

A C program that implements a Nondeterministic Finite Automaton (NFA) to validate C-style block comments. It evaluates user-inputted strings to ensure they exactly start with `/*`, end with `*/`, and do not contain the closing sequence anywhere inside the comment body.

### Automata Formal Definition

* **States (Q):** `{q0, q1, q2, q3, q4}`
* **Alphabet (Σ):** `{a, *, /}` *(where 'a' is a placeholder for any character that isn't a star or slash)*
* **Start State:** `q0`
* **Final/Accept State (F):** `{q4}`

### Sample Outputs
<img width="280" height="391" alt="image" src="https://github.com/user-attachments/assets/4f4801e7-46d1-4614-af21-2d241a6f3586" />
<img width="304" height="472" alt="image" src="https://github.com/user-attachments/assets/2a255a8b-87ee-44cd-9275-94a79a22e040" />

### Prerequisites

* A C compiler (such as `gcc` via MSYS2/MinGW-w64).

### Compilation and Execution

1. Open your terminal in the project directory.
2. Compile the source code using `gcc`:

```bash
gcc main.c -o main

```


## Part 2: DFA Minimization
A Python script that automates the minimization of a Deterministic Finite Automaton (DFA). It displays the original transition table, calculates the 0-equivalence, 1-equivalence, 2-equivalence, and so on until the states are fully minimized, and then plots the new minimized transition table. The script includes examples discussed in class alongside unique custom examples.

### Prerequisites
Python 3.x installed on your system.

### Execution
Open your terminal in the project directory where the Python script is saved.

Run the file using Python (assuming the file is named dfa_minimization.py):

```bash
python dfa_minimization.py
The terminal will output the step-by-step equivalence partitions and the final minimized transition tables for all test cases.
```

### Author
Rachel Joy Pacot

_CS13a - Automata Theory & Formal Language_
