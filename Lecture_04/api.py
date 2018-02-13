import os
import requests
import webbrowser

"""
API stands for Application Programming Interface. Basically, it is a way for two computers to talk to each other via 
software.

A client make a request to a server and the server returns a response.

The simplest example of an API is something you all should be familiar with: a website. Whenever you visit a 
website, your browser makes a GET request (via the HTTP Protocol) to the URL you specify in the address bar.

In addition to the initial GET, most modern websites, especially those with tracking code, make many other API requests
based on information you provide to the site (both voluntarily and involuntarily).

Check out the Network tab in the developer tools of your favorite browser.

More info: https://mlsdev.com/blog/81-a-beginner-s-tutorial-for-understanding-restful-api
"""

""" Here's how you mimic a browser in Python
The client makes a request to a server and the server returns a response to the client.
"""
response = requests.get('http://www.google.com')


# if you'd like to view the html that you got back in the response
# html = response.text
#
# html_filename = 'google.html'
# with open(html_filename, 'w') as outfile:
#     outfile.write(html)
#
# webbrowser.open('file://'+ os.getcwd() + '/' + html_filename)

"""
A lot of modern websites make heavy use of javascript to load the content on individual pages. The get request you make
only returns the html and the javascript as text. The javascript code is not run. Therefore, the data won't be rendered.
You'll notice for some sites what you get using a request like we did above will return different content than you see
in your browser.

There are ways around that.

One of them is to actually drive a browser directly from Python. We'll cover this in depth for the web scraping lecture(s).
"""

from selenium import webdriver

driver = webdriver.Firefox(executable_path='./geckodriver')

driver.get('http://www.nytimes.com')

"""
One of the most popular methodologies for APIs is known as REST, or RE_presentational S_tate T_ransfer.
REST uses 4 HTTP methods as means of communication
- POST --- Create
- GET --- Retrieve
- PUT --- Update
- DELETE --- Delete

more info: https://spring.io/understanding/REST
"""

# Let's send a message to slack using an API
payload = {'username': 'zac_bot',
           'icon_emoji': ':poop:',
           'text': "What's that smell?"
           }

response = requests.post(SLACK_URL, json=payload)
# more info: https://api.slack.com/api_docs_message_builder.php

#more APIs to play with:
'https://www.googleapis.com/books/v1/volumes?q=isbn:0747532699'
'https://maps.googleapis.com/maps/api/geocode/json?address=Oxford%20University,%20uk&sensor=false' # URL encode the address
'https://www.omdbapi.com/?t=star%20wars&y=&plot=short&r=json'

# a lot of other APIs require you to sign up for an API key. I'll leave that to you as an exercise. Read the docs! And as always, Google is your friend.
