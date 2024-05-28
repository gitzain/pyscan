import os, sys, pkg_resources, subprocess, urllib.request

def install_vulnerability_scanner():
    installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    if 'safety' not in installed_packages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

def refresh_vulnerability_database():
    insecure_file = 'safety-db/insecure.json'
    insecure_full_file = 'safety-db/insecure_full.json'

    try:
        os.system('mkdir -p safety-db')
        urllib.request.urlretrieve('https://raw.githubusercontent.com/pyupio/safety-db/master/data/insecure.json', insecure_file)
        urllib.request.urlretrieve('https://raw.githubusercontent.com/pyupio/safety-db/master/data/insecure_full.json', insecure_full_file)
    except:
        if not os.path.exists(insecure_file) or not os.path.exists(insecure_full_file):
            sys.exit(1)

def package_name_and_version(filename):
    filename_without_extention = filename.replace('.tar.gz', '').replace('.whl', '')
    return "==".join(filename_without_extention.split("-", 2)[:2])

def scan(directory="."):
    for path, subdirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.whl') or filename.endswith('.tar.gz'):
                if os.system('echo "' + package_name_and_version(filename) + '" | safety check --stdin --db=safety-db --bare'):
                    package_location = os.path.join(path, filename)
                    os.remove(package_location)

if __name__ == "__main__":
    install_vulnerability_scanner()
    refresh_vulnerability_database()
    scan(sys.argv[1])
    sys.exit()