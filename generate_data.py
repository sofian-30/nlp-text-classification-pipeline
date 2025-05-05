import os
import pandas as pd

# Créer le dossier s'il n'existe pas
output_dir = "data/raw"
os.makedirs(output_dir, exist_ok=True)

# Génération des données
positive_samples = [
    "This movie was fantastic! Highly recommend.",
    "An excellent experience, loved it.",
    "Absolutely amazing! Would watch again.",
    "A brilliant and emotional journey.",
    "Superb direction and storytelling.",
    "I loved the characters and the acting.",
    "Heartwarming and beautifully shot.",
    "Wonderful! One of the best I've seen.",
    "A true masterpiece.",
    "Totally worth it, highly enjoyable."
] * 10  # 100 exemples

negative_samples = [
    "I hated the plot. It was so boring.",
    "The worst film I've ever seen.",
    "Terrible. Waste of time.",
    "A complete disappointment.",
    "Awful acting and direction.",
    "Poorly written and executed.",
    "Boring from start to finish.",
    "Would not recommend.",
    "Absolutely dreadful.",
    "Save your time and skip this one."
] * 10  # 100 exemples

data = {
    "text": positive_samples + negative_samples,
    "label": ["positive"] * 100 + ["negative"] * 100
}

df = pd.DataFrame(data)
file_path = os.path.join(output_dir, "sample_reviews_200.csv")
df.to_csv(file_path, index=False)

print(f"✅ Fichier généré : {file_path}")
