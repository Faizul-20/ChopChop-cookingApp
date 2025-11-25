from dotenv import load_dotenv
import os
from google import genai
from app.services.utils.parse_response import parse_gemini_response
from app.services.utils import sanitize_request
from app.services.utils.sanitize_request import sanitize_input

# === Load .env dan konfigurasi Model ===

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def generate_recipe(query: str):
    """
    Mengirim prompt resep ke Gemini dan mengembalikan raw response.
    """
    sanitized = sanitize_input(query)

    prompt = f"""
    Anda adalah sistem generator resep yang ketat.
    Proses permintaan: "{sanitized}"

    Aturan:
    1. Jika permintaan TIDAK berisi bahan makanan atau nama masakan, hentikan proses dan keluarkan JSON error:
       [{{"error": "Permintaan tidak valid. Harap masukkan bahan atau nama masakan."}}]

    2. Jika permintaan VALID (ada bahan atau masakan), buat 5 resep relevan dan keluarkan HANYA list JSON:
       [{{"nama_resep": "string"}}, ...5 item...]

    Hanya keluarkan array JSON. Jangan sertakan penjelasan atau tanda ```json```.
    """

    return client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )


def get_gemini_response(user_input: str):
    """
    Mengambil response dari model dan mengubahnya menjadi objek Python.
    """
    response = generate_recipe(user_input)
    return parse_gemini_response(response)



## TODO : details recipe


# === Contoh Penggunaan ===
#user_input = input("Bahan yang Anda miliki: ")
#result = get_response(user_input)
#print(result)
