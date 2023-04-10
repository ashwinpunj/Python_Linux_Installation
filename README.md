# Python_Linux_Installation
This is a simple python script meant to list all installed Linux and Python packages in a Debian distribution with their versions. (script.py)

I first started off using pip install distribution to write a script that would list al of the python libraries in the linux enviornment, however pip is a command-line tool and while it did have python capabilities, best practices would suggest not using it within a script. I turned towards the pkg_resources class since there was more API functionality in listing the packages and their versions. Similarly, because I was testing on a local debian distribution, I used apt.cache API to list all installed packages and their versions. Due to the time constraint, I was unable to come up with a solution for listing the installation times for each of the packages/libraries. 

After doing some independent research, I looked into the apt API documentation and I was unable to find any attributes pointing to the installation times of the packages. With the pkg_resources tool, I was unable to find any attributes to point towards the installation times for the python libraries that I listed. 

If I had more time, I would consider using the dbkg function to list and parse through the installed packages log manually to gather the installation time. This is definitely not the most ideal/efficient solution but it would have gotten the job done. 

*****UPDATE*****

After spending some additional time on this solution, (script2.py) I was able to put together a solution to list all linux packages and python libraries installed on a Debian based linux distribution with their version and installation date. With my first solution (script.py), I was attempting to use the package manager for Debian systems which would be apt to work with the packages installed. Unfortunately, I was unable to find an attribute for the apt_pkg, apt, or pkg_resources class which would allow me to easily call the installation date of the packages. No documentation included the proper attributes, such as the ones for package version and name. (https://apt-team.pages.debian.net/python-apt/library/apt.package.html)

I found an alternate solution through subprocess that leverages aptitude for debian based linux systems. Like I described earlier, I had to manually parse through the output by segmenting the data into lines and then further classifying them in a dictionary. With the data segmented and defined, I was able to filter the data further for packages starting with "python" to indicate all python libraries. From here all that was left was to print the data appropriately. 

