#def main():
#    print("Welcome to the Python Project!")

#if __name__ == "__main__":
#    main()

import streamlit as st
import json
import pandas as pd

# Judul aplikasi
st.title("Aplikasi Penilaian Mahasiswa")

# Inisialisasi data mahasiswa awal
data = [
    {"Nama Mahasiswa": f"Mahasiswa {i+1}", "Aspek 1": 1, "Aspek 2": 1, "Aspek 3": 1, "Aspek 4": 1}
    for i in range(10)
]
df = pd.DataFrame(data)

# Tabel interaktif
edited_df = st.data_editor(df, key="editor", num_rows="fixed")

# Tombol simpan untuk menghasilkan file JSON
def handle_save():
    output = {}
    for i in range(1, 5):
        output[f"aspek_penilaian_{i}"] = {
            row["Nama Mahasiswa"]: row[f"Aspek {i}"] for _, row in edited_df.iterrows()
        }

    with open("scores.json", "w") as f:
        json.dump(output, f, indent=2)

    st.success("Data berhasil disimpan sebagai 'scores.json'!")
    st.json(output)

# Tombol untuk menyimpan data
if st.button("Simpan"):
    handle_save()
