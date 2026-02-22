from random import choice
from pygame import *
from settings import *

from sounds import load_sounds
from keys import draw_keys, creare_key_rects
from buttons import Button
from ui.settings_menu import SettingsMenu
from ui.toggle_switch import ToggleSwitch
from soundgen import generate_random_bank
init()
display.set_caption("Piano Game")

sounds = load.sounds(KEYS)
all_sounds_list = list(sounds.values())
GEN_DIR = "assets/data/sounds"
generated_sounds = {}

key_rects = create_key_rects(len(KEYS))
keys_list = list(KEYS.keys())
my_font = font.SysFont("Arial", 24)
pressed_keys = set()

screen_mode = "main"
settings_menu = None
random_toggle = None
use_random_sounds = False
current_volume = 1.0
for s in sounds.values():
    try:
        s.set_volume(current_volume)
    except Exception:
        pass

num_keys = len(KEYS)
keys_list = list(KEYS.keys())[:num_keys]
key_rects = create_key_rects(num_keys)

def _on_toggle_random(value: bool):
    global use_random_sounds, generated_sounds
    use_random_sounds = bool(value)

    if use_random_sounds:
        paths = generate_random_bank(GEN_DIR, len(KEYS))
        generated_sounds = {}
        for key_name, path in zip(KEYS.keys(), paths):
            try:
                snd = mixer.Sound(path)
                snd.set_volume(current_volume)
                generated_sounds[key_name] = snd
            except Exception:
                pass
    else:
        generated_sounds = {}

def apply_settings(volume: float, key_count: int):
    global current_volume, num_keys, keys_list, key_rects, pressed_keys
    current_volume = float(max(0.0, min(1.0, volume)))
    for s in sounds.values():
        try:
            s.set_volume(current_volume)
        except Exception:
            pass

    for s in generated_sounds.values():
        try:
            s.set_volume(current_volume)
        except Exception:
            pass

key_count = max(1, min(len(KEYS), int(key_count)))
if key_count != num_keys:
    num_keys = key_count
    keys_list = list(KEYS.keys())[:num_keys]
    key_rects = create_key_rects(num_keys)
    pressed_keys = {i for i in pressed keys if i < num_keys}