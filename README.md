# R3-SoftwareTask2-AbdullahAdib
# Overview
For this task, what I had to do was implement a client and server connection via tcp connection using sockets. This program is supposed to represent the controls of a rover and the movement of the wheels if they were on differential steering. What the client does is register the input from the keystrokes and then processes all that information before being sent to the server, which then simply outputs the what was sent from client.py. The WASD keys repesent the direction and inputs, and 0 through 5 are the inputs for the speed. The pynput library was used to listen to the keyboard inputs.

![output](https://user-images.githubusercontent.com/91241980/138527145-d43673b4-2b6a-4b66-9ded-7d4647f70a6c.PNG)

# Bugs 
Since I had to work on this during midterm week, I felt as if I wasn't able to give this project my full time and attention. Thus I was more concerned about getting a working version before anything else. These are a few issues that I ran across while testing the program.
- Unable to to run client.py unless server.py is ran first
- Add more hotkeys so that the user can exit and change windows more easily.
- I would like to make the code in client.py to be more efficient by using a different method (i.e arrays, cases, match, isalpha(), isnumeric())
All of these are issues that I would've liked to fix if I had more time.
