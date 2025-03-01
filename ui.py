import flet as ft
import functional


# Основная логика интерфейса
def main(page: ft.Page):
    page.title = 'CLA File Manager'

    def show_alert(text):
        result_dialog = ft.AlertDialog(
            content=ft.Column(
                [ft.Text(text)],
                expand=True,
                scroll=True
            )
        )
        page.open(result_dialog)

    # Тут у нас логика каждой кнопки
    def pick_files_copy(e):
        def copy_button(e: ft.FilePickerResultEvent):
            if not e.files:
                show_alert('Файл не выбран!')
            try:
                functional.copy_file(e.files[0].path)
                show_alert('Файл успешно скопирован!')
            except Exception as ex:
                show_alert(f'Ошибка! {ex}')

        file_picker.pick_files()
        file_picker.on_result = copy_button

    def pick_files_delete(e):
        def delete_button(e: ft.FilePickerResultEvent):
            if not e.files:
                show_alert('Файл не выбран!')
            try:
                functional.delete_file(e.files[0].path)
                show_alert('Файл успешно удален!')
            except Exception as ex:
                show_alert(f'Ошибка! {ex}')

        file_picker.on_result = delete_button
        file_picker.pick_files()

    def pick_dir_count(e):
        def count_button(e: ft.FilePickerResultEvent):
            if not e.path:
                show_alert('Директория не выбрана!')
            try:
                counted = functional.count_files(e.path)
                show_alert(f'В директории {e.path} находится {counted} файл')
            except Exception as ex:
                show_alert(f'Ошибка! {ex}')

        file_picker.on_result = count_button
        file_picker.get_directory_path()

    def pick_re_search(e):
        def re_search_button(e: ft.FilePickerResultEvent):
            if not e.path:
                show_alert('Директория не выбрана!')
            try:
                result = functional.re_search(regex_dialog.value, e.path)
                f_result = '\n'.join(result)
                show_alert(f_result)
            except Exception as ex:
                show_alert(f'Ошибка! {ex}')

        file_picker.on_result = re_search_button
        file_picker.get_directory_path()

    def pick_date_files(e):
        def date_files_button(e: ft.FilePickerResultEvent):
            if not e.path:
                show_alert('Директория не выбрана!')
            try:
                functional.date_file(e.path, check_rec_date.value)
                show_alert('Файла успешно протаймерованы!')
            except Exception as ex:
                show_alert(f'Ошибка! {ex}')

        file_picker.on_result = date_files_button
        file_picker.get_directory_path()

    def pick_analyze(e):
        def analyze_dir_button(e: ft.FilePickerResultEvent):
            if not e.path:
                show_alert('Директория не выбрана!')
            try:
                result = functional.analyze(e.path)
                f_result = '\n'.join(result)
                show_alert(f_result)
            except Exception as ex:
                show_alert(f'Ошибка! {ex}')

        file_picker.on_result = analyze_dir_button
        file_picker.get_directory_path()

    # Файл пикер, который достает файлы
    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)
    # Кнопки мои кнопки
    btn_copy = ft.ElevatedButton('Копировать файл', on_click=pick_files_copy)
    btn_delete = ft.ElevatedButton('Удалить файл', on_click=pick_files_delete)
    btn_count = ft.ElevatedButton('Посчитать файлы', on_click=pick_dir_count)
    btn_research = ft.ElevatedButton('Найти файлы по фильтру', on_click=pick_re_search)
    btn_date = ft.ElevatedButton('Протаймеровать файлы', on_click=pick_date_files)
    regex_dialog = ft.TextField(
        hint_text='Введите регулярное выражение'
    )
    check_rec_date = ft.Checkbox(label='Рекурсивность функции таймерования', value=False)
    btn_analyze = ft.ElevatedButton('Проанализировать директорию', on_click=pick_analyze)
    # Красивое расположение кнопок
    file_operations = ft.Column(
        controls=[
            ft.Row([btn_copy, btn_delete]),
            ft.Row([btn_count, btn_analyze]),
        ],
        spacing=10,
    )
    search_operations = ft.Column(
        controls=[
            ft.Row([regex_dialog, btn_research]),
            ft.Row([check_rec_date, btn_date]),
        ],
        spacing=10,
    )

    page.add(
        ft.Text("Операции с файлами"),
        file_operations,
        ft.Divider(),
        ft.Text("Поиск и таймерование"),
        search_operations,
    )

    page.update()


# Запускаем
ft.app(target=main)