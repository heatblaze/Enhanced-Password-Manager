import tkinter as tk
from tkinter import simpledialog, messagebox
from database import add_password, get_password
from encryption import encrypt_password, decrypt_password
from password_utils import generate_password
from mfa import send_email_otp, send_sms_otp

# Functions
def add_password_gui():
    service = service_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if not service or not username or not password:
        messagebox.showerror("Error", "All fields are required.")
        return

    # Ask user to choose MFA method (email or phone)
    mfa_method = simpledialog.askstring("MFA Method", "Choose MFA method (email/phone):").lower()

    otp = None
    if mfa_method == "email":
        email = simpledialog.askstring("Email Verification", "Enter your email to receive an OTP:")
        if not email:
            messagebox.showerror("Error", "Email is required for OTP verification.")
            return
        otp = send_email_otp(email)
    elif mfa_method == "phone":
        phone_number = simpledialog.askstring("Phone Verification", "Enter your phone number (with country code, e.g., +1234567890):")
        if not phone_number:
            messagebox.showerror("Error", "Phone number is required for OTP verification.")
            return
        otp = send_sms_otp(phone_number)
    else:
        messagebox.showerror("Error", "Invalid MFA method. Please choose either 'email' or 'phone'.")
        return

    if not otp:
        messagebox.showerror("Error", "Failed to send OTP. Please try again.")
        return

    user_otp = simpledialog.askstring("OTP Verification", "Enter the OTP sent to your email or phone:")
    if user_otp != otp:
        messagebox.showerror("Error", "Invalid OTP.")
        return

    # Encrypt and save password
    encrypted_password = encrypt_password(password)
    add_password(service, username, encrypted_password)
    messagebox.showinfo("Success", "Password added successfully!")

def retrieve_password_gui():
    service = service_entry.get()
    if not service:
        messagebox.showerror("Error", "Service name is required.")
        return

    result = get_password(service)
    if result:
        username, encrypted_password = result
        decrypted_password = decrypt_password(encrypted_password)
        messagebox.showinfo("Password", f"Service: {service}\nUsername: {username}\nPassword: {decrypted_password}")
    else:
        messagebox.showerror("Error", "No password found for this service.")

def generate_password_gui():
    length = simpledialog.askinteger("Password Length", "Enter the desired password length (default is 12):", minvalue=6, maxvalue=32)
    password = generate_password(length or 12)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# GUI
app = tk.Tk()
app.title("Enhanced Password Manager")

tk.Label(app, text="Service:").grid(row=0, column=0, padx=10, pady=5)
service_entry = tk.Entry(app)
service_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="Username:").grid(row=1, column=0, padx=10, pady=5)
username_entry = tk.Entry(app)
username_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(app, text="Password:").grid(row=2, column=0, padx=10, pady=5)
password_entry = tk.Entry(app, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(app, text="Generate Password", font=("Arial", 12), bg="#4CAF50", fg="white", command=generate_password_gui).grid(row=2, column=2, padx=10, pady=5)
tk.Button(app, text="Add Password", font=("Arial", 12), bg="#2196F3", fg="white", command=add_password_gui).grid(row=3, column=0, padx=10, pady=10)
tk.Button(app, text="Retrieve Password", font=("Arial", 12), bg="#ff5733", fg="white", command=retrieve_password_gui).grid(row=3, column=1, padx=10, pady=10)

app.mainloop()
