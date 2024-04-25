import openpyxl

def read_excel(file_path):
    # 載入工作簿和工作表
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active  # 假設我們只處理第一個工作表
    problem_ids = set()

    # 迭代每一行，假設從第二行開始有數據（第一行是標題行）
    for row in sheet.iter_rows(min_row=2, values_only=True):
        problem_id = int(row[0])  # 將ID轉換為整數
        problem_name = row[1]
        difficulty = row[3]

        # print(f"Problem ID: {problem_id}, Problem Name: {problem_name}, Difficulty: {difficulty}")
        problem_ids.add(problem_id)

    return problem_ids

if __name__ == "__main__":
    file_path = 'data/meta.xlsx'
    problem_ids = read_excel(file_path)
    print(f"Loaded problem IDs: {problem_ids}, length: {len(problem_ids)}")
