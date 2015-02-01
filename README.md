## Tic Tac Toe

This is a python implementation for the simple game Tic Tac Toe

#### Design

I decided to go with a full stack design mainly so I could leverage the server for caching.  
Since game calculations are so memory intensive, using a server allows me to cache many of the moves
ahead of time.  

#### Backend
For the backend, my original thought was to go with Ruby on Rails as that's what I'm most comfortable in. However, after
some thought, I decided RoR would be overkill - there were several things (asset pipeline, active record, etc) that 
would come with a RoR instance that I would not be needing. So I went with a python microframework called Flask that
I'm quite fond of.  This framework comes with the bare minimum needed to serve up web content. Since I didn't need 
much more, in my opinion this was the optimal choice.

#### Frontend
My goal for the frontend was to make it as dumb as possible.  I offloaded as much computation as I could to the backend. 
All the frontend does is keep track of a structure and pass it to the backend whenever it needs a next move by the 
computer. 

#### Future Enhancements
I tried to make the code as flexible as possible so there are still several enhancements that can be made.  Some of the
interesting enhancements that could be made would be changing the icons for Human/Computer, changing board size, and
varying levels of difficulty from the computer.


#### Running locally
To run locally, there are a few requirements that are needed first:
```
pip install Flask
pip install Flask-Assets
pip install numpy
``` 
(numpy requires python-dev on linux, included on OSX I believe)

Then to run: `python application.py`
