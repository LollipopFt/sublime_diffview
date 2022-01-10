import sublime_plugin
import sublime


class DiffViewCommand(sublime_plugin.TextCommand):
    '''diff_view'''
    def run(self, edit):
        '''run diff_view'''
        sel = self.view.sel()
        old_sel = list(sel)
        sel.clear()
        sel.add(sublime.Region(0, self.view.size()))
        self.view.run_command("toggle_inline_diff", {"args": {"prefer_hide": True}})
        sel.clear()
        sel.add_all(old_sel)
