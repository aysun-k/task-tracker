import sys
from task_manager import (
    add_task,
    get_tasks,
    delete_task,
    update_task,
    update_status,
)


if len(sys.argv) < 2:
    print("Please provide a command.")
    sys.exit()


command = sys.argv[1]


if command == "add":
    description = sys.argv[2]

    task = add_task(description)

    print(f"Task added successfully (ID: {task.id})")


elif command == "list":
    if len(sys.argv) == 3:
        status = sys.argv[2]
        tasks = get_tasks(status)
    else:
        tasks = get_tasks()

    for task in tasks:
        print(f"{task['id']} - {task['description']} [{task['status']}]")

elif command == "delete":
    task_id = int(sys.argv[2])

    deleted = delete_task(task_id)

    if deleted:
        print(f"Task {task_id} deleted successfully")
    else:
        print("Task not found.")


elif command == "update":
    task_id = int(sys.argv[2])
    new_description = sys.argv[3]

    updated = update_task(task_id, new_description)

    if updated:
        print(f"Task {task_id} updated successfully")
    else:
        print("Task not found.")


elif command == "mark-done":
    task_id = int(sys.argv[2])

    updated = update_status(task_id, "done")

    if updated:
        print(f"Task {task_id} marked as done")
    else:
        print("Task not found.")


elif command == "mark-in-progress":
    task_id = int(sys.argv[2])

    updated = update_status(task_id, "in-progress")

    if updated:
        print(f"Task {task_id} marked as in progress")
    else:
        print("Task not found.")

else:
    print("Unknown command.")