from dotenv import load_dotenv
import os
import google.generativeai as genai
from parse_response import parse_gemini_response



#########load .Env############
# Load environment variables from .env file
load_dotenv()
# Ambil API Key dari variabel lingkungan
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

##########Konfigurasi API Gemini###########
# Inisialisasi klien Gemini dengan API Key
genai.configure(api_key = GEMINI_KEY)
# Inisialisasi model Gemini
MODEL_ID = "gemini-2.5-flash"
# Buat instance model generatif
model = genai.GenerativeModel(MODEL_ID)

##Fungsi untuk mengirim permintaan ke model Gemini
def generate_recipe(query):
    
    '''
    FUNGSI:untuk menghasilkan resep masakan berdasarkan permintaan pengguna : 
    
    PARAMS:
        query (str): Permintaan pengguna untuk resep masakan.
    
    RETURN: 
        1. response: Objek response dari model.generate_content() yang berisi teks hasil generasi.
    '''
    
    ### Membuat prompt untuk model Gemini
    prompt = f"""
    Buat sebuah list daftar resep masakan berdasarkan permintaan berikut: {query}".
    Output harus dalam format JSON dengan struktur berikut:
    {{
        "nama_resep": "string",
        "youtube_link": "placeholder_for_youtube_link",
    }}
    hanya keluarkan JSON tanpa penjelasan tambahan.
    """
    
    ##Mengirim permintaan ke model Gemini
    response = model.generate_content(prompt)
    
    # Ambil text hasil generasi
    return response

##Fungsi utama untuk mendapatkan respon resep masakan
def get_response(input_user):
    ''''
    fungsi untuk mendapatkan respon resep masakan dari model Gemini dan memparsingnya menjadi objek Python.
    
    PARAMS:
        input_user (str): Permintaan pengguna untuk resep masakan.
    RETURN:
        dict/list: Objek Python hasil parsing JSON dari respon model Gemini.
    '''
    # Dapatkan respon dari model Gemini
    response = generate_recipe(input_user)
    
    # Parsing respon untuk mengekstrak data JSON
    parsing_response = parse_gemini_response(response)
    
    #  Return hasil parsing yang sudah mendapatkan objek Python
    return parsing_response

## Contoh penggunaan

user_input = input("Bahan Yang anda miliki: ")
result = get_response(user_input)
print(result)
