import pickle
from record import Note
from view import View


class ListOfNotes:
    __notepad = []
    __view = View()
    __index = 0
    __index_stack = []

    def __init__(self):
        try:
            with open('notepad.pkl', 'rb') as file:
                self.__notepad = pickle.load(file)
                self.__index = len(self.__notepad)
            with open('indexes.pkl', 'rb') as file:
                self.__index_stack = pickle.load(file)
        except EOFError:
            self.__notepad = []
            self.__view = View()
            self.__index = 0
            self.__index_stack = []

    def add_record(self):
        record = Note()
        record.set_name(self.__view.input_record_name())
        record.set_text(self.__view.input_record_text())
        record.update_date()
        if len(self.__index_stack) == 0:
            record.set_id(self.__index)
        else:
            record.set_id(self.__index_stack.pop())
        self.__notepad.append(record)
        self.__index = len(self.__notepads)
        self.__view.info_note_msg('add')

    def delete_record(self, record):
        self.__index_stack.append(record.get_id())
        self.__notepad.remove(record)
        if len(self.__notepad) == 0:
            self.__index_stack.clear()
        self.__view.info_note_msg('del')


    def read_all_notepad(self):
        self.__view.show_read_all_banner(len(self.__notepad))
        for record in self.__notepad:
            self.__view.show_record(record)

    def manage_record_by_id(self):
        commands =  {1: self.__view.show_record,
                     2: self.__view.edit_record,
                     3: self.delete_record}
        flag = False
        self.__view.show_manage_record_menu()
        choice = self.__view.input_number(len(commands.keys()), 'menu')
        value = self.__view.input_number(self.__index, 'id')
        for record in self.__notepad:
            if record.get_id() == value:
                commands[choice](record)
                flag = True
        if not flag:
            self.__view.not_found()

    def save_notepad_to_file(self):
        with open('notes.pkl', 'wb') as file:
            pickle.dump(self.__notepad, file,
                        protocol=pickle.HIGHEST_PROTOCOL)
        with open('indexes.pkl', 'wb') as file:
            pickle.dump(self.__index_stack, file,
                        protocol=pickle.HIGHEST_PROTOCOL)
        self.__view.saved_info()




