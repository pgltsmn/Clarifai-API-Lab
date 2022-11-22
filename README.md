# Image recognition API lab!
## Lab 1: Basics
### 1. Fork and clone this repository

1. Fork this repository by clicking "Fork" on this page.
2. Copy this repository's URL by clicking the green clone button.
3. Open your terminal, and clone the repo to your computer( replace with the link from step 2):


### 2. Before you code
To complete this lab, it's very important that you understand the example that we covered in the lecture, you should be familiar with the following concepts:
* json.loads
* json.dumps
* requests.post

### 3. The lab
In this lab, we will build a small app where people can submit a URL of an image, and using the Clarifai API, we will return what the image is about and return the results to the user.

* Look at the app.py and home.html. Run the `app.py` server (`python app.py`), go to your browser familiarize yourself with what is already provided for you.
* In app.py you'll need to code below where it says `YOUR CODE HERE!`
* You'll need an API key to authenticate with the Clarifai API, you can obtain it through creating a free account on https://www.clarifai.com/pricing, scrolling down and clicking on "Obtain a free api key" button, and creating an application. (Once the application is created, an API key will be generated automatically) 
* Build the dictionary for the data we want to send, this should be similar to the example we gave in class

If you have any questions ask an Instructor/TA

*BONUS*: Tell the user if the image provided has a human in it! Test that this works for different images that you provide!
*BONUS* *BONUS*: for an image provided, redirect the user to a Wikipedia page that is most relevant to what's in the image
