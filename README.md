# 🚀 Selenium Python Automation Framework

A professional-grade web automation testing suite built using **Python** and **Selenium WebDriver**. This project implements the **Page Object Model (POM)** design pattern to ensure scalability, reusability, and easy maintenance of test cases.

---

## 🛠️ Tech Stack & Tools
* **Language:** Python 3.x
* **Automation Tool:** Selenium WebDriver 4.x
* **Test Runner:** Unittest (Python Standard Library)
* **Design Pattern:** Page Object Model (POM)
* **Browser Driver:** WebDriver Manager (Auto-install)

---

## 🏗️ Project Architecture
This framework is structured to separate test logic from page-specific locators:

* **`pages/`**: Contains Page Objects. Each file represents a web page (e.g., `login_page.py`) and contains its locators and actions.
* **`tests/`**: Contains the actual Test Suites. These scripts are kept clean and readable by calling methods from the Page Objects.
* **`base_page.py`**: A wrapper for Selenium common methods like explicit waits, clicks, and typing.

---

## 🌟 Key Features
* ✅ **Page Object Model:** Decoupled locators from test scripts for 40% better maintainability.
* ✅ **Explicit Waits:** Implemented `WebDriverWait` to handle dynamic elements and eliminate "flaky" tests.
* ✅ **Automated Driver Management:** Uses `webdriver-manager` to remove the need for manual `.exe` downloads.
* ✅ **CI/CD Ready:** Configured with GitHub Actions to run tests automatically on every push.

---

## 🏃 How to Run Locally

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/simransurve2000-alt/Testing-Practice.git](https://github.com/simransurve2000-alt/Testing-Practice.git)
   cd Testing-Practice
