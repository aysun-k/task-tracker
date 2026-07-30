from task import Task
from datetime import datetime
from storage import load_tasks, save_tasks


def add_task(description):
    tasks = load_tasks()

    new_id = max([task["id"] for task in tasks], default=0) + 1
    task = Task(new_id, description)

    tasks.append(task.to_dict())

    save_tasks(tasks)

    return task

def get_tasks(status=None):
    tasks = load_tasks()

    if status is None:
        return tasks

    return [task for task in tasks if task["status"] == status]


def delete_task(task_id):
    tasks = load_tasks()

    original_length = len(tasks)

    tasks = [task for task in tasks if task["id"] != task_id]

    save_tasks(tasks)

    return len(tasks) < original_length

def update_task(task_id, new_description):
    tasks = load_tasks()

    found = False

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            found = True

    save_tasks(tasks)

    return found


def update_status(task_id, status):
    tasks = load_tasks()

    found = False

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            found = True

    save_tasks(tasks)

    return found