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

def generate_and_save_random_passwords(length, character_set, num_passwords=300, filename="random_passwords.txt"):
    if not character_set:
        print(Fore.RED + "Error: No character type selected for password generation.")
        return
    
    print(Fore.CYAN + f"Generating {num_passwords} random passwords...")
    
    with open(filename, "w") as file:
        for idx in range(num_passwords):
            password = ''.join(random.choices(character_set, k=length))
            file.write(password + '\n')
            
            # Display progress for large sets
            if idx % 50 == 0:
                progress = (idx / num_passwords) * 100
                print(Fore.GREEN + f"Progress: {progress:.2f}% ({idx}/{num_passwords}) passwords generated.")
                time.sleep(0.1)
    
    print(Fore.GREEN + f"{num_passwords} random passwords saved to {filename}")

# Menu-driven password generation based on user choice
def generate_passwords(length, character_set, option_name):
    print(Fore.CYAN + "Choose an option:")
    print(Fore.YELLOW + "1. Generate random passwords")
    print(Fore.YELLOW + "2. Generate all possible combinations")
    choice = input(Fore.CYAN + "Enter your choice (1/2): ").strip()

    filename_prefix = option_name.lower().replace(" ", "_")
    if choice == '1':
        try:
            num_passwords = input(Fore.CYAN + "Enter the number of random passwords to generate (min 2, default 300): ").strip()
            num_passwords = int(num_passwords) if num_passwords else 300
            if num_passwords < 2:
                print(Fore.RED + "Number of passwords should be at least 2.")
                return
            generate_and_save_random_passwords(length, character_set, num_passwords, f"{filename_prefix}_random_pass.txt")
        except ValueError:
            print(Fore.RED + "Invalid input. Generating 300 passwords by default.")
            generate_and_save_random_passwords(length, character_set, filename=f"{filename_prefix}_random_pass.txt")
    elif choice == '2':
        generate_and_save_combinations(length, character_set, f"{filename_prefix}_combinations.txt")
    else:
        print(Fore.RED + "Invalid choice. Please enter 1 or 2.")

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
    choice = input(Fore.CYAN + "Enter your choice (1-12): ").strip()

    options = {
        '1': ("All_Alphabets_Uppercase", string.ascii_uppercase),
        '2': ("All_Alphabets_Lowercase", string.ascii_lowercase),
        '3': ("Both_Upper_Lower", string.ascii_uppercase + string.ascii_lowercase),
        '4': ("All_Numbers", string.digits),
        '5': ("All_Symbols", string.punctuation),
        '6': ("Alphabets_Lowercase_Numbers", string.ascii_lowercase + string.digits),
        '7': ("Alphabets_Lowercase_Symbols", string.ascii_lowercase + string.punctuation),
        '8': ("Alphabets_Uppercase_Numbers", string.ascii_uppercase + string.digits),
        '9': ("Alphabets_Uppercase_Symbols", string.ascii_uppercase + string.punctuation),
        '10': ("Numbers_Symbols", string.digits + string.punctuation),
        '11': ("Custom", load_custom_alphabets()),
        '12': ("All_Alphabets_Symbols_Numbers", string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation)
    }
        
    if choice in options:
        option_name, character_set = options[choice]
        if character_set:
            generate_passwords(password_length, character_set, option_name)
    else:
        print(Fore.RED + "Invalid choice. Please select a number between 1 and 12.")

if __name__ == "__main__":
    main()
