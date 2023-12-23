# Import module package
import streamlit as st
import pickle
# Load file model pickle
pickle_loan = open('model_loan.pkl', 'rb')
classifier = pickle.load(pickle_loan)
# Prediksi model ML
def prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History):
    # Pra-proses input pengguna berdasarkan kolom
    # Buat kondisi untuk kolom Gender dimana 0 = Laki-laki, 1 = Perempuan
    if Gender == "Male":
        Gender = 0
    else:
        Gender = 1
    # Buat kondisi untuk kolom Married berdasarkan status pernikahan dimana 0 = Single, 1 = Married
    if Married == "Unmarried":
        Married = 0
    else:
        Married = 1
    # Buat kondisi untuk kolom Credit_History berdasarkan riwayat pinjaman yaitu 0 = Tidak Lunas, 1 = Lunas
    if Credit_History == 'Unclear Debts':
        Credit_History = 0
    else:
        Credit_History = 1
    
    LoanAmount = LoanAmount / 1000

    # Membuat Prediksi Pinjaman
    prediction = classifier.predict([
        [Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if prediction == 0:
        pred = 'Ditolak!'
    else:
        pred = 'Diterima!'
    return pred

# Membuat judul WebApp Streamlit 
st.header('Aplikasi Model Prediksi Pinjaman Dengan Streamlit')
# Membuat fitur untuk input atau masukan data yang akan di prediksi
# Pengisian kolom Gender
Gender = st.selectbox('Jenis Kelamin',("Male", "Female"))
# Pengisian kolom Status Pernikahan
Married = st.selectbox('Status Pernikahan',("Unmarried", "Married")) 
# Pengisian kolom Pendapatan Nasabah
ApplicantIncome = st.number_input("Total Pendapatan Perbulan") 
# Pengisian kolom Pinjaman
LoanAmount = st.number_input("Total Pengajuan Pinjaman")
# Pengisian kolom Riwayat Pinjaman
Credit_History = st.selectbox('Riwayat Hutang Kredit',("Unclear Debts", "No Unclear Debts"))
# Hasil tiap data yang dimasukkan
result = ""

# Menambahkan fitur tombol prediksi untuk hasil yang telah dimasukkan
if st.button("Predict"): 
    result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History) 
    st.success('Pinjaman Kamu : {}'.format(result))
    st.write(f"Total Pinjaman : {LoanAmount}")