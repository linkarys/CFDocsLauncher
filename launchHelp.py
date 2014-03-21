import sublime, sublime_plugin, webbrowser

class LaunchCfHelpCommand(sublime_plugin.TextCommand):
    def run(self, edit, forward = True):
        word = ""
        for s in self.view.sel():
            word = self.view.word( s )

        s = sublime.load_settings('CFDocsLauncher.sublime-settings')
        doc_chanel = s.get('doc_chanel', 'https://wikidocs.adobe.com/wiki/display/coldfusionen/')

        webbrowser.open(doc_chanel + self.view.substr(word))


class SearchCfDocsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        word = ""
        for s in self.view.sel():
            word = self.view.word( s )

        s = sublime.load_settings('CFDocsLauncher.sublime-settings')
        search_chanel = s.get('search_chanel', 'http://cfquickdocs.com/#')

        webbrowser.open(search_chanel + self.view.substr(word))