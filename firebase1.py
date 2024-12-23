import streamlit as st
import pyrebase

# Konfigurasi Firebase

# Inisialisasi Firebase
firebase_config = st.secrets["firebase"]
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

