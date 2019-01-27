Title: Custom Concert
Team Name: Personal Playlist
Github Team Name: Personal Playlist
Team Members: Tucker Wheaton, Mathew Butera, Lane Henslee, Chris Mobley

<h1>Introduction:</h1>

Personal Playlist presents Custom Concert, which is a web-based python algorithm that uses Spotify's API to generate a curated playlist based on your listening history or inputted artists and songs. The website will allow users to adjust the search parameters based on what they're looking for, and the algorithm will learn and improve from user feedback.

<h2>Motivation behind idea?</h2> <br>
Our members in Personal Playlist have come together to eliminate the long process of making playlists. Custom Concert will help people in several aspects. Have you ever been invited to a concert where you don't know many of the songs? We want to help people familiarize themselves with new music based on what they listen too. Custom Concert will help prepare and excite people for concerts to new artists. We are going to add new music to personal playlists while helping new artists grow their group of listeners on spotify. A second feature in Custom Concert is the ability to generate a playlist with advanced settings that match song tags that the Spotify API provides. Lastly, we will allow the user to sort music by these same tags after the playlist is generated. We want to create a nice graphical user interface to let users have more power over their playlists than they ever have. What if you could sort and/or screen your playlist by song popularity or the likelyhood someone will dance to your music?

<h2>What other markets is our product similar too? Do we have a novel ideas?</h2><br>
We have researched the spotify community for similar programs. One that we want to model is called Dubolt. They have a simple interface that allows you to choose up to 5 artists and how many songs you want in the playlist. It generates a playlist with similar tags to your favorite music. We want to implement this feature and allow users to screen music with the Spotify API tags as well. This will curate the user's playlist to have more popular songs or more underground songs, more or less likelyhood to dance to the music, faster or slower tempo, and more. We want users to have full control of their playlists without the effort it takes to manually build a playlist.

<h2>What are these tags we keep talking about?</h2><br>
We will be using Spotify's API to implement these unique features. These tags/features include:
<ul>
  <li>Duration: How long is the song?</li>
  <li>Key: What is the most proficient key/pitch of the song?</li>
  <li>Mode: Is the song in the major scale or the minor scale?</li>
  <li>Time Signature/Meter: How many beats are in each bar or measure?</li>
  <li>Acousticness: A scale from 0 to 1 of how acoustic the song is.</li>
  <li>Danceability: A scale from 0 to 1 of how likely people are to dance to the song.</li>
  <li>Energy: A scale from 0 to 1 of how much noise and speed is in the song (i.e. death metal has more energy than slow country)</li>
  <li>Instrumentalness: A scale from 0 to 1 predicting the ratio of instruments to vocals.</li>
  <li>Liveness: A scale from 0 to 1 predicting the likelyhood that the song was recorded live (.8 or higher means the song was more than likely performed live)</li>
  <li>Speechiness: A scale from 0 to 1 that detects the presence of spoken words.
  <li>Valence: A scale from 0 to 1 that detects the mood of the song (0 is sad/angry and 1 is happy/cheerful)</li>
  <li>Tempo: The overal tempo of the song in BPM.</li>
</ul>
 * You can head over to https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/ for more information on the tags we are using.<br>
<br>
<h1>Customer Value:</h1>

1) Customer Need 

- Primarily, customers of Custom Concert are looking for a quick and simple way to create playlists curated to thier Spotify profile or genre(s) of choice. We would like to create an easy, fast, and intuitive way for Spotify users to create playlists, whether it be by artist, genre, popularity, mood, tempo, and much more.

- Custom Concert aims to remove the frustration of individually adding songs to your playlist inside of the Spotify application. Tediously searching for each song and remembering what song that fits the playlist's vibe is a thing of the past. We want the user experience to be as simple and intuitive as possible. We want the playlist creation process to be simple while also being able to create complex and highly specific playlists.

- Custom Concert compete's with other web applications using Spotify's API such as Rekl.be, Dubolt, Playlist Miner, and Sort Your Music. Rekl.be creates a connection between users by creating a curated playlist based on Spotify likes within a group. People can be added to the group and as a result the playlist evolves. In Custom Concert, we plan to adopt the idea of user interaction by allowing playlists curated based on who is going to listen to them. Dubolt and Playlist Miner, use keywords, genre, and other attributes of the wanted playlist to create a playlist within the Spotify app. We see Dubolt and Playlist Miner as our main competetion in the market and we plan on making a playlist app that can create Spotify playlists in the same manner but more quickly and intuitively using GUI.

2) Proposed Solution

- Custom Consert aims to allow the the user a seemless and intuitive way to create playlists with the use of GUI. We plan on using methods such as sliders to adjust mood, tempo, popularity, and more. We would also like to create a playlist sort function with in the app to allow users to sort the playlist they are creating based on specific attributes. As a result the user should recieve a quality playist based on the attributes the user input and this should all be done a simple and quick manner. 

3) Measures of Success

- Our main goal of this project is to make the process of creating a playlist on Spotify quick with a simple and natural experience. If customers can create playlists that successfully reflect the the playlist they wanted in a matter of seconds we have successfully completed our main goal of this project.


<h1>Technology:</h1>

1) What will our software do?

- You can connect to your Spotify profile through the app. This will allow the user to manipulate their profile and create/edit playlists they own. 

- You can create playlists based on attributes. These attributes will be assigned to each song and will be used to sort and search for songs as well as find connections to other songs through related attributes. Once the songs are found, a playlist will be created reflecting the attributes you have chosen. 

- You can create playlists based on searching artists and the software will find music that the artist made as well as music made by related or similar artists. You can then change the attributes of the whole playlist with in the scope of the artists' genre. 

- You can sort playlists that are being created based on any attributes you would like to be at the top of the playlist. 

2) What are the main components of the system? What will you use to build the system?

- Our experience will be discussed more later in the proposal but I think it is important to highlight that we have never developed a web application so much of this is subject to change during our first sprint. I've written this part in a way to show the options we are considering to implement. 

- We plan on having a client and server component to our application. The client side will be implemented using Javascript and CSS. We plan on using these languages and few API's to create a seemless user experience. It is important for our team to make this process quick and easy. The server side will mainly be written in Python but I can see us possibly using C++ because we are all very familiar with the language. The server side of this app will be used to connect users to their Spotify account and process search results and changes in attribute sliders. The back end will be doing all of the algorithmic processes to create the list of songs as well as implementing the changes with in the user's Spotify profile such as adding a playlist.

- We have looked into using the AngularJS framework developed by Google and we may use this with tools such as Sublime Text and Webstorm. We can then use a mixture Jasmine and Karma for testing the code.

<h1>Team:</h1><br>
<h2>Skills? Has anyone on the team created or used the tools needed for the project already?</h2>
<ul>
  <li>Tucker: C++/Python/Javascript</li>
  <li>Lane: C/C++/Python/Javascript/HTML/CSS</li>
</ul>
<h2>Roles? What are the roles of each team member? Will the roles change over the course of the semester?</h2>
<ul>  
  <li>Lane: Programmer</li>
</ul>
        
<h1>Project Management:</h1> 
<ul>
  <li>Schedule: </li>
  <li>Constraints: </li>
  <li>Resources: </li>
  <li>Descoping: </li>
<ul>


