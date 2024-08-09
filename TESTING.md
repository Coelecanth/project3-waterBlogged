# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

The structure of the Testing for "Water Blogged" is as follows  

## Feature Testing:

### Usability Testing
- User can register and password are checked for consistency
- the navigation bar functions correctly 
- User can Logon and logoff
- User can create, update and delete their own records  
- The session rating function is working 
- The geo-location recording is working

### Defence programming 

In this section we test that users can only access features and functionality they are supposed to be able to access 
This would include 
- Performing CRUD operations only on records that they have created  
- Superuser have access to Super user functions and normal user do not 
- Normal user not being able to brute force there way into pages to access super user features

## Compatibility Testing:

- Browser Compatibility: Testing on different browsers (Chrome, Firefox, Safari, Edge, etc.) to ensure consistent performance.
- Device Compatibility: Ensuring functionality across various devices (desktops, laptops, tablets, and mobile phones).

## Regression Testing:

## Documentation and Logs:

Maintain records of testing procedures, results, and any bugs encountered along with their resolutions. This helps demonstrate a systematic approach to testing and problem-solving.
User Feedback Incorporation:

If applicable, mention how user feedback has been taken into account and implemented to enhance the user experience.


## Code Validation
 the following items were code checked 
 - HTML
 - Javascript
 - Python
 - CSS

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| templates | add_tasks.html | ![screenshot](documentation/html_validation/add_tasks.png)| |
| templates | edit_task.html | ![screenshot](documentation/html_validation/edit_task.png) | |
| templates | login.html | ![screenshot](documentation/html_validation/login.png) | |
| templates | profile.html | ![screenshot](documentation/html_validation/profile.png) | |
| templates | register.html | ![screenshot](documentation/html_validation/register.png) | |
| templates | tasks.html | ![screenshot](documentation/html_validation/tasks.png) | |
| templates | categories.html | ![screenshot](documentation/html_validation/categories.png) | |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

All the errors found (x3 errors and x649 Warnings) were with frameworks that were being used on Water Blogged site,
the Errors were from: 
 - Leaflet
 - Materiaze 

The Warning were from
 - Font Awesome 

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | style.css | ![screenshot](documentation/css_validation/css.png) | |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

The JSHint tool showed only warning for the JSscript for the Leaflet Geo Location

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | js_script.js | ![screenshot](documentation/js_validation/js_script.png) |  Jscript for Materialize CSS functions |
| static | add_task.html | ![screenshot](documentation/js_validation/add_leaflet.png) |  Jscript for add in g location for geo-location function Leaflet  |
| static | edit_task.html | ![screenshot](documentation/js_validation/edit_leaflet.png) |  Jscript for edit location for geo-location function Leaflet  |


### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | app.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Coelecanth/project3-waterBlogged/main/app.py) | ![screenshot](documentation/python_validation/python.png) | |

## Browser Compatibility


| Browser | Home | add user | register | Notes |
| --- | --- | --- | --- | --- | 
| Chrome | ![screenshot](documentation/browsers/chr-tasks.png) | ![screenshot](documentation/browsers/chr-add.png) | ![screenshot](documentation/browsers/chr-reg.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/ff-tasks.png) | ![screenshot](documentation/browsers/ff-add.png) | ![screenshot](documentation/browsers/ff-reg.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/edg-tasks.png) | ![screenshot](documentation/browsers/edg-add.png) | ![screenshot](documentation/browsers/edg-reg.png) | Works as expected |

## Responsiveness

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss testing the live/deployed site on various device sizes.

The minimum requirement is for the following 3 tests:
- Mobile
- Tablet
- Desktop

**IMPORTANT**: You must provide screenshots of the tested responsiveness, to "prove" that you've actually tested them.

Using the "amiresponsive" mockup image (or similar) does not suffice the requirements.
Consider using some of the built-in device sizes in the Developer Tools.

If you have tested the project on your actual mobile phone or tablet, consider also including screenshots of these as well.
It showcases a higher level of manual tests, and can be seen as a positive inclusion!

Sample responsiveness testing documentation:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Add | register | Notes |
| --- | --- | --- | --- | --- | 
| Mobile (DevTools) | ![screenshot](documentation/resp/m-chr-tasks.png) | ![screenshot](documentation/resp/m-chr-add.png) | ![screenshot](documentation/resp/m-chr-reg.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/resp/t-chr-tasks.png) | ![screenshot](documentation/resp/t-chr-add.png) | ![screenshot](documentation/resp/t-chr-reg.png) | Works as expected |
| Desktop | ![screenshot](documentation/resp/d-chr-tasks.png) | ![screenshot](documentation/resp/d-chr-add.png) | ![screenshot](documentation/resp/d-chr-reg.png)| Works as expected |

## Lighthouse Audit

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports.
Avoid testing the local version (especially if developing in Gitpod), as this can have knock-on effects of performance.

If you don't have Lighthouse in your Developer Tools,
it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Don't just test the home page (unless it's a single-page application).
Make sure to test the Lighthouse Audit results for all of your pages.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

Sample Lighthouse testing documentation:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | Some minor warnings |
| About | ![screenshot](documentation/lighthouse/lighthouse-about-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-about-desktop.png) | Some minor warnings |
| Gallery | ![screenshot](documentation/lighthouse/lighthouse-gallery-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-gallery-desktop.png) | Slow response time due to large images |
| x | x | x | repeat for any other tested pages/sizes |

