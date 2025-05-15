import streamlit as st
from cryptography.fernet import Fernet

st.set_page_config(page_title="Encryption & Decryption Tool", layout="centered")
st.title("🔐 Encryption and Decryption Tool")

option = st.selectbox("Choose an action", ["Encrypt", "Decrypt"])

if option == "Encrypt":
    text = st.text_input("Enter text to encrypt")

    if st.button("Encrypt"):
        if not text:
            st.warning("Please enter text.")
        else:
            key = Fernet.generate_key()
            f = Fernet(key)
            encrypted_text = f.encrypt(text.encode()).decode()

            st.success("✅ Encrypted successfully!")
            st.code(encrypted_text, language="text")
            st.text("Encryption Key:")
            st.code(key.decode(), language="text")

elif option == "Decrypt":
    encrypted_text = st.text_input("Enter the encrypted text")
    key = st.text_input("Enter the encryption key")

    if st.button("Decrypt"):
        if not encrypted_text or not key:
            st.warning("Please enter both the encrypted text and the key.")
        else:
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
