# Roksolana's Identity Verification (Age Guesser)

A Python-based CLI (Command Line Interface) game that challenges the user to guess the author's age correctly.

## Features

- **Limited Attempts:** you only have **3 lives** to guess the correct number.
- **Smart Hints:** the system tells you if your guess is too High or too low.
- **Input Validation:** the program will not crash if you type text instead of a number. it catches the error and lets you try again.
- **Win/Loss States:** clear success messages or a Game Over screen if you run out of tries.

## Prerequisites

- Python 3.x installed on your machine.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/roxaaaaa/personal_devOps.git

## 🛠 DevOps Techniques Applied

This repository serves as a practical implementation of core DevOps principles designed to ensure code quality, reliability, and automated workflows.

### 1. Continuous Integration (CI)
*   **GitHub Actions:** The project utilizes `.github/workflows` to establish an automated CI pipeline. This triggers builds and tests automatically on every push, ensuring that new changes do not break existing functionality.
*   **Automated Testing:** Using `main_test.py`, the project implements **Unit Testing**. These tests are integrated into the CI pipeline to validate code logic before any deployment occurs.

### 2. Dependency Management
*   **Reproducible Environments:** The `requirements.txt` file is used to manage Python dependencies. This ensures the application environment can be recreated identically across Development, Testing, and Production stages, which is fundamental for consistency in DevOps.

### 3. Observability & Logging
*   **Application Logging:** The inclusion of `game.log` demonstrates the implementation of active **Logging**. In a DevOps lifecycle, this is crucial for monitoring application health, debugging real-time issues, and maintaining an audit trail of system events.

### 4. Configuration Management
*   **Environment Settings:** The `setting.json` file indicates a clear separation of code from configuration. This allows the application to adapt to different environments (e.g., switching API endpoints or toggle debug modes) without modifying the core source code.

### 5. Security & Compliance
*   **Security Policy:** The `SECURITY.md` file establishes a protocol for reporting vulnerabilities, aligning with **DevSecOps** best practices for proactive security management.
*   **Standard Licensing:** The use of an **MIT LICENSE** ensures legal compliance and defines clear usage rights for open-source collaboration.

---

### 📊 DevOps Tech Stack Summary

| Layer | Tool/Technology |
| :--- | :--- |
| **Automation** | GitHub Actions (YAML) |
| **Testing Framework** | Unittest / Pytest (Python) |
| **Environment** | Pip / Requirements.txt |
| **Version Control** | Git |
| **Configuration** | JSON-based Config Management |
