import requests
import random
import pyfiglet
from colorama import Fore, Style, init
import subprocess
import os
import time
import sys

init(autoreset=True)





def check_for_updates():
    print(Fore.YELLOW + "Checking for updates...")
    repo_url = 'DarkCipherNinja/Password-Generater'
    api_url = f'https://api.github.com/repos/{repo_url}/commits/main'
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        latest_commit = response.json().get('sha')
        
        try:
            current_commit = subprocess.check_output(["git", "rev-parse", "HEAD"]).strip().decode()
        except subprocess.CalledProcessError:
            print(Fore.RED + "Error: Could not retrieve the current commit. Are you in a Git repository?")
            return

        if latest_commit != current_commit:
            print(Fore.RED + "New update available. Updating...")
            update_script()
        else:
            print(Fore.GREEN + "Your script is up to date.")
    except requests.RequestException as e:
        print(Fore.RED + f"Failed to check for updates: {e}")

def update_script():
    try:
        subprocess.run(["git", "pull"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(Fore.GREEN + "Script updated successfully!")
        sys.exit(0)  # Exit after updating
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Failed to update the script: {e}")
        sys.exit(1)  # Exit with error code if the update fails
    except PermissionError:
        print(Fore.RED + "Permission denied. Try running the script with elevated permissions (e.g., 'sudo').")
        sys.exit(1)

if __name__ == "__main__":
    display_banner_and_social()  # Show banner and social media info
    check_for_updates()  # Check for updates
