class View:
    def greeting(self):
        print("Вас приветствует приложение заметки!")

    def show_main_menu(self):
        print("Выберите пункт меню:\n"
              "\t1. Добавить заметку\n"
              "\t2. Прочитать/Изменить/Удалить заметку\n"
              "\t3. Показать все заметки\n"
              "\t4. Сохранить\n"
              "\t0. Выйти")

    def show_manage_record_menu(self):
        print("Выберите пункт меню:\n"
              "\t1. Прочитать\n"
              "\t2. Изменить\n"
              "\t3. Удалить\n")

    def error(self):
        print("Введите корректное значение")
    def not_found(self):
        print("Значения не найдено. Попробуйте еще раз.")

    def saved_info(self):
        print("Заметки сохранены!")

    def show_record(self, record):
        result = f"ID: {str(record.get_id())}|\t"
        result += f"[{str(record.get_date())}]\t"
        result += f"[{str(record.get_name())}]\n"
        result += f"{str(record.get_text())}\n"
        print(result)

    def show_read_all_banner(self, count):
        result = f"\t***Все заметки***\n" \
                 f"Найдено заметок: {count}\n"
        print(result)

    def info_record_msg(self, key):
        info = {'add': 'добавлена', 'del': 'удалена', 'edit': 'изменена'}
        print(f"Заметка успешно {info[key]}!")

    def input_record_name(self):
        return input(f"Введите название заметки:")

    def input_record_text(self):
        return input(f"Текст заметки:")

    def edit_record(self, record):
        record.set_text(self.input_record_text())
        record.update_date()
        self.info_note_msg('edit')

    def input_number(self, limit, preset):
        presets = {'id': 'заметки', 'menu': 'пункта меню'}
        value = 0
        while True:
            try:
                value = int(input(f"Введите номер {presets[preset]}: "))
            except ValueError:
                self.error()
                continue
            if 0 <= value <= limit:
                break
            else:
                self.not_found()
        return value

    def exit_msg(self):
        print("Досведание!")
