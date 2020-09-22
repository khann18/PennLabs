# Penn Labs Backend Challenge

## Documentation

The extra routes - I made additional routes to allow me to create some (very) simple forms for (very) simple frontend. I did not use the reference frontend and decided to just access http://127.0.0.1:5000

  - /api/home has a navbar that links to those simple forms and tag_count also. I didn't have a chance to finish the functionality for search users (it is 9/21 11:39PM right now), but the /user/:username route should still work by itself. 

SQLAlchemy - I created 3 objects (User, Club, Tag). User has properties of username, password, id, email, firstname, lastname, and clubs. The ones I considered to be private were password, id, and email (so they're not returned in /user). Club has the same characteristics as in the json provided, and I chose to store its tags as a semicolon separated string (at first I didn't have the Tag class, but I decided it was fine not to change it to a many-to-many relationship bc it's not important for someone who is in a club to know the count, which is an attribute of a Tag).

bootstrap.py - I ended up putting most of the SQLAlchemy queries there to keep things more uniform. Some functions in app.py access those in bootstrap.py, such as that creating a new club.



## Installation

1. Click the green "use this template" button to make your own copy of this repository, and clone it. Make sure to create a **private repository**.
2. Change directory into the cloned repository.
3. Install `pipenv`
   - `pip install --user --upgrade pipenv`
4. Install packages using `pipenv install`.

## File Structure

- `app.py`: Main file. Has configuration and setup at the top. Add your [URL routes](https://flask.palletsprojects.com/en/1.1.x/quickstart/#routing) to this file!
- `models.py`: Model definitions for SQLAlchemy database models. Check out documentation on [declaring models](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/) as well as the [SQLAlchemy quickstart](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#quickstart) for guidance
- `bootstrap.py`: Code for creating and populating your local database. You will be adding code in this file to load the provided `clubs.json` file into a database.

## Developing

0. Determine how to model the data contained within `clubs.json` and then complete `bootstrap.py`
1. Run `pipenv run python bootstrap.py` to create the database and populate it.
2. Use `pipenv run flask run` to run the project.
3. Follow the instructions [here](https://www.notion.so/pennlabs/Backend-Challenge-Fall-20-31461f3d91ad4f46adb844b1e112b100).
4. Document your work in this `README.md` file.

## Reference frontend

If you want to use the reference frontend to see if your implementation of the
backend is working correctly, follow the below steps

1. `cd reference-frontend` to enter the directory.
2. `yarn install` to download all the dependencies.
3. `yarn start` to start the server.
4. Navigate to `localhost:3000` to see if the website is working correctly.

Feel free to make changes to the reference frontend as necessary. If you want
to work on the reference frontend as a supplementary challenge, the current
implementation doesn't implement _tags_. Modifying the reference frontend to
list club tags while browsing clubs or allow users to include tags while
creating a new club could be a good place to start with improving the frontend.

## Submitting

Follow the instructions on the Technical Challenge page for submission.

## Installing Additional Packages

Use any tools you think are relevant to the challenge! To install additional packages
run `pipenv install <package_name>` within the directory. Make sure to document your additions.
