# caesar.salad

caesar cipher speed crack, unknown shift condition\
you're not gonna go around doing any hacking with this, this is a pretty crappy encryption\
but if you do end up misusing this it's *not my problem*

in my tests of 52 famous quotes, salad decipherer got 100% accuracy and average 0.040s per cipher text\
but it's pretty bad with pronouns and i'd imagine in real world application it'd be around 90%

### Prerequisites

all you need is **'caesar.py'** and **'wordlist.txt'**\
you may also want *'examples.py'* to see how to use the salads but it's pretty straight forward\
you can also get *'test.py'* to see a bunch of salad quotes and my 52/52,\
100% accuracy and average 0.040s per cipher text

### Use

in python:
```
import caesar
print(caesar.salad(ciphertext))
```

that's it! the salad decipherer has got pretty good accuracy, in all my test cases it has always been the first guess\
but **if** for some reason the first guess is not the plain text you are looking for\
you can add additional guesses like so:
```
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
