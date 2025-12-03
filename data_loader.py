import csv
from typing import List, Dict

def load_tasks(csv_path: str) -> List[Dict]:
    """
    CSV 파일에서 업무 목록을 불러와서
    딕셔너리 리스트 형태로 반환합니다.
    예: [{"id": "1", "assignee": "bu", "status": "done"}, ...]
    """
    tasks = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tasks.append(row)
    return tasks

