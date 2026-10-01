<div align="center">
f
# 🏦 Bank Management System

### A console-based banking simulator built with Python OOP

*Create accounts, deposit, withdraw, transfer, and track transactions — all from your terminal.*

</div>

---

## ✨ Features

| | Feature | Description |
|---|---|---|
| 🆕 | **Create Account** | Register a customer and open a Savings or Current account |
| 💰 | **Deposit Money** | Add funds to any existing account |
| 💸 | **Withdraw Money** | Withdraw funds with balance / overdraft checks |
| 🔁 | **Transfer Money** | Move funds between two accounts instantly |
| 📊 | **Check Balance** | View live account balance |
| 🧾 | **Print Statement** | Full transaction history with timestamps |
| 🔢 | **Total Accounts** | Bank-wide account count via a static method |

---

## 🏗️ Architecture

Built entirely around clean OOP design — abstraction, inheritance, encapsulation, and polymorphism all play a role.

```
                    ┌─────────────┐
                    │   Person    │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  Customer   │
                    └─────────────┘

                    ┌─────────────┐
                    │  Account    │  (Abstract Base Class)
                    │  ABC        │
                    └──────┬──────┘
                ┌──────────┴──────────┐
                │                     │
        ┌───────▼────────┐   ┌────────▼────────┐
        │ Savingsaccount  │   │ Currentaccount  │
        │ + interest_rate │   │ + overdraft     │
        └─────────────────┘   └─────────────────┘

                    ┌─────────────┐
                    │    Bank     │  (manages customers & accounts)
                    └─────────────┘
```

<details>
<summary>📦 <b>Class Reference</b> (click to expand)</summary>

| Class | Role |
|---|---|
| `Person` | Base class — name, age, address |
| `Customer` | Inherits `Person`, adds `customer_id` |
| `Account` (ABC) | Abstract base — balance, transactions, total account counter |
| `Savingsaccount` | 4% interest, standard withdrawal rules |
| `Currentaccount` | ₹50,000 overdraft limit |
| `Bank` | Registry of all customers & accounts |

</details>

### 🧠 OOP Concepts in Action

- **🔒 Encapsulation** — `__balance` and `__total_account` are private, exposed via `@property` and `@staticmethod`
- **🧩 Abstraction** — `Account` is an `ABC` with an abstract `withdraw()` method
- **🌳 Inheritance** — `Savingsaccount` / `Currentaccount` extend `Account`; `Customer` extends `Person`
- **🎭 Polymorphism** — Each account type defines its own `withdraw()` and `acc_type()`

---

## ⚙️ Requirements

- Python **3.7+**
- Zero external dependencies — pure standard library (`abc`, `datetime`, `random`)

## 🚀 Quick Start

```bash
python bank_management_system.py
```

Then just follow the menu prompts. That's it!

---

## 🖥️ Demo

```
===== BANK MANAGEMENT SYSTEM =====
1. Create New Account
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Check Balance
6. Print Statement
7. View Total Accounts (staticmethod)
8. Exit

Enter your choice : 1

Welcome !, please enter your some details
Enter your Name : John Doe
Enter your Age : 30
Enter your Address : 123 Main Street

Name : John Doe
Age : 30
Address : 123 Main Street
Customer ID : 4821

1. Saving Account
2. Current Account

Please enter your choice of Account : 1
Account Number : 728193045612
Account Holder : John Doe
Interest Rate : 4%
Account Type : Saving Account
Balance : 0
```

---

## 📋 Menu Guide

| # | Option | What happens |
|---|---|---|
| 1️⃣ | **Create New Account** | Enter your details → pick Savings (4% interest) or Current (₹50,000 overdraft) → get a random 12-digit account number |
| 2️⃣ | **Deposit Money** | Enter account number + amount (must be positive) |
| 3️⃣ | **Withdraw Money** | Savings can't go negative; Current can dip to `-overdraft_limit` |
| 4️⃣ | **Transfer Money** | Validates both accounts + sufficient sender balance |
| 5️⃣ | **Check Balance** | Shows holder, type, and live balance |
| 6️⃣ | **Print Statement** | Lists every transaction with type, amount & timestamp |
| 7️⃣ | **Total Accounts** | Calls `Account.get_total_account()` |
| 8️⃣ | **Exit** | Ends the session |

---

## ⚠️ Known Limitations

- 🚫 No persistence — all data lives in memory and vanishes on exit
- 🎲 IDs are randomly generated (`random.randint`) — tiny chance of collisions
- ⌨️ Minimal input validation — non-numeric input on numeric prompts will crash the program
- 🗂️ `Bank.customers` / `Bank.accounts` are class-level (shared across all `Bank` instances)

## 🛣️ Roadmap

- [ ] Persistent storage (JSON / SQLite)
- [ ] Robust input validation with `try` / `except`
- [ ] Look up all accounts belonging to a `customer_id`
- [ ] Unit tests for deposit / withdraw / transfer logic
- [ ] GUI or web front-end

---

<div align="center">

## 📄 License

Released under the **MIT License** — free to use, modify, and learn from.

**Made with 🐍 Python & clean OOP design**

</div>