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
                st.success("✅ Decrypted successfully!")
                st.code(decrypted_text, language="text")
            except Exception as e:
                st.error("❌ Decryption failed. Please check your key and encrypted text.")
