import sys
import json
from sentence_transformers import SentenceTransformer

# TO RUN: cat plants.json | python3 get_embeddings.py > semantic_plants.json
# Load the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    # The model.encode() method already returns a list of floats
    return model.encode(text, convert_to_tensor=False).tolist()

if __name__ == "__main__":
    # Read JSON from STDIN
    data = json.load(sys.stdin)

    # Update each document in the JSON data
    for document in data:
        # Extract fields if they exist, otherwise default to empty strings
        name = document.get("Name", "") or ""
        intro = document.get("Introduction", "") or ""
        characteristics = document.get("Characteristics", "") or ""
        habitat = document.get("Habitat", "") or ""
        taxonomy = document.get("Taxonomy", "") or ""
        ecology = document.get("Ecology", "") or ""
        etymology = document.get("Etymology", "") or ""
        genetics = document.get("Genetics", "") or ""
        medicine = document.get("Medicine", "") or ""
        nutrition = document.get("Nutrition", "") or ""
        chemistry = document.get("ChemistryComposition", "") or ""
        toxicity = document.get("Toxicity", "") or ""
        allergenicity = document.get("Allergenicity", "") or ""
        uses = document.get("Uses", "") or ""
        culinary = document.get("CulinaryUses", "") or ""
        cultivation = document.get("Cultivation", "") or ""
        threats = document.get("ThreatsControl", "") or ""

        combined_text = name + " " + intro + " " + characteristics + " " + habitat + " " + taxonomy + " " + ecology + " " + etymology + " " + genetics + " " + medicine + " " + nutrition + " " + chemistry + " " + toxicity + " " + allergenicity + " " + uses + " " + culinary + " " + cultivation + " " + threats
        document["vector"] = get_embedding(combined_text)

    # Output updated JSON to STDOUT
    json.dump(data, sys.stdout, indent=4, ensure_ascii=False)
