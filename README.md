<h1 align="center">VCS services Website</h1>

[View the live project here.](https://https://vcsservices.herokuapp.com/)

This is the website for VCS speech-writing services. The idea is that any person who has a special occasion coming up can hire a professional to write it for them.
A further idea is to provide coaching or a form to take in details to include in the speech but for now only the skeleton structure was created.
This project relies heavily on code from the Boutique Ado App. My idea was to take a top-down approach and then remove the unwanted features but in the end the priority was to get the database deployed.


## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the site.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find content.
        3. As a First Time Visitor, I want to see examples of the products on offer. I also want to locate social media links to determine how trusted and known they are.
        4. As a First Time Visitor, I want to be able to sign up for an account.


    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to find information about rates and available services.
        2. As a Returning Visitor, I want to find the best way to get in contact with any questions I may have.
        3. As a Returning Visitor, I want to be able to sign up for an account.


## Features

-   Responsive on all device sizes

-   Interactive elements

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python ](https://www.python.org/)


### Frameworks, Libraries & Programs Used

1. [Bootstrap 5.1:](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Django](https://www.djangoproject.com/)
    - Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.

allauth - pre-built package that is customisable


### Testing User Stories from User Experience (UX) Section




### Further Testing



### Known Bugs
the procfile prevented the app from deploying to heroku at first because Procfile was not capitalised and later because the heroku app name was used instead of the django project name

## Deployment

### Heroku

The project was deployed to Heroku using the following steps...

1. Create an account in Herokus website
2. Log in to Heroku in the CLI
3. Install pillow, psycopg2 and gunicorn
4. Create app in Heroku
ad dj database in settings.py and paste db url into settings
Add Heroku hostname to allowed hosts in settings.py
back up db to a json file and then migrate and add the data in to the heroku db
comment out the heroku db address so it doesnt get into version control
Create a procfile
In Heroku create a postgres database addon
Install dj_database_url in the CLI and freeze the requirements file again


## Credits

### Code





### Content

-   All content was written by the developer.

### Media

-   All Images were created by the developer 

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.


