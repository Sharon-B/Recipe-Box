# Testing

## Code Validators & Auto Prefixer:
#### CSS code was passed through Auto Prefixer to add vendor prefixes:
* 

#### CSS code was passed through the W3C CSS Validator: 


#### HTML code was passed through the W3C Markup Validator. 


#### Javascript code was passed through jshint. 

#### Python code was passed through PEP8 online. 


## Lighthouse from Chrome Dev Tools Testing:
### Desktop report:

### Mobile Report:

## Responsiveness Testing:

The responsiveness of the website was tested using Chrome Dev Tools and setting it to display on various mobile/tablet devices that are included. Responsiveness is optimised for screen sizes from 320px up and in portrait orientation for smaller devices.

## Device Testing:

All aspects of the website mentioned above were manually tested on the following 
devices: iPad 2, iPhone 8, MacBook Pro.

## Browser Testing:

All aspects of the website mentioned above were manually tested on the following 
browsers: Chrome, Safari, Mozilla Firefox

## Friends & Family User Testing: 

The general feedback was that the site looks well and is easy to navigate. 
Devices used: iPad Pro, iPhone 8 Plus, Laptop (windows running the Chrome browser).

## Testing User Stories

### Testing New User Stories

1. As a user I want to be able to view recipes on my tablet device so that I can use it while cooking in the kitchen.

    * The site is responsive to ensure excellent user experience on tablet devices.

    * The layout of each page is optimised for smaller devices to make it easy to read and navigate.

    * Buttons are used consistently throughout the site which are easily recognisable and clickable for users on smaller devices.

    * Pagination is used to avoid endless scrolling.

2. As a user I want to have my own profile where I can keep track of my own recipes.

    * A registration page is provided so users can register to have their own profile.

    * Once a user has registered they can login via the login page anytime they return to the site.

    * When a user adds a recipe it is displayed on their profile page for easy access.

3. As a user I want a visually appealing site so that I will enjoy browsing recipes for longer.

    * Recipes are displayed in recipe cards for easy browsing, each card contains the basic information of an image, recipe name, timings, recipe description and added by to give the user an overview of the recipe.

    * Professional look and a friendly feel to the website.

    * Intuitive and easy to navigate around the site.

    * Recipes are managed by an admin to ensure a high standard and continuity throughout.

4. As a user I want be able to check recipes on my mobile so that I can see what ingredients I may need while I’m out.

    * The site is responsive to ensure excellent user experience on mobile devices.

    * The full recipe page is easily accessed by clicking the recipe title, the ingredients are then clearly displayed for the user to read.

5. As a user I want to be able to contact the site owner so that I can ask any questions or offer recommendations that I may have.

    * A contact page is provided, so the user can quickly and easily send a message to the site owner.

    * Once the message is submitted the user sees a ‘Thank you’ message displayed on the screen, so they know the message has been sent.

6. As a user I want to be able to view the site owners social media pages so that I can see what else they are doing.

    * Social media links are provided in the footer of each page so the user can access them.

    * The links are provided using instantly recognisable icons.

7. As a user I want to be able to browse other peoples recipes so that I can find inspiration for mealtimes.

    * The recipes page is provided where a user can browse all the recipes available.

    * A search bar is also provided on this page so the user can search for something in particular eg ‘dinner’ or ‘chicken’

8. As a user I want to be able to search for recipes so that I can find recipes for things I enjoy.

    * A search bar is provided on the recipes page so that a user can search for particular things in the recipe database.

    * The search functions across the recipe name, description and category fields of the recipes collection, so a user can search for ‘chicken’ or  meal type eg ‘dinner’.


### Testing Registered Users Stories
9. As a registered user I want to be able to add my own recipes for safe keeping so that I can easily find them.

    * Once registered a user is directed to their profile page, ‘add recipe’ is now available as an option in the navigation menu.

    * A user can click on add recipe to open a page where they can add the details of their recipe, at the bottom of the page an add button is provided so the user can add the recipe to their profile.

    * Once a user adds a recipe it is displayed in their profile page.

10. As a registered user I want to be able to update my own recipes so that I can change them as I want.

    * Once a user adds a recipe it is displayed in their profile page, with an additional button options  to edit or delete the recipe if desired.

    * By clicking the edit button a user can then edit or update their own recipe as they so wish.

11. As a registered user I want to be able to remove my own recipes so that I can maintain what recipes I have in my profile.

    * Once a user adds a recipe it is displayed in their profile page, with an additional button options  to edit or delete the recipe if desired.

    * By clicking on the delete button the recipe is deleted.


