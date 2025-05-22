"""
Пример использования библиотеки rich
"""

from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Список дел")
table.add_column("№", style="cyan")
table.add_column("Задача", style="magenta")
table.add_column("Статус", style="green")

tasks = [
    ("1", "Написать код", "✅"),
    ("2", "Проверить баги", "❌"),
    ("3", "Запустить тесты", "⏳"),
]


def print_tasks():
    for task in tasks:
        table.add_row(*task)

    console.print(table)
