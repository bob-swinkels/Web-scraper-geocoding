# Web-scaper-geocoding

Script to convert the postal codes in the .json file from the [Web-scaper](https://github.com/bob-swinkels/Web-scraper) project to distance from that postal code to the centre of the city using geocoding using the [arcGIS](http://www.arcgis.com/index.html) service.

## Installation

### Requirements
* Python 3.3 and up
* PyPI

## Usage
You can run the script with the name of the .json file as an argument variable.
```
$ python geocode.py appartment-list.json
```

## Development
Clone the project and move into the project head directory using the ```cd``` command. Then create a virtual environment in the head directory of the project, activate this environment and run ```pip install -r requirements.txt```.
```
$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Thanks to **Paula Wabeke** for her creative input, and effective problem-solving during the creation of this program.

## License
[MIT](LICENSE)
