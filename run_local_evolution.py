import logging
import time

from evolve import main

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.INFO)
    res = 0
    while res == 0:
        res = main()
        time.sleep(0.1)