![screenshot of the site on different devices](/assets/images/am-i-responsive.png)
# welcome to MineSweeper! 
## This is an app for those who whant to train thier cognitive ability.
minesweeper is a game for people of all ages, here you can train your cognitive skills or just pass the time, maybe before the next meeting.
### Start Heading.
![screenshot of the navbar](/assets/images/navbar.png)
* The title should make it clear to the user which game he or she is playing, as well as give an aesthetic expression.
* The player has two choices, start the game or choose to read instructions before he or she starts playing.
### Instructions.
![screenshot of two old cottages with grassroof](/assets/images/screenshot-cottage.png)
Instructions give the player a chance to read up on what the game is about and gain an understanding of the rules of the game.

### Minesweeper board.
![Screenshot of some welcome text](/assets/images/welcome.png)<br>
Here we see 6 by 6 symbols and behind some of these symbols there are bombs hiding.

### Inputs X and Y.
![Screenshot of the stone footer with icons to social media and contact information](/assets/images/stone-footer.png)
* The app asks for 2 inputs, one on the x-axis and one on the y-axis.
* if the player has not clicked on a bomb, the game continues and the player gets a point.
* If the player reaches 28 points, the player wins and can then choose whether to restart or end the game.

### Restart.
![Screenshot of a vikingship in a lake](/assets/images/adventure-image.png)
![Screenshot of the text on Event page](/assets/images/adventure-text.png)
If the player clicks on a bomb, the player is given an option to choose to restart or quit the game.

## Error catching.
![A small screenshot of two images in gallery](/assets/images/gallery-example.png)
In order to prevent the game from crashing, a lot of time has been spent on making sure that the player cannot submit values ​​that cause the app to crash, but at the same time reduce user misunderstandings. The last thing we want is for the player not to believe that the game works as it should.

### Error catch 1(Start game/ Instructions).
![Screenshot of the signup page](/assets/images/signup-girl.png)
The app asks for a variable either "1" or "2" the player presses something else a message is displayed explaining what is wrong and letting the player try again.

### Error catch 2 (Input X and Y).
![Screenshot of the thank you text](/assets/images/thank-you.png)<br>
The app asks the player to enter a number between 1-6 on the x-axis and a number between 1-6 on the y-axis. If the player writes, for example, a letter, the player is informed that the game is looking for a number between 1-6.
### Existing features.
* Responsive design
* Signup form and thank you page
### Features left to implement.
I would like to implement IFRAME in the #contact section with a working map.
### Technologies.
* HTML
    * The structure of the Website was developed using HTML as the main language.
* CSS
    * The website was styled using css in a seperate file.
* Git
    * Used to commit and push code during the development of the Website
* Git hub
    * Source code is hosted on GitHub and delpoyed using Git Pages.
* [squoosh](https://squoosh.app/editor)
    * Are used to compress images.
* [pexels](https://www.pexels.com/sv-se/)
    * Was used to download opensource images.
* [Fontawesome](https://fontawesome.com/)
    * Is used to download icons used in the footer.
## Testing.
### Responsivenes.
All pages were tested to ensure responsiveness on screen sizes from 320px and upwards on Chrome and Edge.
### Steps to test:
1. Open browser and navigate to [Viking weekend](/index.html).
2. Open the developer tools (right click and inspect)
3. Set to responsive and decrease width to 320px
4. Set the zoom to 50%
5. Click and drag the responsive window to maximum width
### Expected:
Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.
### Actual:
* Website behaved as expected with the exception of the flex-contact being pushed out to the left when the width is under 353px.
    * This was fixed by setting #flex-contact width:120px and @media #social: removal of flex atributes and letter-spacing
### Website was also opened on the following devices and no responsive issues were seen:
* Samsung S22
* Iphone 13
* Lenovo ideapad S340
## Lighthouse Testing.
![screenshot of index.html lighthouse score](/assets/images/lighthouse-index.png)<br>
![screenshot of events.html lighthouse score](/assets/images/lighthouse-event.png)<br>
![screenshot of gallery.html lighthouse score](/assets/images/lighthouse-gallery.png)<br>
![screenshot of signup.html lighthouse score](/assets/images/lighthouse-signup.png)

Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design. This was done by clicking on the navigation links on each page.
| Navigation | Link Page to Load |
|------------|-------------------|
| HOME       | index.html        |
| EVENTS     | events.html       |
|GALLERY     | gallery.html      |
Links on all pages navigated to the correct pages as exptected.
### Form Testing.
The form on the signup page was tested to ensure it functioned as expected when correct data was input and when incorrect data was input.<br>
Steps to test:
1. Navigate to [Viking weekend signup page.](https://jesdah.github.io/Viking_weekend/signup.html)
2. Scroll down to the form and input the following data:
   - First Name: John
   - Last Name: Doe
   - Email: doe.john@test.com
   - Phonenumber: 123456789
   - age: 8
   - Allergies: none
   - Dates: select a date
   - Anything else you like to add?: This is optional
3. Click Submit
4. User should be redirected to thank-you.html confirmation page.<br>
### Expected:

Form submits with no warnings or errors and user is redirected to index.html confirmation page.

### Actual:

Website behaved as expected with no errors or warnings and redirected to index.html.<br>
If a required field is missing the user will not be able to submit and an error field will be displayed.
### Footer Social Media Icons / Links
Testing was performed on the Font Awesome Social Media icons in the footer to ensure that each one opened in a new tab.

Each item opened a new tab when clicked as expected.

### Validator Testing
- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org)
  ![validator result index.html](/assets/images/validator-index.png)<br>
  ![validator result events.html](/assets/images/validator-events.png)<br>
  ![validator result gallery.html](/assets/images/validator-gallery.png)<br>
  ![validator result signup.html](/assets/images/validator-signup.png)<br>
  ![validator result thank-you.html](/assets/images/validator-thank-you.png)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org)
  ![validator result css](/assets/images/validator-css-vikingweekend.png)
### Unfixed Bugs
No bugs unfixed.
### Deployment.
The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.<br>
```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.<br>
```git push``` - This command was used to push all committed code to the remote repository on github.
### Deployment to Github Pages
- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the menu on left select 'Pages'
  - From the source section drop-down menu, select the Branch: main
  - Click 'Save'
  - A live link will be displayed in a green banner when published successfully. 
The live link can be found here. https://jesdah.github.io/Viking_weekend/
### Clone the Repository Code Locally
Navigate to the GitHub Repository you want to clone to use locally:
- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal
The project will now been cloned on your local machine for use.
### Credit.
* The code for the navbar is taken from the [loverunning project](https://github.com/Code-Institute-Solutions/love-running-2.0-sourcecode/blob/main/07-gallery/02-gallery-images/index.html)
* I learned how to use flex [w3schools](https://www.w3schools.com/css/css3_flexbox_responsive.asp)and at [Flexboxfroggy](https://www.flexboxfroggy.com/)
* I got the code to make the thank-you page redirect to the homepage from gareth_mentor:
```
<meta http-equiv="refresh" content="10; url=index.html">
```
* I have used [w3schools](https://www.w3schools.com/) a lot for inspiration and tips and tricks
* To compress images I have used [squoosh](https://squoosh.app/editor)

* To get a fixed footer I have taken the code from [w3schools](https://www.w3schools.com/howto/howto_css_fixed_footer.asp)

* For symbols in the footer I have used [Fontawesome](https://fontawesome.com/)
* I found the pictures at [pexels](https://www.pexels.com/sv-se/)