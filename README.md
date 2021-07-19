# Automating your WebBrowser with Selenium using Python #

*NOTE: this is a completed version of the activity. An empty and clonable repository can be found [here](https://github.com/igobyDAG/Final_Project_new.git)

Human testing can be and ardous process. How cool could it be if we could create a program that did it for us?
Thankfully, the guys at [Selenium](https://www.selenium.dev) got us covered!

Selenium is a library that can be used to automate processess in a web browser.
There are two main components that we will be using during this project:
### Selenium web driver ###
This is the heart and soul of Selenium.The browser driver -google chrome´s for example- executes commands on the respective browser over HTTP and gets a response of the action back from the browser, which it sends back to the client.

### Selenim IDE ###
Ever done Excel macros? This works on quite the same principle! Selenium IDE allows us to record and playback interactions with the browser. Pretty usefull, huh?

## This Course's Objective ##
In this course we will be automating a webpage using Selenium to test its functionality.
Teamwork using Git flow is advised. Refer to this [very usefull cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/) to use git flow.


## Setting up everything ##
We'll need to install the Selenium library for Python. Make sure you have pipenv installed! if not:
```bash
$ pip install pipenv --dev
```
Lets move to the repository where we will be working. If you don´t have a Git repository created now its the time to do so! Clone this repository into your machine.

Now that we are in our local repository and have pipenv installed we can install Selenium:
```bash
$ pipenv install selenium
```
Also we'll need to install Pytest:
```bash
$ pipenv install pytest
```

Make sure that Selenium, pytest, and pipenv are running correctly by passing into the terminal:
```bash
$ pipenv run python main.py
```

If you can see output with Selenium´s version, we are good to go!
But wait there's more!

By now you should now that there are many different web browsers that respectively do the same things, but their inner workings are pretty different. Selenium can't really guess what browser it'll be using in order to run our code so we have to manually specify which browser to use *and* give it the browser's engine with which Selenium will perform every action.
To do this, well need to [download google chrome's browser](https://chromedriver.chromium.org/downloads). Make sure you are downloading your browser's version driver or else we'll run into trouble!

When the file has been downloaded make sure you place it in this repo. Just make sure to add it to the .gitignore file.

# Our first webpage automation #
First import Selenium into python.<br>
You'll see that there's already a main function called ```main()``` with an instantiation of an object called ```ChromeDriverMac``` and a function called test().<br>You will create the class with its function. Further instructions in the code.

Remember to run the python program the way it was specified in the previous module.


# Using Selenium IDE #
Selenium IDE is actually a plug in for your browser! <br>Remember we are using **google chrome** for this project so you'll need to [install it now](https://www.selenium.dev/selenium-ide/).

Once its installed you're gonna click on the plugin button on the brower and a window will be displayed.

Now we'll have to record a new test in a new project. Read these instruccions before doing anything!<br>
Select the option to Record a New Test and name your project as you wish (there's no need to add an extention).<br>
Next paste the following url into the prompt:
```
http://demo.guru99.com/test/newtours/login.php
```
then click on Start Recording.<br>
Starting **now** every single action that you take will be captured as code, so thread carefully.<br>
But don't worry too much, no mistake is written in stone!<br>
You'll be automatically guided to a vacation site where you'll input *user* and *pass* into the username and password prompts.<br>
Next you'll submit the info and click on plug-in button that's on the top right corner of the screen and then on the stop recording button.

Look at the IDE window now, there is a list of actions that we took. There are clicks and text inputs.<br>
* Do they accurately represent what we did in the webpage?
* Does it follow an intuitive path to get to the required output?

if yes, then good! On to the next thing!

## Downloading and Testing Our Code ##
In the left panel in the Selenium IDE screen you'll see the program we just created. We want that to become Python code. So we'll proceed to click on the options button of the program and<br>*export* -> *Python Pytest* -> *Export*. No further ooptions need tobe selected.<br>
Export into your local github repo.

Let´s take a look at our code!
What seems to be going on?
Is it the same set of instructions that were displayed on Selenium IDE?
Is the program running? lets find out!
Do:
´´´bash
$ pipenv run python {your file name}.py
´´´

If there are any problems related to dependencies or libraries, its time to check them out and solve them before processding any further. If we get an error related to the chromedriver, then we are going in the right direction.
On to the next thing!

### Problem to solve ###
Have you read the displayed error? If not, it´s time to do so. To complete this assignment we'll have to correctly add some code to our program. You should have enough knowledge by now to guess what to change.<br>
Hints:
* Remember the ```main.py``` program, what was a critical element that was needed to launch *google chrome*?
* We are running a pytest file. There's no need to instantiate the class just yet.

Has Pytest detected any errors? has your code passed? Then we can start adding some test cases!

We'll have to use the ```assert``` keyword to verify if we are getting a certain output. You'll use one of the ```find_element``` functions that are already written out.
Hints:
* CSS selectors are a thin check them out!
* Check the ```find_element``` function documentation. How can you select a webpage element? What does the function return?
* When you login successfully, what message is displayed? could that be ussefull?

Lets run our Pytest:
```bash
$ pytest {your test name}.py
```
Can you see the automation?
Is the test passing?
Congratulations, you have used Python to automate a website!