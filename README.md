# Watery Wordplay Wreck

Welcome to my third milestone project, Watery Wordplay Wreck.

Watery Wordplay Wreck is a word guessing game built with Python. It is a <a href="https://en.wikipedia.org/wiki/Hangman_(game)" target="_blank">Hangman</a> game in the style of a sinking ship to represent the progress of the game.

The user is able to choose the number of lives per game to set the difficulty. Through the process of making guesses, either letter by letter or by attempting to guess the entire word, the user endeavors to identify the correct word before the ship succumbs to the depths of the sea. With each unsuccessful attempt, the user loses a life, leading to the gradual sinking of the ship.

The primary objective of this project is to showcase my comprehension and application of the Python modules I have studied thus far. By integrating them into a real-world project, I aim to demonstrate my proficiency in design and development. This terminal application, constructed using a template provided by <a href="https://github.com/Code-Institute-Org/p3-template" target="_blank">Code Institute</a> along with my Python code, serves as a tangible representation of my acquired skills.

I appreciate you taking the time to explore my project, and I sincerely hope you find as much enjoyment in it as I did during the design and development phases.

<a href="https://hcaldwell95.github.io/salt-and-stone-studios/" target="_blank">View the live project here THIS ISN'T FINISHED</a>

<a href="https://github.com/HCaldwell95/watery-wordplay-wreck" target="_blank">View the GitHub repository here CHANGE TO CORRECT REPOSITORY</a>

## UX - User Experience Design

### User Stories

As a first-time user:
  - I would like to understand how the game works and how to play with ease.
  - I would like to be able to adjust the difficulty to suit my level.
  - I would like instant feedback for each of my guesses while playing the game.
  - I would like to see any letters or words that I have already tried to avoid suggesting them again.
  - I would like to see an error message if my guess is invalid and I would like to be told why.
  - I would like to be able to monitor my progress during the game.
  - I would like to have the option to play the game again or finish my session when the game ends.

As a returning user:
  - I would like to be able to relearn the game quickly and easily.
  - I would like the challenge to remain and encounter different words than my last visit.

## Logic Flow
To organise the logic flow of the game, I created a flow chart that outlines the individual steps. Each step is color-coded to differentiate between various types of activities.

<img src="./docs/flow-chart.png" alt="Image of the project flowchart">
  
## Existing Features

### Welcome Page

This is the welcome page for the game. It presents the game title in the form of ASCII Art. On this page, the game prompts the user to press ENTER to begin the game.

### Rules Page

Once the user has pressed ENTER, they will be taken to the Rules Page. This page consists of:
  -  A 'RULES' Title - again presented in ASCII Art.
  -  The rules of the game and explanation of the goal.
  -  A prompt for the user to select their difficulty by selecting the amount of lives they have.

### Game Screen

After the user has chosen their desired number of lives, the game initiates. A randomly selected nautical-themed word is assigned for each game, and the initial screen consistently displays a visual representation of their remaining lives through a sinking ship image, along with the number of letters in the secret word.

At the bottom of the page, the user is prompted to input either a letter or a word.

# IMAGE IMAGE IMAGE IMAGE

#Show screens of each instance of the game page, demonstrating the sinking ship and attempted letters etc



### End Game Page
Upon completion of the game, the player is directed to the End of Game Screen.

If the word is successfully guessed, the message "Congratulations!" is showcased, incorporating ASCII art to heighten the dramatic effect and extend congratulations to the player.

# IMAGE

If the user fails to guess the word before they run out of lives, the "Game Over" message is displayed along with an ASCII Art image of the ocean and no ship. The correct word is also revealed to the user.

# IMAGE

On this final page, the user is presented with the option to either replay the game or conclude it. Opting to play again returns the user to the Rules Page and prompts them to choose the number of lives for a new game. Selecting to finish the game redirects them to the Welcome Page.


## Python Libraries Used 
### random:
  - The random library was incorporated to allow the application to randomly select a word from words.py for each game instance.
### os:
  - The os library facilitated communication with the operating system to refresh the terminal at various points throughout the game, enhancing the player's experience with a neater and more enjoyable interface.

