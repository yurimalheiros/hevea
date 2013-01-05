"""
Hevea: compile latex automagically.
"""

import os
import sys
import time
from watchdog.observers import Observer
from handler import ChangeHandler

BASEDIR = os.path.abspath(os.path.dirname(__file__))

def main():
    """
    Main function.
    """

    watched_dir = os.path.join(BASEDIR, sys.argv[1])
    event_handler = ChangeHandler(watched_dir)
    observer = Observer()
    observer.schedule(event_handler, path=sys.argv[1], recursive=True)
    observer.start()

    print "Watching %s" % watched_dir
    print "Ctrl-C to stop."

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    main()