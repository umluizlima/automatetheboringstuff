import logging, random

logging.basicConfig( level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)
logging.debug('Start of program')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('Guess taken: (%s)' %(guess))
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug('Toss result: (%s)' %(str(toss)))
assert isinstance(guess, int) and isinstance(toss, int), 'Different data types!'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug('Guess taken: (%s)' %(guess))
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

logging.debug('End of program')
