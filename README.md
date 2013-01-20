introbot
========

Introbot is a quick python script to write an introductory e-mail between n parties.

To use, edit `settings.py` and swap in your info.

add a person
------------

Add a person with the `-a` switch. A person has a nickname, a firstname, and a description.

For example:

    python intro.py -a hilary "Hilary thinks you should write scripts to do things instead of just doing them."
    
If the nickname that you want to use is the same as their first name, that's it. If you want to use a different nickname, just specify all three in order (nickname, name, and description):

    python intro.py -a mason Hilary "Hilary thinks..."
    
voila!

write an intro
--------------

To create an intro, just give the nicknames of the people you would like to introduce.

    python intro.py hilary pete
    
The script will generate the intro, print it to STDOUT, and, on a Mac, copy it to your clipboard. Paste it into your favorite e-mail client and take a dramatic sip of coffee.

You can also create an intro with a custom message:

    python intro.py hilary pete -m "You both love sculpture, you should definitely find a time to talk."
    
disclaimers
-----------

This is how my brain organizes people and introductions, I have no idea if it'll work for you. I'd love ideas to make this better!