### Testing Admin User Stories
12. As a admin user I want to be able to edit/remove any recipe so that I can maintain a well curated site.

    * Once an admin user is logged in an ‘admin menu’ option is now available in the navigation menu, which gives the admin user the option to Manage Recipes

    * From the Manage Recipes page the admin can edit or delete any recipe on the site.

13. As an admin user I want to be able to edit/add/remove categories so that I can adapt to the changing needs of our users.

    * Once an admin user is logged in an ‘admin menu’ option is now available in the navigation menu, which gives the admin user the option to Manage Categories.

    * From the Manage Categories page an admin can add, edit or delete categories as needed.

14. As an admin user I want to be able to edit/remove users so that I can keep them up to date.

    * Once an admin user is logged in an ‘admin menu’ option is now available in the navigation menu, which gives the admin user the option to Manage Users.

    * From the Manage Users page an admin can edit or delete users as needed.


### Testing Site Owner Stories

1.	As a site owner I want to provide a good user experience for my users, so that they want to come back.

    * Professional look and a friendly feel to the website.

    * Visually appealing throughout.

    * Intuitive and easy to navigate around the site.

    * Future releases to add more features to keep users interested and offer something new to returning users.

# Manual Testing:

Each page was tested and passed under the criteria set out below.

## All Pages: 

### Header:

* Displays on all pages.

    #### Logo:

* The logo is displayed in the header.

* Displays on all pages.

* The logo is a clickable link which returns the user to the home page.

	#### Navigation:

* Displays on all pages except the 404.html error page.

* On mobile devices a collapsed menu is provided, on clicking the burger icon the navigation menu is revealed.

* On larger devices, from screen sizes 992px and up the navigation menu items appear in the header.

* Each navigation menu item: 

    * Highlights on hover

    * Is clickable

    * Is links to the associated page

* The current active page is highlighted.

* For non-registered users the navigation menu items are:

	    Home, Recipes, Log In, Register & Contact

* For Registered & Logged in users the navigation menu items are:

	    Home, Recipes, Profile, Add Recipe, Log Out & Contact

* For an Admin User the navigation items are:

	    Home, Recipes, Profile, Add Recipe, Admin Menu, Log Out & Contact

* The admin navigation menu has an additional dropdown menu called Admin Menu with 3 further navigation items:

	    Manage Recipes, Manage Categories, Manage Users

### Footer:

* Displays on all pages.

* Contains icons with links to social media pages.

* Icons highlight on hover.

* Social Media icons display on all pages except the 404.html error page.

## Home Page:

* Displays for all users.

### Hero Image:

* Displays a responsive hero image with a welcome message.

* Displays recipe cards for the last 6 recipes added to the database.

### Recipe Cards:

* Provide an overview of each recipe with recipe image, recipe name, timings, recipe description and added by details.

* The recipe name on each recipe card is a clickable link.

* Recipe name highlights on hover.

* Clicking on the recipe name brings the user to the full page of the recipe clicked.

### Delete/ Edit Buttons:

* Only display at the bottom of each card if the recipe was added by the logged in user.

* Buttons highlight on hover.

* Edit button redirects the user to the Edit Recipe page.

* Delete button immediately deletes the recipe from the database and displays a ‘Recipe Deleted’ message to the user.

## Recipes Page:

* Displays for all users.

* Displays recipe cards for all recipes from the database.
	
### Recipe Cards:

* Provide an overview of each recipe with recipe image, recipe name, timings, recipe description and added by details.

* Each recipe name on the recipe card is a clickable link.

* Recipe name highlights on hover.

* Clicking on the recipe name brings the user to the full page of the recipe clicked.

### Delete/ Edit Buttons:

* Only display at the bottom of each card if the recipe was added by the logged in user.

* Buttons highlight on hover.

* Edit button redirects the user to the Edit Recipe page.

* Delete button immediately deletes the recipe from the database and displays a ‘Recipe Deleted’ message to the user.

### Search:

* Search bar is displayed.

* Text search is carried out on the recipes collection.

* Reset and search buttons are displayed for the search.

* Buttons highlight on hover.

* Search button submits the search query and returns the associated results.

* Search results are paginated if greater than 9 results found

* If no search results found a message of ‘no results found’ is displayed

* Reset button reloads the recipes page.

### Pagination:

* Uses pagination, if there are more than 9 recipes.

* Displays the pagination links at the bottom of the page.

* Pagination links are working.

* Pagination links highlight the current page.

## Full Recipe Page:

* Displays for all users.

* Displays the full recipe on the page.

* Displays the recipe name, recipe image, timings, category, recipe description Ingredients heading and the list of ingredients, Method heading and the steps of the method.

### Delete/ Edit Buttons:

