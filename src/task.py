from datetime import datetime


class Task:
    def __init__(self, task_id, description):
        self.id = task_id
        self.description = description
        self.status = "todo"
        self.createdAt = datetime.now().isoformat()
        self.updatedAt = self.createdAt