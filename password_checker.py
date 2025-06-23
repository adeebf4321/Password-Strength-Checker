import re

def check_password_strength(password):
    """
    Assesses the strength of a given password based on multiple criteria.

    Args:
        password (str): The password string to be assessed.

    Returns:
        tuple: A tuple containing:
            - str: A strength rating ('Very Weak', 'Weak', 'Moderate', 'Strong', 'Very Strong').
            - list: A list of feedback messages for improvement.
    """
    score = 0
    feedback = []

    # Criteria 1: Length
    # Aim for at least 8 characters, ideally 12+
    if len(password) < 8:
        feedback.append("Password is too short (aim for at least 8 characters).")
    elif len(password) < 12:
        score += 1
        feedback.append("Password length is moderate (aim for 12+ characters for 'Strong').")
    else:
        score += 2
        feedback.append("Password length is good!")

    # Criteria 2: Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters for a stronger password.")

    # Criteria 3: Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters for a stronger password.")

    # Criteria 4: Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers for a stronger password.")

    # Criteria 5: Special characters
    # Using a common regex pattern for special characters
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?`~]", password):
        score += 1
    else:
        feedback.append("Add special characters (e.g., !@#$) for a stronger password.")

    # Criteria 6: Avoid common patterns or repeating characters (basic check)
    if re.search(r"(.)\1\1", password): # Checks for 3 or more repeating characters
        score = max(0, score - 1) # Deduct a point, but not below zero
        feedback.append("Avoid repeating characters (e.g., 'aaa', '111').")

    # Criteria 7: Avoid common sequences (basic check)
    # This is a very basic check; real checkers use dictionary lookups.
    common_sequences = ["123", "abc", "password", "qwerty"]
    for seq in common_sequences:
        if seq in password.lower():
            score = max(0, score - 2)
            feedback.append(f"Avoid common sequences like '{seq}'.")
            break # Only need to warn for one

    # Determine strength rating based on score
    if score < 2:
        strength = "Very Weak"
    elif score == 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    elif score >= 5:
        strength = "Very Strong"
    else:
        strength = "Unknown" # Should not happen with current logic

    return strength, feedback

def main():
    """Main function to run the password strength checker tool."""
    print("--- Password Strength Checker ---")
    print("Enter a password to check its strength. Type 'exit' to quit.")

    while True:
        password = input("\nEnter your password: ")
        
        if password.lower() == 'exit':
            print("Exiting password checker. Goodbye!")
            break
        
        if not password:
            print("Password cannot be empty. Please try again.")
            continue

        strength, feedback = check_password_strength(password)

        print(f"\nPassword: {password}")
        print(f"Strength: {strength}")
        
        if feedback:
            print("Feedback:")
            for msg in feedback:
                print(f"- {msg}")
        else:
            print("No specific feedback needed for this password!")

if __name__ == "__main__":
    main()