## Technologies Used
### Programming Language
  - Python was used to build the main content of the game.

### Tools Used To Develop The Game
  - <a href="https://www.gitpod.io/" target="_blank">Gitpod</a> served as the platform for creating, editing and previewing code throughout the development process.
  - <a href="https://git-scm.com/" target="_blank">Git</a> was employed for version control, managing and tracking changes in the codebase.
  - <a href="https://github.com/" target="_blank">GitHub</a> was utilised to store both the repository and the codes.
  - <a href="https://dashboard.heroku.com/apps" target="_blank">Heroku</a> was chosen as the deployment platform for the application.

## Testing

### Code Validation

The application underwent thorough validation to identify and rectify any syntax errors. The <a href="https://pep8ci.herokuapp.com/">CI Python Linter</a> was employed for this validation process, and it successfully confirmed the absence of errors in the code.

<details>
  <summary>Validation Results for run.py</summary>
  <img src="">
</details>

<details>
  <summary>Validation Results for sinking_ship.py</summary>
  <img src="">
</details>

<details>
  <summary>Validation Results for ascii_art.py</summary>
  <img src="">
</details>

<details>
  <summary>Validation Results for words.py</summary>
  <img src="">
</details>

<details>
  <summary>Validation Results for game_over.py</summary>
  <img src="">
</details>

<details>
  <summary>Validation Results for game_winner.py</summary>
  <img src="">
</details>

<details>
  <summary>Validation Results for font_styles.py</summary>
  <img src="">
</details>

## Manual Testing


### Welcome Page
| Step  | Description         | Expected Result                                                            | Actual Result                                    | Pass/Fail   |
| ----- | ------------------- | -------------------------------------------------------------------------- | ------------------------------------------------ | ----------- |
| 1     | Deployed Website    | Welcome Page loads with no issues                                          | Welcome Page loads as expected                   | Pass        |
| 2     | Display Title ASCII | Title loads with ASCII Art                                                 | ASCII Art loads as expected                      | Pass        |
| 3     | Font Styles         | Font styles are displayed correctly                                        | Font styles are displayed as expected            | Pass        |
| 4     | Player Input        | Once the player presses ENTER, the terminal clears and loads the Rules Page| The terminal clears and the Rules Page is loaded | Pass        |

### Rules Page
| Step  | Description         | Expected Result                                                                     | Actual Result                                    | Pass/Fail   |
| ----- | ------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------ | ----------- |
| 1     | Rules Page          | Welcome Page loads with no issues                                                   | Welcome Page loads as expected                   | Pass        |
| 2     | Display Title ASCII | Title loads with ASCII Art                                                          | ASCII Art loads as expected                      | Pass        |
| 3     | Font Styles         | Font styles are displayed correctly                                                 | Font styles are displayed as expected            | Pass        |
| 4     | Player Input        | Only "4", "6" and "8" are accepted                                                  | Input validation works as expected               | Pass        |
| 5     | Player Input        | If the input is not valid, display error message                                    | Error message is displayed as expected           | Pass        |
| 6     | Player Input        | Continues to request an input until a valid input is provided                       | Loops function as expected                       | Pass        |
| 7     | Player Input        | Once a valid input has been entered, the terminal clears and the Game Page is loaded| The terminal clears and the Games Page is loaded | Pass        |

# Image for validation

### Game Page
| Step  | Description         | Expected Result                                                                     | Actual Result                                    | Pass/Fail   |
| ----- | ------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------ | ----------- |
| 1     | Rules Page          | Welcome Page loads with no issues                                                   | Welcome Page loads as expected                   | Pass        |
| 2     | Display Title ASCII | Title loads with ASCII Art                                                          | ASCII Art loads as expected                      | Pass        |
| 3     | Font Styles         | Font styles are displayed correctly                                                 | Font styles are displayed as expected            | Pass        |
| 4     | Player Input        | Only "4", "6" and "8" are accepted                                                  | Input validation works as expected               | Pass        |
| 5     | Player Input        | If the input is not valid, display error message                                    | Error message is displayed as expected           | Pass        |
| 6     | Player Input        | Continues to request an input until a valid input is provided                       | Loops function as expected                       | Pass        |
| 7     | Player Input        | Once a valid input has been entered, the terminal clears and the Game Page is loaded| The terminal clears and the Games Page is loaded | Pass        |


