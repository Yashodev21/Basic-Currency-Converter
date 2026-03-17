import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Country-currency map without flags
country_currency = {
    "United States (USD)": "USD",
    "Eurozone (EUR)": "EUR",
    "United Kingdom (GBP)": "GBP",
    "India (INR)": "INR",
    "Japan (JPY)": "JPY",
    "Australia (AUD)": "AUD",
    "Canada (CAD)": "CAD",
    "Switzerland (CHF)": "CHF",
    "China (CNY)": "CNY",
    "Russia (RUB)": "RUB",
    "Brazil (BRL)": "BRL",
    "South Africa (ZAR)": "ZAR",
    "Mexico (MXN)": "MXN",
    "South Korea (KRW)": "KRW",
    "Singapore (SGD)": "SGD",
    "New Zealand (NZD)": "NZD",
    "Turkey (TRY)": "TRY",
    "Saudi Arabia (SAR)": "SAR",
    "UAE (AED)": "AED",
    "Malaysia (MYR)": "MYR"
}

# Fetch exchange rates
def get_exchange_rate():
    try:
        url = "https://v6.exchangerate-api.com/v6/a767700cf8e23d87576bf465/latest/USD"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return data['conversion_rates']
        else:
            messagebox.showerror("Error", "Failed to fetch exchange rates.")
            return None
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return None

# Convert currency
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = country_currency[from_combo.get()]
        to_currency = country_currency[to_combo.get()]
        if rates:
            if from_currency == "USD":
                converted = amount * rates[to_currency]
            else:
                converted = amount / rates[from_currency] * rates[to_currency]
            label_result.config(
                text=f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}"
            )
        else:
            label_result.config(text="Error fetching rates.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Clear fields
def clear_fields():
    entry_amount.delete(0, tk.END)
    label_result.config(text="Converted Amount:")

# Reset all
def reset_all():
    entry_amount.delete(0, tk.END)
    from_combo.set("United States (USD)")
    to_combo.set("Eurozone (EUR)")
    label_result.config(text="Converted Amount:")

# Main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("950x650")
root.config(bg="#000000")  # Black background

# Frame: Dark blue for contrast
frame = tk.Frame(root, bg="#1E3A8A", padx=40, pady=40, bd=8, relief="groove")
frame.place(relx=0.5, rely=0.5, anchor="center")

style = ttk.Style()
style.configure("TCombobox", font=("Segoe UI", 20), padding=5)

# Entry and Dropdown Font
entry_font = ("Segoe UI", 24)
label_font = ("Segoe UI", 24, "bold")

# Amount
tk.Label(frame, text="Amount:", font=label_font, bg="#1E3A8A", fg="#FFFFFF").grid(row=0, column=0, pady=20, sticky="e")
entry_amount = tk.Entry(frame, font=entry_font, width=20, bd=4, relief="groove")
entry_amount.grid(row=0, column=1, pady=20)

# From Currency
tk.Label(frame, text="From Currency:", font=label_font, bg="#1E3A8A", fg="#FFFFFF").grid(row=1, column=0, pady=15, sticky="e")
from_combo = ttk.Combobox(frame, state="readonly", font=entry_font, width=28)
from_combo['values'] = list(country_currency.keys())
from_combo.set("United States (USD)")
from_combo.grid(row=1, column=1, pady=15)

# To Currency
tk.Label(frame, text="To Currency:", font=label_font, bg="#1E3A8A", fg="#FFFFFF").grid(row=2, column=0, pady=15, sticky="e")
to_combo = ttk.Combobox(frame, state="readonly", font=entry_font, width=28)
to_combo['values'] = list(country_currency.keys())
to_combo.set("Eurozone (EUR)")
to_combo.grid(row=2, column=1, pady=15)

# Button style
btn_style = {
    "font": ("Segoe UI", 20, "bold"),
    "padx": 20,
    "pady": 15,
    "bd": 3,
    "relief": "raised",
    "width": 20
}

# Buttons
convert_button = tk.Button(frame, text="💱 Convert", bg="#388e3c", fg="white", command=convert_currency, **btn_style)
convert_button.grid(row=3, column=0, columnspan=2, pady=20)

clear_button = tk.Button(frame, text="🧹 Clear", bg="#fb8c00", fg="white", command=clear_fields, **btn_style)
clear_button.grid(row=4, column=0, pady=10)

reset_button = tk.Button(frame, text="🔄 Reset", bg="#e53935", fg="white", command=reset_all, **btn_style)
reset_button.grid(row=4, column=1, pady=10)

# Result Label
label_result = tk.Label(frame, text="Converted Amount:", font=label_font, bg="#1E3A8A", fg="#FFFFFF", pady=20)
label_result.grid(row=5, column=0, columnspan=2)

# Load exchange rates
rates = get_exchange_rate()

# Start app
root.mainloop()