from class_data import Data
from class_view import View
from class_process import Process

if __name__ == "__main__":
    data = Data()
    view = View()
    process = Process(data)

    process.get_user_input()
    view.display_table(data.get_entries())
