# Criar solução de lista simplesmente encadeada

class Task:
    def __init__(self, name: str, description=''):
        self.name = name.lower()
        self.description = description.lower()
        self.next = None


class TasksManager:
    first_task = None
    tasks_quantity = 0

    def add_task(self, name: str, description='', add_position=None):
        if not name:
            return

        if add_position is None:
            add_position = self.tasks_quantity + 1

        if add_position < 0 or add_position > self.tasks_quantity + 1:
            return

        if self.find_task(name) != -1:
            return

        new_task = Task(name, description)
        self.tasks_quantity += 1
        if self.first_task is None:
            self.first_task = new_task
            return

        if add_position == 0:
            new_task.next = self.first_task
            self.first_task = new_task
            return

        position = 0
        previous = None
        task = self.first_task
        while task.next is not None:
            if position == add_position:
                previous.next = new_task
                new_task.next = task
                return

            previous = task
            task = task.next
            position += 1

        if position == add_position:
            previous.next = new_task
            new_task.next = task
            return

        task.next = new_task

    def remove_task(self, name: str):
        if self.tasks_quantity == 0:
            return

        previous = None
        position = 0
        task = self.first_task
        while task.next is not None:
            if task.name == name:
                self.tasks_quantity -= 1
                if position == 0:
                    self.first_task = task.next
                    return task

                previous.next = task.next
                return task

            previous = task
            task = task.next
            position += 1

        if task.name == name:
            previous.next = None
            self.tasks_quantity -= 1
            return task

    def find_task(self, name: str):
        if self.tasks_quantity == 0:
            return -1

        position = 0
        task = self.first_task
        while task.next is not None:
            if task.name == name:
                return position

            position += 1
            task = task.next

        if task.name == name:
            return position

        return -1

    def move_task(self, name: str, new_position: int):
        if self.tasks_quantity == 0:
            return

        if new_position < 0 or new_position > self.tasks_quantity - 1:
            return

        moved_task = self.remove_task(name)
        if moved_task is None:
            return

        self.add_task(moved_task.name, moved_task.description, new_position)

    def list_tasks(self):
        if self.first_task is None:
            return []

        tasks = []
        task = self.first_task
        while task.next is not None:
            tasks.append(task)
            task = task.next

        tasks.append(task)
        return tasks
