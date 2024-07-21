import itertools
import string

# Function to read passwords from a file
def read_passwords(filename):
    passwords = []
    try:
        with open(filename, 'r') as f:
            passwords = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("File not found.")
    return passwords

# Brute force attack
def brute_force(chars, length):
    for password_length in range(1, length + 1):
        for password in itertools.product(chars, repeat=password_length):
            yield ''.join(password)

# Dictionary attack
def dictionary_attack(passwords, dictionary):
    for password in passwords:
        if password in dictionary:
            yield password

# Pattern matching
def pattern_matching(passwords, pattern):
    for password in passwords:
        if pattern in password:
            yield password

# Main function
def main():
    # Read passwords from a file
    password_file = input("Enter the name of the file containing passwords: ")
    passwords = read_passwords(password_file)
    print("Loaded passwords:", passwords)

    # Options for the user
    print("Choose an attack type:")
    print("1. Brute Force")
    print("2. Dictionary Attack")
    print("3. Pattern Matching")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        charset = string.ascii_letters + string.digits + string.punctuation
        max_length = int(input("Enter the maximum password length to brute force: "))
        print("Starting brute force attack...")
        for password in brute_force(charset, max_length):
            if password in passwords:
                print(f"Password found: {password}")
                break
        else:
            print("Brute force attack failed.")
    elif choice == '2':
        dictionary_file = input("Enter the name of the dictionary file: ")
        dictionary = read_passwords(dictionary_file)
        for password in dictionary_attack(passwords, dictionary):
            print(f"Password found: {password}")
            break
    elif choice == '3':
        pattern = input("Enter the pattern to search for: ")
        for password in pattern_matching(passwords, pattern):
            print(f"Password found: {password}")
            break
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()