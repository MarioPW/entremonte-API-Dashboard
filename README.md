# API:
## Django Rest Framework is employed in the backend with the aim of utilizing the administrative panel for the following aspects:

- User management on the website
- User role management
- Management and updating of the menu
- Handling of images and captions for the homepage carousel.
- Handling of images and captions for the dishes from the menu.
- Handling of available dates for reservation.

# Steps to run The Project in local:

### 1. Clone the Repository
To clone the repository to your local machine:

```bash
git clone <repository_url>
cd <project_name>
```

### 2. Check Python Version
To ensure the project runs correctly, it’s essential to have the appropriate version of Python installed.

Required Python Version:
Python 3.8 to 3.11 is required for compatibility with Django 4.2.
Django 4.2 does not support Python versions later than 3.11, so using Python 3.12 or higher might cause compatibility issues.

To check your Python version:
- Windows:

```bash
python --version
```
- Linux / macOS:

```bash
python3 --version
```
If your Python version is outside the required range, you can download a compatible version from here.

If needed, install a compatible version of Python:
- On Linux (using apt for Ubuntu/Debian-based systems):

```bash
sudo apt update
sudo apt install python3.11
```
- On macOS (using Homebrew):

```bash
brew install python@3.11
Once the correct Python version is installed, you can proceed to create the virtual environment.
```

### 3. Create a Virtual Environment
Create a virtual environment for the project. This helps isolate project dependencies and prevents conflicts with other projects.
#### Windows
```python 
# In a directory where you want to create the virtual environment
-m venv venv
```
#### 🔧 Linux / macOS
```bash
python3 -m venv venv
```
### 4. Activate the Virtual Environment
The method varies depending on the operating system:

- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:

```bash
source venv/bin/activate
```
### 5. Install Requirements
To install the project dependencies:

```bash
pip install -r requirements.txt
```
### 6. Apply Migrations
To apply migrations to set up the database:

```bash
python manage.py migrate
```
### 7. Create a Superuser
On the root directory of your Django project run the following command:

```bash
python manage.py createsuperuser
```
Follow the instructions provided in the console to complete the superuser creation process.
The superuser account is essential for accessing the Django admin interface and managing various aspects of your application.
### 8. Run the Development Server
To start the Django development server:

```bash
python manage.py runserver
```
The server will be available at http://127.0.0.1:8000/ by default.

### 9. Access the Project
Open your web browser and go to http://127.0.0.1:8000/. If you created a superuser, you can also access the Django admin at http://127.0.0.1:8000/admin/.

Remember, this development server is not suitable for production environments and is provided for development purposes only.

# ".env" file configuration
Create the .env File:

In the root of your project, create a file named .env. You can do this using the terminal or your operating system's file explorer.

Define Environment Variables:

Open the .env file and define the following variables:

```python
SECRET_KEY='django-insecure-#n(...)'
DEBUG=True

 # Allowed hosts for the development environment:
ALLOWED_HOSTS_DEV=['*']

 # Allowed hosts for the production environment:
ALLOWED_HOSTS_DEPLOY=[]

# REACT local host (or change it for your local host frontend):
CORS_ALLOWED_ORIGINS=["http://127.0.0.1:5173",]  

# Relational database connection (replace with your actual configuration)
DATABASE_URL=postgres://user:password@localhost:5432/db_name

# Cloudinary configuration for image storage
CLOUDINARY_STORAGE={"CLOUD_NAME":"your_cloud_name","API_KEY":"your_api_key","API_SECRET":"your_api_secret"}

# Default file storage in Cloudinary
DEFAULT_FILE_STORAGE='cloudinary_storage.storage.MediaCloudinaryStorage'

# Social Auth:
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY="your-google-client-id"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET="your-google-client-secret"

SOCIAL_AUTH_FACEBOOK_KEY = 'TU_APP_ID'
SOCIAL_AUTH_FACEBOOK_SECRET = 'TU_APP_SECRET'
```
Be sure to replace "your_cloud_name"," your_api_key", and "your_api_secret" with the actual credentials provided by Cloudinary. Also, adjust the database configuration according to your environment.
