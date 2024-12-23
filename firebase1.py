import streamlit as st
import pyrebase

# Konfigurasi Firebase
firebase_config = {
    "apiKey": "AIzaSyC_xc9BJVQvKkpe3jIbtd8tGir4svj4gIY",
    "authDomain": "belajar-firestore-d98f9.firebaseapp.com",
    "databaseURL": "https://belajar-firestore-d98f9-default-rtdb.firebaseio.com",
    "projectId": "belajar-firestore-d98f9",
    "storageBucket": "belajar-firestore-d98f9.firebasestorage.app",
    "messagingSenderId": "433046519507",
    "appId": "1:433046519507:web:0b92823e8821795d775e26",
    "measurementId": "G-7P0ZL6JFZR"
}

# Inisialisasi Firebase
firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

# Streamlit UI
st.title("Integrasi Firebase Realtime Database")

# Input data baru
name = st.text_input("Nama:")
age = st.number_input("Umur:", min_value=0, step=1)

if st.button("Tambahkan Data"):
    if name:
        data = {"name": name, "age": age}
        db.push(data)
        st.success("Data berhasil ditambahkan!")
    else:
        st.error("Nama tidak boleh kosong.")

# Tampilkan data dari Firebase
st.subheader("Data Tersimpan")
data = db.get().val()

if data:
    for key, value in data.items():
        st.write(f"Nama: {value['name']}, Umur: {value['age']}")
else:
    st.write("Tidak ada data.")