* Only display if the recipe was added by the logged in user.

* Buttons highlight on hover.

* Edit button redirects the user to the Edit Recipe page.

* Delete button immediately deletes the recipe from the database and displays a ‘Recipe Deleted’ message to the user.

## Profile Page:

* Only available when a user is logged in.

* Displays the users name in the heading eg User’s Profile.

* Displays the users recipes as Recipe Cards so the user can easily see what recipes they have added.

* Recipe Name on recipe cards is clickable, highlights on hover and opens the recipe in full page.

### Recipe Cards:

* Provide an overview of each recipe with recipe image, recipe name, timings, recipe description and added by details.

* Each recipe name on the recipe card is a clickable link.

* Recipe name highlights on hover.

* Clicking on the recipe name brings the user to the full page of the recipe clicked.

### Delete/ Edit Buttons:

* Display at the bottom of each recipe card.

* Buttons highlight on hover.

* Edit button redirects the user to the Edit Recipe page for that recipe.

* Delete button immediately deletes that recipe from the database and displays a ‘recipe deleted’ message to the user.

## Add Recipe Page:

* Only available when a user is logged in.

* Displays a form for the user to fill in with their recipe details.

* Form does not submit if any fields are empty.

* Placeholder text is provided to help guide the user in filling out the form.

* Help text is also provided where the user must comply to specific input criteria eg Cook Time should be in the format of: 90 mins

* If user submits the form with an empty field a message will be displayed on that field, indicating that it must be filled in.

* If the Select Category dropdown field is not filled in a message will appear asking the user to select an item from the list.

### Add Recipe/Cancel buttons:

* Highlight on hover.

* Add Recipe button only submits the form if all fields are filled out correctly, otherwise the user is asked to fill out the required fields.

* Add Recipe button submits the recipe and the user is redirected to their profile page and a ‘Recipe Successfully Added’ message is displayed.

* Cancel button redirects the user back to their profile page.

## Edit Recipe Page:

* Only available when a user is logged in for recipe that they have added.

* Displays a form pre-populated with the details of the recipe to be edited for the user to make changes to.

* All fields are required for the form to submit.

* Placeholder text is provided to help guide the user in filling out the form.

* Help text is also provided where the user must comply to specific input criteria eg Cook Time should be in the format of: 90 mins

* If user submits the form with an empty field a message will be displayed on that field, indicating that it must be filled in.

### Edit Recipe/ Cancel Buttons:

* Highlight on hover.

* Edit Recipe button only submits the form if all fields are filled out correctly, otherwise the user is asked to fill out the required fields.

* Edit recipe button submits the recipe and the user is redirected to their profile page and a ‘Recipe Successfully Updated’ message is displayed.

* Cancel button redirects the user back to their profile page.

## Register Page:

* Displays for all users.

* Displays a registration form.

* User must enter a username of between 5 -15 characters.

* If username already exists when the form is submitted a ‘Username Already Exists, Please Choose Another’ message is displayed and the page is reloaded.

* User must enter an email in the valid format.

* User must enter a password of between 5 - 15 characters

### Register Button:

* Highlights on hover.

* Form does not submit if fields are not filled in correctly.

* No field can be empty.

* Submits form and redirects the user to their profile page with a ‘Registration Successful’ message.

### Log In link:

* Highlights on hover.

* For users already registered there is a link that redirects them to the 
log in page.

## Log In Page:

* Displays for all users.

* Displays a log in form.

* User must enter their username of between 5 -15 characters.

* User must enter their password of between 5 - 15 characters.

* If user enters an invalid username or an incorrect username/password combination a 'Incorrect Username/Password' message displays.

### Log In Button:

* Highlights on hover.

* Form does not submit if fields are not filled in correctly.

* No field can be empty.

* Submits form and redirects the user to their profile page with a ‘Log In Successful’ message.

### Register link:

* Highlights on hover.

* For users not already registered there is a link that redirects them to the Register page.

## Contact Page:

* Displays for all users.

* Displays a contact form.

* Users must enter their name.

* Users must enter their email.

* Users must enter a message in the text area.

### Send Button:

* Highlights on hover.

* Form does not submit if fields are left empty.

* Submits the form and displays a ‘Thank you for your email, we will be in touch’ message.

## Manage Recipes Page:

* Only accessible to an admin user.

* If user is not logged in and tries to access the page, they are redirected to the login page and a ‘Please Log In Message is displayed’

* If a user is logged in but not an admin and tries to access the page they are redirected to the recipes page and a ‘You do not have permission for that’ message is displayed.

* Displays recipe cards for all recipes from the database.

### Recipe Cards:

