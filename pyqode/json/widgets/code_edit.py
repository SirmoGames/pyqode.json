import sys
from pyqode.core import api, modes, panels
from pyqode.core.api import Panel
from pyqode.core.backend import server
from pyqode.json import modes as json_modes
from pyqode.json.api import JSONFoldDetector


class JSONCodeEdit(api.CodeEdit):
    mimetypes = ['application/json']

    def __init__(self, parent=None,
                 server_script=server.__file__,
                 interpreter=sys.executable, args=None,
                 create_default_actions=True):
        super(JSONCodeEdit, self).__init__(
            parent, create_default_actions=create_default_actions)

        self.backend.start(server_script, interpreter, args)

        # append panels
        self.panels.append(panels.FoldingPanel())
        self.panels.append(panels.LineNumberPanel())
        self.panels.append(panels.SearchAndReplacePanel(),
                           Panel.Position.BOTTOM)
        self.panels.append(panels.EncodingPanel(),
                           Panel.Position.TOP)

        # append modes
        self.modes.append(modes.AutoCompleteMode())
        self.add_separator()
        self.modes.append(modes.CaseConverterMode())
        self.modes.append(modes.FileWatcherMode())
        self.modes.append(modes.CaretLineHighlighterMode())
        self.sh = self.modes.append(json_modes.JSONSyntaxHighlighter(
            self.document()))
        self.modes.append(modes.ZoomMode())
        self.modes.append(modes.CodeCompletionMode())
        self.modes.append(modes.AutoIndentMode())
        self.modes.append(json_modes.AutoIndentMode())
        self.modes.append(modes.SymbolMatcherMode())
        self.modes.append(modes.OccurrencesHighlighterMode())
        self.modes.append(modes.SmartBackSpaceMode())
        self.modes.append(modes.ExtendedSelectionMode())

        self.syntax_highlighter.fold_detector = JSONFoldDetector()
