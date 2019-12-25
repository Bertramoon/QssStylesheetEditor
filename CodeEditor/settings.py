# -*- coding: utf-8 -*-
""" Language lexers and their file extensions

(Name, extensions) tuples, where <Name> must match QsciLexer<Name>

Copyright (c) 2019 lileilei <hustlei@sina.cn>
"""

import os
from PyQt5.QtCore import Qt, QVariant, QCoreApplication
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (QWidget, QGroupBox, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpinBox, QCheckBox,
                             QComboBox, QColorDialog)
from PyQt5.Qsci import QsciScintilla
from setting_enums import EnumError, SettingEnums
from lang import language_extensions


class EditorSettings():
    """A dialog window for configuring a QsciScintilla editor."""
    settingItems = {
        # Boolean settings
        'tabIndents': {
            'type': 'bool',
            'label': QCoreApplication.translate('EditorSettings', 'Tab indents'),
            'help': QCoreApplication.translate('EditorSettings', 'Use the tab key to indent text'),
        },
        'backspaceUnindents': {
            'type': 'bool',
            'label': QCoreApplication.translate('EditorSettings', 'Backspace unindents'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Backspace will unindent a line instead of just deleting a character'),
        },
        'autoIndent': {
            'type': 'bool',
            'label': QCoreApplication.translate('EditorSettings', 'Auto-indent'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Automatically indent text to match the preceding line'),
        },
        'indentationGuides': {
            'type': 'bool',
            'label': QCoreApplication.translate('EditorSettings', 'Indentation guides'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Display visible guidelines to help keep indentation consistent'),
        },
        'indentationsUseTabs': {
            'type': 'bool',
            'label': QCoreApplication.translate('EditorSettings', 'Use tab character'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Tab key inserts an actual tab character instead of spaces'),
        },
        'eolVisibility': {
            'type': 'bool',
            'label': QCoreApplication.translate('EditorSettings', 'Show CR/LF'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Display a visible icon for carriage return and line feeds'),
        },

        # Color settings
        'color': {
            'type': 'color',
            'label': QCoreApplication.translate('EditorSettings', 'Text color'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Default text color'),
        },
        'paper': {
            'type': 'color',
            'label': QCoreApplication.translate('EditorSettings', 'Paper color'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Default background color'),
        },

        # Numeric settings
        'edgeColumn': {
            'type': 'number',
            'label': QCoreApplication.translate('EditorSettings', 'Text width'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Number of characters per line before wrapping occurs'),
        },
        'tabWidth': {
            'type': 'number',
            'label': QCoreApplication.translate('EditorSettings', 'Tab width'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Width of tabs in characters, or the number of spaces to insert when tab is pressed'),
        },

        # Multiple-selection settings
        'braceMatching': {
            'type': 'combo',
            'valuetype': QsciScintilla.BraceMatch,
            'label': QCoreApplication.translate('EditorSettings', 'Brace Matching'),
            'help': QCoreApplication.translate('EditorSettings',
                                               'Whether and how to highlight matching {} [] () braces'),
        },
        'edgeMode': {
            'type': 'combo',
            'valuetype': QsciScintilla.EdgeMode,
            'label': QCoreApplication.translate('EditorSettings', 'Edge Mode'),
            'help': QCoreApplication.translate('EditorSettings', 'How the edge of the text width is indicated'),
        },
        'eolMode': {
            'type': 'combo',
            'valuetype': QsciScintilla.EolMode,
            'label': QCoreApplication.translate('EditorSettings', 'Line Endings'),
            'help': QCoreApplication.translate('EditorSettings', 'End lines with carriage return and/or line feed'),
        },
        'folding': {
            'type': 'combo',
            'valuetype': QsciScintilla.FoldStyle,
            'label': QCoreApplication.translate('EditorSettings', 'Folding'),
            'help': QCoreApplication.translate('EditorSettings', 'What kind of icons to display for code-folding')
        },
        'whitespaceVisibility': {
            'type': 'combo',
            'valuetype': QsciScintilla.WhitespaceVisibility,
            'label': QCoreApplication.translate('EditorSettings', 'Whitespace'),
            'help': QCoreApplication.translate('EditorSettings', 'Whether whitespace is indicated with visible markers')
        },
        'wrapMode': {
            'type': 'combo',
            'valuetype': QsciScintilla.WrapMode,
            'label': QCoreApplication.translate('EditorSettings', 'Wrap Mode'),
            'help': QCoreApplication.translate('EditorSettings', 'How to wrap text when it reaches the text width')
        },
        'language': {
            'type': 'combo',
            'valuetype': 'language',
            'label': QCoreApplication.translate('EditorSettings', 'Language'),
            'help': QCoreApplication.translate('EditorSettings', 'Syntax highlighting language'),
        },

        # TODO: Need a getter for this
        # 'caretWidth': {
        # 'label': 'Caret width (pixels)',
        # },

        # Stuff the user probably doesn't care about configuring
        # (or do you?)
        # 'annotationDisplay': {
        # 'label': 'Annotation Display',
        # 'type': 'combo',
        # 'values': (
        # ('Hidden', 'AnnotationHidden'),
        # ('Standard', 'AnnotationStandard'),
        # ('Boxed', 'AnnotationBoxed'),
        # ),
        # },
        # 'autoCompletionSource': {
        # 'label': 'Auto Completion Source',
        # 'type': 'combo',
        # 'values': (
        # ('None', 'AcsNone'),
        # ('All', 'AcsAll'),
        # ('Document', 'AcsDocument'),
        # ('APIs', 'AcsAPIs'),
        # ),
        # },
        # 'callTipsStyle': {
        # 'label': 'Call Tips Style',
        # 'type': 'combo',
        # 'values': (
        # ('None', 'CallTipsNone'),
        # ('No Context', 'CallTipsNoContext'),
        # ('No Auto-completion Context', 'CallTipsNoAutoCompletionContext'),
        # ('Context', 'CallTipsContext'),
        # ),
        # },
    }

    # Setting groups
    settingGroups = {
        'Colors': {'label': QCoreApplication.translate('EditorSettings', 'Colors'),
                   'items': {'color', 'paper', }},
        'Indentation': {'label': QCoreApplication.translate('EditorSettings', 'Indentation'),
                        'items': {'tabWidth', 'tabIndents', 'backspaceUnindents', 'autoIndent', 'indentationGuides',
                                  'indentationsUseTabs', }},
        'Wrapping': {'label': QCoreApplication.translate('EditorSettings', 'Wrapping'),
                     'items': {'edgeMode', 'wrapMode', 'edgeColumn', }},
        'Formatting': {'label': QCoreApplication.translate('EditorSettings', 'Formatting'),
                       'items': {'whitespaceVisibility', 'eolMode', 'eolVisibility', }},
        'Coding aids': {'label': QCoreApplication.translate('EditorSettings', 'Coding aids'),
                        'items': {'language', 'folding', 'braceMatching', }},
    }

    # Write-only color settings.
    # FIXME: Can't effectively include these until getters are written.
    _other_color_settings = (
        # Selection
        'selectionForegroundColor',
        'selectionBackgroundColor',
        # Caret (current line)
        'caretForegroundColor',
        'caretLineBackgroundColor',
        # Edge marker
        'edgeColor',
        # Indentation guides
        'indentationGuidesForegroundColor',
        'indentationGuidesBackgroundColor',
        # Brace matching
        'matchedBraceForegroundColor',
        'matchedBraceBackgroundColor',
        'unmatchedBraceForegroundColor',
        'unmatchedBraceBackgroundColor',
        # Marker colors
        'markerForegroundColor',
        'markerBackgroundColor',
        # Margins
        'marginsForegroundColor',
        'marginsBackgroundColor',
        # CallTips
        'callTipsForegroundColor',
        'callTipsBackgroundColor',
        'callTipsHighlightColor',
    )

    def __init__(self, editor=None):
        self.previousSettings = {}  # settings exist
        self.nextSettings = {}  # settings changed to be applied
        # settings in toml format (all enum using name intead)
        self.tomlDictSettings = {}
        # all setting group widgets
        self.groupWidgets = {}
        if editor:
            self.editor = editor
            for item in self.settingItems:
                self.previousSettings[item] = self.editor.getConfig(item)

    def defaultLayout(self):
        """Create and return the main layout for the dialog widget.
        """
        # Indexed group boxes, for easier rearrangement

        self.createWidgets()
        layout = QVBoxLayout()
        for g in self.groupWidgets.values():
            layout.addWidget(g)

        # Layout columns section and OK button vertically

        # OK button at the bottom
        ok = QPushButton('OK')
        # ok.clicked.connect(self.accept)
        layout.addWidget(ok)

        return layout

    def createWidgets(self):
        """Create widgets for setting and save them into self.settingWidgets, each widget is a QGroup"""
        for values in self.settingGroups.values():
            label = values['label']
            names = values['items']
            self.groupWidgets[label] = QGroupBox(label)
            group_layout = QVBoxLayout()
            for name in names:
                group_layout.addLayout(self._create_widget(name))
            self.groupWidgets[label].setLayout(group_layout)
            self.groupWidgets[label].setFlat(False)

    def _create_widget(self, name):
        """Return an appropriate widget for the given configuration setting.
        """
        setting = self.settingItems[name]
        type_ = setting['type']

        # Get the appropriate widget type
        if type_ == 'bool':
            widget = self._create_checkbox(name)
        elif type_ == 'number':
            widget = self._create_number_box(name)
        elif type_ == 'combo':
            widget = self._create_combobox(name)
        elif type_ == 'color':
            widget = self._create_color_picker(name)

        # Label with possible tooltip
        label = QLabel(setting['label'])

        # Add tooltip to widget
        if 'help' in setting:
            widget.setToolTip(setting['help'])

        # Add label and widget
        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addStretch(1)
        hbox.addWidget(widget)

        return hbox

    def _create_checkbox(self, name):
        """Return a ``QCheckBox`` for the given setting."""
        checkbox = QCheckBox()

        def checkbox_changed(state):
            """Event handler for the given setting.
            """
            if state == Qt.Checked:
                self.nextSettings[name] = True
            elif state == Qt.Unchecked:
                self.nextSettings[name] = False

        checkbox.stateChanged[int].connect(checkbox_changed)

        # Set the initial checkbox state based on current getValue
        if self.previousSettings.get(name, True):
            checkbox.setCheckState(Qt.Checked)
        else:
            checkbox.setCheckState(Qt.Unchecked)

        return checkbox

    def _create_combobox(self, name):
        """Return a combobox for modifying a multiple-getValue setting."""
        setting = self.settingItems[name]
        valuetype = setting['valuetype']
        # Create the combobox and populate it
        combo = QComboBox()
        combo.setMinimumWidth(100)
        for value, valueinfo in SettingEnums.enums[valuetype].items():
            data = QVariant(value)
            combo.addItem(valueinfo["display"], data)

        # Set the initial getValue, if any
        current = self.previousSettings.get(name, list(SettingEnums.enums[valuetype].values())[0])
        index = combo.findData(current)
        combo.setCurrentIndex(index)

        # Ugly event handler!
        def combo_changed(index):
            data = combo.itemData(index)
            self.nextSettings[name] = data

        # Connect event handler
        combo.currentIndexChanged[int].connect(combo_changed)

        return combo

    def _create_color_picker(self, name):
        """Return a color-picker widget for a color-based setting."""
        # Button with colored background
        button = QPushButton()
        button.setMinimumWidth(80)
        current_color = self.previousSettings.get(name, Qt.red)
        try:
            current_color = current_color.name()
        except:
            pass

        # Event handler
        def button_pressed():
            color = QColorDialog.getColor(QColor(current_color))
            if color.isValid():
                button.setStyleSheet("background-color: %s" % color.name())
                self.nextSettings[name] = color.name()

        # Connect event handler
        button.pressed.connect(button_pressed)

        # Set default background color
        button.setStyleSheet("background-color: %s" % current_color)

        return button

    def _create_number_box(self, name):
        """Return a numeric entry widget for a numeric setting.
        """
        spinbox = QSpinBox()
        spinbox.setMaximumWidth(120)

        # Set initial getValue
        spinbox.setValue(self.previousSettings.get(name, 5))

        def spinbox_changed(value):
            self.nextSettings[name] = value

        # Connect event handler
        spinbox.valueChanged[int].connect(spinbox_changed)

        return spinbox

    def _create_line_number_checkbox(self):
        """Return a widget for enabling/disabling line numbers."""

        # Line numbers
        def checkbox_changed(state):
            """Event handler for the given setting.
            """
            if state == Qt.Checked:
                self.nextSettings['marginLineNumbers'] = True
            elif state == Qt.Unchecked:
                self.nextSettings['marginLineNumbers'] = False

        # Create the checkbox and connect the event handler
        checkbox = QCheckBox('Line numbers', self)
        checkbox.stateChanged[int].connect(checkbox_changed)

        # Set the initial checkbox state based on current getValue
        if self.previousSettings['marginLineNumbers']:
            checkbox.setCheckState(Qt.Checked)
        else:
            checkbox.setCheckState(Qt.Unchecked)

        return checkbox


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    from editor import Editor

    app = QApplication(sys.argv)
    win = QWidget()
    layout = QHBoxLayout()
    win.setLayout(layout)
    ed = Editor()
    d = QWidget(win)
    d.setLayout(EditorSettings(ed).defaultLayout())
    layout.addWidget(ed)
    layout.addWidget(d)
    win.show()
    sys.exit(app.exec_())
