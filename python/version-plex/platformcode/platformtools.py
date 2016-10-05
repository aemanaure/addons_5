# -*- coding: utf-8 -*-
#------------------------------------------------------------
# pelisalacarta - XBMC Plugin
# platformtools
# http://blog.tvalacarta.info/plugin-xbmc/pelisalacarta/
#------------------------------------------------------------
# Herramientas responsables de adaptar los diferentes 
# cuadros de dialogo a una plataforma en concreto,
# en este caso plex
# ------------------------------------------------------------

import os
from core import config

BUTTON_DEFAULT = {'label': "Por defecto", 'function': 'SettingsWindow_default', 'visible': True, 'close': False}


def dialog_ok(heading, line1, line2="", line3=""):
    return True


def dialog_notification(heading, message, icon=0, time=5000, sound=True):
    return True


def dialog_yesno(heading, line1, line2="", line3="", nolabel="No", yeslabel="Si", autoclose=""):
    return True


def dialog_select(heading, list): 
    return 1


def dialog_progress(heading, line1, line2="", line3=""):
    class Dialog(object):
        def __init__(self,heading, line1, line2="", line3=""):
            self.canceled = False
            pass

        def iscanceled(self):
            return self.canceled

        def update(self,percent, text):
            return True

        def close(self):
            self.canceled = True
            return True

    return Dialog(heading, line1, line2, line3)


def dialog_progress_bg(heading, message=""):
    pass


def dialog_input(default="", heading="", hidden=False):
    return default


def dialog_numeric(type, heading, default=""):
    pass


def itemlist_refresh():
    pass


def itemlist_update(item):
    pass


def render_items(itemlist, parentitem):
    pass


def is_playing():
    return False


def play_video(item):
    pass


def show_channel_settings(list_controls=None, dict_values=None, caption="", callback=None, item=None,
                          custom_button=BUTTON_DEFAULT, channelpath = None):
    """
    Muestra un cuadro de configuracion personalizado para cada canal y guarda los datos al cerrarlo.

    Parametros: ver descripcion en xbmc_config_menu.SettingsWindow
    @param list_controls: lista de elementos a mostrar en la ventana.
    @type list_controls: list
    @param dict_values: valores que tienen la lista de elementos.
    @type dict_values: dict
    @param caption: titulo de la ventana
    @type caption: str
    @param callback: función que se llama al pulsar el boton 'Ok'. Recibe item y dict_values como argumentos.
    @type callback: str
    @param item: item para el que se muestra la ventana de configuración.
    @type item: Item
    @param custom_button: botón personalizado, que se muestra junto a "OK" y "Cancelar".
    @type custom_button: dict con las siguientes claves obligatorias:
        1. 'label':  Etiqueta mostrada en el boton
        2. 'function': Funcion que se llama al pulsar este boton. Recibe el item como argumento.
        3. 'visible': Si es True el boton sera mostrado, sino no.
        4. 'close': Si es True la ventana se cerrara al pulsar el boton.

    @return: devuelve el valor devuelto por la funcion callback o custom_button['function'] en funcion del boton pulsado.
    @rtype: SettingsWindow
    """
    from platformcode import plex_config_menu
    return plex_config_menu.show_channel_settings(list_controls=list_controls, dict_values=dict_values, caption=caption,
                                                  callback=callback, item=item, custom_button=custom_button, channelpath=channelpath)