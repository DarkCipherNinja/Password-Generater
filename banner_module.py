# banner_module.py

import os
import random
import shutil
from colorama import init, Fore, Style
import pyfiglet

# Initialize colorama for color support
init(autoreset=True)

# Set banner text and social media information
banner_text = "DarkCipherNinja"
social_media_usernames = [
    ("GitHub", "@DarkCipherNinja"),
    ("Telegram", "@black_ninja_pk"),
    ("Coder", "@crazy_arain"),
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_gradient_banner(text):
    fonts = ['slant', 'banner3-D', 'block', 'digital', 'banner', 'isometric1']
    selected_font = random.choice(fonts)
    
    # Get console width and center the banner text
    console_width = shutil.get_terminal_size((80, 20)).columns
    banner = pyfiglet.figlet_format(text, font=selected_font).splitlines()
    centered_banner = [line.center(console_width) for line in banner]
    
    # Display banner with gradient effect
    colors = [Fore.GREEN + Style.BRIGHT, Fore.YELLOW + Style.BRIGHT, Fore.RED + Style.BRIGHT]
    total_lines = len(centered_banner)
    section_size = total_lines // len(colors)
    for i, line in enumerate(centered_banner):
        if i < section_size:
            print(colors[0] + line)
        elif i < section_size * 2:
            print(colors[1] + line)
        else:
            print(colors[2] + line)

def display_banner_and_social():
    clear_console()
    create_gradient_banner(banner_text)
    print(Fore.LIGHTMAGENTA_EX + "Follow us on:")
    for platform_name, username in social_media_usernames:
        print(f"{Fore.CYAN}{platform_name + ':'} {Fore.GREEN}{username}")
