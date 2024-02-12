import requests
from sentence_transformers import SentenceTransformer
import json

def text_to_embedding(text):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding = model.encode(text, convert_to_tensor=False).tolist()
    
    # Convert the embedding to the expected format
    embedding_str = "[" + ",".join(map(str, embedding)) + "]"
    return embedding_str

def solr_knn_query(endpoint, collection, embedding):
    url = f"{endpoint}/{collection}/select"

    data = {
        "q": f"{{!knn f=vector topK=20}}{embedding}",
        "fl": "Name",
        "rows": 20,
        "wt": "json"
    }
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    return response.json()

def display_results(results):
    docs = results.get("response", {}).get("docs", [])
    if not docs:
        print("No results found.")
        return

    for doc in docs:
        print(f"* {doc.get('Name')} {doc.get('Introduction')} {doc.get('Description')} {doc.get('Characteristics')}")

def save_results_to_json(results, file_name):
    docs = results.get("response", {}).get("docs", [])
    if not docs:
        print("No results found.")
        return

    with open(file_name, 'w') as file:
        json.dump(docs, file, indent=4)

def save_results_to_txt(results, file_name):
    docs = results.get("response", {}).get("docs", [])
    if not docs:
        print("No results found.")
        return

    with open(file_name, 'w') as file:
        for doc in docs:
            # Extracting fields and filtering out None values
            fields = [doc.get(field) for field in ['Name', 'Introduction', 'Description', 'Characteristics']]
            filtered_fields = ' '.join(filter(lambda x: x is not None, fields))
            
            file.write(filtered_fields + '\n')

def main():
    solr_endpoint = "http://localhost:8983/solr"
    collection = "semantic_plants"
    
    query_type = input("Enter query type: ")
    query_text = input("Enter your query: ")
    embedding = text_to_embedding(query_text)

    try:
        results = solr_knn_query(solr_endpoint, collection, embedding)
        
        # Adjust the file path construction here
        file_path = f"M3/notebooks/with-semantic/{query_type}_results.txt"
        save_results_to_txt(results, file_path)

        display_results(results)
    except requests.HTTPError as e:
        print(f"Error {e.response.status_code}: {e.response.text}")


if __name__ == "__main__":
    main()