* Provide an overview of each recipe with recipe image, recipe name, timings, recipe description and added by details.

* Each recipe name on the recipe card is a clickable link.

* Recipe name highlights on hover.

* Clicking on the recipe name brings the user to the full page of the recipe clicked.

### Delete/ Edit Buttons:

* Display at the bottom of each recipe card.

* Buttons highlight on hover.

* Edit button redirects the user to the Edit Recipe page for that recipe.

* Delete button immediately deletes that recipe from the database and displays a ‘Recipe deleted’ message to the user.

### Pagination:

* Uses pagination, if there are more than 9 recipes.

* Displays the pagination links at the bottom of the page.

* Pagination links are working.

* Pagination links highlight the current page.

## Manage Categories Page:

* Only accessible to an admin user.

* If user is not logged in and tries to access the page, they are redirected to the login page and a ‘Please Log In Message is displayed’

* If a user is logged in but not an admin and tries to access the page they are redirected to the recipes page and a ‘You do not have permission for that’ message is displayed.

* Displays a search bar, add category button and all the categories with edit & delete buttons for each.


### Search:

* Search bar is displayed.

* Text search is carried out on the categories collection.

* Reset and search buttons are displayed for the search functionality.

* Buttons highlight on hover.

* Search button submits the search query and returns the associated results.

* If no search results found a message of ‘no results found’ is displayed

* Reset button reloads the manage categories page.

### Add Category Button:

* Highlights on hover.

* Redirects the user to the add category page.

### Categories:

* A list of available categories is displayed, with delete/edit buttons for each

### Delete/ Edit Buttons:

* Display for each category listed

* Buttons highlight on hover.

* Edit button redirects the user to the Edit Category page for that category.

* Delete button immediately deletes that category from the database and displays a ‘Category deleted’ message to the user.

## Edit Categories Page:

* Only accessible to an admin user.

* If user is not logged in and tries to access the page, they are redirected to the login page and a ‘Please Log In Message is displayed’.

* If a user is logged in but not an admin and tries to access the page they are redirected to the recipes page and a ‘You do not have permission for that’ message is displayed.

* A pre-populated form is displayed to allow the user to update the selected category.

### Cancel/ Edit Buttons:

* Buttons highlight on hover.

* Edit button submits the form, returns the user to the manage categories page with a ‘Category updated” message

* Cancel button returns the user to the manage categories page.

## Add Category Page:

* Only accessible to an admin user.

* If user is not logged in and tries to access the page, they are redirected to the login page and a ‘Please Log In Message is displayed’.

* If a user is logged in but not an admin and tries to access the page they are redirected to the recipes page and a ‘You do not have permission for that’ message is displayed.

* Displays a form where the user can enter a new category name.

### Cancel/ Add Buttons:

* Buttons highlight on hover.

* Add button submits the form, returns the user to the manage categories page with a ‘New category added” message.

* Cancel button returns the user to the manage categories page.

## Manage Users Page:

* Only accessible to an admin user.

* If user is not logged in and tries to access the page, they are redirected to the login page and a ‘Please Log In Message is displayed’.

* If a user is logged in but not an admin and tries to access the page they are redirected to the recipes page and a ‘You do not have permission for that’ message is displayed.

* Displays a search bar and all the users with edit & delete buttons for each.

### Search:

* Search bar is displayed.

* Text search is carried out on the users collection.

* Reset and search buttons are displayed for the search functionality.

* Buttons highlight on hover.

* Search button submits the search query and returns the associated results.

* If no search results found a message of ‘no results found’ is displayed.

* Reset button reloads the manage users page.

### Categories:

* A list of available users is displayed, with delete/edit buttons for each

### Delete/ Edit Buttons:

* Display for each user listed

* Buttons highlight on hover.

* Edit button redirects the user to the Edit User page for that user.

* Delete button immediately deletes that user and displays a ‘User deleted’ message to the user.

## Edit Users Page:

* Only accessible to an admin user.

* If user is not logged in and tries to access the page, they are redirected to the login page and a ‘Please Log In Message is displayed’.

* If a user is logged in but not an admin and tries to access the page they are redirected to the recipes page and a ‘You do not have permission for that’ message is displayed.

* A pre-populated form is displayed to allow the user to update the selected user.

### Cancel/ Edit Buttons:

* Buttons highlight on hover.

* Edit button submits the form, returns the user to the manage categories page with a ‘User updated” message

* Cancel button returns the user to the manage categories page.

## 404 Error Page:

* Displays when a 404 - page not found error is encountered.

* Tells the user that the page could not be found.

* Provides a return home button.

### Return Home Button:

* Highlights on hover.

* Returns the user to the home page.
