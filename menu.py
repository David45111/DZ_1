from list import ListOfNotes
from view import View


class Menu:
    __view = View()
    __notepad = ListOfNotes()
    __commands = {1: __notepad.add_record, 2: __notepad.manage_record_by_id, 3: __notepad.read_all_notepad,
                  4: __notepad.save_notepad_to_file}

    def start(self):
        self.__view.greeting()
        while(True):
            self.__view.show_main_menu()
            choice = self.__view.input_number(len(self.__commands.keys()), 'menu')
            if choice == 0:
                self.__view.exit_msg()
                break
            else:
                self.__commands[choice]()