## Deployment

This application has been deployed using Heroku. Link to live project - Watery Wordplay Wreck.

The steps for deploying the application are as follows:

### Preparation:
1. Ensure proper functionality of input methods in the terminal on the deployed website by adding a new line character \n at the end of each text inside the input method. This ensures that the input request will be correctly displayed in the terminal.

2. If there are dependencies required for running the application on Heroku, update the "requirements.txt" file by running the command pip3 freeze > requirements.txt.

3. Push all updates to GitHub.

### Deploying the Application to Heroku:
1. Log into Heroku website.

2. From the Dashboard page, click on "New" and then select "Create new app."

3. Assign a name for the application, choose the region and click "Create app."

4. Once the application is created, go to the "Settings" tab and then "Reveal Config Vars" to set up config vars.

5. In the KEY input field, enter "PORT" in all capitals, and set the VALUE to "8000". Click "Add." If there are other config vars required to run the application, add them here. This application does not require additional config vars.

6. Scroll down to the "Buildpacks" section and click "Add buildpack."

7. Add the necessary buildpacks for the application. For this project, "Python" and "Nodejs" are required.

    It is crucial to maintain the correct order of buildpacks. "Python" should be the first, followed by "Nodejs." Adjust the order by clicking and dragging if needed.

8. Click "Deploy" in the top submenu.
    - Under "Deployment method", select "GitHub" to connect to GitHub.
    - In the "Connect to GitHub" section, enter the repository name and click "Search."
    - Once the repository is located, click "Connect" to link the repository to the Heroku application.

9. Choose either "Enable Automatic Deploys" to deploy a new version automatically whenever changes are pushed to GitHub or select "Manual Deploy." This application has "Automatic Deploys" enabled.

10. After the deployment, scroll to the top of the screen and click "Open app."

    If "Enable Automatic Deploys" is selected, the application will be built and available after the next changes are pushed to GitHub.

### Forking the Github Repository:

You can fork a GitHub Repository to make a copy of the original repository to view or make changes without it affecting the original repository.

1. Find the GitHub repository.
2. At the top of the page to the right, under your account, click the <em>Fork</em> button.
3. You will now have a copy of the repository in your GitHub account.

### Cloning the Repository on GitHub:

1. Find the GitHub Repository.
2. <em>Click</em> the Code button
3. <em>Copy</em> the link shown.
4. In <em>Gitpod</em>, change the directory to the location you would like the cloned directory to be located.
5. <em>Type</em> <code>git clone</code>, and <em>paste</em> the link you copied in step 3.
6. Press <em>Enter</em> to have the local clone created.

## Credits

#### Code

- <a href="https://codeinstitute.net/" target="_blank">Code Institute, Various Tutors</a>
  - Helped me to find solutions to many of my coding issues/queries and allowed me to refer to specific modules for further guidance.

- <a href="https://www.geeksforgeeks.org/clear-screen-python/" target="_blank">GeeksforGeeks</a>
    - Provided the code for clearing the terminal.

- <a href="https://stackoverflow.com" target="_blank">Stack Overflow</a>
    - <a href="https://stackoverflow.com/questions/39378020/how-to-display-table-in-readme-md-file-in-github" target="_blank">(Source)</a> - Provided the code to create tables in the README.md.
    - <a href="https://stackoverflow.com/questions/28607382/is-it-possible-to-create-a-toggle-switch-in-markdown" target="_blank">(Source)</a> Provided the code for adding toggle switches in README.md.

### Media

- <a href="https://patorjk.com/software/taag/#p=testall&f=Slant%20Relief&t=Watery%20Wordplay" target="_blank">Patorjk</a>
    - Provided all of the Ascii Art for the titles throughout the application.