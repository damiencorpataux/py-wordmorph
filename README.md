py-wordmorph
============

A basic python word morphing library.

```script.py``` outputs the first shortest path found between two given words.


### Usage

1. Strip the word list in order to obtain a clean wordlist to process (eg. no quotes or caps)<br>
```
cat linuxwords | python strip.py
```
2. Morph words<br>
```
python script.py --from cast --to hurt
```

More options: ```python script.py -h```
