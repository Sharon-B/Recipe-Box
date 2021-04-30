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


## Device testing:



## Browser Testing:




## Friends & Family User Testing: 



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
