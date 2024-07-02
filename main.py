from collections import Counter

# Dosyalardan metinleri oku ve kelimelere ayır
with open("nikke.txt", "r", encoding="utf-8") as f:
    nikke_text = f.read().strip().split()

with open("rgaming.txt", "r", encoding="utf-8") as f:
    gaming_text = f.read().strip().split()

with open("visualnovel.txt", "r", encoding="utf-8") as f:
    novel_text = f.read().strip().split()

nikke_counter = Counter(nikke_text)
gaming_counter = Counter(gaming_text)
novel_counter = Counter(novel_text)

top_n = 10
top_nikke = nikke_counter.most_common(top_n)
top_gaming = gaming_counter.most_common(top_n)
top_novel = novel_counter.most_common(top_n)

print("Nikke'nin En Çok Kullanılan Kelimeleri:")
print(top_nikke)
print()

print("Rgaming'in En Çok Kullanılan Kelimeleri:")
print(top_gaming)
print()

print("Visual Novel'in En Çok Kullanılan Kelimeleri:")
print(top_novel)