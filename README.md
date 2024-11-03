# Replacement_Quiz

# Quoting System

it is a system that can request for a quote for their project and the number of their materials that they are going to use. the user can make his own account to log in and make a request that will the admin/manager will see the the pending quote card, then the admin is the one who choose to approve or declined the card quotation.

Before cloning and running this project, ensure you have the following installed:

Python (version 3.12)

Git

 - Cloning The Project
   
   get the repository url, copy the HTTPS link (it should look like https://github.com/username/repository-name.git).

 - Open the terminal
   
   find a directory on your local machine where you want to save the project

 - Clone the Project

    in terminal type:
   git clone https://github.com/username/repository-name.git
 
   then replace https://github.com/username/repository-name.git with the URL you copied.

 - navigate into the project folder you can type to the terminal: cd repository-name

 - Setting Up the Project

   In the terminal, create a virtual environment:

   python3 -m venv env

- Activate the virtual environment:

   On Windows:
   .\env\Scripts\activate

- Install Dependencies

   Install required packages:

   Ensure you have a requirements.txt file in the root directory run the following command to install all dependencies:

   pip install -r requirements.txt

- Database Setup

   Apply migrations to set up the database:

   python manage.py migrate

   Create a superuser to access the admin interface:

  python manage.py createsuperuser

  Follow the prompts to set up the admin credentials.

- Running the project

  type in the terminal: python manage.py runserver

  then open the link (like this:  http://127.0.0.1:8000/) to view the web site


















    
