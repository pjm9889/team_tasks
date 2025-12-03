from typing import List, Dict

def count_total_tasks(tasks: List[Dict]) -> int:
    return len(tasks)

def count_tasks_by_assignee(tasks: List[Dict]) -> Dict[str, int]:
    result = {}
    for t in tasks:
        name = t["assignee"]
        result[name] = result.get(name, 0) + 1
    return result

def count_tasks_by_status(tasks: List[Dict]) -> Dict[str, int]:
    result = {}
    for t in tasks:
        status = t["status"]
        result[status] = result.get(status, 0) + 1
    return result

