import sublime_plugin
import sublime
import subprocess
import os
from os.path import *

COFFEE_PLUGIN_FOLDER = dirname(realpath(__file__)) + os.sep


class CoffeeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        selection = self.view.sel()[0]
        selection_text = self.view.substr(selection)
        if(selection.empty()):
            selection = sublime.Region(0, self.view.size())
            selection_text = self.view.substr(selection)
        fileBase = "tmp"
        tmpFile = fileBase + ".coffee"
        tmp_file = open(COFFEE_PLUGIN_FOLDER + tmpFile, "w")
        tmp_file.write(selection_text)
        tmp_file.close()

        p = subprocess.Popen(["coffee -c " + tmpFile], cwd=COFFEE_PLUGIN_FOLDER, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        (out, err) = p.communicate()

        outFile = COFFEE_PLUGIN_FOLDER + fileBase + ".js"
        out_file = open(outFile, "r")
        data = out_file.read()
        out_file.close()
        os.remove(outFile)
        os.remove(COFFEE_PLUGIN_FOLDER + tmpFile)

        self.view.replace(edit, selection, data)
