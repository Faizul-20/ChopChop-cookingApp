from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
if not YOUTUBE_API_KEY:
    raise ValueError("API YOUTUBE belum di konfigurasi")

def get_youtube_link(recipe_name: str) -> str:
    """
    Mencari video YouTube berdasarkan nama resep dan mengembalikan link video pertama.
    Memfilter Shorts (durasi <4 menit) menggunakan videoDuration='medium'.
    """
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    request = youtube.search().list(
        q=recipe_name,
        part='snippet',
        type='video',
        maxResults=1,          # ambil beberapa hasil
        videoDuration='medium' # filter durasi > 4 menit
    )
    response = request.execute()

    items = response.get('items', [])
    if not items:
        return ""

    for item in items:
        video_id = item['id']['videoId']
        # skip shorts
        if "short" not in item['snippet']['thumbnails']['default']['url']:
            return f"https://www.youtube.com/watch?v={video_id}"

    return ""  # kalau semua items ternyata shorts

## TODO : Dapetin transkrip dari video youtube

#=== Contoh Penggunaan ===
#if __name__ == "__main__":
#    recipe_name = input("Masukkan nama resep untuk mencari video YouTube: ")
#    link = get_youtube_link(recipe_name)
#    print("Link YouTube:", link)
