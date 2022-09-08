import function_generator as fg
from checkpas_interface import CheckUI, check_interface
import checkpas_interface as cp
from main_menu.interface import main_menu_interface
from generator_interface import symbolbet, required_symbolbet, range_len_pas
from tkinter import messagebox
import tkinter as tk

def check_password():
    password = CheckUI.check_password_entry.get()
    if fg.selection_letters(fg.only_type_symbols(password, 'letters'), 'great_letters') == '' and cp.allow_letter.get() and cp.allow_gr_letter.get():
        result = 'Нет больших букв'
    elif fg.selection_letters(fg.only_type_symbols(password, 'letters'), 'small_letters') == '' and cp.allow_letter.get() and cp.allow_sm_letter.get():
        result = 'Нет маленьких букв'
    elif fg.only_type_symbols(password, 'numbers') == '' and cp.allow_number.get():
        result = 'В пароле нет цифр'
    elif fg.only_type_symbols(password, 'other') == '' and cp.allow_other.get():
        result = 'В пароле нет символов помимо цифр и букв'
    elif not cp.len_checkpas_range.get()[0] <= len(password) <= cp.len_checkpas_range.get()[1]:
        result = f'Длина пароля не в рамках длины [{cp.len_checkpas_range.get()[0]}, {cp.len_checkpas_range.get()[1]}]'
    else:
        result = 'Проверка пройдена успешно'
        for symbol in password:
            if cp.allowed_symbolbet.get().count(symbol) == 0:
                result = f'Символа "{symbol}" нету в разрешенном списке!'
                break
    messagebox.showinfo("Результат", result)


def delete_symbols():
    def logic_delete_symbols(example_symbolbet):
        list_of_symbols = check_interface.delete_symbols_entry.get().fg.split(' ')
        check_interface.delete_symbols_entry.delete(0)
        result = example_symbolbet.delete_symbols(list_of_symbols)
        messagebox.showinfo('Результат', result)
        automatically_update_list()
    if cp.select_checksymbolbet_action.get() == 1:
        logic_delete_symbols(cp.allowed_symbolbet)
    elif cp.select_checksymbolbet_action.get() == 2:
        logic_delete_symbols(cp.required_check_symbolbet)


def add_symbols():
    def logic_add_symbols(example_symbolbet):
        list_of_symbols = check_interface.add_symbols_entry.get().split(' ')
        check_interface.add_symbols_entry.delete(0)
        result = example_symbolbet.add_symbols(list_of_symbols)
        messagebox.showinfo('Результат', result)
    if cp.select_checksymbolbet_action.get() == 1:
        logic_add_symbols(cp.allowed_symbolbet)
    elif cp.select_checksymbolbet_action.get() == 2:
        logic_add_symbols(cp.required_check_symbolbet)



def stay_symbols():
    def logic_stay_symbols(example_symbolbet):
        list_of_symbols = check_interface.stay_symbols_entry.get().split(' ')
        check_interface.stay_symbols_entry.delete(0)
        result = example_symbolbet.stay_symbols(list_of_symbols)
        messagebox.showinfo("Результат", result)
    if cp.select_checksymbolbet_action.get() == 1:
        logic_stay_symbols(cp.allowed_symbolbet)
    elif cp.select_checksymbolbet_action.get() == 2:
        logic_stay_symbols(cp.required_check_symbolbet)


def select_range():
    diapason_list = check_interface.select_range_entry.get().split(' ')
    check_interface.select_range_entry.delete(0)
    if len(diapason_list) == 1:
        result = cp.len_checkpas_range.set(diapason_list[0], diapason_list[0])
    elif len(diapason_list) > 1:
        result = cp.len_checkpas_range.set(diapason_list[0], diapason_list[1])
    messagebox.showinfo("Результат", result)


def get_range():
    result = str(cp.len_checkpas_range.get()[0]) + ' ' + str(cp.len_checkpas_range.get()[1])
    check_interface.get_range_entry.delete(0)
    check_interface.get_range_entry.insert(0, result)


def stay_letters():
    if cp.allow_letter.get():
        cp.allowed_symbolbet.delete_black_symbols(fg.split(fg.only_type_symbols(cp.allowed_symbolbet.get_black(), 'letters')))
        check_interface.gr_letter_checkbutton['state'] = tk.NORMAL
        check_interface.sm_letter_checkbutton['state'] = tk.NORMAL
    else:
        cp.allowed_symbolbet.add_black_symbols(fg.split(fg.only_type_symbols(cp.allowed_symbolbet.get(), 'letters')))
        check_interface.gr_letter_checkbutton['state'] = tk.DISABLED
        check_interface.sm_letter_checkbutton['state'] = tk.DISABLED


