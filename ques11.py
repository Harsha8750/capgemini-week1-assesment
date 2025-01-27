import re

def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[@#$%^&*()_+=\-{}\[\]:\";'<>?,./]", password):
        return False
    return True

def main():
    password = input("Enter a password to check its strength: ")
    if is_strong_password(password):
        print("The password is strong.")
    else:
        print("The password is weak. Make sure it has at least 8 characters, includes uppercase, lowercase, digits, and special characters.")

if __name__ == "__main__":
    main()
