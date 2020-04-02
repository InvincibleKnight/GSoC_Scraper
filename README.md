# GSoC Student Scraper #

This project scrapes a GSoC project archive url and converts this data in a csv file.
this project also filters the students of IIT Kanpur from this scraped data.

## General Instructions

The default webpage to be scraped is the [GSoC-'19 archive](https://summerofcode.withgoogle.com/archive/2019/projects/) if you wish to scrape another Google Summer of Code archive enter the relevant URL when prompted.

The 'student.json' file is used as given.
    
## Install packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install 
requests and bs4 packages

 ```bash
pip install requests
pip install bs4
```

## Usage

First enter the 'scrape' directory.
```bash
cd scrape
```

Then execute the following

```bash
python scrape_data.py
python sanitize_and_combine_data.py
```
