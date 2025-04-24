from datetime import datetime

from classes.Import_Module_Package.application.db.people import get_employees
from classes.Import_Module_Package.application.print_tables import rich_example
from classes.Import_Module_Package.application.print_tables.rich_example import print_tasks
from classes.Import_Module_Package.application.salary import calculate_salary

if __name__ == "__main__":
    print(f'Текущая дата:{datetime.today().date()}')
    calculate_salary()
    get_employees()

    #     задание № 4
    print(rich_example.__doc__)
    print_tasks()
