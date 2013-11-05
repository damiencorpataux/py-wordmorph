py-wordmorph
============

A basic python word morphing library.

```script.py``` outputs the first path found between two given words.


### Usage
**Strip the word list in order to obtain a clean wordlist to process (eg. no quotes or caps):**
```
python strip.py -i linuxwords -o words
```

**Morph words:**
```
python script.py --wordlist words --from cast --to hurt
```

You can also pipe data:
```
cat linuxwords | python strip.py | python script.py --wordlist words --from cast --to hurt
```


### More options
```python script.py -h``` and ```python strip.py -h```


### Unittests
Run the unittests:
```
python tests/consistency.py
```
