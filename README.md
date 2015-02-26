MyAKAMAITools
=============
Based on https://github.com/akamai-open/api-kickstart I made some scripts for my own use that I
want to share with internet

Currently, this repository has:
* Libraries and clients for python

After cloning, get the needed libraries by doing the following from the examples/python directory:
python tools/setup.py install --user

If you have issues with the setup command, check the following link:
http://stackoverflow.com/questions/4495120/combine-user-with-prefix-error-with-setup-py-install

The easiest way to walk through the needed provisioning and authentication to get your 
credentials is under "provisioning" in the Getting started guide on our site:
https://developer.akamai.com/introduction/index.html

You can get your credentials set up by using the gen_edgerc.py command in the examples/python directory:
python gen_edgerc.py

For examples other than diagnostic_tools you'll want to pass the name of the appropriate section as an
argument, for example this is how you'd set up ccu.py:

python gen_edgerc.py ccu
python userlist.py

Contact original developers khunter@akamai.com, dkazemi@akamai.com or open-developer@akamai.com for help, comments, suggestions.

Tweet your thoughts to original developers @synedra, @tinysubversions or me at @kour2k
