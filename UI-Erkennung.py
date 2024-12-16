import tkinter as tk
from tkinter import messagebox

# Funktion zur Benutzeranmeldung
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login erfolgreich", "Willkommen, " + username)
    else:
        messagebox.showerror("Login fehlgeschlagen", "Ungültiger Benutzername oder Passwort")

# Erstellen der Hauptfenster-Oberfläche
root = tk.Tk()
root.title("Benutzerverwaltung")

# Benutzername und Passwort Eingabefelder
label_username = tk.Label(root, text="Benutzername:")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Passwort:")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Anmelde-Button
login_button = tk.Button(root, text="Anmelden", command=login)
login_button.pack()

root.mainloop()
