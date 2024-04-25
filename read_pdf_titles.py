import pdfplumber
import os

def read_pdf_titles(folder_path):
    # 遍歷文件夾中的所有PDF文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            with pdfplumber.open(file_path) as pdf:
                first_page = pdf.pages[0]  # 假設標題在每個文件的第一頁
                text = first_page.extract_text()
                # 假設標題是每頁第一行的文字
                title = text.split('\n')[0]
                print(f"File: {filename}, Title: {title}")

def count_total_pages(folder_path):
    total_pages = 0
    # 遍歷文件夾中的所有PDF文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            with pdfplumber.open(file_path) as pdf:
                num_pages = len(pdf.pages)  # 獲取當前PDF文件的頁數
                total_pages += num_pages
                print(f"File: {filename}, Pages: {num_pages}")
    print(f"Total number of pages in all PDFs: {total_pages}")

if __name__ == "__main__":
    folder_path = 'data'
    count_total_pages(folder_path)
