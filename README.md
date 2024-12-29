# Enhanced-Password-Manager

A secure and feature-rich password manager implemented in Python with Tkinter for GUI, incorporating multi-factor authentication (MFA) via email or SMS. This tool provides secure storage, retrieval, and management of credentials, ensuring enhanced security with encrypted passwords and MFA.

---

## Features
- **Multi-Factor Authentication (MFA):** Choose between email or SMS for OTP verification.
- **Secure Encryption:** Passwords are encrypted using AES (Advanced Encryption Standard) before storage.
- **Random Password Generation:** Generate strong passwords with custom options for length and character types.
- **User-Friendly Interface:** Easy-to-use Tkinter GUI for managing passwords.

---

## Tech Stack
- **Programming Language:** Python
- **GUI Framework:** Tkinter
- **Database:** SQLite
- **Encryption:** cryptography library
- **MFA via Email:** SMTP with Gmail
- **MFA via SMS:** Twilio API

---

## Prerequisites
- Python 3.6 or higher
- Required Python libraries: tkinter, cryptography, twilio
- Twilio account and credentials for SMS-based MFA
- Gmail account and app password for email-based MFA

---

# Usage

## Add Password
- Enter the Service Name, Username, and Password in the respective fields.
- Choose the MFA method (email or phone).
- Enter the OTP sent to your email or phone.
- Click Add Password to securely store the credentials.

## Retrieve Password
- Enter the Service Name.
- Click Retrieve Password to view the stored credentials.

## Generate Password
- Click Generate Password to create a random password.
- Optionally, specify the desired password length.

## Security
- Passwords are encrypted using AES before being stored in the SQLite database.
- MFA ensures additional security during password addition.

---

## Notes
1. Ensure the SQLite database (database.db) and encryption key (key.key) are kept secure.
2. Twilio and email credentials should not be shared or exposed publicly.
3. Need to have a premium Twilio or any other substitute to run it in case of region +91.

---

## Contributing
**Contributions are welcome!**

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Open a pull request.

---

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/heatblaze/Enhanced-Password-Manager.git
