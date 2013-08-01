# parser.py

**parser.py** is Python script for parsing RSS and Atom feeds. Based on [one of IBM developerWorks](http://www.ibm.com/developerworks/xml/library/x-tipufp/).

## Usage

Run:
```bash
$ ./parser.py $feed
```

Replace `$feed` with your wanted feed.

## Notes

* Requires [feedparser](http://code.google.com/p/feedparser/) module.
* Some Atom feeds cannot be parsed (feedparser bug).

## Author

**Zlatan Vasović**
* https://twitter.com/ZXeDroid
* https://github.com/ZDroid
