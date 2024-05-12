import json
import pdfplumber
import os
from PyPDF2 import PdfWriter, PdfReader

def export_matched_pages_using_index(problem_ids, folder_path, json_path, output_pdf_path):
    pdf_writer = PdfWriter()
    with open(json_path, 'r') as json_file:
        index = json.load(json_file)

        print("Starting the PDF export process...")

        for problem_id in problem_ids:
            if str(problem_id) in index:
                for entry in index[str(problem_id)]:
                    file_path = os.path.join(folder_path, entry["file"])
                    pdf_reader = PdfReader(file_path)
                    pdf_writer.add_page(pdf_reader.pages[entry["page"] - 1])

                    print(f"Adding page {entry['page']} from '{entry['file']}' for problem ID {problem_id}.")

    with open(output_pdf_path, 'wb') as out:
        pdf_writer.write(out)

def export_matched_pages(folder_path, problem_ids, output_pdf_path):
    page_counter = 0
    match_count = 0  # 初始化匹配計數器
    pdf_writer = PdfWriter()  # 使用新的PdfWriter創建一個PDF寫入器

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
                            match_count += 1
                            # 將當前頁面添加到新的PDF文件中
                            pdf_path = os.path.join(folder_path, filename)
                            pdf_to_add = PdfReader(pdf_path)
                            pdf_writer.add_page(pdf_to_add.pages[page.page_number - 1])

    print(f"Total matches found: {match_count}")

    # 將匯集的頁面輸出到一個新的PDF文件中
    with open(output_pdf_path, 'wb') as out:
        pdf_writer.write(out)

if __name__ == "__main__":
    folder_path = 'data'
    # problem_ids = read_excel('data/meta.xlsx')
    problem_ids = [200]
    json_path = 'problem_index.json'
    output_pdf_path = 'meta_notes.pdf'
    # export_matched_pages(folder_path, problem_ids, output_pdf_path)
    export_matched_pages_using_index(problem_ids, folder_path, json_path, output_pdf_path)
