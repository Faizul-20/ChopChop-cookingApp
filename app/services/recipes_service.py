from app.models.data import Recipe
from api.gemini_response import get_gemini_response
from api.youtube_response import get_youtube_link
from typing import List


def build_recipes(user_input: str) -> List[Recipe]:
    """
    Mengambil daftar resep dari Gemini dan menambahkan link YouTube untuk setiap resep.
    """
    raw_recipes = get_gemini_response(user_input)
    if not raw_recipes:
        return [{"Eror": "Gemini gagal menghasilkan resep"}]

    valid_recipes = []
    for item in raw_recipes:
        name = item.get("nama_resep")
        if not name or not isinstance(name, str):
            continue  # skip item invalid

        youtube_link = get_youtube_link(name)
        valid_recipes.append(Recipe(name=name, youtube_link=youtube_link))

    if not valid_recipes:
        return [{"Eror": "Tidak ada resep valid dari Gemini"}]

    return valid_recipes


#====Usage Example====#
if __name__ == "__main__":
    user_input = input("Bahan yang Anda miliki: ")
    recipes_objects = build_recipes(user_input)

    for recipe in recipes_objects :
        print("Nama Resep : " + recipe.name)
        print("Link Resep : " + recipe.youtube_link)

    #url_name = input("Masukan Url Youtube")
    #recipes_details = generate_detail(url_name)
    #print(recipes_details)

