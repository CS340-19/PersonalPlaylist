<h1>Personal Playlist</h1>
Team Name: Personal Playlist<br>
Github Team Name: Personal Playlist<br>
Team Members: Tucker Wheaton, Matthew Butera, Lane Henslee, Chris Mobley<br>
Team Number: 6<br>

<h2>Introduction: </h2> 

<h2>Customer Value:</h2>
<p>Our main goal of this project is to make the process of creating a playlist on Spotify quick with a simple and natural experience. If customers can create playlists that successfully reflect the playlist they wanted in a matter of seconds, we have successfully completed our main goal of this project. Our goal and the value of the application to the customer has not changed since the creation of our proposal at the begginning of the semester.</p>

<h2>Technology:</h2>

Several different technologies were used to develop our playlist creator up to this point. The webpage itself is being created using a combination of html, css, and javascript. In the future we plan to implement angularJS to bind the slider positions to specific values to be used in our python playlist creator.

The current webpage layout (as seen below) will allow users to sign in to their spotify accounts through our webpage, search for songs, and create new playlists based upon the track descriptors they set. Several sliders were added on the left hand side to let users adjust several track descriptors to personalize the generated playlists. In the center of the page we plan to display the album covers of the playlist's tracks along with the trackname. 

<img src="https://github.com/CS340-19/PersonalPlaylist/blob/master/ExampleUI.png">

The backend of our project with be run by the Python library Spotipy. This library lets us to use the Spotify API through Python. It allows us to authenticate Spotify user credentials, access track data, and generate playlists based on track descriptors and similar tracks. This Python algorithm will take the track descriptor values set by the user and generate new playlists.

Currently we have designs for the webpage itself as well as the playlist generator itself. Moving forward our goal is to combine these two so that the Python algorithm will be able to read the sliders to generate playlists based on their values as well as to display the generated playlist on the webpage.

<h2>Team:</h2>
<p> We decided to split up our current work and research into two seperate categories. We did this as we could see a clear divide in our research process. Half of our group researched the Spotify API and used Python to fiddle with some of its features while the other half researched ways to implement a web application. During our first iteration, Tucker Wheaton and Mathew Butera focused on creating the front end design for the web application and plan to continue researching ways to implement a solid back end. Chris Mobely and Lane Henslee focused their attention on creating a Python based algorithm that works with Spotify's API to create a curated list of songs based on a user's Spotify account information.

As we get closer to implementing the backend of our web application, our team plans to work more closely together to integrate our Python algorithm with the internal playlist creation of the web application.
</p> 

<h2>Project Management:</h2>
<p>During our first iteration, we spent most of our time understanding Spotify's API and how to manipulate a user's metadata. Though we planned to finish the entire web application during the semester, we are concerned we will not have enough time to complete the back end of the website and integrate the python algorithm into the web application. Since many of our team members have never created a web application, we did not expect the tremendous learning curve and the amount of time we would need to research and implement our design. We are hopeful that we will have a working web application by the end of the semester but our team is confident our python algorithm will be able to create curated playlists based on the user's metadata.

In the next iteration, our team plans to setup a login system to allow user's to sign into thier Spotify account. We would like for the python algorithm to then allow the user to adjust thier curated playlist based on specific attributes(duration, key, danceability, energy, liveness, etc.) the Spotify API supports.</p>

<h2>Reflection:</h2>
