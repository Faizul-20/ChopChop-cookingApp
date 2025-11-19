import json
import re


## Fungsi untuk parsing response dari model Gemini
def parse_gemini_response(response):
    """
    FUNGSI: Mengekstrak data JSON dari response API Gemini

    PARAMS:
      response: Objek response dari model.generate_content() yang berisi teks hasil generasi.
      bentuknya adalah struktur nested sesuai dengan dokumentasi Gemini.             

    RETURN:
      - dictionary: Objek Python hasil parsing JSON
      - None: Jika parsing gagal
    """

    # 1. EKSTRAKSI TEKS MENTAH
    # Ambil teks dari struktur nested response Gemini
    text = response.candidates[0].content.parts[0].text

    # 2. EKSTRAKSI BLOK JSON
    # Pattern regex untuk mencari blok kode JSON yang diapit ```json ... ```
    # [\s\S]*? -> Mencocokan semua karakter termasuk newline (non-greedy)
    pattern = r"```json\s*([\s\S]*?)\s*```"
    match = re.search(pattern, text)

    if match:
        # Jika ditemukan blok JSON, ambil isi di dalamnya
        json_text = match.group(1)
    else:
        # Fallback: gunakan seluruh teks jika tidak ada blok kode
        # PERINGATAN: Ini berisiko jika teks mengandung non-JSON!
        json_text = text

    # 3. PEMBERSIHAN TEKS
    # Hapus spasi/whitespace di awal dan akhir teks
    json_text = json_text.strip()

    # 4. PARSING JSON
    try:
        # Ubah string JSON menjadi objek Python (dictionary)
        data = json.loads(json_text)
        return data
    except json.JSONDecodeError as e:
        # ERROR HANDLING: Tampilkan error dan teks asli jika parsing gagal
        print("Error parsing JSON:", e)
        print("Raw text:", json_text)
        return None