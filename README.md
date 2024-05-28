# PyScan
PyScan quickly and easily scans a folder full of python packages for vulnerabilities.

## Table of content
- [Table of content](#table-of-content)
- [Motivation](#motivation)
- [Installation \& Usage](#installation--usage)
- [Contributing](#contributing)
- [History](#history)
- [Credits](#credits)
- [License](#license)

## Motivation
Needed a way to scan Python packages for vulnerabilities as a part of a CI/CD pipeline.

## Installation & Usage
To run from the commandline:
1. Save the pyscan.py file to a directory of your choice
2. Open and run terminal/powershell to the directory you just saved scanner.py
3. Run `python pyscan.py "/path/to/python/packages"` replace the string at the end with the path to the directory with the python packages. Any packages with vulnerabilities will be deleted and a list of the packages that were deleted will be returned.
Note: You can use `python -m pip download -r requirements.txt -d .` to download some test files.

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History
23/02/21: V1 Initial release

## Credits
- Template for this README is <a href="https://github.com/gitzain/template-README">Template-README</a> created by <a href="https://iamzain.com">Zain Khan</a>
- The actual vulnerability scanner used for this project is <a href="https://github.com/pyupio/safety">Safety</a> created by <a href="https://pyup.io/">pyup</a>

## License
See the LICENSE file in this project's directory.
