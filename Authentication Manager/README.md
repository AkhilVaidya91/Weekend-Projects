# Authentication-Manager
This is an Authentication Manager that uses mysql-connector and cryptography libraries in Python and MySQL database to store and validate User ID and the respective password in an encrypted format.

# Authentication Manager

This program provides a simple Authentication Manager with options for user sign-up and login. It uses MySQL for data storage and the cryptography library for password encryption.

## Requirements

1. **Two Options**: The program offers two options for the user - Sign up or Login.

2. **Sign Up Option**: When a user chooses to sign up, the program stores the user ID and password in the 'login' table in the 'authManager' database.

3. **Login Option**: When the user chooses the login option, the program prompts for the username and password. It searches within the 'login' table in the 'authManager' database:
   - If the username is not found, it throws an error 'Invalid username.'
   - If the username is found, it checks if the entered password matches the stored encrypted password.
     - If the passwords match, it prints 'Login successful' and exits.
     - If the passwords do not match, it throws 'Invalid password.'

## Setup

1. **Database Configuration**: The program connects to a MySQL database with the following credentials:
   - Host: localhost
   - User: root
   - Password: akhil912004

   Make sure to have a MySQL server running with the specified configuration.

2. **Encryption Key**: The program uses the Fernet encryption algorithm. It reads the encryption key from the 'key.key' file. If you are running this program for the first time, uncomment the 'write_key()' function to generate and store the encryption key.

## Functions

### `login(user_id, password)`

- Takes user input for user ID and password.
- Compares the entered user ID with the 'login' table in the 'authManager' database.
- Returns 1 for a successful login, else returns 0.

### `sign_up(user_id, password)`

- Adds the username and encrypted password to the 'login' table in the 'authManager' database.

## Usage

1. Run the program, and it will prompt you with options to login, sign up, or exit.
2. Enter 'login' to log in, 'signup' to create a new account, or 'exit' to terminate the program.
3. Follow the prompts to enter the required information.

Note: The program assumes the existence of the 'authManager' database and the 'login' table within it. Ensure that these are set up before running the program.

Feel free to customize the program according to your specific database setup and security requirements.
