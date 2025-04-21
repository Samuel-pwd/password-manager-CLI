#!/usr/bin/env python3
"""
Linux Password Manager
A simple terminal-based password manager that stores credentials in JSON format.
"""

import json 
import os
from getpass import getpass  # For secure password input

# Configuration
PASSWORDS_FILE = os.path.expanduser("~/.local/share/password_manager.json")
os.makedirs(os.path.dirname(PASSWORDS_FILE), exist_ok=True)

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def load_passwords():
    """Load passwords from JSON file"""
    try:
        if os.path.exists(PASSWORDS_FILE):
            with open(PASSWORDS_FILE, "r") as f:
                return json.load(f)
    except json.JSONDecodeError:
        print("Corrupted password file! Starting fresh.")
    return {}

def save_passwords(passwords):
    """Save passwords to JSON file"""
    with open(PASSWORDS_FILE, "w") as f:
        json.dump(passwords, f, indent=4, ensure_ascii=False)

def add_password(passwords):
    """Add new password entry"""
    clear_screen()
    print("➕ Add New Password")
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = getpass("Password: ").strip()

    if website and password:  # Basic validation
        passwords[website] = {
            "username": username,
            "password": password
        }
        save_passwords(passwords)   
        print(f"✅ Password for {website} saved securely!")
    else:
        print("❌ Website and Password are required!") 
    input("\nPress Enter to continue...")

def view_passwords(passwords):
    """Display all saved passwords"""
    clear_screen()
    if not passwords:
        print("🔍 No passwords stored yet!")
    else:
        print("🔑 Stored Passwords:")
        for idx, (website, data) in enumerate(passwords.items(), 1):
            print(f"\n{idx}. {website}")
            print(f"   👤 Username: {data['username']}")
            print(f"   🔐 Password: {'*' * len(data['password'])}")
    input("\nPress Enter to continue...")

def search_password(passwords):
    """Search for specific password"""
    clear_screen()
    website = input("Search Website: ").strip().lower()
    found = False

    for site, data in passwords.items():
        if website in site.lower():
            print(f"\n🏷️  {site}")
            print(f"👤 Username: {data['username']}")
            print(f"🔐 Password: {data['password']}")
            found = True

    if not found:
        print("🔍 No matching passwords found")
    input("\nPress Enter to continue...")

def delete_password(passwords):
    """Delete password entry"""
    clear_screen()
    view_passwords(passwords)
    if passwords:
        try:
            choice = int(input("\nEnter number to delete: ")) - 1
            website = list(passwords.keys())[choice]
            del passwords[website]
            save_passwords(passwords)
            print(f"🗑️  Deleted {website} successfully!")
        except (ValueError, IndexError):
            print("❌ Invalid selection!")
    input("\nPress Enter to continue...")

def main_menu():
    """Display main menu"""
    clear_screen()
    print("🔒 Linux Password Manager")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Delete Password")
    print("5. Exit")

def main():
    """Main application loop"""
    passwords = load_passwords()

    while True:
        main_menu()
        choice = input("\nSelect option (1-5): ").strip()

        if choice == "1":
            add_password(passwords)
        elif choice == "2":
            view_passwords(passwords)
        elif choice == "3":
            search_password(passwords)
        elif choice == "4":
            delete_password(passwords)
        elif choice == "5":
            print("\n🔒 Exiting. Your passwords are secure!")
            break
        else:
            print("❌ Invalid choice!")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()





 

    
