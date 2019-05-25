import sublime
import sublime_plugin
import os

fileName = "conf.py"

class SphinxRefCommand(sublime_plugin.WindowCommand):

    refDict = {}
    refList = []
    displayList = []

    def run(self):
        folders = self.window.folders()
        print(folders)

        self.refDict = {}
        self.refList = []
        self.displayList = []

        self.getRefs(folders[0])
        self.setupRefList()
        self.window.show_quick_panel(self.displayList, self.insertRef)

    def setupRefList(self):
        self.refList = []
        for key in self.refDict:
            self.refList.append(key)
            self.displayList.append(key + " (" + self.refDict[key] + ")")

    def insertRef(self, index):
        if index == -1:
            return
        theView = self.window.active_view()
        theView.run_command("insert", {"characters": ":ref:`" + self.refList[index] + "`"})

    def grep_r (self, pattern, dir, extensions, excludePatterns):

        output = []
        for parent, dnames, fnames in os.walk(dir):
            fnames = [f for f in fnames if not f[0] == '.'] #ignore hidden files
            fnames = [f for f in fnames if f.endswith(extensions)]
            dnames[:] = [d for d in dnames if not d[0] == '.'] #ignore hidden directories
            dnames[:] = [d for d in dnames if d not in excludePatterns]


            for fname in fnames:
                filename = os.path.join(parent, fname)
                if os.path.isfile(filename):
                    try:
                        with open(filename, encoding='utf-8', errors='ignore') as f: 
                            for line in f:
                                if pattern in line:
                                    line = line.strip()
                                    line = filename + ":" + line
                                    output.append(line)
                    except UnicodeDecodeError as e: 
                            next

        return output

    def getRefs(self, dir):

        os.chdir(dir)                

        try: 
            with open(fileName) as f:
                lines = f.readlines()
        except EnvironmentError: 
            lines = []    

        for line in lines:
            if "exclude_patterns" in line:
                line = line.strip() 
                line = line.replace(" ", "")
                line = line.split('=') 
                patterns = line[1].strip("[]")
                patterns = patterns.replace("'","")
                exclude_patterns = patterns.split(',')
                # would prefer to use: exec(line) - doesn't appear to work inside of sublime text

        try:
            exclude_patterns
        except NameError:
            exclude_patterns = []

        # grep all of the references in the project and remove the ones that
        # are in excluded directories
        extensions = ('.rst','.txt','.md')
        pattern = ".. _"
        grepOutput = self.grep_r(pattern, ".", extensions, exclude_patterns)
        #grepOutput = grepOutput.splitlines()
        htmlRefPattern = "://"

        for ref in grepOutput:
            refVals = ref.split(':', 1)   
            if htmlRefPattern not in refVals[1]:
                key = refVals[1]
                key = key.lstrip(".. _")
                key = key.rstrip(":")
                self.refDict[key] = refVals[0]