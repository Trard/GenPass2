from main_menu.interface import main_menu_interface
from checkpas_interface import check_interface
from generator_interface import gen_interface
from set_interface import settings_interface

def entry_togenerator():
    main_menu_interface.place_forget()
    gen_interface.place()

def entry_tocheck():
    main_menu_interface.place_forget()
    check_interface.place()

def entry_toset():
    main_menu_interface.place_forget()
    settings_interface.place()

main_menu_interface.portal_generatepas_button['command'] = entry_togenerator
main_menu_interface.portal_checkpas_button['command'] = entry_tocheck
main_menu_interface.portal_settings_button['command'] = entry_toset
