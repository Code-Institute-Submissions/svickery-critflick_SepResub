# CritFlick
## Movie Review Website

[View website in Github pages!](https://github.com/svickery/critflick)

[View in Heroku](https://critflick.herokuapp.com)

![alt text](https://github.com/svickery/critflick/blob/a34fd119aa083fdadd7bcf025550fc65077fbb73/testing/critflick.jpg "Website Screenshot")

A website designed for movie fans around the world to post their own reviews of movies. It's purpose is to be an alternative to the status quo of movie reviewers working in the industry today. While most professional reviewers are looking for the most "worthy" of movies, CritFlick aims to give the opinion back to the people. 

Users can become a member almost instantly and start writing their reviews for the rest of the world to see. Anyone can read the reviews, but to write one you have to join. It is free and the only goal is to spread word the about movies new or old. 

The user goals of the website are as follows:

* See reviews of movies new and old
* To be able to search for a movie review
* To join the website
* Once the user has joined, they would like to contribute reviews
* To be able to add, delete and edit their reviews
* Have the option to log in and out of website
* See details of movies. Title, genre, director, actor etc.

## UX

#### Ideal user for the website:

* Movie lovers
* Aspiring writers
* People within the industry 
* Willing to become a member 
* Enjoys an alternative to mainstream media

#### Visitors for the website will be looking for:

* Movie reviews
* Be able to check the ratings of movies
* Check the running time of movies
* Search for whichever movie they like in the database
* A pleasant visual experience in line withe a cinema like feel

#### This website is best to help users because:

* Most review sites are filled with long winded and pretentious articles
* It allows the user to be involved with the website and become a contributor
* This website is:
    - Easy to navigate
    - Efficient with information
    - Professionally desinged and visually appealing

#### User stories:

As a site user, I want to:

1. As a new visitor I want to be able to access the website on any device available to me
2. As a new visitor I want to easily navigate the website
3. As a new visitor I want it so content is easily read and information must be displayed correctly 
4. As a user I want to be able to view movie reviews and navigate there easily 
5. As a user I want to be able to contribute my own articles to the website
6. As a user I want to be able to be able to create, edit and delete an article of my choosing 
7. As a user I want to be able to log in and out as and when
8. As a user I want to be able to search for particular movie reviews
9. As a potential user I want to find social media links
10. As a potential user I want to be able to join the site easily as a member 
11. As a returning user I want to be able to log in easily 
12. As a returning user I want to be able navigate easily to section I would like

As a site owner, I want to:

1. Provide the best information for a user to make their choices to contribute to the website 
2. Provide information on movies stored in the database 
3. Provide information for movies such as genre, director, run time etc
4. Provide the user with a clean looking and professional website
5. Allow the user to access our social media so they can access the information they need on whichever format they choose

#### Wireframes:

[View Wireframes Here](https://www.figma.com/file/TLfVJCGUaDK7M33SHrGGYG/CritFlick?node-id=0%3A1)

The site changed a lot from its original conception. Time constraints didn't allow me to use a Movie API to show current cinema listings and the color scheme was changed to a darker effect to replicate the cinema feel. I had to change a lot of cards etc to make the site work correctly. 

## Features

The website has a scrolling effect on the index page and reviews page using a parallax effect. This is so the website not only looks good but also be navigated easily. There are seperate pages for different needs such as sign up form, log in form and add review form once a member. The navigation bar has been fixed at the top so that all pages are available during use of the site. In total there are nine pages available to use. However if you are not a member there are only four pages to view. On the reviews page there is a search bar to search for whichever movie they would like to see a review of. There is a footer with social media links at the bottom of each page. This footer also contatins copyright information.  

#### Home

The Home page features one large photography covering the top of the page. This includes hero text on the image. The hero text has a link to join the website as a member. Below the image there is an about section explaining to the user what the website is for and how they can get involved themselves. The name of the site also appears as a header and there is no logo used for the site. 

#### Reviews

The reviews page has a similar layout to the home page with a large image at the top and hero text allowing the user to join as a member easily. Below this image there are then cards which have large eye catching images and beneath those images, there is all the information you would need about a movie. Below that further is the review of the movie. This review section has a scrolling effect so that the user doesn't have to navigate elsewhere to read it in its full form. At the bottom of the review is the contributors name.  

#### Sign Up

A page linked on both the home and review pages. There is a basic form for your details to become a contributor to the site. This form also has a link to the terms and conditions of the website.   

#### Log In

This page has a simple log in form for users who are already members. 

#### Profile 

Once a user has logged in, they will be redirected immediately to their own profile page. This has a flash message to welcome the user, a title for the profile user and an add review button underneath. This is designed to encourage the user to contribute immediately. Beneath that the user will be able to see all their past reviews they have written. Each review has an option to edit and delete in bold red. The edit function opens a new page.

#### Add Review

Located in the navigation bar as well as being able to from the previously mentioned add review button on the profile page. Users can add a review whenever the choose and will be given a simple form to follow. This includes a url link for the user to add for the review. Once the information is complete and the review is written, there is a submit button to add this to the site. This review will be visible to all people navigating to the site. 

#### Edit Review

This is not available in the navigation but links directly from the edit button. This page will render all the previous information supplied in the review. 

#### Log Out

This is located in the navbar and is only a single click function. 

#### Terms and Conditions

Not located in the navbar and only accessible from the sign up form. 

#### Footer

In the footer is copyright information and links to the social media sites.

#### Possible Future Features

* Use an API to bring local current showing times in cinemas near them. 
* A comments section for each review. Only members are allowed to use this.
* Could be expanded to include TV shows also.

## Technologies Used

* The project uses HTML, CSS and JavaScript languages. 
* [Github](https://github.com/) - I used this for all coding (IDE) while building the website.
* [Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/) - Used for grid layouts and cards on my page. Also allowed me to use Font Awesome icons for my social media links. 
* [Font Awesome](https://fontawesome.com/) - Used for icons in conjuction with bootstrap. 
* [Google Fonts](https://fonts.google.com/) - Used for entire website fonts.
* [Stack Overflow](https://stackoverflow.com/) - Used for styling forms etc from bootstrap. 
* [Web Formatter](https://webformatter.com/) - Used to make my code cleaner and easier to read.
* [W3Schools](https://www.w3schools.com/) - Used to help with various coding questions.
* [Autoprefixer](https://autoprefixer.github.io/) - Used to ensure CSS is correct
* [JQuery](https://jquery.com/) - Used for JQuery elements applied in JavaScript and some help with writing code.
* [Rotten Tomatoes](https://www.rottentomatoes.com/) - Used to have reviews added to site.
* [W3 Validator](https://validator.w3.org/#validate_by_input) - Used to ensure HTML is correct.
* [JS Lint](https://jslint.com/) - Used to ensure JavaScript is correct.

## Testing

To test the website, the project code was run through both a Markup checker, a CSS checker and a JavaScript checker, below are the screenshots of the results and explanations. 

[Markup Validator](https://validator.w3.org/#validate_by_input) 

![alt text](https://github.com/svickery/critflick/blob/a34fd119aa083fdadd7bcf025550fc65077fbb73/testing/html-validator.jpg "HTML Validator")

The errors that have shown up are ones that can't be avoided. The errors are either in the head or the scripts section. The validator doesn't recognise jquery correctly and the head data is from VS Code's own template. 

[CSS Validator](https://jigsaw.w3.org/css-validator/ "CSS Validator") 

![alt text](https://github.com/svickery/critflick/blob/a34fd119aa083fdadd7bcf025550fc65077fbb73/testing/css-validator.jpg "CSS Validator")

The errors shown here are from a getbootstrap styling I used which the validator does not recognise.

[JavaScript Validator](https://jslint.com/)

![alt text](https://github.com/svickery/critflick/blob/a34fd119aa083fdadd7bcf025550fc65077fbb73/testing/jslint.jpg)

The JS validator shows up some issues with certain characters being used, such as the use of '$' and to use double quotes. However this would make the code unusable. Validator doesn't seem to recognise jquery.

#### Testing User Stories

 * ##### New Visitor Goals
   
    i. *As a new visitor I want to be able to access the website on any device available to me*
  
     a. Site is fully functional upon load and is designed with mobile first in mind. 
     b. All info is available in any format, no information has been removed or shortened.
     
    ii. *As a new visitor I want to easily navigate the website*
    
     a. As soon as the website is clicked there is a navigation bar at the top of the page.
     b. Scrolling down the page, navigation is still easy as the navigation bar stays at the top of the page.
     c. The site uses a parallax effect and fixed navbar therefore navigation is always smooth. There is no need to keep going back and forth through pages, all         information is on one scrolling page. 
    
    iii. *As a new visitor I want it so content is easily read and information must be displayed correctly*
   
     a. As site loads, colour scheme is modern and clean.  
     b. Font is clear and professional, easy to read and large where necessary.
     c. All functions are explained to the user, such as buttons and clickable pictures in Shopping section.
     
![alt text](https://github.com/svickery/critflick/blob/a34fd119aa083fdadd7bcf025550fc65077fbb73/testing/home.jpg)
    
 * ##### User Goals
 
    i. *As a user I want to be able to view movie reviews and navigate there easily*
    
     a. Navigation immediately shows Reviews page as an option. 
     b. All reviews areas are titled. 
     
 ![alt text](https://github.com/svickery/critflick/blob/a34fd119aa083fdadd7bcf025550fc65077fbb73/readme/reviews.jpg)
    
   ii. *As a user I want to be able to contribute my own articles to the website*
    
     a. Add Review is in Navbar and Profile page once a user.
     b. Add Review form is self explanatory and easy to use.
     
![alt text](https://github.com/svickery/critflick/blob/a34fd119aa083fdadd7bcf025550fc65077fbb73/readme/addreview.jpg)
     
   iii. *As a user I want to be able to be able to create, edit and delete an article of my choosing*
     
     a. Profile page has all these functions.
     
![alt text](https://github.com/svickery/critflick/blob/a34fd119aa083fdadd7bcf025550fc65077fbb73/readme/profile.jpg)

![alt text](https://github.com/svickery/critflick/blob/a34fd119aa083fdadd7bcf025550fc65077fbb73/readme/profileone.jpg)
     
   iv. *As a user I want to be able to log in and out as and when*
    
     a. Log in clearly displayed in navigation when arrive on page.
     b. Log out clearly displayed in navigation once signed in. 
     
   v. *As a user I want to be able to search for particular movie reviews*
   
     a. Search bar clearly displayed on reviews page immediately after logging in. 

![alt text](https://github.com/svickery/critflick/blob/a34fd119aa083fdadd7bcf025550fc65077fbb73/readme/search.jpg)

 * #### Potential User Goals

    i. *As a potential user I want to find social media links*
    
     a. Social media links clearly displayed in footer.
     
   ii. *As a potential user I want to be able to join the site easily as a member*
   
     a. Join Us button displayed on home page and can't be missed.
 
 * ##### Returning User Goals
 
    i. *As a returning user I want to be able to log in easily*
    
     a. Log in immediately available in fixed navbar.
     
    ii. *As a returning user I want to be able navigate easily to section I would like*
    
     a. If returning, a user will most likely be looking for a specific section most likely.
     b. All sections are easily seen in navigation bar at top of page as a logged in user.

#### Further Testing

 * Testing was completed on desktop browsers Google Chrome, Safari and Microsoft Edge.
 * Testing was completed on numerous devices iPhone X, iPhone 12, iPad, Google Pixel, Laptop and Desktop(including larger screen).
 * All testing went well apart from a couple of issues with parallax images on smaller devices. On inspect of the page all looked fine until tested in real life  

#### Known Bugs

 * One bug is that the footer will only be at the bottom of the viewport and not the bottom of the page. 
 * For some reason the parallax images are not showing correctly on mobile. During inspection on the website this appeared fine, but not when viewing on actual mobile phone.
 * There is minial site wobble and not sure how this can be addressed further.

## Deployment

This site is hosted by GitHub pages and deployed directly from the master branch. The site updates automatically from updates that are new commits from the master branch. For the site to deploy on GitHub pages the landing page must be correctly named 'index.html'.

I deployed the site by following the next steps:

1. Logged into GitHub and located the correct repository
2. Went into Settings at the top of my Enjoy Bristol repository
3. Located GitHub "Pages" in settings
4. Selected "Master Branch" from the "Source" dropdown
5. Page automatically refreshed, I scrolled back to "Pages" section to find the newly published site

To make a clone of this site, please follow these steps:

1. Log in to GitHub and find the repository required
2. Click "Clone or download"
3. Use the "Clone with HTTPS" option and copy the link
4. Open Git Bash
5. Edit the working directory to a location you want it to be cloned in
6. Type `git clone` and paste the url you copied previously which should look as follows:

`https://github.com/YOUR-USERNAME/YOUR-REPOSITORY` 

7. Press enter and the repository should be cloned


## Credits

#### Content

All text and content on the page was written by myself apart from some Python logic which I found on a fellow code institute's website called Travel Reviews. I also took the user authentication and CRUD functionality from the code institute lessons. 

#### Media

All images used on this page were taken from [unsplash.com](https://unsplash.com/). URL links taken from Google.

#### Code

Code for the navigation bar and footer were taken from [Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/).

Code for the forms and buttons was taken from [W3 Schools](https://www.w3schools.com/).

Code for User Authentication and CRUD functionality taken from Code Institue lessons.

All other code was written by myself with help from sites [Stack Overflow](https://stackoverflow.com/)


## Acknowledgments

Acknowledgment has to be made to Gille Matea who is on the same course as me. Her site was an inspiration to me for my project and I used her python logic code to help make my site work. Very appreciative. Another acknoledgments are my mentor Adegbenga Adeye. Jim Morel, Brian XS and Sean Young who I met through Slack helped with various other issues. 
