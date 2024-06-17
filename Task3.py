import random
import string

def generate_password(length):
    # Define the character sets to use
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    # Get desired password length from user
    try:
        length = int(input("Enter the desired length of your password: "))
    except ValueError:
        print("Length should be a positive integer.")
        return
    
    # Generate the password
    password = generate_password(length)
    
    # Display the password
    print("Your generated password is:", password)

# Run the main function
if __name__ == "__main__":
    main()
