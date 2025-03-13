import tkinter as tk
from tkinter import messagebox, ttk
from cryptography.fernet import Fernet


class EncryptionTool:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Encryption and Decryption Tool")
        self.window.geometry("300x250")

        self.option_label = tk.Label(self.window, text="Select an option:")
        self.option_label.pack()

        self.option_combobox = ttk.Combobox(self.window, values=["Encrypt", "Decrypt"])
        self.option_combobox.set("Encrypt")  # Set default option to Encrypt
        self.option_combobox.pack()

        self.process_button = tk.Button(self.window, text="Process", command=self.process_option)
        self.process_button.pack()

    def process_option(self):
        selected_option = self.option_combobox.get()

        if selected_option == "Encrypt":
            self.open_encryption_box()
        elif selected_option == "Decrypt":
            self.open_decryption_box()

    def open_encryption_box(self):
        encryption_box = tk.Toplevel(self.window)
        encryption_box.title("Encryption")
        encryption_box.geometry("300x250")

        input_label = tk.Label(encryption_box, text="Enter the text:")
        input_label.pack()

        input_entry = tk.Entry(encryption_box)
        input_entry.pack()

        key_label = tk.Label(encryption_box, text="Encryption Key:")
        key_label.pack()

        key_entry = tk.Entry(encryption_box, state="readonly")
        key_entry.pack()

        encrypt_button = tk.Button(encryption_box, text="Encrypt",
                                   command=lambda: self.perform_encryption(input_entry.get(), key_entry))
        encrypt_button.pack()

        encrypted_label = tk.Label(encryption_box, text="Encrypted Text:")
        encrypted_label.pack()

        encrypted_entry = tk.Entry(encryption_box, state="readonly")
        encrypted_entry.pack()

        ok_button = tk.Button(encryption_box, text="OK", command=encryption_box.destroy)
        ok_button.pack()

        key = Fernet.generate_key().decode()
        key_entry.config(state="normal")
        key_entry.delete(0, tk.END)
        key_entry.insert(tk.END, key)
        key_entry.config(state="readonly")

    def perform_encryption(self, text, key_entry):
        key = key_entry.get()
        if text and key:
            f = Fernet(key.encode())
            encrypted_text = f.encrypt(text.encode()).decode()
            key_entry.selection_range(0, tk.END)
            self.copy_to_clipboard(encrypted_text)
            messagebox.showinfo("Encrypted Text",
                                f"The text has been encrypted and copied to the clipboard.\n\nEncrypted Text: {encrypted_text}")
        else:
            messagebox.showinfo("Error", "Please enter the text to encrypt.")

    def open_decryption_box(self):
        decryption_box = tk.Toplevel(self.window)
        decryption_box.title("Decryption")
        decryption_box.geometry("300x200")

        encrypted_label = tk.Label(decryption_box, text="Enter the encrypted text:")
        encrypted_label.pack()

        encrypted_entry = tk.Entry(decryption_box)
        encrypted_entry.pack()

        key_label = tk.Label(decryption_box, text="Encryption Key:")
        key_label.pack()

        key_entry = tk.Entry(decryption_box)
        key_entry.pack()

        decrypt_button = tk.Button(decryption_box, text="Decrypt",
                                   command=lambda: self.perform_decryption(encrypted_entry.get(), key_entry.get()))
        decrypt_button.pack()

        ok_button = tk.Button(decryption_box, text="OK", command=decryption_box.destroy)
        ok_button.pack()

    def perform_decryption(self, encrypted_text, key):
        if encrypted_text and key:
            try:
                f = Fernet(key.encode())
                decrypted_text = f.decrypt(encrypted_text.encode()).decode()
                messagebox.showinfo("Decrypted Text", f"Decrypted Text: {decrypted_text}")
            except:
                messagebox.showinfo("Error", "Decryption failed! Invalid encrypted text or encryption key.")
        else:
            messagebox.showinfo("Error", "Please enter the encrypted text and encryption key.")

    def copy_to_clipboard(self, text):
        self.window.clipboard_clear()
        self.window.clipboard_append(text)

    def run(self):
        self.window.mainloop()


tool = EncryptionTool()
tool.run()
