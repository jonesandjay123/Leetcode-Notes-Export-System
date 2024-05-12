import os
import json
import pdfplumber

def build_index(folder_path):
    index = {}
    page_counter = 0

    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            with pdfplumber.open(file_path) as pdf:
                for page_number, page in enumerate(pdf.pages, start=1):
                    page_counter += 1
                    text = page.extract_text()
                    if text:
                        first_line = text.split('\n')[0]
                        page_problem_id = first_line.split()[0].replace('.', '')
                        if page_problem_id.isdigit():
                            if page_problem_id not in index:
                                index[page_problem_id] = []
                            index[page_problem_id].append({"file": filename, "page": page_number})
                            print(f"{page_counter}. {filename} on page {page_number}: {page_problem_id}")

    return index

def save_index_to_json(index, json_path):
    with open(json_path, 'w') as f:
        json.dump(index, f)

def load_index_from_json(json_path):
    with open(json_path, 'r') as f:
        return json.load(f)

def search_by_Qnum(folder_path, problem_ids, json_path):
    if os.path.exists(json_path):
        print("Loading index from JSON...")
        index = load_index_from_json(json_path)
    else:
        print("Building index...")
        index = build_index(folder_path)
        save_index_to_json(index, json_path)
    
    results = {str(pid): index.get(str(pid), "Not found") for pid in problem_ids}
    return results

if __name__ == "__main__":
    folder_path = 'data'
    json_path = 'problem_index.json'
    problem_ids = [200]
    results = search_by_Qnum(folder_path, problem_ids, json_path)
    print(results)
