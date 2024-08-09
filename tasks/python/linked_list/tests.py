import pytest
from tasks.python.linked_list.solution import Task, TasksManager


@pytest.fixture
def tm():
    task_a = Task('a')
    task_a.next = task_b = Task('b')
    task_b.next = Task('c')

    task_manager = TasksManager()
    task_manager.first_task = task_a
    task_manager.tasks_quantity = 3
    return task_manager


@pytest.mark.full
class TestAddTask:
    @pytest.mark.basic
    def test_add_task_first_task(self):
        tm = TasksManager()
        tm.add_task('task')
        assert tm.tasks_quantity == 1
        assert tm.first_task.name == 'task'
        assert tm.first_task.description == ''

    def test_add_task_without_name(self):
        tm = TasksManager()
        tm.add_task('')
        assert tm.tasks_quantity == 0
        assert tm.first_task is None

    @pytest.mark.basic
    def test_add_task_without_position(self):
        tm = TasksManager()
        tm.add_task('task1')
        tm.add_task('task2')
        assert tm.tasks_quantity == 2
        assert tm.first_task.name == 'task1'
        assert tm.first_task.next.name == 'task2'

    def test_add_task_at_first_position(self, tm):
        tm.add_task('task', add_position=0)
        assert tm.tasks_quantity == 4
        assert tm.first_task.name == 'task'
        assert tm.first_task.next.name == 'a'
        assert tm.first_task.next.next.name == 'b'
        assert tm.first_task.next.next.next.name == 'c'

    def test_add_task_at_second_position(self, tm):
        tm.add_task('task', add_position=1)
        assert tm.tasks_quantity == 4
        assert tm.first_task.name == 'a'
        assert tm.first_task.next.name == 'task'
        assert tm.first_task.next.next.name == 'b'
        assert tm.first_task.next.next.next.name == 'c'

    def test_add_task_at_last_position(self, tm):
        tm.add_task('task', add_position=4)
        assert tm.tasks_quantity == 4
        assert tm.first_task.name == 'a'
        assert tm.first_task.next.name == 'b'
        assert tm.first_task.next.next.name == 'c'
        assert tm.first_task.next.next.next.name == 'task'

    def test_add_task_negative_position(self, tm):
        tm.add_task('task', add_position=-1)
        assert tm.tasks_quantity == 3
        assert tm.first_task.name == 'a'
        assert tm.first_task.next.name == 'b'
        assert tm.first_task.next.next.name == 'c'

    def test_add_task_invalid_position(self, tm):
        tm.add_task('task', add_position=10)
        assert tm.tasks_quantity == 3
        assert tm.first_task.name == 'a'
        assert tm.first_task.next.name == 'b'
        assert tm.first_task.next.next.name == 'c'

    @pytest.mark.basic
    def test_add_task_same_name(self, tm):
        tm.add_task('a')
        assert tm.tasks_quantity == 3


@pytest.mark.full
class TestRemoveTask:
    def test_remove_first_task(self, tm):
        removed_task = tm.remove_task('a')
        assert removed_task.name == 'a'
        assert tm.tasks_quantity == 2
        assert tm.first_task.name == 'b'
        assert tm.first_task.next.name == 'c'

    @pytest.mark.basic
    def test_remove_second_task(self, tm):
        removed_task = tm.remove_task('b')
        assert removed_task.name == 'b'
        assert tm.tasks_quantity == 2
        assert tm.first_task.name == 'a'
        assert tm.first_task.next.name == 'c'

    def test_remove_last_task(self, tm):
        removed_task = tm.remove_task('c')
        assert removed_task.name == 'c'
        assert tm.tasks_quantity == 2
        assert tm.first_task.name == 'a'
        assert tm.first_task.next.name == 'b'

    def test_remove_non_existent_task(self, tm):
        removed_task = tm.remove_task('task')
        assert removed_task is None
        assert tm.tasks_quantity == 3
        assert tm.first_task.name == 'a'
        assert tm.first_task.next.name == 'b'
        assert tm.first_task.next.next.name == 'c'

    @pytest.mark.basic
    def test_remove_task_empty(self):
        tm = TasksManager()
        removed_task = tm.remove_task('task')
        assert removed_task is None
        assert tm.tasks_quantity == 0


@pytest.mark.full
class TestFindTask:
    def test_find_task_first_position(self, tm):
        position = tm.find_task('a')
        assert position == 0

    @pytest.mark.basic
    def test_find_task_second_position(self, tm):
        position = tm.find_task('b')
        assert position == 1

    def test_find_task_last_position(self, tm):
        position = tm.find_task('c')
        assert position == 2

    def test_find_non_existent_task(self, tm):
        position = tm.find_task('d')
        assert position == -1

    @pytest.mark.basic
    def test_find_task_empty(self, tm):
        position = tm.find_task('d')
        assert position == -1


@pytest.mark.full
class TestMoveTask:
    def test_move_first_task_to_first(self, tm):
        tm.move_task('a', 0)
        assert tm.find_task('a') == 0

    def test_move_first_task_to_second(self, tm):
        tm.move_task('a', 1)
        assert tm.find_task('a') == 1

    def test_move_first_task_to_last(self, tm):
        tm.move_task('a', 2)
        assert tm.find_task('a') == 2

    @pytest.mark.basic
    def test_move_second_task_to_first(self, tm):
        tm.move_task('b', 0)
        assert tm.find_task('b') == 0

    def test_move_second_task_to_second(self, tm):
        tm.move_task('b', 1)
        assert tm.find_task('b') == 1

    @pytest.mark.basic
    def test_move_second_task_to_last(self, tm):
        tm.move_task('b', 2)
        assert tm.find_task('b') == 2

    def test_move_last_task_to_first(self, tm):
        tm.move_task('c', 0)
        assert tm.find_task('c') == 0

    def test_move_last_task_to_second(self, tm):
        tm.move_task('c', 1)
        assert tm.find_task('c') == 1

    def test_move_last_task_to_last(self, tm):
        tm.move_task('c', 2)
        assert tm.find_task('c') == 2

    def test_move_non_existent_task(self, tm):
        tm.move_task('task', 0)
        assert tm.find_task('task') == -1


@pytest.mark.full
class TestListTasks:
    @pytest.mark.basic
    def test_list_tasks(self, tm):
        tasks = tm.list_tasks()
        assert len(tasks) == 3
        assert tasks[0].name == 'a'
        assert tasks[1].name == 'b'
        assert tasks[2].name == 'c'

    def test_list_tasks_only_one(self):
        tm = TasksManager()
        tm.add_task('task')
        tasks = tm.list_tasks()
        assert tasks[0].name == 'task'

    @pytest.mark.basic
    def test_list_tasks_empty(self):
        tm = TasksManager()
        tasks = tm.list_tasks()
        assert tasks == []


if __name__ == "__main__":
    pytest.main()
