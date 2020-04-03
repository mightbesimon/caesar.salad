![caesar.salad](https://github.com/mightbesimon/caesar.salad/blob/master/thumbnail.jpg)

# caesar.salad

caesar cipher speed crack, unknown shift condition\
this cipher's a pretty useless encryption and rarely used\
but if you do end up misusing this it's *not my problem*

in my tests of 52 quotes, salad decipherer got 100% accuracy and average 0.040s per cipher text\
but it's pretty bad with pronouns and i'd imagine in real world application it'd be around 90%

### Prerequisites

a dictionary file,\
there's one provided: **'wordlist.txt'**\
works fine with base python, don't need any libraries\
see 'examples.py' to get you started

### Use

in python:
```python
import caesar
print(caesar.salad(ciphertext))
```

that's it! the salad decipherer has got pretty good accuracy, in all my test cases it has always been the first guess\
but **if** for some reason the first guess is not the plain text you are looking for\
you can add additional guesses like so:
```python
caesar.salad(ciphertext, numGuesses)
```

this will make a list of the [1st, 2nd ... nth] most likely plain text

### Automated tests

just run `python3 test.py` in the same folder as *'caesar.py'*

## Authors

- **simon** - *buy my merch* - [mightbesimon](https://github.com/mightbesimon)

Shoutout to julie C (44 BCE), 60 assissins but only 23 stab wounds what a legend

## License

please give me credit, this took me an afternoon

## Acknowledgments

- rip Caesar (44 BCE)
