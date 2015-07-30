# udpchat
Simple UDP connection establishment in Python 2.x


###New addition

Added basic level reliability:
Sender send both current msg and previous msg to check if previous msg was lost.
Drawback:
Works only for one loss. Could be problematic if same msg sent more than once continuosly.