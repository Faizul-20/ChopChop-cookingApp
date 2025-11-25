import bleach
import re

# Fungsi untuk membersihkan input user
def sanitize_input(text: str, max_length: int = 200) -> str:
    """
    Bersihkan input user dan batasi panjangnya.
    """

    cleaned = bleach.clean(text, tags=[], attributes={}, strip=True)

    if not _validate_input(cleaned):
        raise ValueError("Input mengandung karakter berbahaya")

    return cleaned[:max_length]

#fungsi untuk validasi input user dari karakter berbahaya atau scripting
def _validate_input(text : str) -> bool :
    """
    Validasi Iput Bahan makanan
    """
    pattern = r'^[a-zA-Z0-9\s,\.\-]+$'
    return bool(re.match(pattern,text)) and len(text) <=200