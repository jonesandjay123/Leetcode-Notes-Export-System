import pdfplumber
import os

def search_by_Qnum(folder_path, problem_ids):
    page_counter = 0
    match_count = 0  # 初始化匹配計數器
    question_type = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_counter += 1
                    text = page.extract_text()
                    if text:
                        first_line = text.split('\n')[0]
                        page_problem_id = first_line.split()[0].replace('.', '')
                        print(f"{page_counter}. {filename} on page {page.page_number}: {page_problem_id} {first_line[len(page_problem_id)+1:]}")
                        if page_problem_id.isdigit() and int(page_problem_id) in problem_ids:
                            print("=========MATCH FOUND==========")
                            question_type.append(filename)
                            match_count += 1

    print(f"Total matches found: {match_count}")
    print(f"problem_ids: {problem_ids} is in {question_type}")


if __name__ == "__main__":
    folder_path = 'data'
    problem_ids = [339]
    search_by_Qnum(folder_path, problem_ids)
