import pdfplumber
import os

from read_excel import read_excel

def check_pdf_pages(folder_path, problem_ids):
    page_counter = 0
    match_count = 0  # 初始化匹配計數器

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
                        print(f"{page_counter}. Title in {filename} on page {page.page_number}: {page_problem_id} {first_line[len(page_problem_id)+1:]}")
                        # 確保page_problem_id是一個有效的數字
                        if page_problem_id.isdigit() and int(page_problem_id) in problem_ids:
                            print("=========MATCH FOUND==========")
                            match_count += 1

    print(f"Total matches found: {match_count}")

if __name__ == "__main__":
    folder_path = 'data'
    problem_ids = read_excel('data/meta.xlsx')
    check_pdf_pages(folder_path, problem_ids)
