import os
import subprocess
from string import Template
from watchdog.events import FileSystemEventHandler

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class ChangeHandler(FileSystemEventHandler):
    """
    React to changes in .tex files
    """

    def __init__(self, directory, mainfile):
        self.directory = directory
        self.mainfile = mainfile

    def on_any_event(self, event):
        """If any file or folder is changed"""

        if event.is_directory:
            return
        # verifying .swp to work with vim
        if self._get_extension(event.src_path) in ('.tex', '.swp'):  
            self.make()

    def make(self):
        print "Compiling..."

        if not os.path.exists(os.path.join(self.directory, 'Makefile')):
            makefile = open(os.path.join(BASEDIR, 'Makefile'))
            template = Template(makefile.read())
            makefile.close()

            new_makefile = open(os.path.join(self.directory, 'Makefile'), 'w')
            new_makefile.write(template.substitute(mainfile=self.mainfile, bibtexfile=self.mainfile))
            new_makefile.close()

        FNULL = open(os.devnull, 'w')
        os.chdir(self.directory)
        subprocess.call(r'make', stdout=FNULL)

    def _get_extension(self, filepath):
        "Get the file extension."

        return os.path.splitext(filepath)[-1].lower()
