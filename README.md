# Tsurei
Tsurei is a online library of manga/manhwa, where the administrators can upload the content to the website, and the users can freely read. It's the capstone project for the CS50W Web Programming Course.

# Distinctiveness and Complexity
This project uses almost all the concepts that were explained through the course, where it contains a lot of complex functions and models, focusing on the user experience. Where the user can enjoy reading, and navigating through the page.
The project uses Django as the backend with 5 models, and JavaScript on the front-end, also it's used SwiperJS for displaying the mangas on slides. 
The basic idea is enter the website, find a desired manga to read(search for a keyword, filter all mangas, see the most readed or the latest manga releases), select a manga, read the manga information and read the chapters, also the user can bookmark the mangas if desired.
It provides functions to navigate through the mangas and chapters, and also fits the images/content in all devices as it's mobile-responsive.


# Directories
- `capstone/`
	- `manga/` - Main application directory.
		- `static/` - CSS, Images, Fonts and JS files.
			- `css` - All CSS files used in the project.
                - `categories.css` 
                - `index.css` - Style for the index html
                - `latest.css` - Style for the latest html
                - `layout.css` - Style for the layout which is the base html file
                - `login.css` - Style for the login html
                - `manga_chapter.css` - Style for the manga_chapter html
                - `profile.css` - Style for the profile html
                - `queries.css` - Responsive style for all html
                - `register.css` - Style for the register html
                - `search.css` - Style for the search button
                - `show_manga.css` - Style for the show_manga html
                - `upload_manga.css` - Style for the upload_manga form
                - `util.css` - General styles
			- `images` - Contains all images of the project
			- `js` - Contains all javascript files used in the project
				- `index.js` - Contains the settings for the swiperJS
				- `mobile-nav.js` - Toggle between open and close mobile menu.
				- `profile.js` - Contains settings for the swiperJS.
				- `search.js` - Toggle a input in the search button
				- `bookmark.js` - Bookmarks a manga, toggle the button with the current status
                - `modal.js` - Shows and hide the modal
				- `sticky.js` - Fixes the navigation when scrolling.
		- `templates/manga` - All HTML files used in the project.
			- `categories.html` - Filter all mangas
			- `index.html` - Home page.
			- `latest.html` - Show all latest release mangas.
			- `layout.html` - Template html layout.
			- `login.html` - Template login page.
			- `manga_chapter.html` - Shows the manga chapter.
			- `profile.html` - Shows the user profile page
			- `register.html` - Template register page.
			- `search.html` - Shows the result of the search function.
			- `show_manga.html` - Displays a detailed manga information and chapters.
			- `upload_manga` - A form to upload mangas to the website.
		- `admin.py` - Register all the models created into the admin page.
		- `forms.py`  - Contains forms to get user information.
		- `models.py` - All models of the project.
		- `urls.py` - Contains the app url paths to the correspondent view function.
		- `views.py` - Contains all the functions to return web responses, and also gets the web requests.
	- `tsurei/` - Project configuration folder
        - `settings/` - Contains the project settings
        - `urls.py` - Contains all the urls from the apps
	- `requirements.txt` - Contains all dependencies of the project.

# How to Run the Project

    python -m venv venv

## Download dependencies

    pip install -r requirements.txt

Set .env file

    touch .env

### With your favorite editor edit the file and include the line below

    SECRET_KEY=*GENERATE A SECRET KEY*
    DEBUG=TRUE

ex: https://djecrety.ir/

## Migrate django models

    python manage.py makemigrations manga
    python manage.py migrate

## Run server

    python manage.py runserver
