from typing import Dict

def print_summary(total: int,
                  by_assignee: Dict[str, int],
                  by_status: Dict[str, int]) -> None:
    print("==== 팀 업무 요약 ====")
    print(f"- 전체 작업 수: {total}")
    print("\n[팀원별 작업 수]")
    for name, cnt in by_assignee.items():
        print(f"  {name}: {cnt}개")

    print("\n[상태별 작업 수]")
    for status, cnt in by_status.items():
        print(f"  {status}: {cnt}개")
    print("======================")

def save_report(path: str,
                total: int,
                by_assignee: Dict[str, int],
                by_status: Dict[str, int]) -> None:
    lines = []
    lines.append("==== 팀 업무 요약 리포트 ====\n")
    lines.append(f"전체 작업 수: {total}\n\n")

    lines.append("[팀원별 작업 수]\n")
    for name, cnt in by_assignee.items():
        lines.append(f"- {name}: {cnt}개\n")
    lines.append("\n")

    lines.append("[상태별 작업 수]\n")
    for status, cnt in by_status.items():
        lines.append(f"- {status}: {cnt}개\n")

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)

