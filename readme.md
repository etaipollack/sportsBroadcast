Sports Broadcast - Live

This is a small project that I created for a pickup soccer game between me and my friends. It allows the user to setup their home computer as a python server, that recieves post requests from an outside webpage in order to change a scoreboard on a livestream.

USAGE:
1. Run the "server.py" file on your home computer (Ensure that the port used in the file is freed via port forwarding)
2. Host the "index.html" file on a website (find and replace "IP" with your home computer IP)
3.    Note: If your computer is not secured via HTTPS, the index.html file must be run on an HTTP webpage, or else the request will not work. I worked around this by making a subdomain on my website, which was not HTTPS secured unlike my normal website.
4. Create two text files in the folder of server.py, named "team1score.txt" and "team2score.txt" respectively. Add a "0" to the contents of both of these files
5. I used OBS as my livestreaming software. Through OBS, create a two text objecst that recieves data from the two text files that we created (can be done through the objects preferences).
6. Whenever the "increase score" button is pressed on the webpage, it should increase the score shown on OBS
