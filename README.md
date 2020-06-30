# Welcome to the RentGraph project! #

This project has been built for users to purchase graphics related services such as Twitch emotes, characatuers and blueprints. When logged in, users can add posts and edit the posts on the site. Users can also leave user feedback which will help improve the site in the longrun.

## UX #

This project has a mobile first approach. The website provides a clear and approachable format for all users, regardless of device or resolution. The user will also be able to navigate around the site using the nav bar, this will show as top bar in desktop, and as a burger menu in mobile.

### User Stories #

* As a user I want to be able to pruchase the posts shown on the site.
* As a user I want to be able to leave feedback on the site.
* As a user I want to be able to login to edit and add posts.
* As a user I want to know what I am buying in a checkout screen.

### Features #

Here you can find a list of available features from the RentGraph website.

* Purchase any of the advertised posts
* Create or edit posts whilst logged in
* Leave feedback on the website
* Register an account for the site
* View posts on the website

### Further Functionality #

Further functionality I would like to add in the future includes but is not limited to:

* Search for posts
* Filter posts based on tag
* Have posts be tied to user's accounts
* Add ability to link up paypal so artists receive their revenue automatically
* Have feedback be stored in a table to read at a later date

### Technologies Used #

-  **HTML**
    - Hypertext Markup Language (HTML) is the standard markup language for documents designed to be displayed in a web browser.
- **CSS**
    - Cascading Style Sheets (CSS) is a stylesheet language used to describe the presentation of a document written in HTML or XML.
- **JavaScript**
    - JavaScript (JS) is a high-level programming language, often just-in-time compiled, and multi-paradigm. It has curly-bracket syntax, dynamic typing, prototype-based object-orientation, and first-class functions.
- **Python**
    - Python is an interpreted, high-level, general-purpose programming language.
- **Django**
    - Django is a Python-based free and open-source web framework, which follows the model-template-view (MTV) architectural pattern.

Alot of this project was borrowed from previous sections of the Django Frameworks module, this was to set up the user authentication and adding posts.

### Deployment #

Deployment was done initially through GitHub, when I checked that everything was coming through correctly, I then deployed to Heroku. As you are unable to deploy projects directly through to Heroku when creating a Django application, this was instead facilitated by AWS by hosting any local files on their S3 service.

Deployment was completed regularly throughout the project as a form of backup if anything were to go wrong with my local version.

You can see evidence of my regular deployments in GitHub and Heroku.

### Testing #

Testing was completed as developed, through trial and error. Main testing was done after I had completed the setup of the initial template (borrowed from Code Institute as mentioned above).

The testing methods included checking that user navigation was fluid i.e. all links worked correctly and allowed for accessing the previously accessed page and the home page. This mainly helped for my Feedback and order Confirm pages as it highlighted that there was no way to get back to the home page from these pages.

Other testing included allowing family and friends to view the site from Heroku and provide feedback which I then worked around as and when this was spoken about.

Another form of very helpful testing was completed by the Code Institute support team as they were helping me write this project. A member of the team named Tim pointed out that the site did not look very personalised when initially viewing, I changed the site to include a footer that included contact details and links to point to my socials and GitHub repos.