def stay_sm_letters():
    if cp.allow_sm_letter.get():
        cp.allowed_symbolbet.delete_black_symbols(
            fg.split(fg.selection_letters(fg.only_type_symbols(cp.allowed_symbolbet.get_black(), 'letters'), 'small_letters')))
        if cp.allow_gr_letter.get():
            check_interface.letter_checkbutton['state'] = tk.NORMAL
    else:
        cp.allowed_symbolbet.add_black_symbols(
            fg.split(fg.selection_letters(fg.only_type_symbols(cp.allowed_symbolbet.get(), 'letters'), 'small_letters')))
        check_interface.letter_checkbutton['state'] = tk.DISABLED


def stay_gr_letters():
    if cp.allow_gr_letter.get():
        cp.allowed_symbolbet.delete_black_symbols(
            fg.split(fg.selection_letters(fg.only_type_symbols(cp.allowed_symbolbet.get_black(), 'letters'), 'great_letters')))
        if cp.allow_sm_letter.get():
            check_interface.letter_checkbutton['state'] = tk.NORMAL
    else:
        cp.allowed_symbolbet.add_black_symbols(
            fg.split(fg.selection_letters(fg.only_type_symbols(cp.allowed_symbolbet.get(), 'letters'), 'great_letters')))
        check_interface.letter_checkbutton['state'] = tk.DISABLED


def stay_numbers():
    if cp.allow_number.get():
        cp.allowed_symbolbet.delete_black_symbols(fg.split(fg.only_type_symbols(cp.allowed_symbolbet.get_black(), 'numbers')))
    else:
        cp.allowed_symbolbet.add_black_symbols(fg.split(fg.only_type_symbols(cp.allowed_symbolbet.get(), 'numbers')))


def stay_other():
    if cp.allow_other.get():
        cp.allowed_symbolbet.delete_black_symbols(fg.split(fg.only_type_symbols(cp.allowed_symbolbet.get_black(), 'other')))
    else:
        cp.allowed_symbolbet.add_black_symbols(fg.split(fg.only_type_symbols(cp.allowed_symbolbet.get(), 'other')))

def automatically_update_list():
    if check_interface.get_list_entry.get() != '':
        get_list()

def get_list():
    def logic_get_list(example_symbolbet):
        check_interface.get_list_entry.delete(0)
        check_interface.get_list_entry.insert(0, fg.divide_word(example_symbolbet.get()))
    if cp.select_checksymbolbet_action.get() == 1:
        logic_get_list(cp.allowed_symbolbet)
    elif cp.select_checksymbolbet_action.get() == 2:
        logic_get_list(cp.required_check_symbolbet)


def leave():
    check_interface.place_forget()
    main_menu_interface.place()

def set_standart():
    cp.allowed_symbolbet.delete_symbols(fg.split(cp.allowed_symbolbet.get()))
    cp.allowed_symbolbet.add_symbols(fg.split('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*'))
    cp.allowed_symbolbet.delete_black_symbols(fg.split(cp.allowed_symbolbet.get_black()))
    cp.allowed_symbolbet.update_reserve()
    cp.required_check_symbolbet.delete_symbols(fg.split(cp.required_check_symbolbet.get()))
    cp.len_checkpas_range.set()
    automatically_update_list()


def set_generator_settings():
    cp.allowed_symbolbet.delete_symbols(fg.split(cp.allowed_symbolbet.get()))
    cp.required_check_symbolbet.delete_symbols(fg.split(cp.required_check_symbolbet.get()))
    cp.allowed_symbolbet.delete_black_symbols(fg.split(cp.allowed_symbolbet.get_black()))
    cp.allowed_symbolbet.add_symbols(fg.split(symbolbet.get()))
    cp.required_check_symbolbet.add_symbols(fg.split(required_symbolbet.get()))
    cp.allowed_symbolbet.add_black_symbols(fg.split(symbolbet.get_black()))
    cp.len_checkpas_range.set(range_len_pas.get()[0], range_len_pas.get()[1])


check_interface.check_password_button['command'] = check_password
check_interface.add_symbols_button['command'] = add_symbols
check_interface.delete_symbols_button['command'] = delete_symbols
check_interface.stay_symbols_button['command'] = stay_symbols
check_interface.get_list_button['command'] = get_list
check_interface.select_range_button['command'] = select_range
check_interface.get_range_button['command'] = get_range
check_interface.letter_checkbutton['command'] = stay_letters
check_interface.gr_letter_checkbutton['command'] = stay_gr_letters
check_interface.sm_letter_checkbutton['command'] = stay_sm_letters
check_interface.number_checkbutton['command'] = stay_numbers
check_interface.other_checkbutton['command'] = stay_other
check_interface.set_default_button['command'] = set_standart
check_interface.set_gen_settings_button['command'] = set_generator_settings
check_interface.leave_button['command'] = leave
