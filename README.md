# Property Agency Commission System

## 📌 Overview
This project implements a Property Agency Commission System using Python and Object-Oriented Programming (OOP). The system models real-world entities such as properties, property agents, and directors, and calculates commissions earned from property sales.

The program demonstrates key OOP concepts including inheritance, encapsulation, and modular design by separating each class into individual files.

---

## 📁 Project Structure

```
project/
│
├── property.py              # Base Property class
├── commercial_property.py   # Inherits from Property
├── property_agent.py        # Handles property lists and commission
├── director.py              # Inherits from PropertyAgent
├── commission_slip.py       # Prints commission reports
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

## 📊 Program Output

The program will display:
- Commission breakdown for each property sold
- Total commission earned by each agent
- Override commission earned by each director
- Total income for each director

---

## 🧠 OOP Design

- **Inheritance**
  - `CommercialProperty` extends `Property`
  - `Director` extends `PropertyAgent`

- **Encapsulation**
  - Each class manages its own data and behaviour

- **Modularity**
  - Each class is implemented in a separate file

---

## 🎯 Coursework Requirements Covered

- ✔ At least 2 directors  
- ✔ Each director has at least 3 agents  
- ✔ Each agent has:
  - ≥ 5 unsold properties  
  - 3–10 sold properties  
- ✔ Commission slip printed for all agents and directors  

---

## 👨‍💻 Author
Coursework Project – Algorithms & Data Structures
