# 🔐 Password Strength Checker

A simple Python-based cybersecurity project that evaluates the strength of a password based on its length and character variety.

This project was developed as **Cybersecurity Project 1 – Password Strength Checker** for the DecodeLabs internship track.

## 📌 Project Overview

The Password Strength Checker is a defensive cybersecurity tool that analyzes a user's password and classifies it as:

* **Weak**
* **Medium**
* **Strong**

The program checks whether the password contains different types of characters and assigns a score based on these security criteria.

## 🎯 Objectives

The main objectives of this project are:

* Understand basic password security principles
* Practice Python string handling
* Use conditional statements
* Validate user input
* Evaluate password strength
* Understand the importance of character variety in passwords

## ⚙️ Features

The program checks:

* Password length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

Based on these checks, it displays the overall password strength.

## 🛠️ Technologies Used

* **Python 3**
* String Handling
* Conditional Statements
* Built-in Python String Methods

## 🧠 How It Works

The program assigns points according to the following criteria:

| Security Check                     | Score |
| ---------------------------------- | ----: |
| Password has at least 8 characters |    +1 |
| Contains uppercase letter          |    +1 |
| Contains lowercase letter          |    +1 |
| Contains a number                  |    +1 |
| Contains a special character       |    +1 |

### Strength Classification

| Score | Strength |
| ----: | -------- |
|   0–2 | Weak     |
|   3–4 | Medium   |
|     5 | Strong   |

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python installation:

python --version

### 2. Clone the Repository

git clone https://github.com/yourusername/password-strength-checker.git

### 3. Open the Project Folder

cd password-strength-checker


### 4. Run the Program

python password_checker.py

## 💻 Example

Enter your password: Hello@123

Password Strength: STRONG

Another example:

Enter your password: hello

Password Strength: WEAK

## 🔒 Security Note

This project is designed for educational purposes.

It demonstrates basic password-strength validation but should **not** be considered a complete enterprise-level password security solution.

A production password security system should also consider factors such as:

* Common password detection
* Password breach databases
* Password dictionaries
* Password entropy
* Rate limiting
* Secure password hashing
* Multi-factor authentication (MFA)

## 🚀 Future Improvements

Possible improvements include:

* Add common/leaked password detection
* Calculate password entropy
* Provide detailed feedback to the user
* Detect repeated characters
* Add a graphical user interface (GUI)
* Add a password generator
* Check passwords against a local dictionary of commonly used passwords

## 📚 Skills Demonstrated

This project demonstrates:

* Python programming
* String manipulation
* Conditional logic
* Input validation
* Basic cybersecurity concepts
* Password security principles

## 👨‍💻 Author

**Abdur Rehman Toor**

Cybersecurity Intern
DecodeLabs – Cybersecurity Project 1

---

⭐ If you find this project useful, consider giving the repository a star.
