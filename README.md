# [PROJECT3 WATERBLOGGED](https://water-blogged-flask-app-0fb53df2979a.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Coelecanth/project3-waterLogged)](https://github.com/Coelecanth/project3-waterLogged/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Coelecanth/project3-waterLogged)](https://github.com/Coelecanth/project3-waterLogged/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Coelecanth/project3-waterLogged)](https://github.com/Coelecanth/project3-waterLogged)

My project idea was to create a journal for fly fisherman, who could use this as a blog site to share with people.  

This was born out the research I did on this and there didn’t seem to be a site out there that could deliver this specifically for fly fishers. Specifically a site to share your individual experiences with others fly fishers where it wasn’t just sole platform for one fly fisher. Create a collective of like minded individuals who all share there experiences in the same place. 

Essentially the idea was for the fly fisherman to be able to record there fishing sessions which could be a simple local visit or at the other end of the spectrum, a full expedition holiday. Where they could record most of the useful information on the place they visited, and then share this with others, provide information such as location.
 To show how they rated individual visits and the locations of these venues.

![Waterblogged site](documentation/ami-resp.png)

See the fully interactive version here - source:  [amiresponsive](https://ui.dev/amiresponsive?url=https://water-blogged-flask-app-0fb53df2979a.herokuapp.com)

## UX

The UX for this site was very much driven by the need to be simple to use; but also, that the site is an interactive site driven by a database, and so needed to have clean way of potentially show hundreds of records of data, and provide access to a known identity.  
so the structure of the site was presented in the following way;
- Logon 
- Logoff 
- Recognition of user type (eg superuser) 
- Create, update, delete of data
- integrate graphical location into the above data record management 
- Simplify selection for known data types 
- make it easy for user to update their own data records

The look and feel of the site would be represented by colours, imagery, and icons relating to the subject matter, the colour scheme would be reflective of this. The layout of the pages would be centred to allow the information to be displayed but with wide margins to allow imagery of the river scene to be visible both to the side and behind. The vivid imagery used for the river could be distracting so I decided to tone this down by fading the image with a grey tone to compliment the colour scheme. 

### Colour Scheme

The colour scheme chosen was to provide an idyllic reflective colour scheme of the river or lake environment with greens and blues, and deeper shades represented by grey. As I was using Materialize CSS framework, which has good functionality for colours. I decided to match my colour scheme, using the Materialize colour scheme, so where I couldn’t use the Materialize framework i could call a css class.  

- Materialize grey lighten-2 - defined as class l-grey colour #e0e0e0
- Materialize teal darken-1 - defined as class teal colour #00897b
- Materialize teal darken-4 - defined as class green colour #004d40 
- Materialize grey lighten-2 - defined as class blue colour #0d47a1
- Materialize grey darken-2 - defined as class d-grey colour #616161 


The colour scheme was refined and tuned in the [coolors.co](https://coolors.co/bac1b8-00897b-0c7c59-0d47a1-2b303a) web site and the link shows the colour scheme as seen from the website. 

For completeness the colour scheme is shown below as an image 
![](/documentation/colour_pal.png) 


### Typography

i used the website fontjoy to pick a pair of fonts which are complimentary in there styles but provide a mild contrast to the rest of the text on the page. The fonts chosen were sourced form google fonts and imported into my css, these were then applied with there own classes to slected text.
The fonts used are shown below    

- [Roboto Slab](https://fonts.google.com/specimen/Roboto+Slab) was used for the primary headers and titles.

- [Titillium web](https://fonts.google.com/specimen/Titillium+Web) was used for all other secondary text.

#### Icons
I used font awesome for the icons as it was able to provide the diverse colection of I cons I needed to repreent the individual elelemt

## User stories

### New Site Users
- As a new site user, I would like to register on the site, so that I am known by the site and my entries are recorded to me.
- As a new site user, I would like to record new fishing, which are attributed to me on creation.
- As a new site user, I would like to be able to select whether my entries are public or private (e.g. so that only I can see them or all users can see them, at both time of creation or later update).
- As a new site user, I would like to be able to see all entries I have created 
- As a new site user, I would like to be able to see all entries that are public 
- As a new site user, I would like to record the following elements in the site,
  - Venue name I visited and the topography eg river lake, sea, etc
  - The conditions, weather, water temperature etc.
  - The fish caught and the flies used to catch them.
  - Have notes section where I can add my own comments and also place links to any Images I may wish link to this session eg host my own photographs.
  - Link a geo location so I can show where this venue is, making it easier for readers of public session to find it, (or even to remember for myself) 
  - Record  my rating of the session, good, average, bad, and then show this rating in my overall list of entries I created.
- As a new site user, I would like to be able to edit the records I have created for the  following elements of each session recorded,
  - Venue name I visited and the topography eg river lake, sea, etc
  - The conditions, weather, water temperature etc.
  - The fish caught and the flies used to catch them.
  - Have notes section where I can add my own comments and also place links to any Images I may wish link to this session eg host my own photographs.
  - Link a geo location so I can show where this venue is, making it easier for readers of public session to find it, (or even to remember for myself) 
  - Record  my rating of the session, good, average, bad, and then show this rating in my overall list of entries I created.
- As a new site user, I would like to be able to search document for elements such as 
  - Venue others have visited previously 
  - Fish they have caught and from where
  - Venue which have been given a good rating  ( or bad, or average) 

### Returning Site Users
- As a  a returning site user, I would like to logon to the site, so that I am known by the site.
As a returning site user, I would like to record new fishing sessions, which are attributed to me.
-	As a returning site user, I would like to be able to select whether my entries are public or private (e.g. so that only I can see them or all users can see them, at both time of creation or later update).
- As a returning site user, I would like to be able to see all entries I have created 
- As a returning site user, I would like to be able to see all entries that are public 
- As a returning site user, I would like to be able to see all entries I have created
- As a returning site user, I would like to record new sessions with the following elements in the site,
  - Venue name I visited and the topography eg river lake, sea, etc
  - The conditions, weather, water temperature etc.
  - The fish caught and the flies used to catch them.
  - Have notes section where I can add my own comments and also place links to any Images I may wish link to this session eg host my own photographs.
  - Link a geo location so I can show where this venue is, making it easier for readers of public session to find it, (or even to remember for myself) 
  - Record  my rating of the session, good, average, bad, and then show this rating in my overall list of entries I created.
- As a returning site user, I would like to be able to edit the records I have created for the  following elements  of each session recorded,
  - Venue name I visited and the topography eg river lake, sea, etc
  - The conditions, weather, water temperature etc.
  - The fish caught and the flies used to catch them.
  - Have notes section where I can add my own comments and also place links to any Images I may wish link to this session eg host my own photographs.
  - Link a geo location so I can show where this venue is, making it easier for readers of public session to find it, (or even to remember for myself) 
  - Record  my rating of the session, good, average, bad, and then show this rating in my overall list of entries I created.
  - As a returning site user, I would like to be able to search ann document for elements such as 
  - Venue I have or other have visited previously 
  - Fish I have caught and from where
  - Venue which have been given a good rating  ( or bad, or average) 

### Site Admin
- As a site administrator, I should be able to change the location types  types for fishing , so that I can add edit or delete details such as Lake , river , or add different subcategories to this.
- As a site administrator, I should be able to been given access to these functions as an administrator, e.g. they’re not globally available to all.
- As a site administrator, I should be able to perform all the create, edit update and delete function taht both new ansd retunring site users can do. 

## Wireframes

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑 START OF NOTES (to be deleted)

In this section, display your wireframe screenshots using a Markdown `table`.
Instructions on how to do Markdown `tables` start on line #213 on this site: https://pandao.github.io/editor.md/en.html

Alternatively, dropdowns are a way to condense several wireframes into a collapsible menu to save space.
Dropdowns in Markdown are considered some of the only acceptable HTML components that are allowed for assessment purposes.

⚠️ **IMPORTANT**! ⚠️ **IMPORTANT**! ⚠️ **IMPORTANT**! ⚠️
The example below uses the `details` and `summary` code elements.
However, for these scripts to work, I've had to add spaces within the `< >` elements.

You MUST remove these spaces for it to work properly on your own README/TESTING files.
Remove the spaces within the `< >` brackets for the `details` and `summary` code elements,
for the Mobile, Tablet, and Desktop wireframes.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Mobile Wireframes

< details >
< summary > Click here to see the Mobile Wireframes < / summary >

Home
  - ![screenshot](documentation/wireframes/mobile-home.png)

About
  - ![screenshot](documentation/wireframes/mobile-about.png)

Contact
  - ![screenshot](documentation/wireframes/mobile-contact.png)

Gallery
  - ![screenshot](documentation/wireframes/mobile-gallery.png)

etc.
  - repeat for any remaining mobile wireframes

< / details >

### Tablet Wireframes

< details >
< summary > Click here to see the Tablet Wireframes < / summary >

Home
  - ![screenshot](documentation/wireframes/tablet-home.png)

About
  - ![screenshot](documentation/wireframes/tablet-about.png)

Contact
  - ![screenshot](documentation/wireframes/tablet-contact.png)

Gallery
  - ![screenshot](documentation/wireframes/tablet-gallery.png)

etc.
  - repeat for any remaining tablet wireframes

< / details >

### Desktop Wireframes

< details >
< summary > Click here to see the Desktop Wireframes < / summary >

Home
  - ![screenshot](documentation/wireframes/desktop-home.png)

About
  - ![screenshot](documentation/wireframes/desktop-about.png)

Contact
  - ![screenshot](documentation/wireframes/desktop-contact.png)

Gallery
  - ![screenshot](documentation/wireframes/desktop-gallery.png)

etc.
  - repeat for any remaining desktop wireframes

< / details >

## Features

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑 START OF NOTES (to be deleted)

Added check for password to be the same ands logic to check both passwords entered are the same 
Provide a geo-locatioon function for users to show on amap where the fishing laocation is 


🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

### Existing Features

- **PAssword secuirty**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/features/feature01.png)

- **Superuser identity**

- **geo location for places fished**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/features/feature02.png)

- **user segreation**

    - Details about this particular feature, including the value to the site, and benefit for the user. Be as detailed as possible!

![screenshot](documentation/features/feature03.png)

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑 START OF NOTES (to be deleted)

Repeat as necessary for as many features as your site contains.

Hint: the more, the merrier!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

### Future Features

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑 START OF NOTES (to be deleted)

Do you have additional ideas that you'd like to include on your project in the future?
Fantastic! List them here!
It's always great to have plans for future improvements!
Consider adding any helpful links or notes to help remind you in the future, if you revisit the project in a couple years.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- Public/Private Entires 
    - Any additional notes about this feature.
- YOUR-TITLE-FOR-FUTURE-FEATURE-#2
    - Any additional notes about this feature.
- YOUR-TITLE-FOR-FUTURE-FEATURE-#3
    - Any additional notes about this feature.

## Tools & Technologies Used

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑 START OF NOTES (to be deleted)

In this section, you should explain the various tools and technologies used to develop the project.
Make sure to put a link (where applicable) to the source, and explain what each was used for.
Some examples have been provided, but this is just a sample only, your project might've used others.
Feel free to delete any unused items below as necessary.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage. 
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![VSCode](https://img.shields.io/badge/VSCode-grey?logo=visualstudiocode&logoColor=007ACC)](https://code.visualstudio.com) used as my local IDE for development.
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.
- [![jQuery](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) used for user interaction on the site with materiliaze and also Leaflet 
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![Materialize](https://img.shields.io/badge/Materialize-grey?logo=materialdesign&logoColor=F5A5A8)](https://materializecss.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Flask](https://img.shields.io/badge/Flask-grey?logo=flask&logoColor=000000)](https://flask.palletsprojects.com) used as the Python framework for the site.
- [![MongoDB](https://img.shields.io/badge/MongoDB-grey?logo=mongodb&logoColor=47A248)](https://www.mongodb.com) used as the non-relational database management with Flask.
- [![Balsamiq](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) used for creating wireframes.
- [![Leaflet](https://img.shields.io/badge/Leaflet-grey?logo=leaflet&logoColor=199900)](https://leafletjs.com) used as a free open-source interactive map on my site.
- [![Font Awesome](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) used for the icons.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.

## Database Design

My project uses a non-relational database with MongoDB, and therefore the database architecture
doesn't have actual relationships like a relational database would.

My database is called **task_manager**.

It contains 3 collections:

- **categories**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | category_name | String | |

- **fdata**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | fd_cat_name | String | selected from *categories* collection |
    | fd_venue | String | fishing venue name |
    | fd_rate | String | user rating for the session they have recorded |
    | fd_wtemp  | String | water temperature |
    ! fd_geoloc | String | numerical string giving co-ordinates to a map location  |
    | fd_  | String | |
    | fd_created_by | String | selected from the *users* collection |

- **users**
    | Key | Type | Notes |
    | --- | --- | --- |
    | _id | ObjectId() | |
    | username | String | |
    | password | String | uses Secure Hash Algorithm (SHA) |
    | is_superuser | String | Used to identify super user for database |

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://water-blogged-flask-app-0fb53df2979a.herokuapp.com).

### MongoDB Non-Relational Database

This project uses [MongoDB](https://www.mongodb.com) for the Non-Relational Database.

To obtain your own MongoDB Database URI, sign-up on their site, then follow these steps:

- The name of the database on MongoDB should be called **insert-your-database-name-here**.
- The collection(s) needed for this database should be **insert-your-collection-names-here**.
- Click on the **Cluster** name created for the project.
- Click on the **Connect** button.
- Click **Connect Your Application**.
- Copy the connection string, and replace `password` with your own password (also remove the angle-brackets).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `DATABASE_URL` | user's own value |
| `IP` | 0.0.0.0 |
| `MONGO_DBNAME` | user's own value |
| `MONGO_URI` | user's own value |
| `PORT` | 5000 |
| `SECRET_KEY` | user's own value |

Heroku needs three additional files in order to deploy properly.

- requirements.txt
- Procfile
- runtime.txt

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: python app.py > Procfile`
- *replace **app.py** with the name of your primary Flask app name; the one at the root-level*

The **runtime.txt** file needs to know which Python version you're using:
1. type: `python3 --version` in the terminal.
2. in the **runtime.txt** file, add your Python version:
	- `python-3.9.19`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

If you are using SQLAlchemy for your project, you need to create a local PostgreSQL database.
In this example, the example database name is **db-name**.

```shell
workspace (branch) $ set_pg
workspace (branch) $ psql

... connection to postgres ...

postgres=# CREATE DATABASE db-name;
CREATE DATABASE
postgres=# \c db-name;
You are now connected to database "db-name" as user "foobar".
db-name=# \q
```

Once that database is created, you must migrate the database changes from your models.py file.
This example uses **app-name** for the name of the primary Flask application.

```shell
workspace (branch) $ python3

... connection to Python CLI ...

>>> from app-name import db
>>> db.create_all()
>>> exit()
```

To confirm that the database table(s) have been created, you can use the following:

```shell
workspace (branch) $ psql -d db-name

... connection to postgres ...

postgres=# \dt

	List of relations
Schema | Name | Type | Owner
-------+------+------+--------
public | blah1 | table | foobar
public | blah2 | table | foobar
public | blah3 | table | foobar

db-name=# \q
```

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps, plus a few extras.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("MONGO_DBNAME", "user's own value")
os.environ.setdefault("MONGO_URI", "user's own value")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DB_URL", "user's own value")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
```

If using Flask-Migrate, make sure to include the following steps as well.

During the course of development, it became necessary to update the PostgreSQL data models.
In order to do this, [Flask-Migrate](https://flask-migrate.readthedocs.io) was used.

- `pip3 install Flask-Migrate`
- Import the newly installed package on your main `__init__.py` file:
	- `from flask_migrate import Migrate`
- Define **Migrate** in the same file after **app** and **db** are defined:
	- `migrate = Migrate(app, db)`
- Initiate the migration changes in the terminal:

```shell
workspace (branch) $ flask db init

	... generating migrations ...

workspace (branch) $ set_pg
workspace (branch) $ flask db migrate -m "Add a commit message for this migration"

	... migrating changes ...

workspace (branch) $ flask db upgrade

	... updating database ...
```

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/Coelecanth/project3-waterLogged) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git shell or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/Coelecanth/project3-waterLogged.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Coelecanth/project3-waterLogged)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Coelecanth/project3-waterLogged)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!


## Credits

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

In this section you need to reference where you got your content, media, and extra help from.
It is common practice to use code from other repositories and tutorials,
however, it is important to be very specific about these sources to avoid plagiarism.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

### Content

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to provide attribution links to any borrowed code snippets, elements, or resources.
A few examples have been provided below to give you some ideas.

Ideally, you should provide an actual link to every resource used, not just a generic link to the main site!

⚠️⚠️ EXAMPLE LINKS - REPLACE WITH YOUR OWN ⚠️⚠️

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | version control | "How to Write a Git Commit Message" |
| [W3Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp) | entire site | responsive HTML/CSS/JS navbar |
| [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp) | contact page | interactive pop-up (modal) |
| [StackOverflow](https://stackoverflow.com/a/2450976) | quiz page | Fisher-Yates/Knuth shuffle in JS |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |


### Media

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to provide attribution links to any images, videos, or audio files borrowed from online.
A few examples have been provided below to give you some ideas.

If you're the owner (or a close acquaintance) of all media files, then make sure to specify this.
Let the assessors know that you have explicit rights to use the media files within your project.

Ideally, you should provide an actual link to every media file used, not just a generic link to the main site!
The list below is by no means exhaustive. Within the Code Institute Slack community, you can find more "free media" links
by sending yourself the following command: `!freemedia`.

⚠️⚠️ EXAMPLE LINKS - REPLACE WITH YOUR OWN ⚠️⚠️

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [Pexels](https://www.pexels.com) | entire site | image | favicon on all pages |
| [Lorem Picsum](https://picsum.photos) | home page | image | hero image background |
| [Unsplash](https://unsplash.com) | product page | image | sample of fake products |
| [Pixabay](https://pixabay.com) | gallery page | image | group of photos for gallery |
| [Wallhere](https://wallhere.com) | footer | image | background wallpaper image in the footer |
| [This Person Does Not Exist](https://thispersondoesnotexist.com) | testimonials | image | headshots of fake testimonial images |
| [Audio Micro](https://www.audiomicro.com/free-sound-effects) | game page | audio | free audio files to generate the game sounds |
| [Videvo](https://www.videvo.net/) | home page | video | background video on the hero section |
| [TinyPNG](https://tinypng.com) | entire site | image | tool for image compression |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his support and deep knowlege and help advice throughout this project throughout the development of this project. His support which kept me going during periods of self doubt and imposter syndrome. 
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
