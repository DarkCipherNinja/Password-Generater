# password_generator.py
import random
import string
from itertools import product
import time
from colorama import Fore, Style, init
import banner_module  # Import the banner module

init(autoreset=True)

def load_custom_alphabets(filename="custom_pass_file.txt"):
    try:
        with open(filename, "r") as file:
            custom_alphabets = file.read().strip()
            if custom_alphabets:
                return custom_alphabets
            else:
                print(Fore.RED + "Error: The custom alphabet file is empty.")
                return None
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file {filename} was not found.")
        return None

def generate_and_save_combinations(length, character_set, filename):
    if not character_set:
        print(Fore.RED + "Error: No character type selected for password generation.")
        return
    
    total_combinations = len(character_set) ** length
    print(Fore.CYAN + f"Generating {total_combinations} combinations...")

    with open(filename, "w") as file:
        for idx, combination in enumerate(product(character_set, repeat=length), start=1):
            file.write(''.join(combination) + '\n')
            if idx % 1000 == 0:
                progress = (idx / total_combinations) * 100
                print(Fore.GREEN + f"Progress: {progress:.2f}% ({idx}/{total_combinations})")
                time.sleep(0.1)
    print(Fore.GREEN + f"All combinations saved to {filename}")

def display_menu():
    print(Fore.CYAN + Style.BRIGHT + "Select an option:")
    print(Fore.YELLOW + "1. All Alphabets (Uppercase)")
    print(Fore.YELLOW + "2. All Alphabets (Lowercase)")
    print(Fore.YELLOW + "3. Both Uppercase & Lowercase")
    print(Fore.YELLOW + "4. All Numbers")
    print(Fore.YELLOW + "5. All Symbols")
    print(Fore.YELLOW + "6. Alphabets (Lowercase) & Numbers")
    print(Fore.YELLOW + "7. Alphabets (Lowercase) & Symbols")
    print(Fore.YELLOW + "8. Alphabets (Uppercase) & Numbers")
    print(Fore.YELLOW + "9. Alphabets (Uppercase) & Symbols")
    print(Fore.YELLOW + "10. Numbers & Symbols")
    print(Fore.YELLOW + "11. Custom (from file custom_pass_file.txt)")
    print(Fore.YELLOW + "12. All (Alphabets Lowercase & Uppercase, Symbols, Numbers)")

def main():
    banner_module.display_banner_and_social()  # Display banner and social media info
    password_length = int(input(Fore.CYAN + "Enter password length (min 2): "))
    display_menu()
    # Continue with the rest of your password generator logic here

if __name__ == "__main__":
    main()
