import os
import subprocess
from string import Template
from watchdog.events import FileSystemEventHandler

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class ChangeHandler(FileSystemEventHandler):
    """React to changes in .tex files."""

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
        """Call the make command."""

        print "Compiling..."

        self._verify_and_create_makefile()

        os.chdir(self.directory)
        FNULL = open(os.devnull, 'w')
        subprocess.call(r'make', stdout=FNULL)

    def _get_extension(self, filepath):
        """Get the file extension."""

        return os.path.splitext(filepath)[-1].lower()

    def _verify_and_create_makefile(self):
        """Create a Makefile if there is not one in the watched directory"""

        if not os.path.exists(os.path.join(self.directory, 'Makefile')):
            makefile = open(os.path.join(BASEDIR, 'Makefile'))
            template = Template(makefile.read())
            makefile.close()

            new_makefile = open(os.path.join(self.directory, 'Makefile'), 'w')
            new_makefile.write(template.substitute(mainfile=self.mainfile, bibtexfile=self.mainfile))
            new_makefile.close()
