# Programming in Python Language

This repository contains a collection of laboratory assignments and scripts developed for the **"Programming in Python Language"** course. The primary focus of this codebase is to demonstrate core Python programming concepts, algorithm implementation, standard library usage, and integration with external packages for data processing.

## Project Overview

The repository is organized into progressive modules, covering fundamental syntax through to more complex algorithmic problems and file manipulation.

* **Lab 1: Fundamentals & Control Flow**: Introduction to Python syntax, basic input/output operations, function definitions, and time measurement modules.
* **Lab 2: System Operations & Multimedia**: Interaction with the operating system (file system traversal) using the `os` module, and procedural image generation using **NumPy** and **Pillow (PIL)**.
* **Lab 3: Text Processing & File I/O**: Implementation of text filters, string manipulation techniques, and robust file handling (reading/writing) to process raw data.
* **Lab 4: Algorithms & Mathematical Logic**: Development of scripts for solving mathematical problems, including quadratic equations with error handling and complex matrix operations (e.g., recursive determinant calculation).

## Technologies

* **Language**: Python 3.x
* **Standard Libraries**: `os`, `math`, `random`, `string`, `time`
* **External Libraries**: `NumPy`, `Pillow`
* **IDE**: PyCharm / Visual Studio Code

## Repository Structure

The repository is structured by laboratory sessions, each focusing on specific programming concepts.

```text
├── Lab1/
│   ├── lab1_1.py            # Basic syntax, functions, and timing
│   └── ...                  # Introductory exercises
├── Lab2/
│   ├── Lab2_1.py            # System file operations (os directory listing)
│   ├── Generate_jpg.py      # Image generation using NumPy arrays & PIL
│   └── ...                  # Multimedia processing scripts
├── Lab3/
│   ├── lab3_1_1.py          # Text filtering and file manipulation logic
│   ├── lab3.txt             # Sample text data for processing
│   └── ...                  # String operation exercises
├── Lab4/
│   ├── lab4_1.py            # Quadratic equation solver with Exception handling
│   ├── lab4_6.py            # Recursive matrix determinant algorithm
│   └── ...                  # Mathematical logic implementation
├── .gitignore               # Standard Python exclusion rules
├── requirements.txt         # List of external dependencies
└── README.md                # Project documentation
```

## Setup and Installation

To set up the development environment, ensure you have Python 3 installed.

1. Clone the repository:

```Bash
git clone [https://github.com/BeneNat/python-programming-labs.git](https://github.com/BeneNat/python-programming-labs.git)
cd python-programming-labs
```

2. (Optional) Create a virtual environment:

```Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies: Required for Lab 2 (Image Processing).

```Bash
pip install -r requirements.txt
```

4. Run a script:

```Bash
# Example: Run the matrix determinant script
python Lab4/lab4_6.py
```

## Authors and Context

* **Author:** Filip Żurek
* **Institution:** AGH University of Krakow
* **Faculty:** Faculty of Computer Science, Electronics and Telecommunications
* **Field of Study:** Electronics and Telecommunications
* **Course:** Programming in Python Language

## License

This software is distributed under the MIT License. Refer to the LICENSE file for the full text.

---
*AGH University of Krakow - Programming in Python Language 2025*