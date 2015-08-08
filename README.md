# UDP Socket Communication
Simple UDP socket communication establishment in Python2


###Version Details
v3 <br/>
*Plus*: Doesn't anymore work for only one loss. Instead won't allow next request until the previous request receives the response. Definitely better alternative than previous version.
<br/>
*Minus*: Not exactly "time-out and hence resend request". Because doesn't wait for any "particular duration" of user-choice before resending request.
<br/>
<br/>
v2 <br/>
*Plus*: ~~Sender sends both current msg and previous msg to check if previous msg was lost and display the apt msg.~~
<br/>
*Minus*: ~~Works only for one loss. Could be problematic if same msg sent more than once continuosly.~~
<br/>
<br/>
v1 <br/>
Simple send and receive ~~(no reliability).~~