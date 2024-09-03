import subprocess

def install_package(package):
    subprocess.call(['pip', 'install', package])
with open('requirements.txt', 'r') as f:
    for line in f:
        package = line.strip()
        if package:
            install_package(package)