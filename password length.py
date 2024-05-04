import re

def assess_password_strength(password):
    # Check length
    length_error = len(password) < 8

    # Check for uppercase letters
    uppercase_error = not re.search(r'[A-Z]', password)

    # Check for lowercase letters
    lowercase_error = not re.search(r'[a-z]', password)

    # Check for numbers
    digit_error = not re.search(r'\d', password)

    # Check for special characters
    special_error = not re.search(r'[!@#$%^&*()-+]', password)

    # Calculate score
    errors = [length_error, uppercase_error, lowercase_error, digit_error, special_error]
    score = len([error for error in errors if error])

    # Assess strength
    if score == 0:
        return "Strong", []
    elif score <= 2:
        suggestions = []
        if length_error:
            suggestions.append("Password should be at least 8 characters long")
        if uppercase_error:
            suggestions.append("Use at least one uppercase letter")
        if lowercase_error:
            suggestions.append("Use at least one lowercase letter")
        if digit_error:
            suggestions.append("Use at least one digit")
        if special_error:
            suggestions.append("Use at least one special character (!@#$%^&*()-+)")
        return "Weak", suggestions
    else:
        return "Moderate", []

# Main function
def main():
    while True:
        print("Choose an option:")
        print("1. Check password strength")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            password = input("Enter your password: ")
            strength, suggestions = assess_password_strength(password)
            if strength == "Weak":
                print("Password is weak.\n Suggestions:")
                for suggestion in suggestions:
                    print("-", suggestion)
            else:
                print(f"Password strength: {strength}")
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
