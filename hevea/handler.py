import os
import subprocess
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    """
    React to changes in .tex files
    """

    def __init__(self, directory):
        self.directory = directory

    def on_any_event(self, event):
        """If any file or folder is changed"""

        if event.is_directory:
            return
        # verifying .swp to work with vim
        if self._get_extension(event.src_path) in ('.tex', '.swp'):  
            self.make()

    def make(self):
        print "Compiling..."

        FNULL = open(os.devnull, 'w')
        os.chdir(os.path.join(self.directory))
        subprocess.call(r'make', stdout=FNULL)

    def _get_extension(self, filepath):
        "Get the file extension."

        return os.path.splitext(filepath)[-1].lower()
