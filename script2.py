
import subprocess
import os

output = subprocess.check_output(["aptitude", "search", "~i", "-F", "%p %V %I"])
lines = output.decode().splitlines()

# Linux packages
linux_packages = {}
for line in lines:
    seg = line.split()
    name = seg[0]
    version = seg[1]
    date = seg[2]
    linux_packages[name] = {"version": version, "date": date}

# Python packages
python_libraries = [name for name in linux_packages if name.startswith("python")]

# Print result
print('Installed Linux Packages: \n')
for name, data in linux_packages.items():
    print(f"{name} version {data['version']} was installed on {data['date']}")
print("\n Installed Python Libraries: \n")
for name in python_libraries:
    print(f"{name} version {linux_packages[name]['version']} was installed on {linux_packages[name]['date']}")
