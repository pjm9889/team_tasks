from data_loader import load_tasks
from analytics import (
    count_total_tasks,
    count_tasks_by_assignee,
    count_tasks_by_status,
)
from reporter import print_summary, save_report

def main():
    csv_path = "tasks.csv"
    report_path = "report.txt"

    tasks = load_tasks(csv_path)

    total = count_total_tasks(tasks)
    by_assignee = count_tasks_by_assignee(tasks)
    by_status = count_tasks_by_status(tasks)

    print_summary(total, by_assignee, by_status)
    save_report(report_path, total, by_assignee, by_status)

    print(f"\n리포트가 '{report_path}' 파일로 저장되었습니다.")

if __name__ == "__main__":
    main()

