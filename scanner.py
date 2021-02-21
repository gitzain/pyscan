import sys, subprocess, pkg_resources, os, urllib.request

def install_prerequisties():
    required = {'safety'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

def update_vulnerability_database():
    os.system('mkdir -p safety-db')
    urllib.request.urlretrieve('https://raw.githubusercontent.com/pyupio/safety-db/master/data/insecure.json', 'safety-db/insecure.json')
    urllib.request.urlretrieve('https://raw.githubusercontent.com/pyupio/safety-db/master/data/insecure_full.json', 'safety-db/insecure_full.json')

def scan(directory="."):
    install_prerequisties()
    update_vulnerability_database()

    bad_packages = []

    for path, subdirs, files in os.walk(directory):
        for name in files:
            if name.endswith('.whl') or name.endswith('.tar.gz'):
                filename = os.path.join(path, name)
                packagename_and_version = "==".join(name.split("-", 2)[:2])

                if os.system('echo "' + packagename_and_version + '" | safety check --stdin --db=safety-db --bare'):
                    os.remove(filename)
                    bad_packages.append(packagename_and_version)

    return bad_packages


if __name__ == "__main__":
    if len(sys.argv) > 1:
        scan(sys.argv[1])
    else:
        scan()