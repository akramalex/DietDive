# DietDive
![](static/images/sc.jpg)


## Welcome ! 
[View the live project here .](https://dietdive-013196ebea26.herokuapp.com/)

[View GitHub repository .](https://github.com/akramalex/DietDive)


## Introduction

DietDive is a project designed to provide users with easy access to valuable information about various diet plans, nutrition, and healthy living. Our platform offers an extensive collection of blog posts that explore popular diets, tips for maintaining a healthy lifestyle, and the latest wellness trends.


Visitors to the website have the opportunity to explore each blog post, accessing detailed information and captivating images of various diet. Additionally, users can initiate contact with DietDive through an integrated contact form, facilitating seamless communication.


Administrators have full CRUD capabilities to manage (add, edit, delete) blog posts on the front-end through the use of a user-friendly and intuitive UI.


To maintain the integrity of the platform, all comments undergo verification and approval by an administrator prior to publication on the website. This ensures that only authenticated and relevant contributions are displayed to the audience.






## UX

  ### The Strategy
  
  #### Site  Aims & Goals
  
   Provide Comprehensive Information on Various Diet Plans

  - Aim: To educate users on a wide range of diet plans, including their benefits, challenges, and suitability for different lifestyles.

   - Goal: Help users make informed decisions about diet and wellness by offering detailed, evidence-based content on diets like Mediterranean, Intermittent Fasting, Vegan, DASH, and more.
   User Interaction and Engagement

  - Aim: To allow users to engage with the content through comments and likes, creating a community of people interested in health and wellness.

  - Goal: Enhance user interaction by enabling the comment and like features on blog posts, allowing users to share their thoughts, experiences, and recommendations.
  Facilitate a Personalized Experience



  - Aim: To create a platform that encourages healthy living by promoting knowledge on diets, nutrition, and fitness.

 - Goal: Drive awareness about the importance of a balanced diet, and inspire users to explore different dietary approaches that can contribute to a healthier lifestyle.
Provide a User-Friendly and Accessible Platform

 - Aim: To ensure that users have a seamless, intuitive experience on the website, regardless of their device (mobile, tablet, desktop).

 - Goal: Design DietDive with responsive layouts, clear navigation, and an 
   easy-to-use interface to enhance usability and make content accessible to a diverse audience.



 - Aim: To foster a supportive community of health-conscious individuals who can share experiences, ask questions, and offer support to others on their diet journeys.

 - Goal: Engage users with a space to connect, learn from others, and share 
  advice. DietDive can become a community-driven platform that offers both expert opinions and user-generated content.
  Support Content Creation and Community Contributions



 - Aim: To improve visibility and ranking on search engines like Google.

- Goal: Implement SEO best practices, ensuring the website is easily discoverable by users searching for diet and wellness content. This includes optimizing blog posts, images, and page titles for SEO.



#### Scope 


 Due to the time and resources available, there will be some trade-offs in terms of features and development efforts. However, I anticipate that some further trade-offs may need to be made in later phases of the project. In order to focus on the MVP (Minimum Viable Product) and launch a basic proof of concept, I have divided the features into three categories to help prioritize and clarify which features are most essential for the initial release.

#### UX Efforts Must Address These:

 1- User Login & Authentication

 * Users must be able to register and log in to the website in order to 
  interact with the content (comment, like.).

 2- Commenting on Posts

 * Users must be able to comment on diet-related blog posts. Comments will be submitted for approval by the administrator before they are made publicly visible.

3- Liking Posts

 * Users must be able to like diet-related blog posts to show their interest. Liking functionality will also be available only for logged-in users.

4- Responsive Design

 * The website must be responsive, ensuring it functions well on both desktop 
  and mobile devices, providing a seamless user experience across different 
   screen sizes.


 5- Diet Information Pages

 * A page dedicated to each diet type (e.g., Mediterranean, Vegan, etc.) with detailed information, images, and health benefits.



6- Admins must be able to manage blog posts (create, edit, delete) and approve comments submitted by users before they are published.

#### UX Efforts Should Accommodate These:

1- Post Excerpts on Homepage

* Display short excerpts of blog posts with a  link on the homepage and category pages.

2- Contact Form

* Include a simple form for users to reach out to the administrators with inquiries or comments.

3- Basic Analytics for Admin

* Track key metrics such as the number of likes and comments on each post to provide admins with insights on content performance.


#### Unwise Use of Time to Address There:


1- User-Generated Content (Posts)

* Allowing users to create and submit their own blog posts is not a priority for the MVP and will be postponed for future phases.

2- Advanced User Analytics

* Tracking detailed user behavior, such as which posts users spend the most time reading or interacting with, should be deprioritized.

3- Advanced Search & Filters

for user search filters (e.g., based on health benefits, calorie count, etc.) are not critical at this stage.


4- Complex Community Features

* Features such as discussion boards or community chat should be postponed to future phases. For now, commenting and liking are sufficient for user interaction.

5- Interactive Diet Tools

* Tools like calorie calculators, diet planners, or interactive charts should be avoided in the MVP, as they would require significant development time and resources.

### Structure

To help me visualize a typical user journey around the site, I used [lucid.app](https://lucid.app/) to help me plan out the various routes.

![](static/images/sc-d.jpeg)


#### User Stories :

 - As an Admin i can..

   *  view comments on an individual post so that I can read the conversation.

   * create, read, update and delete posts so that I can manage my blog content.

   * create draft posts so that I can finish writing the content later.

   * approve or disapprove comments so that I can filter out objectionable comments.

   * create or update the about page content so that it is available on the site.

   * view all contact submissions so that I can respond to inquiries or feedback.


 - As a Site User I can...

   *  view a paginated list of posts so that I can I can select which post I want to view.
   
   * click on a post so that I can read the full text.

   *  view comments on an individual post so that I can read the conversation.

   * register an account so that I can comment on a post.

   * leave comments on a post so that I can be involved in the conversation.

   *  modify or delete my comment on a post so that I can be involved in the conversation.

   *  like a post so that I can show my appreciation for the content.

   *  unlike a post that I previously liked so that I can change my preference.

   * click on the About link so that I can read about the site.

   * use the Contact Us form so that I can reach out with questions or feedback.


###### Acceptance Criteria
   ![](static/images/sc-us.jpg)



###  Skeleton

  #### Wireframes:
  The appearance of each page of the website was planned by making wireframes. It was essential to provide a positive user experience for the user.

Initially, wireframes plans were hand-drawn on a notepad. More detailed wireframes were then created using a desktop version of [Balsamiq](https://balsamiq.cloud/). 
They can be found below:
 - home page

![](static/images/home.jpg)

- about 

![](static/images/about.jpg)

- contact 

![](static/images/cu.jpg)


- small screen


![](static/images/ss.jpg)

![](static/images/ss-2.jpg)




#### Surface

#### Color Scheme: 

I used the following Image to generate the following color scheme on [coolers](https://coolors.co/).co. The resultant color scheme was:

![](static/images/cs.jpg)


##### Typography:


 * Lato:

     Used for: The brand name in the navbar and text in the hero section for a clean, modern look.
.

* Roboto:

     Used for: Body text and general content to provide readability and clarity.



## Features

The following features have been implemented:

* Fully responsive website consisting of:
* Home (the blog)
* About
* Contact
* Login
* Logout
* Register
* Blog Detail - with CRUD functionality for logged in users to like a post and/or comment on a post (comments can be edited or deleted)

* Blog Admin - with CRUD functionality for logged in superadministrators

### Site Navigation

### Navbar

* Featured at the top of the page, the navigation shows the DietDive the left corner. For smaller devices. 

* The other navigation links are: Home, About, Contact , Register,  and LogiLogout which link to different pages of the site.

* The active page which the user is currently on is underlinedH.

* When the user hovers over a link, the link is in bold.

* The navigation makes clear the name of the company and website.

* The navigation makes the different sections of information easy to find.

* On smaller devices the navigation converts to a burger menu

![](static/images/nav.jpg)
![](static/images/nav-l.jpg)
![](static/images/nav-s.jpg)

### Homepage

* The homepage consists of a large hero image. Here the user is welcomed to the blog and provided a short blub about the site.

* The 'learn about Diet Dive and our mission' button takes the user to the 'About' page.

* below the hero section is all of the blog posts. The posts are displayed in 3 columns, with 6 posts per page.

* Each post is in a bootstrap card, with the post's: dietname, title, author, excerpt, date created and feature image.

* On smaller devices the layout changes to one column per post to maximise usable screen space.

* The next button takes the user to the next 6 blog posts (pagination)

* The user can click on the blog post's title/excerpt/image to take them to that post's post detail page. Here they can view the whole post.

       
![](static/images/home-2.jpg)
![](static/images/home-3.jpg)



### Blog


* Each blog post can be clicked - bringing the user to the blog details page for that post.

* The header section contains the blog title, feature image, author and date the post was created.

* The blog post is rendered to the page for the user to read.

* Below the post is a like button and a comment sections. These features are read-only for non-logged in users. Logged in users can like or comment on the post.

* For non-logged-in users, a login button is provided with a link that directs them to the sign-in/sign-up page, allowing them to comment and like posts once they are authenticated.

* Clicking the heart icon likes the post. Users can click on the heart again to unlike the post.

* The number of likes and comments for that particular blog post is clearly visible.

* Logged in users can write a comment using the comment form and submit it to the DB. It must be approved by an administrator in order to appear on the front end.

* A logged in user can edit or delete their own comment. Editing a comment will resubmit the new comment to the DB for approval.


![](static/images/blog-1.jpg)
![](static/images/blog-2.jpg)
![](static/images/blog-3.jpg)
![](static/images/blog-4.jpg)
![](static/images/blog-5.jpg)
![](static/images/blog-6.jpg)
![](static/images/blog-7.jpg)



### About page 

* The About page is a simple page to inform site users all about DietDive.

* It consists of about content, an image, and the date edited (from the about DB table).

* The contents of the about page can be edited with a UI from the admin area.

![](static/images/about-1.jpg)
![](static/images/about-2.jpg)
![](static/images/about-3.jpg)

### Contact Page

* The Contact page consists of a form a user can use to get in touch with DietDive.

* Front end validation code ensures users must fill out all fields in order to submit the contact form.

* Once the user submits a message, they are shown a confirmation message stating: 'Thank you! Your message has been submitted successfully. We will get back to you shortly.' Below the message, a button is provided to redirect users back to the homepage.



* I also ensured that any required elements removed from the front-end trigger an error message stating, "there was an error . Please try again."

![](static/images/c1.jpg)


![](static/images/c2.jpg)
![](static/images/c3.jpg)




### login, logout, register 


* Users can register for an account by filling out the registration form.

* This form is validated on the front end so that users must submit required 
  information.

* Passwords rules apply:
  - Your password can’t be too similar to your other personal information.
  - Your password must contain at least 8 characters.
  - Your password can’t be a commonly used password.
  - Your password can’t be entirely numeric.
  - The password must be entered twice and the 2 passwords must match.


* Clicking the sign up button will create a new user and the user can then sign in and use the user functionality on the website.

* Users can login from the login page. They must enter the correct username and password.

* User can easily log out by clicking the logout button in the navigation bar.


![](static/images/reg1.jpg)


![](static/images/reg2.jpg)
![](static/images/reg3.jpg)
![](static/images/l1.jpg)
![](static/images/l2.jpg)




### Footer
* The footer is simple with a navigation menu and social links.

![](static/images/footer.jpg)





## Unresolved bugs

* There are no other unresolved bugs that I am aware of.

## Future Features/Improvements

 * User Profile

   - Ability to post blogs.
   - Option to save blogs to a favorites list.
   - Ability to update profile image.

* sign up 

  - Email verification upon registration for security.
  
  - Account verification for added user authentication.



###  Database Design

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.


Below is the database structure:

![](static/images/data-b.jpg)




## Testing 


* I tested that this page works in different browsers: Chrome, Firefox, Safari, Internet Explorer.

* I confirmed that this project is responsive, looks good, and functions on all standard screen sizes using devtools and the device toolbar.

* I confirmed that the navigation header, "About Us," "Sign Up," and "Contact" text are all readable and easy to understand.

* I have confirmed that the form works, requires entries in every field, and will only accept an email in the email field.


## bugs
### Solved bugs 
 
 * When I deployed my project to GitHub Pages, I discovered that it was broken. The links to other files, specifically images, did not work. 
  
 * I discovered that this was because I had used the wrong file paths, even though they were supposed to be relative.
 


## validator Testing
 * HTML
  
  * No errors were returned when passing through the official W3C validator.

* CSS 
  
    - No errors were found when passing through the official (jigsaw) validator.

* Accessibility 
  
      - I confirmed that the colors and fonts chosen are easy to read and accessible by running it through Lighthouse in DevTools
      
![](assets/images/light-house.png)

## Unfixed Bugs

No unfixed bugs were identified.


## Deployment 

* The Site was deployed to GitHub pages. The Steps to deploy are as follows:
  
  - In the GitHub repository. navigate to the setting tab.

  - From the source section drop-down menu, select the Master Branch.

  * Once the master branch has been selected, the page provides the link to the completed website.
  
  The live link can be found here- [ Coding Club ](https://akramalex.github.io/Portfolio1/)


  ## Credits

  ### Content
  
  * The Code to make the social media links was taken from the CI [ Love Runing ](https://akramalex.github.io/LOVE-RUNING/) project.

### Media

* The image in the header was taken from [ Pexels ](https://www.pexels.com/)


