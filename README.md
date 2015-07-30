# udpchat
Simple UDP connection establishment in Python 2.x


###New addition
<br/>
+ Added basic level reliability:
<br/>
Sender sends both current msg and previous msg to check if previous msg was lost and display the apt msg.
<br/>
- Drawback:
<br/>
Works only for one loss. Could be problematic if same msg sent more than once continuosly.