## Defensive Programming

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | When the user is not logged on as a user, they should be able to see records, and have no ability to edit records  | Tested the feature by loading the default site page | The feature behaved as expected, and the page was loaded showing records without any edit function either on records or in the navbar | Test concluded and passed | ![screenshot](documentation/def/default-logon.png) |
| | User (not logged on) cannot brute force there way to ADD records from home page | Tested this by copying the URL for add records (From a logged on user) and then pasting this into a browser, in the current not logged on session | The page reloaded with the message "You need to logon", loading the logon page. | Test concluded and passed | ![screenshot](documentation/def/acc-add-without-logon.png) |
| | User (not logged on) cannot brute force there way to EDIT records from home page | Tested this by copying the URL for edit records (From a logged on user) and then pasting this into a browser, in the current not logged on session | The page reloaded with the message "You need to logon", loading the logon page. | Test concluded and passed | ![screenshot](documentation/def/acc-add-without-logon.png) |
| | User (not logged on) cannot brute force there way to superuser features such as edit/add/categories | Tested this by copying the URL for edit categries (From a logged on superuser) and then pasting this into a browser, in the current not logged on session | The page reloaded with the message "You need to logon", loading the logon page. | Test concluded and passed | ![screenshot](documentation/def/acc-add-without-logon.png) |
| | Logged on user cannot brute force there way to EDIT records from home page for other peoples records  | Tested this by copying the URL for edit records (From a different logged on user) and then pasting this into a browser, in the current logged on session | The page reloaded with the message "You dont have access to this page", loading the home page. | Test concluded and passed | ![screenshot](documentation/def/bf-anothers-rec.png)| 
| | Logged on standard user cannot brute force there way to superuser features such as edit/add/categories | Tested this by copying the URL for edit categries (From a logged on superuser) and then pasting this into a browser, in the current not logged on session. Was then repeated for the ADD categroies, EDIT categroies. | For each of tests, the result was the same. The page reloaded with the message "Access denied: superuser access only", loading the home page. | Test concluded and passed | ![screenshot](documentation/def/acc-cats.png) |
| | Logged on standard user cannot brute force there way to superuser feature of  delete categories | Tested this by copying the URL for edit categries (From a logged on superuser) and then pasting this into a browser, in the current not logged on session. The delte categories calls a modal. So in this test I copied just the Modal URL and appended this to URL for the site e.g.   "get_categories#modal-66b0ca41aa243e156b3aaa16" to test this. | The page reloaded with the message "Access denied: superuser access only", loading the home page. | Test concluded and passed | ![screenshot](documentation/def/acc-cats.png) |
Logon/Logoff | | | | | |
| | When Logged in with a standard user level account, they should not see the edit categories in the navbar | Logged on with the standard account and was taken to the profile page | The feature behaved as expected, the navbar did NOT show the edit categories page and the profile text tells me "Im not a supperuser" | Test concluded and passed | ![screenshot](documentation/def/std-level-access.png) |
| | When Logged in with a super user level account, they should see the edit categories in the navbar | Logged on with the super user account and was taken to the profile page | The feature behaved as expected, the navbar DID show the edit categories page and the profile text tells me "I am a supperuser" | Test concluded and passed | ![screenshot](documentation/def/std-level-access.png) |
| | When the Logged on user presses the logout text the in the navbar | logged on user should be logged out and receive a flash message and be taken to the logon page | The feature behaved as expected, the user was logged out and recieved the flash message "You have been logged out" | Test concluded and passed | ![screenshot](documentation/def/logout.png) |
| | When the Logging on the fields name and password will report an error if not completed and login button pressed, eg if they are empty or the correct number of character are not entered. | The test was executed by trying to log onto the site with no user name | The feature behaved as expected, the user was not logged on and message "Please fill in the field" shown | Test concluded and passed | ![screenshot](documentation/def/logon-val.png) |
| Register | | | | | |
| | On registering a new user with site, the user is created and the DB collection user.is_superuser key is set to false, in addtion to this the session(is_superuser) is set to boolean "False" as well, and then user is logged on to the site. | This as tested by trying to create a new user | However when this was tried it was found that register failed as the is_superuser key was not defined, this was rectified by adding the 'session["is_superuser"] = False' to the register function. Aftert this change, the registration behaved as expected. | Test concluded and passed after making code changes | ![screenshot](documentation/def/success-reg.png) |
| | On registerinfg with the site, the site will perform a registration check to make sure your password is correct it does this bay asking you to repeat the password, so if the password do not match the it should fail the check | Tested this by trying to create a users with differing passwords | The feature behaved as expected, the registration failed and the messsgae "Passwords do not match!" is shown | Test concluded and passed | ![screenshot](documentation/def/reg-fail.png) |
Add and Edit pages  | | | | | |
| | Logged on user cannot ADD records which have blank fields  | Tested this by creating a new record for a logged on user | Any fields marked as mandatory are highlighted in orange, (see image), in addiiton the the geo location has to have selection made on the map, as otherwise ADD session button is greyed out | Test concluded and passed | ![screenshot](documentation/def/add-valid.png)| 
| | Logged on user cannot EDIT and save records which have blank fields  | Tested this by editing and existing record and blanking out a field and then trying to save it | When testing any fields marked as mandatory blanks fields are highlighted in orange (see image) | Test concluded and passed | ![screenshot](documentation/def/edit-valid.png)| 



## User Story Testing

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature09.png) |
| repeat for all remaining user stories | x |

## Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

This section is primarily used for JavaScript and Python applications,
but feel free to use this section to document any HTML/CSS bugs you might run into.

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

## Unfixed Bugs

> [!NOTE]  
> There are no remaining bugs that I am aware of.
