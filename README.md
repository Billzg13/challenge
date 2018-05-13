# challenge

Coding Challenge using Python

idea: The idea is that this program can predict a name's gender assuming you gave a correct input, and it works like this:
1.you give a name and it starts searching for the name in a Database.
2.if the name doesn't exist in the DB it then makes a GET request at an API that returns the gender, afterwards we save the results
and we save it in our Database for further use.
3.if the name exists in the DB it returns the gender and the process ends there.

the API is https://gender-api.com/ and has a free version with 500 searches, assuming we save the results of each get in time we
won't need the API 


Developed with Pycharm IDE using the Flask framework and it runs on a virtual enviroment

Dependecies:

Flask
requests
json



Documentation:

The Utilities dir has the functions that are responsible for fetching data from the API or the Database

The Templates dir has the html files.
On '/' it will return the index.html. 
On '/send' if its a 'GET' it will return the index.html, if its a 'POST' it will return the gender.html.  
On '/admin' if it's a 'GET' it returns the adminLogin.html, if its a 'POST' it will return the adminTrue.html. 
On '/checkName' if it's a 'GET' it returns the adminTrue.html, if its a 'POST' it will return the adminLogin.html. 

on /admin it will ask for your credentials to log in at the moment they are 
username: "bill" 
password: "123"

if you log in then you can ask for any name
if you can't log in successfully it will take you back at username and password screen


at /send you can ask for any name without logging in 

