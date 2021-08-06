# funhouse-weather

A little program that pulls outside weather as well as shows you inside weather. Wakes up when you walk close to it, given it is powered.

## Development

### Structure

There are a couple of helpful scripts added to the project to help copy libraries or deploy the code. The basic structure is below,

- `code.py` - this is the main code that you want to run on the Funhouse.
- `libs` - this is where the adafruit libraries that you want to use are stored.
- `secrets.py` - this file contains any and all secrets that you want your code to ingest including the wifi password if you're connecting to the internet with the Funhouse.

They recommend that you don't use the macOS Finder to copy the files because it creates a trash and stores metadata in some hidden files. This is where the scripts come to help.

### Sripts

As mentioned, there are a couple of helpful scripts (also written in Python) that you can use to help with development. One is called `copy-lib` and the other is called `deploy-code`.

`copy-lib` can be used along with a `libraries.json` file to copy the libraries that you want to use from the large collection of adafruit libraries into either the `./lib` folder in the project or the `lib` folder on the board itself. Run `copy-lib` with the `-h` flag to see the options.

`deploy-code` can be used to deploy the code to the board. It will copy file called `code.py` to `code.py` on the board. This is the convention that CircuitPython uses so it is hardcoded into the script. Additionally, it will overwrite the code that exists on the board.

If you develop out of this project, this won't be a problem for you but if you're deploying this project's code for the first time, it might be worthwhile to backup your code somewhere else before running this script. Optionally, the `deploy-code` script can also copy the libraries to the board with the right flags passed in. Run `deploy-code -h` to see the options.

## References

- [Adafruit Funhouse introduction](https://learn.adafruit.com/adafruit-funhouse)
- [Adafruit Funhouse documentation](https://circuitpython.readthedocs.io/projects/funhouse/en/latest/index.html)
- [Creating with Funhouse](https://learn.adafruit.com/creating-funhouse-projects-with-circuitpython)
