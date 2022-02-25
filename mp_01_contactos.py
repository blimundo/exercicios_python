"""Contactos

Elabore uma aplicação de gestão de contactos, onde será armazenado o
nome da pessoa, instituição e uma lista de contactos (telefone,
telemóvel e e-mail).

A aplicação deverá permitir a inserção, pesquisa, edição e eliminação
dos contatos. 
"""

import curses

_COLOR_PAIR_NORMAL = 1
_COLOR_PAIR_TITLE = 2
_COLOR_PAIR_INFO = 3
_COLOR_PAIR_ERROR = 4

_KEY_UP = 450
_KEY_DOWN = 456
_KEY_LEFT = 452
_KEY_RIGHT = 454

def init_colors():
    """Define colors pair in use by application"""
    curses.init_pair(_COLOR_PAIR_NORMAL, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(_COLOR_PAIR_TITLE, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(_COLOR_PAIR_INFO, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(_COLOR_PAIR_ERROR, curses.COLOR_RED, curses.COLOR_BLACK)

def write_text_xy(screen, y, x, text, color = _COLOR_PAIR_NORMAL) -> None:
    """Write a text in the given coordinate"""
    screen.addstr(y, x, text, curses.color_pair(color))

def write_info_text(screen, options: dict) -> None:
    """Write the footer text (wich hold the options avaible)"""
    screen.addstr(curses.LINES - 2, 0, '-' * curses.COLS, curses.color_pair(_COLOR_PAIR_INFO))
    x = 0
    for key, value in options.items():
        screen.addstr(curses.LINES - 1, x, f'{key:>3}', curses.color_pair(_COLOR_PAIR_TITLE))
        screen.addstr(curses.LINES - 1, x + 3, f' {value}', curses.color_pair(_COLOR_PAIR_INFO))
        x += 9 + len(value)

def show_main_screen(screen) -> int:
    """show application main screen and return user option"""
    screen.clear()
    x = (curses.COLS - 15) // 2
    y = curses.LINES // 2
    write_text_xy(screen, y, x, '~~~ Kontact ~~~', _COLOR_PAIR_TITLE)
    options = {
        'N': 'Novo contacto',
        'P': 'Pesquisar contacto',
        'S': 'Sobre',
        'X': 'Sair',
    }
    write_info_text(screen, options)
    screen.refresh()
    while True:
        key = screen.getkey()
        if key in ['n', 'p', 's', 'x']:
            return key

def show_about_screen(screen) -> None:
    """Show about screen"""
    screen.clear()
    write_text_xy(screen, 0, 0, 'Sobre', _COLOR_PAIR_TITLE)
    write_text_xy(screen, 2, 10, 'Kontact')
    write_text_xy(screen, 3, 10, 'V 0.0.1')
    write_text_xy(screen, 5, 10, 'Rolando Sanches')
    write_text_xy(screen, 6, 10, 'rolando.sanches@nosi.cv')
    write_info_text(screen, {'': 'Qualquer tecla para continuar'})
    screen.refresh()
    screen.getkey()

def show_new_contact_screen(screen) -> None:
    """Show form to create a new contact"""
    screen.clear()
    write_text_xy(screen, 0, 0, 'Novo contato', _COLOR_PAIR_TITLE)
    form = [
        {'name': 'name', 'label': 'Nome'},
        {'name': 'entity', 'label': 'Entidade'},
        {'name': 'address', 'label': 'Morada'},
        {'name': 'birthday', 'label': 'Data Nascimento'},
        {'name': 'note', 'label': 'Nota'},
    ]
    draw_form(screen, form)
    screen.refresh()
    # screen.getkey()

def draw_form(screen, form: list) -> None:
    line = 2
    for field in form:
        write_text_xy(screen, line, 3, f"{field['label']:>15}: ")
        line += 1
    line = 2
    screen.move(line, 20)
    while True:
        key = screen.get_wch()
        if key == _KEY_UP:
            if line > 2:
                line -= 1
                screen.addstr(line, 19, ' ')
        elif key == _KEY_DOWN:
            if line < 5:
                line += 1
                screen.addstr(line, 19, ' ')
        elif key == 'g':
            break
        else:
            screen.addstr(str(key))
        screen.refresh()

def main(screen) -> None:
    """Application entry point"""
    init_colors() 
    while True:
        option = show_main_screen(screen)
        if option == 'x':
            break
        elif option == 's':
            show_about_screen(screen)
        elif option == 'n':
            show_new_contact_screen(screen)

if __name__ == '__main__':
    curses.wrapper(main)
