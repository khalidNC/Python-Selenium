# Browser Automation:
Browser automation refers to the process of using a script or program to perform tasks in a web browser
as if a human were interacting with it. This involves simulating user actions such as clicking buttons, 
filling out forms, navigating through web pages, and extracting information. It is often employed for 
various purposes, including web scraping, testing web applications, and automating repetitive tasks.

There are several tools and libraries available for browser automation, each with its own strengths 
and use cases. Here is a common method, Selenium used for browser automation:

# Selenium:
Description: Selenium is a widely used open-source framework for browser automation. It supports multiple 
programming languages, including Python, Java, and JavaScript.
Use Cases: Web testing, web scraping, automating repetitive tasks on websites.
Features: It provides a WebDriver API for interacting with web browsers, allowing users to write scripts 
that automate browser actions.

Here is an example:
Let's a we are going to test a funtion of a website, realpython.com so we will automate the signin function
in python and selenium. The sign in fucntion we will automate as below:

      1. Open the website in chrome: realpython.com
      2. Then go to signin page
      3. Then fill out the signin form
      4. Then click on the signin button
      5. It logs in to the website
      6. Then click on the avater
      7. Then click on the Profile
      8. It takes you to the profile page
      9. Then check my prifle name and give an accersion
      10. Then logout and close the browser

Note: Here is only the document but we will do the rel project in a separate directory - browserAutomatonTest

The full steps of the new project as below:

# 1. Create a new project directory:
      a. Open the terminal
      b. Go to users: cd
      c. Make a directory: mkdir browserAutomation
      d. Go the new directory: cd browserAutomaton
      e. Open the directory in vscode: code .

# 2. Create virtual environment and package installation:
      a. Create virtual environment and install selenium in vscode terminal: pipenv install selenium
      b. Drvier, is a piece of software to automate a specfic browser and we need to manually download:
            i. Go to pypi.org
            ii. And search for selenium and go inside to the page
            iii. Scroll down to the page and under driver you will see the tabale of different browsers
            iv. Click on the Chrome driver link
            v. Most recent one is ont top. click on it
            vi. It takes you to the download page
            vii. Then choose the right one for you machine e.g for mac and click on the download link
            viii. It downloads the zip file on your machine
            vix. Now extract the file and you get the executable file
            x. Now we need put this in the path:
                  1. If you are in mac then add this to local bin directory
                  2. Open the terminal and go to the folder that just downloaded: cd chromedriver_mac64
                  3. Run copy chrome driver: cp chromedriver /usr/local/bin

# 3. Select the virtual environment to vscode:
      a. Go back to the vscode and create a py file let's say login.py
      b. Then select the virtual environment that just created 
      c. To active the virtual environment: pipenv shell

# 4. Start codding:
      a. Import webdriver module from selenium:
```python
          Codes:
                  from selenium import webdriver
```
      b. In this module we have classes that represents all the popular browsers, like chrome, safari, 
         firefox and so on. To automate chrome we need to create an instence of chrome class.
```python
          Codes: 
                  from selenium import webdriver

                  # Create an chrome class instance
                  webdriver.Chrome()

                  # And this returns a browser object
                  browser = webdirever.Chrome()
```
      c. Now the browser boject has method called get() to open the browser and it takes web address in
         string as argument.
```python
          Codes:
                  from selenium import webdirever

                  browser = webdirever.Chrome()
                  browser.get("https://realpython.com")
```
         At this point you can save the changes and run the program. You can see this open a new instance of 
         chrome browser and open the realpython site.

      d. Now we need to click on the Sign In button. So we need to tell selenium to click. The way is to find 
         element from html and there are few options. 
            1. Find element by their id, class, name and tag
            2. So right click on the element on the website and inspect to open the pannel
            3. Here in the html tags we cna see classes, id and so on.
            4. we need to see either the classes or id is uniquely indentify
            5. If it is not, then we can find the element by it's text, which is "Sign-In"
            6. So back in the vscode:
            Note: to command find_element_by we need to import By form webdriver
```python
                Codes:
                        from selenium import webdirever
                        from selenium.webdriver.common.by import By

                        browser = webdirever.Chrome()
                        browser.get("https://realpython.com")
                        browser.find_element(By.LINK_TEXT, "Sign-In")
```
            7. Now this returns the web element we can store this in a variable called signin_link. Then click.
```python            
                Codes:
                        from selenium import webdirever
                        from selenium.webdriver.common.by import By

                        browser = webdirever.Chrome()
                        browser.get("https://realpython.com")
                        signin_link = browser.find_element(By.LINK_TEXT, "Sign-In")
                        signin_link.click()
```
         At this point, save the changes and run program and see it open the browser then open the wepage
         then click on the signin button that takes it to the signin page. Next ste is fill out the form.

      e. Same as again find the element on the form by inspecting the element. We see the input tag we see
         id: "id_login" so we use find_element_by_id method and store the elememnt in a variable, let's say 
         user_email then we need to use send_keys() method. It takes string, it is simillar to typing somthing.
```python
          Codes:
                  from selenium import webdirever
                  from selenium.webdriver.common.by import By

                  browser = webdirever.Chrome()
                  browser.get("https://realpython.com")
                  signin_link = browser.find_element(By.LINK_TEXT, "Sign-In")
                  signin_link.click()

                  user_email = browser.find_element(By.ID, "id_login")
                  user_email.send_keys("user_name@gmail.com")
```
      d. In same way we need to write codes for password field.
