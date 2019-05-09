<h1>Personal Playlist</h1>
Team Name: Personal Playlist<br>
Github Team Name: Personal Playlist<br>
Team Members: Tucker Wheaton, Matthew Butera, Lane Henslee, Chris Mobley<br>
Team Number: 6<br>

<h2>Introduction: </h2> 

<p>Our product is called Personal Playlist, which is a web application that uses Spotify's API to generate a curated playlist based on your listening history or inputted artists and songs. The website will allow users to adjust the search parameters based on what they're looking for, and web app returns with a curated playlist.

While most of our time was spent researching how to implement different features and design options, we made a basic structure of our website, creating a template with the main features to create a curated a playlist. We discovered through testing that we were a bit too ambitious to attempt an original algorithm to generate recommendations from inputted songs, but instead, we will be using the Spotify API's built-in recommend feature to create the curated playlist. Our researching phase of development took much longer than we originally expected, and we didn't accomplish all the project goals we made at the beginning of the semester. Our final product was a basic working version of the original design, but there were many features we still struggled to implement.</p>

<h2>Customer Value:</h2>

<p>Our main goal of this project is to make the process of creating a playlist on Spotify quick with a simple and natural experience. If customers can create playlists that successfully reflect the playlist they wanted in a matter of seconds, we have successfully completed our main goal of this project. Our goal and the value of the application to the customer has not changed since the creation of our proposal at the begginning of the semester.

NO CHANGES</p>

<h2>Technology:</h2>

<p>Several different technologies were used to develop our playlist creator. The webpage itself is being created       using a combination of html, css, and javascript. We hoped to eventually used angularJS to allow the webpage to give live updates to the playlist as the user adjusted the search parameters, but we were unable to get it working by the end of the semester.

The current webpage layout (as seen below) will allow users to sign in to their spotify accounts through our webpage, search for songs, and create new playlists based upon the track descriptors they set. Several sliders were added on the left hand side to let users adjust several track descriptors to personalize the generated playlists. In the center of the webpage we display the album covers of the playlist's tracks along with the trackname. 

<img src="https://github.com/CS340-19/PersonalPlaylist/blob/master/ExampleUI.png">

The backend of our project is run by the Python library Spotipy. This library lets us to use the Spotify API through Python. It allows us to authenticate Spotify user credentials, access track data, and generate playlists based on track descriptors and similar tracks. This Python algorithm takes the track descriptor values set by the user and generates new playlists.

A few features that we were aiming to implement after we created the minimum viable system, such as a search bar and the ability to play songs through the web app, were more difficult than we expected, and we weren't able to accomplish the complete final product we originally hoped for.

Although our product doesn't aim towards a lot of testing, we tried and failed to host the web application through Google's Cloud Platform. We were able to host a basic Docker application, but once we added the database features with caching, a lot of bugs were created because of the mishandling of data.</p>

<h2>Team:</h2>

<p>We decided to split up our work and research into two seperate categories. We did this as we could see a clear divide in our research process. Half of our group researched the Spotify API and used Python to fiddle with some of its features while the other half researched ways to implement a web application. During our first iteration, Tucker Wheaton and Mathew Butera focused on creating the front end design for the web application and plan to continue researching ways to implement a solid back end. Chris Mobely and Lane Henslee focused their attention on creating a python application with Django that works with Spotify's API to create a curated list of songs based on a user's Spotify account information.

The roles for each team member stayed mostly static over the course of the project timeline, but we also helped each other when we reached a bug or had to make decisions about features we were unable to implement. Each team member contributed about the same amount and managment of the project was shared among all the group members.</p> 

<h2>Project Management:</h2>

<p>During our first iteration, we spent most of our time understanding Spotify's API and how to manipulate a user's metadata. Though we planned to finish the entire web application during the semester, we are concerned we will not have enough time to complete the back end of the website and integrate the python algorithm into the web application. Since many of our team members have never created a web application, we did not expect the tremendous learning curve and the amount of time we would need to research and implement our design. We are hopeful that we will have a working web application by the end of the semester but our team is confident our python algorithm will be able to create curated playlists based on the user's metadata.

In the next iteration, we implemented all the main features of the web app to create a basic working product that could generate a basic curated playlist based on an inputted genre and different attribute values. We didn't accomplish all of the goals we originally made in the project proposal, and a lot of features were still left out of the final product. One of the main issues of our group was inexperience, so the research portion of the project took much longer than we expected. Our original idea with a machine learning python algorithm proved to be too difficult for us to make in the time given, so we had to reinvent our project to be based on Spotify API's recommendation feature.</p>

<h2>Reflection:</h2>

<p>Each of the group members was committed to learning about each of their assigned features of the final project, and we were able to distribute the work fairly well. However, our group struggled with time management, as no definitive checkpoints were set beyond the research phase, so it was unclear when each of the features of the website should be finished. Instead of approaching the project with small milestones to ensure each feature is implemented over time, we attempted to complete the final project all at once. 

Our method of splitting the two main parts of the project was very successful, but we never had a designated team leader that ensured we were making our project timeline, leaving the completion of each feature up to the team member that chose to work on it. The original plan we made for this project was very ambitious, and we were not dilligent enough on using GitHub to simplify our issues with project management and keeping up with our project timeline. 

Overall our project was mostly a success because our final product can create a basic curated playlist, and it accomplishes what our design was hoping to do.</p>
