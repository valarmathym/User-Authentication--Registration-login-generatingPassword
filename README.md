# User Registration and Login System in Python

A simple console-based Python application for user registration and login authentication using file handling.
Features include user registration, auto-generated or custom passwords, login authentication, admin account management, and credential storage using a text file system. Password generation supports letters, numbers, symbols, and custom length selection.

## Features

- New user registration
- Existing user login
- Password auto-generation option
- Custom password creation
- Stores user credentials in `accounts.txt`
- Admin access to view registered accounts
- Uses file handling and dictionaries for authentication

---

## Technologies Used

- Python
- File Handling
- Random Password Generation
- Dictionary Data Structure

---

## Project Description

This project is a basic authentication system developed in Python.  
Users can:

- Register as new users
- Create their own password or auto-generate one
- Login using registered credentials

The application stores usernames and passwords inside an `accounts.txt` file and validates login information from the file.

An admin functionality is also included to allow viewing all registered accounts.

---

## Admin Login

Admin credentials:

```text
Username: admin
Password: Pass
```

After successful admin login, the contents of `accounts.txt` can be viewed.

---

## Password Generator Features

The auto-generated password can include:

- Lowercase letters
- Uppercase letters
- Numbers
- Symbols

Users can also choose the password length.

---

## File Structure

```text
project-folder/
│
├── main.py
├── accounts.txt
└── README.md
```

---

## How to Run

### Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

---

### Step 2: Clone Repository

```bash
git clone https://github.com/valarmathym/User-Authentication---Registration-login-Auto-generating-Password.git
```

---

### Step 3: Run the Program

```bash
python main.py
```

---

## Sample Workflow

```text
Are you a new user? Y/N:
```

### Existing User

- Login with username and password

### New User

- Create username
- Choose:
  - Custom password
  - Auto-generated password

---

## Learning Outcomes

This project helped in understanding:

- Python functions
- File handling
- Authentication logic
- Password generation
- Conditional statements
- Dictionaries in Python

---

## Future Improvements

- Encrypt passwords
- Add database support (MySQL)
- Create GUI version
- Add password validation
- Improve security

---

## Author

Valarmathy Murugan

Created on: 14-06-2022

Enhanced admin functionality added on: 17-06-2022
