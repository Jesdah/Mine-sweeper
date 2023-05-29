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

### Error catch 3 (Restart).
The player has clicked on a bomb which means the game is over. he or she is asked if you want to continue playing or quit. The player must then enter "y" or "n" if the player writes something else, for example a number or several letters, a warning message will be displayed.
### Existing features.
* left blank
### Features left to implement.
Left blank
### Technologies.
* Python
    * The structure of the app was developed using Python as the main language.
* Git
    * Used to commit and push code during the development of the Website
* Git hub
    * Source code is hosted on GitHub and delpoyed using Git Pages.
# Testing.
## Manual testing.
left blank
### Test cells:
| Test Item          | Method |  Input details | Desired Result                          | Result     | Pass |
| ------------------ | ------ | -------------- | --------------------------------------- | ---------- | ---- |
| Command Line Input | Input  |      x=1 y=1   | The corresponding cell will display a 0 | As desired | Yes  |
| Command Line Input | Input  |      x=2 y=2   | The corresponding cell will display a 0 | As desired | Yes  |
| Command Line Input | Input  |      x=3 y=3   | The corresponding cell will display a 0 | As desired | Yes  |
| Command Line Input | Input  |      x=4 y=4   | The corresponding cell will display a 0 | As desired | Yes  |
| Command Line Input | Input  |      x=5 y=5   | The corresponding cell will display a 0 | As desired | Yes  |
| Command Line Input | Input  |      x=6 y=6   | The corresponding cell will display a 0 | As desired | Yes  |

All cells were checked with no issues.

### Test cells X = symbols, dubble numbers and letters.
| Test Item          | Method |  Input details | Desired Result                          | Result     | Pass |
| ------------------ | ------ | -------------- | --------------------------------------- | ---------- | ---- |
| Command Line Input | Input  |      x=! y=1   | Error message                           | As desired | Yes  |
| Command Line Input | Input  |      x=" y=1   | Error message                           | As desired | Yes  |
| Command Line Input | Input  |      x=# y=1   | Error message                           | As desired | Yes  |
| Command Line Input | Input  |      x=¤ y=1   | Error message                           | As desired | Yes  |
| Command Line Input | Input  |  x=blank y=1   | Error message                           | As desired | Yes  |
| Command Line Input | Input  |     x=11 y=1   | Error message                           | As desired | Yes  |
| Command Line Input | Input  |      x=a y=1   | Error message                           | As desired | Yes  |
| Command Line Input | Input  |      x=[ y=1   | Error message                           | As desired | Yes  |
| Command Line Input | Input  |      x=0 y=1   | Error message                           | As desired | Yes  |
| Command Line Input | Input  |    x="1" y=1   | Error message                           | As desired | Yes  |

All cells were checked with no issues.

### Test cells Y = symbols, dubble numbers and letters.
| Test Item          | Method |  Input details | Desired Result                          | Result     | Pass |
| ------------------ | ------ | -------------- | --------------------------------------- | ---------- | ---- |
| Command Line Input | Input  |      x=1 y=-7  | Error message                        |not as desired | No   |
| Command Line Input | Input  |      x=1 y=!   | Error message                           | As desired | Yes  |
| Command Line Input | Input  |      x=1 y="   | Error message                           | As desired | Yes  |
| Command Line Input | Input  |      x=1 y=#   | Error message                           | As desired | Yes  |
| Command Line Input | Input  |      x=1 y=¤   | Error message                           | As desired | Yes  |
| Command Line Input | Input  |      x=1 y=%   | Error message                           | As desired | Yes  |
| Command Line Input | Input  |   x=1 y=blank  | Error message                           | As desired | Yes  |
| Command Line Input | Input  |      x=1 y=11  | Error message                           | As desired | Yes  |
| Command Line Input | Input  |      x=1 y="1" | Error message                           | As desired | Yes  |
| Command Line Input | Input  |      x=1 y=a   | Error message                           | As desired | Yes  |

when testing the inputs i found that men entering -7 broke the game this was fixed by adding this code on line i56:
```
if 0 <= player_first <= 5 and 0 <= player_second <= 5:
```


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