```python
          Codes:
                  from selenium import webdirever
                  from selenium.webdriver.common.by import By

                  browser = webdirever.Chrome()
                  browser.get("https://realpython.com")
                  signin_link = browser.find_element(By.LINK_TEXT, "Sign-In")
                  signin_link.click()

                  user_email = browser.find_element(By.ID, "id_login")
                  user_email.send_keys("user_name@gmail.com")

                  password = browser.find_element(By.ID, "id_password")
                  password.send_keys("actual_password")
                  password.submit()
```
          Form is filled out now we need to submit that is easy use submit() method. 
          Now save the changes and run the program and you can see up to this:
            - Open browser
            - Open Website
            - Open sign in page
            - Fill out the form
            - Then login in and we are on the homepage.

      e. Now we must not hardcode the user's credential in the source code. We can hide this information
         by applying few ways a couple of them could:

            1. Create a configaration file and keep those info there and put this file in gitignore so keep
               the info out of the source code. Steps are:
                a. Create a configaration file in source directory: config.py
                b. Write the sensitive information in string and store in a varuable. Like: password = "****"
                c. Create .gitignore file in source directory
                d. List the config.py file in the .gitignore file
                e. Now go to the py file where we are writing the script e.g login.py
                e. Then import config at the top of the page
                d. and instead hradcode user_email or password call config as module. e.g config.user_name

            2. We cn use python enviroment variables. The steps are;
                a. Open terminal
                b. Open bash_profile: nano .bash_profile
                c. Add info: 
                            - export user_email = "actual_user_email"
                            - export password = "actual_password"
                d. Save the chnages and exit
                e. source the changes: source .bash_profile
                f. Go to source code in vscode
                e. import os module
                g. This os module has a method called getenv() it takes the string(the vaiable on bash_profile)
         For this project we apply the configaration file approach. 

      f. Now the next step is to go to profile page. So simillarly find the profile element and click;
```python
          Codes:
                  from selenium import webdirever
                  from selenium.webdriver.common.by import By

                  browser = webdirever.Chrome()
                  browser.get("https://realpython.com")
                  signin_link = browser.find_element(By.LINK_TEXT, "Sign-In")
                  signin_link.click()

                  user_email = browser.find_element(By.ID, "id_login")
                  user_email.send_keys("user_name@gmail.com")

                  password = browser.find_element(By.ID, "id_password")
                  password.send_keys("actual_password")
                  password.submit()

                  # Find element of avatar and then click
                  avatar = browser.find_element(By.CLASS_NAME, ".align-self-center.p-0.m-0.dropdown-toggle")
                  avatar.clic()
```
      g. Now the tray opens now we need to click on the Manage account item in the dropdown. We can find the 
         element by text link and then click.
```python
          Codes:
                  from selenium import webdirever
                  from selenium.webdriver.common.by import By

                  browser = webdirever.Chrome()
                  browser.get("https://realpython.com")
                  signin_link = browser.find_element(By.LINK_TEXT, "Sign-In")
                  signin_link.click()

                  user_email = browser.find_element(By.ID, "id_login")
                  user_email.send_keys("user_name@gmail.com")

                  password = browser.find_element(By.ID, "id_password")
                  password.send_keys("actual_password")
                  password.submit()

                  # Find element of avatar and then click
                  avatar = browser.find_element(By.CLASS_NAME, "align-self-center")
                  avatar.click()

                  # Click on the Manage Account item in the dropdown
                  manage_account = browser.find_element(By.TEXT_LINK, "Manage Account")
                  manage_account.click()
```
      h. It takes you to the profile page. Here we will find the text element for the user name and give assertion 
         that this text is rendered in the html content.
```python
          Codes:
                  from selenium import webdirever
                  from selenium.webdriver.common.by import By

                  browser = webdirever.Chrome()
                  browser.get("https://realpython.com")
                  signin_link = browser.find_element(By.LINK_TEX, "Sign-In")
                  signin_link.click()

                  user_email = browser.find_element(By.ID, "id_login")
                  user_email.send_keys("user_name@gmail.com")

                  password = browser.find_element(By.ID, "id_password")
                  password.send_keys("actual_password")
                  password.submit()

                  # Find element of avatar and then click
                  avatar = browser.find_element(By.CLASS_NAME, "align-self-center")
                  avatar.clic()

                  # Click on the Manage Account item in the dropdown
                  manage_account = browser.find_element(By.TEXT_LINK, "Manage Account")
                  manage_account.click()

                  # Get user name element on profile page store in user_name variable
                  user_name = browser.find_element(By.TAG_NAME, "strong")

                  # Now user_name object has a method called get_attribute() that takes string "innerHTML" that returns html of the element
                  user_name_label = user_name.get_attribute("innerHTML")

                  # Assert the text "khalid280284" is in the user_name_label
                  assert "khalid280284" in user_name_label
```
      i. Now logout:
```python
          Codes:
                  avatar.click()
                  logout_button = browser.find_element(By.LINK_TEXT, "Sign Out")
                  logout_button.click()
                  confirm_signout = browser.find_element(By.CLASS_NAME, "btn-danger")
                  confirm_signout.click()

                  # Public page has a alert message that you logged out, get the innerHTML of this element then assert that the message text in rendered in the html
                  alert_msg = browser.find_element(By.CLASS_NAME, "alert-dismissible")
                  alert_msg_label = alert_msg.get_attribute("innerHTML")

                  assert "You have signed out." in alert_msg_label
```
      j. Close the browser: After the function is done we need to close the browser.
```python
          Codes:
                  browser.quit()
```
This is the basic of automation with python selenium.