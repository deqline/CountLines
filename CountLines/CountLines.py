import sublime
import sublime_plugin
import os

class CountLinesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        project_folders = self.get_project_folders()
        line_count = 0

        for folder in project_folders:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    if file.endswith(('.c', '.cpp', '.h', '.hpp','.py','.java','.asm', '.js', '.html', '.css')):
                        filepath = os.path.join(root, file)
                        with open(filepath, 'r', encoding='utf-8') as f:
                            for line in f.readlines():
                                if(len(line.strip()) > 0):
                                    line_count += 1

        sublime.message_dialog("Total code lines in project: {}".format(line_count))

    def get_project_folders(self):
        window = sublime.active_window()
        folders = window.folders() if window else []
        return folders
