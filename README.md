# RS232-Outlet-Control

Small python script meant to be used with Server Technology (legrand) PDUs which support POPS over RS232

Runs on Python 3.5+

Just a general rule of thumb, this code is not commented much and only applied to a specific use case (switching christmas light on and off randomly) a lot of code is specifically timed with 'magic numbers' because POPS over RS232 is difficult when your PDU has a ~3/4 second forced belay between when each outlet can toggle on or off. I tried to make it as fast as feasable for a quick winter project. 

Security was not a concern, so default PDU creds were kept.
