# LoginSystem
This code is a graphical login system developed in Python with Tkinter, CustomTkinter, and SQLite. Below, I describe the main components and functionality of the code to facilitate understanding and maintenance.

General Description of the Code

Graphical User Interface (GUI): Uses CustomTkinter to create an interface with a modern look and options for login and registration.
Database: SQLite is used to store user information, such as username and password.

Main Components:

   »Input fields for username and password.
   »Buttons for "Login" and "Register."
   »Functions for user authentication and registration.

Code Components:

1.Initial Configuration
   »Sets the window's default appearance and color.
   »Defines the icon and background image for the window.
   
2.Main Functions
   »login(): Checks if the provided username and password match those registered in the database. Displays a success or error message with a message box.
   »cadastrar(): Hides login elements and displays input fields for creating a new account.
   »backToMain(): Stores the new username and password in the database after validating the fields and re-displays the login elements.
   
3.Interface Elements
   »Frame: Structure that organizes the layout and facilitates interface control.
   »Labels: Descriptive text for the user, with instructions and warnings.
   »Entrys: Fields for the user to enter their username and password.
   »Buttons:
      *log_button: To attempt login.
      *cadastro_button: To access the registration screen.
      *backToMain_button: To confirm registration and return to the login screen.
      
4.Main Loop
   »janela.mainloop(): Keeps the window open while the program is running
