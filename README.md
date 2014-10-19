Yscreens
========

**Automatic...**

-   Screenshot maker
-   Screenshot and file uploader

**Information**  
Uploads a screenshot of the *primary* display, or a given file to the configured SSH-server,
 and puts the link directly to the clipboard, ready to paste.  
Screenshots are named with a continuous number.  
Notifies with a standard Windows tray pop-up if the upload finished.

-   Taking screenshots with PILL works only on Windows.
-   Whole script is untested on Linux and Mac.
-   Coded with Python 3.3
-   Works also on Python 3.4

To make a screenshot and upload, start the script with a argument
`yscreen.py screen`
To get a prompt for the file to upload
`yscreen.py`

Most of the things are configurable in the *yscreens.ini*.  
Leave *pw* blank in the *yscreens.ini* to use a key-file to authenticate.

If tray pop-up is desired, PyWin32 will be needed as well as *balloons.py*, which I took and modified from [here](http://stackoverflow.com/a/15921588).

*Do whatever you want with this code.*
*Just show me what awesome things you did.*

**Requirements for Windows**
[PyCrypto](http://www.voidspace.org.uk/python/modules.shtml)
[Pillow](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow)
[PyWin32](http://sourceforge.net/projects/pywin32/)
pip install https://pypi.python.org/packages/source/p/pyperclip/pyperclip-1.5.4.zip (or replace with newer version, if any)