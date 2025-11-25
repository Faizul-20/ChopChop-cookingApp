import json
import re
import bleach


def parse_gemini_response(response):
    """
    Mengambil blok JSON dari response Gemini dan mengubahnya menjadi list of dict.
    Mengembalikan None jika parsing gagal.
    """
    try:
        text = response.candidates[0].content.parts[0].text

        # Ekstrak blok JSON jika ada
        match = re.search(r"```json\s*([\s\S]*?)\s*```", text)
        json_text = match.group(1).strip() if match else text.strip()

        data = json.loads(json_text)
        return validate_recipe_data(data)

    except json.JSONDecodeError as e:
        raw_text_to_print = json_text if 'json_text' in locals() else text
        print(f"Gagal parsing JSON: {e}\nRaw text: {raw_text_to_print}")
        return None


def validate_recipe_data(data):
    """
    Memvalidasi data resep.
    Kembalikan list resep bersih atau list error.
    """
    if not isinstance(data, list):
        return [{"Eror": "Format data bukan list"}]

    # JSON error dari model
    if len(data) == 1 and isinstance(data[0], dict) and 'eror' in data[0]:
        return [{"Eror": bleach.clean(data[0]['eror'], strip=True)}]

    validated = []
    for item in data:
        if 'error' in item:
            continue
        nama = item.get("nama_resep")
        if isinstance(nama, str):
            validated.append({"nama_resep": bleach.clean(nama, strip=True)})

    if not validated:
        return [{"Eror": "Tidak ada resep valid"}]

    return validated
