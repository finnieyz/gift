from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 1. Membaca untaian kata dari file puisi.txt
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 2. Meracik Word Cloud dengan estetika soft pink & vintage
print("Sedang melukis mahakarya Anda, Mademoiselle...")
wordcloud = WordCloud(width=1000, height=800, 
                      background_color='#fdfbf7', # Warna latar champagne/off-white
                      colormap='RdPu',            # Palet warna bernuansa pink romantis
                      max_words=150, 
                      min_font_size=10,
                      font_path=None).generate(text)

# 3. Menyimpan karya seni tersebut
wordcloud.to_file('poetry_art.png')
print("L'art est prêt! (Seni telah siap!). Silakan cek file poetry_art.png di folder Anda 🎀")