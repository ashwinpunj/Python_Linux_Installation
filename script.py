import apt 
import pkg_resources

    #Used the apt.Cache class to access all installed packages in a Debian env.
print('Linux packages list and versions: \n')
cache = apt.Cache()    
for debian_package in cache:
    if debian_package.is_installed:
        print(debian_package.name, debian_package.versions)

    #Used the pkg_resources class to get a list of all installed python libraries. 
print('Python library list and versions: \n')
installed_lib = pkg_resources.working_set
for python_library in installed_lib:
    print(python_library.project_name, python_library.version)
    


