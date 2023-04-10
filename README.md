# Python_Linux_Installation
This is a simple python script meant to list all installed Linux and Python packages in a Debian distribution with their versions. 

I first started off using pip install distribution to write a script that would list al of the python libraries in the linux enviornment, however pip is a command-line tool and while it did have python capabilities, best practices would suggest not using it within a script. I turned towards the pkg_resources class since there was more API functionality in listing the packages and their versions. Similarly, because I was testing on a local debian distribution, I used apt.cache API to list all installed packages and their versions. Due to the time constraint, I was unable to come up with a solution for listing the installation times for each of the packages/libraries. 

After doing some independent research, I looked into the apt API documentation and I was unable to find any attributes pointing to the installation times of the packages. With the pkg_resources tool, I was unable to find any attributes to point towards the installation times for the python libraries that I listed. 

If I had more time, I would consider using the dbkg function to list and parse through the installed packages log manually to gather the installation time. This is definitely not the most ideal/efficient solution but it would have gotten the job done. 

