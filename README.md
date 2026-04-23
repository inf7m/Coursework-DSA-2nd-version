# Property Agency Commission System

## 📌 Overview
This project implements a Property Agency Commission System using Python and Object-Oriented Programming (OOP). The system models real-world entities such as properties, property agents, and directors, and calculates commissions earned from property sales.

The program demonstrates key OOP concepts including inheritance, encapsulation, and modular design by separating each class into individual files.

---

## 📁 Project Structure

```
project/
│
├── Property.py              # Base Property class
├── CommercialProperty.py   # Inherits from Property
├── Property.py            # Handles property lists and commission
├── Director.py              # Inherits from PropertyAgent
├── CommissionSlip.py       # Prints commission reports
└── main.py                  # Entry point (creates data & runs program)
```

---

## ⚙️ Features

- Manage property information (address, valuation, type, etc.)
- Separate **unsold** and **sold** properties
- Calculate commission based on:
  - Property valuation
  - Commission rate (default 1%)
  - Agent sharing rate (default 70%)
- Director override commission from agents
- Generate commission slips with:
  - Commission per property
  - Total commission per agent
  - Override income for directors

---

## ▶️ How to Run

### 1. Requirements
- Python 3 installed

Check version:
```bash
python --version
```

---

### 2. Run the program

Navigate to the project folder and run:

```bash
python main.py
```

---
