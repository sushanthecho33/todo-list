from datetime import datetime
from typing import Dict, Optional

Task = Dict[str, object]

class TaskManager:
    def __init__(self, filename: str = 'tasks.txt') -> None:
        self.filename = filename
    
    def add_task(self, task_name: str, description: str = '') -> Task:
        """Add a new task and store it in txt file"""
        task: Task = {
            'name': task_name,
            'description': description,
            'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'completed': False
        }
        self.save_task(task)
        return task
    
    def save_task(self, task: Task) -> None:
        """Save task to txt file"""
        try:
            with open(self.filename, 'a', encoding='utf-8') as f:
                f.write(f"Task: {task['name']}\n")
                f.write(f"Description: {task['description']}\n")
                f.write(f"Created: {task['created']}\n")
                f.write(f"Completed: {task['completed']}\n")
                f.write("-" * 50 + "\n")
            print(f"Task saved: {task['name']}")
        except Exception as e:
            print(f"Error saving task: {e}")
    
    def load_tasks(self) -> Optional[str]:
        """Load all tasks from txt file"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print("No tasks file found")
            return None
    
    def clear_tasks(self) -> None:
        """Clear all tasks from txt file"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write("")
            print("Tasks cleared")
        except Exception as e:
            print(f"Error clearing tasks: {e}")

# Execute tasks from main.py
if __name__ == "__main__":
    manager = TaskManager('tasks.txt')
    
    # Example: Add sample tasks
    manager.add_task("Buy groceries", "Milk, eggs, bread")
    manager.add_task("Complete project", "Finish todo list app")
    manager.add_task("Study Python", "Learn decorators and OOP")
    
    # Display all tasks
    print("\n=== All Tasks ===")
    print(manager.load_tasks())
