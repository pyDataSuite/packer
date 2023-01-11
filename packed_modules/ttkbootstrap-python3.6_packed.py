# MIT License
# 
# Copyright (c) 2023 pyDataSuite - Joey Meadows
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pathlib import Path
from argparse import ArgumentParser
from typing import Any, List, Dict
import sys

def parse_arguments(args: List[str]) -> Dict[str, Any]:
    "Parses the command-line arguments given to the unpacker tool"

    parser = ArgumentParser(
        prog="ttkbootstrap-python3.6_packed.py",
        description="""
            This file is a plain-text unpacking tool. Execute it
            to generate a folder structure of plain text files identical
            to the structure of the directory that was used to make this.
        """
    )

    parser.add_argument(
        "-o", "--output", type=Path,
        default=None, help="Path to generate the output. Defaults to this filename."
    )

    return parser.parse_args(args).__dict__

args = parse_arguments(sys.argv[1:])
output_root: Path = args["output"]
if output_root is None:
    output_root = Path(__file__).parent/f"{Path(__file__).stem}"

print(f"Unpacking to {output_root}")

dirs = [
    "ttkbootstrap-python3.6",
    "ttkbootstrap-python3.6/ttkcreator",
    "ttkbootstrap-python3.6/ttkbootstrap",
    "ttkbootstrap-python3.6/ttkbootstrap/dialogs",
    "ttkbootstrap-python3.6/ttkbootstrap/localization",
    "ttkbootstrap-python3.6/ttkbootstrap/themes",
    ]

files = { 
    
    "ttkbootstrap-python3.6/README.md": """![](https://img.shields.io/github/release/israel-dryer/ttkbootstrap.svg)
[![Downloads](https://pepy.tech/badge/ttkbootstrap)](https://pepy.tech/project/ttkbootstrap)
[![Downloads](https://pepy.tech/badge/ttkbootstrap/month)](https://pepy.tech/project/ttkbootstrap)
![](https://img.shields.io/github/issues/israel-dryer/ttkbootstrap.svg)
![](https://img.shields.io/github/issues-closed/israel-dryer/ttkbootstrap.svg)
![](https://img.shields.io/github/license/israel-dryer/ttkbootstrap.svg)
![](https://img.shields.io/github/stars/israel-dryer/ttkbootstrap.svg)
![](https://img.shields.io/github/forks/israel-dryer/ttkbootstrap.svg)

# ttkbootstrap
English | [中文](README_zh.md)

A supercharged theme extension for tkinter that enables on-demand modern flat style themes inspired by Bootstrap. 

👀 Check out the [documentation](https://ttkbootstrap.readthedocs.io/en/latest/).


> **1.0+ is a complete rebuild of the library.** If you are using [version 0.5](https://github.com/israel-dryer/ttkbootstrap/tree/version-0.5)
   you may run into issues trying to import themes with the themes.json as this 
   has been removed from 1.0. You can now import and save themes directly using 
   the ttkcreator.

![](https://raw.githubusercontent.com/israel-dryer/ttkbootstrap/master/docs/assets/themes/themes.gif)

## Features

✔️ [**Built-in Themes**](https://ttkbootstrap.readthedocs.io/en/latest/themes/)   
Over a dozen curated dark and light themes.

✔️ [**Pre-defined Styles:**](https://ttkbootstrap.readthedocs.io/en/latest/styleguide/)  
Loads of beautiful pre-defined widget styles such as **outline** and **round toggle** buttons.

✔️ [**Simple keyword API:**](https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/tutorial/#use-themed-widgets)  
Apply colors and types using simple keywords such as **primary** and **striped** instead of the legacy approach of **primary.Striped.Horizontal.TProgressbar**. If you've used Bootstrap for web development, you are already familiar with this approach using css classes.

✔️ [**Lots of new Widgets:**](https://ttkbootstrap.readthedocs.io/en/latest/api/widgets/dateentry/)  
ttkbootstrap comes with several new beautifully designed widgets such as **Meter**, **DateEntry**, and **Floodgauge**. Additionally, **dialogs** are now themed and fully customizable.

✔️ [**Built-in Theme Creator:**](https://ttkbootstrap.readthedocs.io/en/latest/themes/themecreator/)  
Want to create your own theme? Easy! ttkboostrap includes a built-in **theme creator** that enables you to easily build, load, expore, and apply your own custom themes.

## Installation

```python
python -m pip install ttkbootstrap
```

## Simple Usage
Instead of using long, complicated ttk style classes, you can use simple keywords with the \"bootstyle\" parameter.

```python
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename=\"superhero\")

b1 = ttk.Button(root, text=\"Submit\", bootstyle=\"success\")
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text=\"Submit\", bootstyle=\"info-outline\")
b2.pack(side=LEFT, padx=5, pady=10)

root.mainloop()
```

The new keyword API is very flexible. The following examples all produce the same result:
- `bootstyle=\"info-outline\"`
- `bootstyle=\"info outline\"`
- `bootstyle=(\"info\", \"outline\")`
- `bootstyle=(INFO, OUTLINE)`

## Links
- **Documentation:** https://ttkbootstrap.readthedocs.io/en/latest/  
- **GitHub:** https://github.com/israel-dryer/ttkbootstrap
""",
    
    "ttkbootstrap-python3.6/LICENSE": """MIT License

Copyright (c) 2021 Israel Dryer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the \"Software\"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""",
    
    "ttkbootstrap-python3.6/ttkcreator/__init__.py": """""",
    
    "ttkbootstrap-python3.6/ttkcreator/__main__.py": """import shutil
import json
from uuid import uuid4
from pathlib import Path
import ttkbootstrap as ttk
from tkinter import Frame
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfilename
from ttkbootstrap.themes import standard, user
from ttkbootstrap.style import ThemeDefinition
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox


class ThemeCreator(ttk.Window):
    def __init__(self):
        super().__init__(\"TTK Creator\")
        self.configure_frame = ttk.Frame(self, padding=(10, 10, 5, 10))
        self.configure_frame.pack(side=LEFT, fill=BOTH, expand=YES)
        self.demo_frame = ttk.Frame(self, padding=(5, 10, 10, 10))
        self.demo_frame.pack(side=LEFT, fill=BOTH, expand=YES)
        self.setup_theme_creator()
        self.demo_widgets = DemoWidgets(self, self.style)
        self.demo_widgets.pack(fill=BOTH, expand=YES)

    def setup_theme_creator(self):
        # application menu
        self.menu = ttk.Menu()
        self.menu.add_command(label=\"Save\", command=self.save_theme)
        self.menu.add_command(label=\"Reset\", command=self.change_base_theme)
        self.menu.add_command(label=\"Import\", command=self.import_user_themes)
        self.menu.add_command(label=\"Export\", command=self.export_user_themes)
        self.configure(menu=self.menu)

        # theme configuration settings
        # user theme name
        f1 = ttk.Frame(self.configure_frame, padding=(5, 2))
        ttk.Label(f1, text=\"name\", width=12).pack(side=LEFT)
        self.theme_name = ttk.Entry(f1)
        self.theme_name.insert(END, \"new theme\")
        self.theme_name.pack(side=LEFT, fill=X, expand=YES)
        f1.pack(fill=X, expand=YES)

        # base theme
        f2 = ttk.Frame(self.configure_frame, padding=(5, 2))
        ttk.Label(f2, text=\"base theme\", width=12).pack(side=LEFT)
        self.base_theme = ttk.Combobox(f2, values=self.style.theme_names())
        self.base_theme.insert(END, \"litera\")
        self.base_theme.pack(side=LEFT, fill=X, expand=YES)
        f2.pack(fill=X, expand=YES, pady=(0, 15))
        self.base_theme.bind(\"<<ComboboxSelected>>\", self.change_base_theme)

        # color options
        self.color_rows = []
        for color in self.style.colors.label_iter():
            row = ColorRow(self.configure_frame, color, self.style)
            self.color_rows.append(row)
            row.pack(fill=BOTH, expand=YES)
            row.bind(\"<<ColorSelected>>\", self.create_temp_theme)

    def create_temp_theme(self, *_):
        \"\"\"Creates a temp theme using the current configure settings and
        changes the theme in tkinter to that new theme.
        \"\"\"
        themename = \"temp_\" + str(uuid4()).replace(\"-\", \"\")[:10]
        colors = {}
        for row in self.color_rows:
            colors[row.label[\"text\"]] = row.color_value
        definition = ThemeDefinition(themename, colors, self.style.theme.type)
        self.style.register_theme(definition)
        self.style.theme_use(themename)
        self.update_color_patches()

    def change_base_theme(self, *_):
        \"\"\"Sets the initial colors used in the color configuration\"\"\"
        themename = self.base_theme.get()
        self.style.theme_use(themename)
        self.update_color_patches()

    def update_color_patches(self):
        \"\"\"Updates the color patches next to the color code entry.\"\"\"
        for row in self.color_rows:
            row.color_value = self.style.colors.get(row.label[\"text\"])
            row.update_patch_color()

    def export_user_themes(self):
        \"\"\"Export user themes saved in the user.py file\"\"\"
        inpath = Path(user.__file__)
        outpath = asksaveasfilename(
            initialdir=\"/\",
            initialfile=\"user.py\",
            filetypes=[(\"python\", \"*.py\")],
        )
        if outpath:
            shutil.copyfile(inpath, outpath)
            Messagebox.ok(
                parent=self,
                title=\"Export\",
                message=\"User themes have been exported.\",
            )

    def import_user_themes(self):
        \"\"\"Import user themes into the user.py file. Any existing data
        in the user.py file will be overwritten.\"\"\"
        outpath = Path(user.__file__)
        inpath = askopenfilename(
            initialdir=\"/\",
            initialfile=\"user.py\",
            filetypes=[(\"python\", \"*.py\")],
        )
        confirm = Messagebox.okcancel(
            title=\"Import\",
            message=\"This import will overwrite the existing user themes. Ok to import?\",
        )
        if confirm == \"OK\" and inpath:
            shutil.copyfile(inpath, outpath)
            Messagebox.ok(
                parent=self,
                title=\"Export\",
                message=\"User themes have been imported.\",
            )

    def save_theme(self):
        \"\"\"Save the current settings as a new theme. Warn using if
        saving will overwrite existing theme.\"\"\"
        name = self.theme_name.get().lower().replace(\" \", \"\")

        if name in user.USER_THEMES:
            result = Messagebox.okcancel(
                title=\"Save Theme\",
                alert=True,
                message=f\"Overwrite existing theme {name}?\",
            )
            if result == \"Cancel\":
                return

        colors = {}
        for row in self.color_rows:
            colors[row.label[\"text\"]] = row.color_value

        theme = {name: {\"type\": self.style.theme.type, \"colors\": colors}}
        user.USER_THEMES.update(theme)
        standard.STANDARD_THEMES[name] = theme[name]

        # save user themes to file
        formatted = json.dumps(user.USER_THEMES, indent=4)
        out = 'USER_THEMES = ' + formatted
        filepath = user.__file__
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(out)

        definition = ThemeDefinition(name, colors, self.style.theme.type)
        self.style.register_theme(definition)
        self.style.theme_use(name)
        new_themes = []
        for themename in self.style.theme_names():
            if not themename.startswith(\"temp\"):
                new_themes.append(themename)
        self.base_theme.configure(values=new_themes)
        Messagebox.ok(f\"The theme {name} has been created\", \"Save theme\")


class ColorRow(ttk.Frame):
    def __init__(self, master, color, style):
        super().__init__(master, padding=(5, 2))
        self.colorname = color
        self.style = style

        self.label = ttk.Label(self, text=color, width=12)
        self.label.pack(side=LEFT)
        self.patch = Frame(
            master=self, background=self.style.colors.get(color), width=15
        )
        self.patch.pack(side=LEFT, fill=BOTH, padx=2)
        self.entry = ttk.Entry(self, width=12)
        self.entry.pack(side=LEFT, fill=X, expand=YES)
        self.entry.bind(\"<FocusOut>\", self.enter_color)
        self.color_picker = ttk.Button(
            master=self,
            text=\"...\",
            bootstyle=SECONDARY,
            command=self.pick_color,
        )
        self.color_picker.pack(side=LEFT, padx=2)

        # set initial color value and patch color
        self.color_value = self.style.colors.get(color)
        self.update_patch_color()

    def pick_color(self):
        \"\"\"Callback for when a color is selected from the color chooser\"\"\"
        color = askcolor(color=self.color_value)
        if color[1]:
            self.color_value = color[1]
            self.update_patch_color()
        self.event_generate(\"<<ColorSelected>>\")

    def enter_color(self, *_):
        \"\"\"Callback for when a color is typed into the entry\"\"\"
        try:
            self.color_value = self.entry.get().lower()
            self.update_patch_color()
        except:
            self.color_value = self.style.colors.get(self.label[\"text\"])
            self.update_patch_color()
        self.event_generate(\"<<ColorSelected>>\")

    def update_patch_color(self):
        \"\"\"Update the color patch frame with the color value stored in
        the entry widget.\"\"\"
        self.entry.delete(0, END)
        self.entry.insert(END, self.color_value)
        self.patch.configure(background=self.color_value)


class DemoWidgets(ttk.Frame):
    \"\"\"Builds a frame containing an example of most ttkbootstrap widgets
    with various styles and states applied.
    \"\"\"

    ZEN = \"\"\"Beautiful is better than ugly. 
    Explicit is better than implicit. 
    Simple is better than complex. 
    Complex is better than complicated.
    Flat is better than nested. 
    Sparse is better than dense.  
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!\"\"\"

    def __init__(self, master, style):
        super().__init__(master)

        self.style: ttk.Style = style
        self.create_left_frame()
        self.create_right_frame()

    def create_right_frame(self):
        container = ttk.Frame(self)
        container.pack(side=RIGHT, fill=BOTH, expand=YES, padx=5)

        # demonstrates various button styles
        btn_group = ttk.Labelframe(
            master=container, text=\"Buttons\", padding=(10, 5)
        )
        btn_group.pack(fill=X)

        menu = ttk.Menu(self)
        for i, t in enumerate(self.style.theme_names()):
            menu.add_radiobutton(label=t, value=i)

        default = ttk.Button(master=btn_group, text=\"solid button\")
        default.pack(fill=X, pady=5)
        default.focus_set()

        mb = ttk.Menubutton(
            master=btn_group,
            text=\"solid menubutton\",
            bootstyle=SECONDARY,
            menu=menu,
        )
        mb.pack(fill=X, pady=5)

        cb = ttk.Checkbutton(
            master=btn_group,
            text=\"solid toolbutton\",
            bootstyle=(SUCCESS, TOOLBUTTON),
        )
        cb.invoke()
        cb.pack(fill=X, pady=5)

        ob = ttk.Button(
            master=btn_group, text=\"outline button\", bootstyle=(INFO, OUTLINE)
        )
        ob.pack(fill=X, pady=5)

        mb = ttk.Menubutton(
            master=btn_group,
            text=\"outline menubutton\",
            bootstyle=(WARNING, OUTLINE),
            menu=menu,
        )
        mb.pack(fill=X, pady=5)

        cb = ttk.Checkbutton(
            master=btn_group,
            text=\"outline toolbutton\",
            bootstyle=\"success-outline-toolbutton\",
        )
        cb.pack(fill=X, pady=5)

        lb = ttk.Button(master=btn_group, text=\"link button\", bootstyle=LINK)
        lb.pack(fill=X, pady=5)

        cb1 = ttk.Checkbutton(
            master=btn_group,
            text=\"rounded toggle\",
            bootstyle=(SUCCESS, ROUND, TOGGLE),
        )
        cb1.invoke()
        cb1.pack(fill=X, pady=5)

        cb2 = ttk.Checkbutton(
            master=btn_group, text=\"squared toggle\", bootstyle=(SQUARE, TOGGLE)
        )
        cb2.pack(fill=X, pady=5)
        cb2.invoke()

        input_group = ttk.Labelframe(
            master=container, text=\"Other input widgets\", padding=10
        )
        input_group.pack(fill=BOTH, pady=(10, 5), expand=YES)
        entry = ttk.Entry(input_group)
        entry.pack(fill=X)
        entry.insert(END, \"entry widget\")

        password = ttk.Entry(master=input_group, show=\"•\")
        password.pack(fill=X, pady=5)
        password.insert(END, \"password\")

        # spinbox = ttk.Spinbox(master=input_group, from_=0, to=100)
        # spinbox.pack(fill=X)
        # spinbox.set(45)

        cbo = ttk.Combobox(
            master=input_group,
            text=self.style.theme.name,
            values=self.style.theme_names(),
        )
        cbo.pack(fill=X, pady=5)
        cbo.current(self.style.theme_names().index(self.style.theme.name))

        de = ttk.DateEntry(input_group)
        de.pack(fill=X)

    def create_left_frame(self):
        \"\"\"Create all the left frame widgets\"\"\"
        container = ttk.Frame(self)
        container.pack(side=LEFT, fill=BOTH, expand=YES, padx=5)

        # demonstrates all color options inside a label
        color_group = ttk.Labelframe(
            master=container, text=\"Theme color options\", padding=10
        )
        color_group.pack(fill=X, side=TOP)
        for color in self.style.colors:
            cb = ttk.Button(color_group, text=color, bootstyle=color)
            cb.pack(side=LEFT, expand=YES, padx=5, fill=X)

        # demonstrates all radiobutton widgets active and disabled
        cr_group = ttk.Labelframe(
            master=container, text=\"Checkbuttons & radiobuttons\", padding=10
        )
        cr_group.pack(fill=X, pady=10, side=TOP)
        cr1 = ttk.Checkbutton(cr_group, text=\"selected\")
        cr1.pack(side=LEFT, expand=YES, padx=5)
        cr1.invoke()
        cr2 = ttk.Checkbutton(cr_group, text=\"deselected\")
        cr2.pack(side=LEFT, expand=YES, padx=5)
        cr3 = ttk.Checkbutton(cr_group, text=\"disabled\", state=DISABLED)
        cr3.pack(side=LEFT, expand=YES, padx=5)
        cr4 = ttk.Radiobutton(cr_group, text=\"selected\", value=1)
        cr4.pack(side=LEFT, expand=YES, padx=5)
        cr4.invoke()
        cr5 = ttk.Radiobutton(cr_group, text=\"deselected\", value=2)
        cr5.pack(side=LEFT, expand=YES, padx=5)
        cr6 = ttk.Radiobutton(
            cr_group, text=\"disabled\", value=3, state=DISABLED
        )
        cr6.pack(side=LEFT, expand=YES, padx=5)

        # demonstrates the treeview and notebook widgets
        ttframe = ttk.Frame(container)
        ttframe.pack(pady=5, fill=X, side=TOP)
        table_data = [
            (\"South Island, New Zealand\", 1),
            (\"Paris\", 2),
            (\"Bora Bora\", 3),
            (\"Maui\", 4),
            (\"Tahiti\", 5),
        ]
        tv = ttk.Treeview(
            master=ttframe, columns=[0, 1], show=\"headings\", height=5
        )
        for row in table_data:
            tv.insert(\"\", END, values=row)
        tv.selection_set(\"I001\")
        tv.heading(0, text=\"City\")
        tv.heading(1, text=\"Rank\")
        tv.column(0, width=300)
        tv.column(1, width=70, anchor=CENTER)
        tv.pack(side=LEFT, anchor=NE, fill=X)

        nb = ttk.Notebook(ttframe)
        nb.pack(side=LEFT, padx=(10, 0), expand=YES, fill=BOTH)
        nb_text = (
            \"This is a notebook tab.\\nYou can put any widget you want here.\"
        )
        nb.add(ttk.Label(nb, text=nb_text), text=\"Tab 1\", sticky=NW)
        nb.add(
            child=ttk.Label(nb, text=\"A notebook tab.\"),
            text=\"Tab 2\",
            sticky=NW,
        )
        nb.add(ttk.Frame(nb), text=\"Tab 3\")
        nb.add(ttk.Frame(nb), text=\"Tab 4\")
        nb.add(ttk.Frame(nb), text=\"Tab 5\")

        # text widget
        txt = ttk.Text(master=container, height=5, width=50, wrap=\"none\")
        txt.insert(END, DemoWidgets.ZEN)
        txt.pack(side=LEFT, anchor=NW, pady=5, fill=BOTH, expand=YES)

        # demonstrates scale, progressbar, and meter, and scrollbar widgets
        lframe_inner = ttk.Frame(container)
        lframe_inner.pack(fill=BOTH, expand=YES, padx=10)
        scale = ttk.Scale(
            master=lframe_inner, orient=HORIZONTAL, value=75, from_=100, to=0
        )
        scale.pack(fill=X, pady=5, expand=YES)

        ttk.Progressbar(
            master=lframe_inner,
            orient=HORIZONTAL,
            value=50,
        ).pack(fill=X, pady=5, expand=YES)

        ttk.Progressbar(
            master=lframe_inner,
            orient=HORIZONTAL,
            value=75,
            bootstyle=\"success-striped\",
        ).pack(fill=X, pady=5, expand=YES)

        m = ttk.Meter(
            master=lframe_inner,
            metersize=150,
            amountused=45,
            subtext=\"meter widget\",
            bootstyle=\"info\",
            interactive=True,
        )
        m.pack(pady=10)

        sb = ttk.Scrollbar(
            master=lframe_inner,
            orient=HORIZONTAL,
        )
        sb.set(0.1, 0.9)
        sb.pack(fill=X, pady=5, expand=YES)

        sb = ttk.Scrollbar(
            master=lframe_inner, orient=HORIZONTAL, bootstyle=\"danger-round\"
        )
        sb.set(0.1, 0.9)
        sb.pack(fill=X, pady=5, expand=YES)


if __name__ == \"__main__\":

    creator = ThemeCreator()
    creator.mainloop()
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/toast.py": """from tkinter import font
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import utility

# https://www.fontspace.com/freeserif-font-f13277

DEFAULT_ICON_WIN32 = \"\\ue154\"
DEFAULT_ICON = \"\\u25f0\"


class ToastNotification:
    \"\"\"A semi-transparent popup window for temporary alerts or messages.
    You may choose to display the toast for a specified period of time,
    otherwise you must click the toast to close it.

    ![toast notification](../assets/toast/toast.png)

    Examples:

        ```python
        import ttkbootstrap as ttk
        from ttkbootstrap.toast import ToastNotification

        app = ttk.Window()

        toast = ToastNotification(
            title=\"ttkbootstrap toast message\",
            message=\"This is a toast message\",
            duration=3000,
        )
        toast.show_toast()

        app.mainloop()
        ```
    \"\"\"

    def __init__(
        self,
        title,
        message,
        duration=None,
        bootstyle=LIGHT,
        alert=False,
        icon=None,
        iconfont=None,
        position=None,
        **kwargs,
    ):
        \"\"\"
        Parameters:

            title (str):
                The toast title.

            message (str):
                The toast message.

            duration (int):
                The number of milliseconds to show the toast. If None
                (default), then you must click the toast to close it.

            bootstyle (str):
                Style keywords used to updated the label style. One of
                the accepted color keywords.

            alert (bool):
                Indicates whether to ring the display bell when the
                toast is shown.

            icon (str):
                A unicode character to display on the top-left hand
                corner of the toast. The default symbol is OS specific.
                Pass an empty string to remove the symbol.

            iconfont (Union[str, Font]):
                The font used to render the icon. By default, this is
                OS specific. You may need to change the font to enable
                better character or emoji support for the icon you
                want to use. Windows (Segoe UI Symbol),
                Linux (FreeSerif), MacOS (Apple Symbol)

            position (Tuple[int, int, str]):
                A tuple that controls the position of the toast. Default
                is OS specific. The tuple cooresponds to
                (horizontal, vertical, anchor), where the horizontal and
                vertical elements represent the position of the toplevel
                releative to the anchor, which is \"ne\" or top-left by
                default. Acceptable anchors include: n, e, s, w, nw, ne,
                sw, se. For example: (100, 100, 'ne').

            **kwargs (Dict):
                Other keyword arguments passed to the `Toplevel` window.
        \"\"\"
        self.message = message
        self.title = title
        self.duration = duration
        self.bootstyle = bootstyle
        self.icon = icon
        self.iconfont = iconfont
        self.iconfont = None
        self.titlefont = None
        self.toplevel = None
        self.kwargs = kwargs
        self.alert = alert
        self.position = position

        if \"overrideredirect\" not in self.kwargs:
            self.kwargs[\"overrideredirect\"] = True
        if \"alpha\" not in self.kwargs:
            self.kwargs[\"alpha\"] = 0.95

        if position is not None:
            if len(position) != 3:
                self.position = None

    def show_toast(self, *_):
        \"\"\"Create and show the toast window.\"\"\"

        # build toast
        self.toplevel = ttk.Toplevel(**self.kwargs)
        self._setup(self.toplevel)

        self.container = ttk.Frame(self.toplevel, bootstyle=self.bootstyle)
        self.container.pack(fill=BOTH, expand=YES)
        ttk.Label(
            self.container,
            text=self.icon,
            font=self.iconfont,
            bootstyle=f\"{self.bootstyle}-inverse\",
            anchor=NW,
        ).grid(row=0, column=0, rowspan=2, sticky=NSEW, padx=(5, 0))
        ttk.Label(
            self.container,
            text=self.title,
            font=self.titlefont,
            bootstyle=f\"{self.bootstyle}-inverse\",
            anchor=NW,
        ).grid(row=0, column=1, sticky=NSEW, padx=10, pady=(5, 0))
        ttk.Label(
            self.container,
            text=self.message,
            wraplength=utility.scale_size(self.toplevel, 300),
            bootstyle=f\"{self.bootstyle}-inverse\",
            anchor=NW,
        ).grid(row=1, column=1, sticky=NSEW, padx=10, pady=(0, 5))

        self.toplevel.bind(\"<ButtonPress>\", self.hide_toast)

        # alert toast
        if self.alert:
            self.toplevel.bell()

        # specified duration to close
        if self.duration:
            self.toplevel.after(self.duration, self.hide_toast)

    def hide_toast(self, *_):
        \"\"\"Destroy and close the toast window.\"\"\"
        try:
            alpha = float(self.toplevel.attributes(\"-alpha\"))
            if alpha <= 0.1:
                self.toplevel.destroy()
            else:
                self.toplevel.attributes(\"-alpha\", alpha - 0.1)
                self.toplevel.after(25, self.hide_toast)
        except:
            if self.toplevel:
                self.toplevel.destroy()

    def _setup(self, window: ttk.Toplevel):
        winsys = window.tk.call(\"tk\", \"windowingsystem\")

        self.toplevel.configure(relief=RAISED)

        # minsize
        if \"minsize\" not in self.kwargs:
            w, h = utility.scale_size(self.toplevel, [300, 75])
            self.toplevel.minsize(w, h)

        # heading font
        _font = font.nametofont(\"TkDefaultFont\")
        self.titlefont = font.Font(
            family=_font[\"family\"],
            size=_font[\"size\"] + 1,
            weight=\"bold\",
        )
        # symbol font
        self.iconfont = font.Font(size=30, weight=\"bold\")
        if winsys == \"win32\":
            self.iconfont[\"family\"] = \"Segoe UI Symbol\"
            self.icon = DEFAULT_ICON_WIN32 if self.icon is None else self.icon
            if self.position is None:
                x, y = utility.scale_size(self.toplevel, [5, 50])
                self.position = (x, y, SE)
        elif winsys == \"x11\":
            self.iconfont[\"family\"] = \"FreeSerif\"
            self.icon = DEFAULT_ICON if self.icon is None else self.icon
            if self.position is None:
                x, y = utility.scale_size(self.toplevel, [0, 0])
                self.position = (x, y, SE)
        else:
            self.iconfont[\"family\"] = \"Apple Symbols\"
            self.toplevel.update_idletasks()
            self.icon = DEFAULT_ICON if self.icon is None else self.icon
            if self.position is None:
                x, y = utility.scale_size(self.toplevel, [50, 50])
                self.position = (x, y, NE)

        self.set_geometry()

    def set_geometry(self):
        self.toplevel.update_idletasks()  # actualize geometry
        anchor = self.position[-1]
        x_anchor = \"-\" if \"w\" not in anchor else \"+\"
        y_anchor = \"-\" if \"n\" not in anchor else \"+\"
        screen_w = self.toplevel.winfo_screenwidth() // 2
        screen_h = self.toplevel.winfo_screenheight() // 2
        top_w = self.toplevel.winfo_width() // 2
        top_h = self.toplevel.winfo_height() // 2

        if all([\"e\" not in anchor, \"w\" not in anchor]):
            xpos = screen_w - top_w
        else:
            xpos = self.position[0]
        if all([\"n\" not in anchor, \"s\" not in anchor]):
            ypos = screen_h - top_h
        else:
            ypos = self.position[1]

        self.toplevel.geometry(f\"{x_anchor}{xpos}{y_anchor}{ypos}\")


if __name__ == \"__main__\":

    app = ttk.Window()

    ToastNotification(
        \"ttkbootstrap toast message\",
        \"This is a toast message; you can place a symbol on the top-left that is supported by the selected font. You can either make it appear for a specified period of time, or click to close.\",
    ).show_toast()

    app.mainloop()
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/window.py": """\"\"\"
    This module contains a class of the same name that wraps the 
    tkinter.Tk and ttkbootstrap.style.Style classes to provide a more
    consolidated api for initial application startup.
\"\"\"
import tkinter
from ttkbootstrap.constants import *
from ttkbootstrap.publisher import Publisher
from ttkbootstrap.style import Style
from ttkbootstrap.icons import Icon
from ttkbootstrap import utility


def get_default_root(what=None):
    \"\"\"Returns the default root if it has been created, otherwise
    returns a new instance.\"\"\"
    if not tkinter._support_default_root:
        raise RuntimeError(\"No master specified and tkinter is \"
                           \"configured to not support default root\")
    if not tkinter._default_root:
        if what:
            raise RuntimeError(f\"Too early to {what}: no default root window\")
        root = tkinter.Tk()
        assert tkinter._default_root is root
    return tkinter._default_root


def apply_class_bindings(window: tkinter.Widget):
    \"\"\"Add class level event bindings in application\"\"\"
    for className in [\"TEntry\", \"TSpinbox\", \"TCombobox\", \"Text\"]:
        window.bind_class(
            className=className, 
            sequence=\"<Configure>\", 
            func=on_disabled_readonly_state,
            add=\"+\")

        for sequence in [\"<Control-a>\", \"<Control-A>\"]:
            window.bind_class(
                className=className, 
                sequence=sequence,
                func=on_select_all)

    window.unbind_class(\"TButton\", \"<Key-space>\")

    def button_default_binding(event):
        \"\"\"The default keybind on a button when the return or enter key
        is pressed and the button has focus or is the default button.\"\"\"
        try:
            widget = window.nametowidget(event.widget)
            widget.invoke()
        except KeyError:
            window.tk.call(event.widget, 'invoke')

    window.bind_class(\"TButton\", \"<Key-Return>\", button_default_binding,
                      add=\"+\")
    window.bind_class(\"TButton\", \"<KP_Enter>\", button_default_binding, add=\"+\")


def apply_all_bindings(window: tkinter.Widget):
    \"\"\"Add bindings to all widgets in the application\"\"\"
    window.bind_all('<Map>', on_map_child, '+')
    window.bind_all('<Destroy>', lambda e: Publisher.unsubscribe(e.widget))


def on_disabled_readonly_state(event):
    \"\"\"Change the cursor of entry type widgets to 'arrow' if in a 
    disabled or readonly state.\"\"\"
    try:
        widget = event.widget
        state = str(widget.cget('state'))
        cursor = str(widget.cget('cursor'))
        if state in (DISABLED, READONLY):
            if cursor == 'arrow':
                return
            else:
                widget['cursor'] = 'arrow'
        else:
            if cursor in ('ibeam', ''):
                return
            else:
                widget['cursor'] = None
    except:
        pass


def on_map_child(event):
    \"\"\"Callback for <Map> event which generates a <<MapChild>> virtual
    event on the parent\"\"\"
    widget: tkinter.Widget = event.widget
    try:
        if widget.master is None: # root widget
            return
        else:
            widget.master.event_generate('<<MapChild>>')
    except:
        # not a tkinter widget that I'm handling (ex. Combobox.popdown)
        return


def on_select_all(event):
    \"\"\"Callback to select all text in the input widget when an event is
    executed.\"\"\"
    widget = event.widget
    if widget.__class__.__name__ == \"Text\":
        widget.tag_add(SEL, \"1.0\", END)
        widget.mark_set(INSERT, END)
        widget.see(END)
    else:
        widget.select_range(0, END)
        widget.icursor(END)
    return 'break'    


class Window(tkinter.Tk):
    \"\"\"A class that wraps the tkinter.Tk class in order to provide a
    more convenient api with additional bells and whistles. For more
    information on how to use the inherited `Tk` methods, see the
    [tcl/tk documentation](https://tcl.tk/man/tcl8.6/TkCmd/wm.htm)
    and the [Python documentation](https://docs.python.org/3/library/tkinter.html#tkinter.Tk).

    ![](../../assets/window/window-toplevel.png)

    Examples:

        ```python
        app = Window(title=\"My Application\", themename=\"superhero\")
        app.mainloop()
        ```
    \"\"\"

    def __init__(
        self,
        title=\"ttkbootstrap\",
        themename=\"litera\",
        iconphoto='',
        size=None,
        position=None,
        minsize=None,
        maxsize=None,
        resizable=None,
        hdpi=True,
        scaling=None,
        transient=None,
        overrideredirect=False,
        alpha=1.0,
    ):
        \"\"\"
        Parameters:

            title (str):
                The title that appears on the application titlebar.

            themename (str):
                The name of the ttkbootstrap theme to apply to the
                application.

            iconphoto (str):
                A path to the image used for the titlebar icon.
                Internally this is passed to the `Tk.iconphoto` method
                and the image will be the default icon for all windows.
                A ttkbootstrap image is used by default. To disable
                this default behavior, set the value to `None` and use
                the `Tk.iconphoto` or `Tk.iconbitmap` methods directly.

            size (Tuple[int, int]):
                The width and height of the application window.
                Internally, this argument is passed to the
                `Window.geometry` method.

            position (Tuple[int, int]):
                The horizontal and vertical position of the window on
                the screen relative to the top-left coordinate.
                Internally this is passed to the `Window.geometry`
                method.

            minsize (Tuple[int, int]):
                Specifies the minimum permissible dimensions for the
                window. Internally, this argument is passed to the
                `Window.minsize` method.

            maxsize (Tuple[int, int]):
                Specifies the maximum permissible dimensions for the
                window. Internally, this argument is passed to the
                `Window.maxsize` method.

            resizable (Tuple[bool, bool]):
                Specifies whether the user may interactively resize the
                toplevel window. Must pass in two arguments that specify
                this flag for _horizontal_ and _vertical_ dimensions.
                This can be adjusted after the window is created by using
                the `Window.resizable` method.

            hdpi (bool):
                Enable high-dpi support for Windows OS. This option is
                enabled by default.

            scaling (float):
                Sets the current scaling factor used by Tk to convert
                between physical units (for example, points, inches, or
                millimeters) and pixels. The number argument is a
                floating point number that specifies the number of pixels
                per point on window's display.

            transient (Union[Tk, Widget]):
                Instructs the window manager that this widget is
                transient with regard to the widget master. Internally
                this is passed to the `Window.transient` method.

            overrideredirect (bool):
                Instructs the window manager to ignore this widget if
                True. Internally, this argument is passed to the
                `Window.overrideredirect(1)` method.

            alpha (float):
                On Windows, specifies the alpha transparency level of the
                toplevel. Where not supported, alpha remains at 1.0. Internally,
                this is processed as `Toplevel.attributes('-alpha', alpha)`.
        \"\"\"
        if hdpi:
            utility.enable_high_dpi_awareness()

        super().__init__()
        self.winsys = self.tk.call('tk', 'windowingsystem')

        if scaling is not None:
            utility.enable_high_dpi_awareness(self, scaling)

        if iconphoto is not None:
            if iconphoto == '':
                # the default ttkbootstrap icon
                self._icon = tkinter.PhotoImage(master=self, data=Icon.icon)
                self.iconphoto(True, self._icon)
            else:
                try:
                    # the user provided an image path
                    self._icon = tkinter.PhotoImage(file=iconphoto, master=self)
                    self.iconphoto(True, self._icon)
                except tkinter.TclError:
                    # The fallback icon if the user icon fails.
                    print('iconphoto path is bad; using default image.')
                    self._icon = tkinter.PhotoImage(data=Icon.icon, master=self)
                    self.iconphoto(True, self._icon)

        self.title(title)

        if size is not None:
            width, height = size
            self.geometry(f\"{width}x{height}\")
        
        if position is not None:
            xpos, ypos = position
            self.geometry(f\"+{xpos}+{ypos}\")
        
        if minsize is not None:
            width, height = minsize
            self.minsize(width, height)
        
        if maxsize is not None:
            width, height = maxsize
            self.maxsize(width, height)
        
        if resizable is not None:
            width, height = resizable
            self.resizable(width, height)
        
        if transient is not None:
            self.transient(transient)
        
        if overrideredirect:
            self.overrideredirect(1)
        
        if alpha is not None:
            if self.winsys == 'x11':
                self.wait_visibility(self)
            self.attributes(\"-alpha\", alpha)

        apply_class_bindings(self)
        apply_all_bindings(self)
        self._style = Style(themename)


    @property
    def style(self):
        \"\"\"Return a reference to the `ttkbootstrap.style.Style` object.\"\"\"
        return self._style

    def place_window_center(self):
        \"\"\"Position the toplevel in the center of the screen. Does not
        account for titlebar height.\"\"\"
        self.update_idletasks()
        w_height = self.winfo_height()
        w_width = self.winfo_width()
        s_height = self.winfo_screenheight()
        s_width = self.winfo_screenwidth()
        xpos = (s_width - w_width) // 2
        ypos = (s_height - w_height) // 2
        self.geometry(f'+{xpos}+{ypos}')

    position_center = place_window_center # alias


class Toplevel(tkinter.Toplevel):
    \"\"\"A class that wraps the tkinter.Toplevel class in order to
    provide a more convenient api with additional bells and whistles.
    For more information on how to use the inherited `Toplevel`
    methods, see the [tcl/tk documentation](https://tcl.tk/man/tcl8.6/TkCmd/toplevel.htm)
    and the [Python documentation](https://docs.python.org/3/library/tkinter.html#tkinter.Toplevel).

    ![](../../assets/window/window-toplevel.png)

    Examples:

        ```python
        app = Toplevel(title=\"My Toplevel\")
        app.mainloop()
        ```
    \"\"\"

    def __init__(
        self,
        title=\"ttkbootstrap\",
        iconphoto='',
        size=None,
        position=None,
        minsize=None,
        maxsize=None,
        resizable=None,
        transient=None,
        overrideredirect=False,
        windowtype=None,
        topmost=False,
        toolwindow=False,
        alpha=1.0,
        **kwargs,
    ):
        \"\"\"
        Parameters:

            title (str):
                The title that appears on the application titlebar.

            iconphoto (str):
                A path to the image used for the titlebar icon.
                Internally this is passed to the `Tk.iconphoto` method.
                By default the application icon is used.

            size (Tuple[int, int]):
                The width and height of the application window.
                Internally, this argument is passed to the
                `Toplevel.geometry` method.

            position (Tuple[int, int]):
                The horizontal and vertical position of the window on
                the screen relative to the top-left coordinate.
                Internally this is passed to the `Toplevel.geometry`
                method.

            minsize (Tuple[int, int]):
                Specifies the minimum permissible dimensions for the
                window. Internally, this argument is passed to the
                `Toplevel.minsize` method.

            maxsize (Tuple[int, int]):
                Specifies the maximum permissible dimensions for the
                window. Internally, this argument is passed to the
                `Toplevel.maxsize` method.

            resizable (Tuple[bool, bool]):
                Specifies whether the user may interactively resize the
                toplevel window. Must pass in two arguments that specify
                this flag for _horizontal_ and _vertical_ dimensions.
                This can be adjusted after the window is created by using
                the `Toplevel.resizable` method.

            transient (Union[Tk, Widget]):
                Instructs the window manager that this widget is
                transient with regard to the widget master. Internally
                this is passed to the `Toplevel.transient` method.

            overrideredirect (bool):
                Instructs the window manager to ignore this widget if
                True. Internally, this argument is processed as
                `Toplevel.overrideredirect(1)`.

            windowtype (str):
                On X11, requests that the window should be interpreted by
                the window manager as being of the specified type. Internally,
                this is passed to the `Toplevel.attributes('-type', windowtype)`.

                See the [-type option](https://tcl.tk/man/tcl8.6/TkCmd/wm.htm#M64)
                for a list of available options.

            topmost (bool):
                Specifies whether this is a topmost window (displays above all
                other windows). Internally, this processed by the window as
                `Toplevel.attributes('-topmost', 1)`.

            toolwindow (bool):
                On Windows, specifies a toolwindow style. Internally, this is
                processed as `Toplevel.attributes('-toolwindow', 1)`.

            alpha (float):
                On Windows, specifies the alpha transparency level of the
                toplevel. Where not supported, alpha remains at 1.0. Internally,
                this is processed as `Toplevel.attributes('-alpha', alpha)`.

            **kwargs (Dict):
                Other optional keyword arguments.
        \"\"\"
        if 'iconify' in kwargs:
            iconify = kwargs.pop('iconify')
        else:
            iconify = None

        super().__init__(**kwargs)
        self.winsys = self.tk.call('tk', 'windowingsystem')
        
        if iconify:
            self.iconify()

        if iconphoto != '':
            try:
                # the user provided an image path
                self._icon = tkinter.PhotoImage(file=iconphoto, master=self)
                self.iconphoto(True, self._icon)
            except tkinter.TclError:
                # The fallback icon if the user icon fails.
                print('iconphoto path is bad; using default image.')
                pass

        self.title(title)

        if size is not None:
            width, height = size
            self.geometry(f'{width}x{height}')

        if position is not None:
            xpos, ypos = position
            self.geometry(f\"+{xpos}+{ypos}\")
        
        if minsize is not None:
            width, height = minsize
            self.minsize(width, height)
        
        if maxsize is not None:
            width, height = maxsize
            self.maxsize(width, height)

        if resizable is not None:
            width, height = resizable
            self.resizable(width, height)
        
        if transient is not None:
            self.transient(transient)
        
        if overrideredirect:
            self.overrideredirect(1)
        
        if windowtype is not None:
            if self.winsys == 'x11':
                self.attributes(\"-type\", windowtype)
        
        if topmost:
            self.attributes(\"-topmost\", 1)
        
        if toolwindow:
            if self.winsys == 'win32':
                self.attributes(\"-toolwindow\", 1)
        
        if alpha is not None:
            if self.winsys == 'x11':
                self.wait_visibility(self)
            self.attributes(\"-alpha\", alpha)

    @property
    def style(self):
        \"\"\"Return a reference to the `ttkbootstrap.style.Style` object.\"\"\"
        return Style()

    def place_window_center(self):
        \"\"\"Position the toplevel in the center of the screen. Does not
        account for titlebar height.\"\"\"
        self.update_idletasks()
        w_height = self.winfo_height()
        w_width = self.winfo_width()
        s_height = self.winfo_screenheight()
        s_width = self.winfo_screenwidth()
        xpos = (s_width - w_width) // 2
        ypos = (s_height - w_height) // 2
        self.geometry(f'+{xpos}+{ypos}')

    position_center = place_window_center # alias

if __name__ == \"__main__\":

    root = Window(themename=\"superhero\", alpha=0.5, size=(1000, 1000))
    #root.withdraw()
    root.place_window_center()
    #root.deiconify()

    top = Toplevel(title=\"My Toplevel\", alpha=0.4, size=(1000, 1000))
    top.place_window_center()

    root.mainloop()
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/colorutils.py": """from PIL import ImageColor
from colorsys import rgb_to_hls

RGB = 'rgb'
HSL = 'hsl'
HEX = 'hex'
NAME = 'name'

HUE = 360
SAT = 100
LUM = 100


def color_to_rgb(color, model=HEX):
    \"\"\"Convert color value to rgb.

    The color and model parameters represent the color to be converted.
    The value is expected to be a string for \"name\" and \"hex\" models and
    a Tuple or List for \"rgb\" and \"hsl\" models.
    
    Parameters:
        
        color (Any):
            The color values for the model being converted.
            
        model (str):
            The color model being converted.
    
    Returns:
    
        Tuple[int, int, int]:
            The rgb color values.
    \"\"\"
    color_ = conform_color_model(color, model)    
    try:
        return ImageColor.getrgb(color_)
    except:
        print('this')
    
def color_to_hex(color, model=RGB):
    \"\"\"Convert color value to hex.

    The color and model parameters represent the color to be converted.
    The value is expected to be a string for \"name\" and \"hex\" models and
    a Tuple or List for \"rgb\" and \"hsl\" models.
    
    Parameters:
        
        color (Any):
            The color values for the model being converted.
            
        model (str):
            The color model being converted.
    
    Returns:
    
        str:
            The hexadecimal color value.
    \"\"\"
    r, g, b = color_to_rgb(color, model)
    return f'#{r:02x}{g:02x}{b:02x}'

def color_to_hsl(color, model=HEX):
    \"\"\"Convert color value to hsl.

    The color and model parameters represent the color to be converted.
    The value is expected to be a string for \"name\" and \"hex\" models and
    a Tuple or List for \"rgb\" and \"hsl\" models.
    
    Parameters:
        
        color (Any):
            The color values for the model being converted.
            
        model (str):
            The color model being converted.
    
    Returns:
    
        Tuple[int, int, int]:
            The hsl color values.
    \"\"\"
    r, g, b = color_to_rgb(color, model)
    hls = rgb_to_hls(r/255, g/255, b/255)
    h = int(hls[0]*HUE)
    l = int(hls[1]*LUM)
    s = int(hls[2]*SAT)
    return h, s, l

def update_hsl_value(color, hue=None, sat=None, lum=None, inmodel=HSL, outmodel=HSL):
    \"\"\"Change hue, saturation, or lumenosity of the color based on the
    hue, sat, lum parameters provided.
    
    Parameters:

        color (Any):
            The color

        hue (int):
            A number between 0 and 360.

        sat (int):
            A number between 0 and 100.

        lum (int):
            A number between 0 and 100.

        inmodel (str):
            The color model used by the color to be changed. One of
            hsl, rgb, hex, name.

        outmodel (str):
            The color value model to be returned when the color is
            changed. One of hsl, rgb, hex.

    Returns:

        Union[Tuple[int, int, int], str]:
            The color value based on the selected color model.
    \"\"\"
    h, s, l = color_to_hsl(color, inmodel)
    if hue is not None:
        h = hue
    if sat is not None:
        s = sat
    if lum is not None:
        l = lum
    if outmodel == RGB:
        return color_to_rgb([h, s, l], HSL)
    elif outmodel == HEX:
        return color_to_hex([h, s, l], HSL)
    else:
        return h, s, l


\"\"\"
https://stackoverflow.com/questions/1855884/determine-font-color-based-on-background-color

\"\"\"

def contrast_color(color, model=RGB, darkcolor='#000', lightcolor='#fff'):
    \"\"\"Returns the best matching contrasting light or dark color for
    the given color.
    
    Parameters:

        color (Any):
            The color value to evaluate.

        model (str):
            The model of the color value to be evaluated. 'rgb' by 
            default.

        darkcolor (Any):
            The color value to be returned when the constrasting color 
            should be dark.

        lightcolor (Any):
            The color value to be returned when the constrasting color
            should be light.

    Returns:

        str:
            The matching color value.
    \"\"\"
    if model != RGB:
        r, g, b = color_to_rgb(color, model)
    else:
        r, g, b = color

    luminance = ((0.299 * r) + (0.587 * g) + (0.114 * b))/255
    if luminance > 0.5:
        return darkcolor
    else:
        return lightcolor


def conform_color_model(color, model):
    \"\"\"Conform the color values to a string that can be interpreted
    by the `PIL.ImageColor.getrgb method`.

    Parameters:

        color (Union[Tuple[int, int, int], str]):
            The color value to conform.

        model (str):
            One of 'HSL', 'RGB', or 'HEX'

    Returns:

        str:
            A color value string that can be used as a parameter in the
            PIL.ImageColor.getrgb method.
    \"\"\"    
    if model == HSL:
        h, s, l = color
        return f'hsl({h},{s}%,{l}%)'
    elif model == RGB:
        r, g, b = color
        return f'rgb({r},{g},{b})'
    else:
        return color
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/__init__.py": """from ttkbootstrap.style import Style
from ttkbootstrap.style import Bootstyle
from ttkbootstrap.widgets import *
from ttkbootstrap.window import Window, Toplevel

from tkinter.scrolledtext import ScrolledText
from tkinter import Variable, StringVar, IntVar, BooleanVar, DoubleVar
from tkinter import Canvas, Menu, Text
from tkinter import PhotoImage

Bootstyle.setup_ttkbootstap_api()
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/style.py": """import json
import re
import colorsys
import tkinter as tk
from tkinter import font
from math import ceil
from tkinter import TclError, ttk
from typing import Any, Callable
from PIL import ImageTk, ImageDraw, Image, ImageFont
from ttkbootstrap.constants import *
from ttkbootstrap.themes.standard import STANDARD_THEMES
from ttkbootstrap.publisher import Publisher, Channel
from ttkbootstrap import utility as util
from ttkbootstrap import colorutils
from PIL import ImageColor


try:
    # prevent app from failing if user.py gets corrupted
    from ttkbootstrap.themes.user import USER_THEMES
except (ImportError, ModuleNotFoundError):
    USER_THEMES = {}


class Colors:
    \"\"\"A class that defines the color scheme for a theme as well as
    provides several static methods for manipulating colors.

    A `Colors` object is attached to a `ThemeDefinition` and can also
    be accessed through the `Style.colors` property for the
    current theme.

    Examples:

        ```python
        style = Style()

        # dot-notation
        style.colors.primary

        # get method
        style.colors.get('primary')
        ```

        This class is an iterator, so you can iterate over the main
        style color labels (primary, secondary, success, info, warning,
        danger):

        ```python
        for color_label in style.colors:
            color = style.colors.get(color_label)
            print(color_label, color)
        ```

        If, for some reason, you need to iterate over all theme color
        labels, then you can use the `Colors.label_iter` method. This
        will include all theme colors.

        ```python
        for color_label in style.colors.label_iter():
            color = Colors.get(color_label)
            print(color_label, color)
        ```

        If you want to adjust the hsv values of an existing color by a
        specific percentage (delta), you can use the `Colors.update_hsv`
        method, which is static. In the example below, the \"value delta\"
        or `vd` is increased by 15%, which will lighten the color:

        ```python
        Colors.update_hsv(\"#9954bb\", vd=0.15)
        ```
    \"\"\"

    def __init__(
        self,
        primary,
        secondary,
        success,
        info,
        warning,
        danger,
        light,
        dark,
        bg,
        fg,
        selectbg,
        selectfg,
        border,
        inputfg,
        inputbg,
        active,
    ):
        \"\"\"
        Parameters:

            primary (str):
                The primary theme color; used by default for all widgets.

            secondary (str):
                An accent color; commonly of a `grey` hue.

            success (str):
                An accent color; commonly of a `green` hue.

            info (str):
                An accent color; commonly of a `blue` hue.

            warning (str):
                An accent color; commonly of an `orange` hue.

            danger (str):
                An accent color; commonly of a `red` hue.

            light (str):
                An accent color.

            dark (str):
                An accent color.

            bg (str):
                Background color.

            fg (str):
                Default text color.

            selectfg (str):
                The color of selected text.

            selectbg (str):
                The background color of selected text.

            border (str):
                The color used for widget borders.

            inputfg (str):
                The text color for input widgets.

            inputbg (str):
                The text background color for input widgets.

            active (str):
                An accent color.
        \"\"\"
        self.primary = primary
        self.secondary = secondary
        self.success = success
        self.info = info
        self.warning = warning
        self.danger = danger
        self.light = light
        self.dark = dark
        self.bg = bg
        self.fg = fg
        self.selectbg = selectbg
        self.selectfg = selectfg
        self.border = border
        self.inputfg = inputfg
        self.inputbg = inputbg
        self.active = active

    @staticmethod
    def make_transparent(alpha, foreground, background='#ffffff'):
        \"\"\"Simulate color transparency.
        
        Parameters:

            alpha (float):
                The amount of transparency; a number between 0 and 1.

            foreground (str):
                The foreground color.

            background (str):
                The background color.

        Returns:

            str:
                A hexadecimal color representing the \"transparent\" 
                version of the foreground color against the background 
                color.
        \"\"\"
        fg = ImageColor.getrgb(foreground)
        bg = ImageColor.getrgb(background)
        rgb_float = [alpha * c1 + (1 - alpha) * c2 for (c1, c2) in zip(fg, bg)]
        rgb_int = [int(x) for x in rgb_float]
        return '#{:02x}{:02x}{:02x}'.format(*rgb_int)    

    @staticmethod
    def rgb_to_hsv(r, g, b):
        \"\"\"Convert an rgb to hsv color value.

        Parameters:
            r (float):
                red
            g (float):
                green
            b (float):
                blue

        Returns:
            Tuple[float, float, float]: The hsv color value.
        \"\"\"
        return colorsys.rgb_to_hsv(r, g, b)

    def get_foreground(self, color_label):
        \"\"\"Return the appropriate foreground color for the specified
        color_label.

        Parameters:

            color_label (str):
                A color label corresponding to a class property
        \"\"\"
        if color_label == LIGHT:
            return self.dark
        elif color_label == DARK:
            return self.light
        else:
            return self.selectfg

    def get(self, color_label: str):
        \"\"\"Lookup a color value from the color name

        Parameters:

            color_label (str):
                A color label corresponding to a class propery

        Returns:

            str:
                A hexadecimal color value.
        \"\"\"
        return self.__dict__.get(color_label)

    def set(self, color_label: str, color_value: str):
        \"\"\"Set a color property value. This does not update any existing
        widgets. Can also be used to create on-demand color properties
        that can be used in your program after creation.

        Parameters:

            color_label (str):
                The name of the color to be set (key)

            color_value (str):
                A hexadecimal color value
        \"\"\"
        self.__dict__[color_label] = color_value

    def __iter__(self):
        return iter(
            [
                \"primary\",
                \"secondary\",
                \"success\",
                \"info\",
                \"warning\",
                \"danger\",
                \"light\",
                \"dark\",
            ]
        )

    def __repr__(self):
        out = tuple(zip(self.__dict__.keys(), self.__dict__.values()))
        return str(out)

    @staticmethod
    def label_iter():
        \"\"\"Iterate over all color label properties in the Color class

        Returns:

            iter:
                An iterator for color label names
        \"\"\"
        return iter(
            [
                \"primary\",
                \"secondary\",
                \"success\",
                \"info\",
                \"warning\",
                \"danger\",
                \"light\",
                \"dark\",
                \"bg\",
                \"fg\",
                \"selectbg\",
                \"selectfg\",
                \"border\",
                \"inputfg\",
                \"inputbg\",
                \"active\",
            ]
        )

    @staticmethod
    def hex_to_rgb(color: str):
        \"\"\"Convert hexadecimal color to rgb color value

        Parameters:

            color (str):
                A hexadecimal color value

        Returns:

            tuple[int, int, int]:
                An rgb color value.
        \"\"\"
        r, g, b = colorutils.color_to_rgb(color)
        return r/255, g/255, b/255

    @staticmethod
    def rgb_to_hex(r: int, g: int, b: int):
        \"\"\"Convert rgb to hexadecimal color value

        Parameters:

            r (int):
                red

            g (int):
                green

            b (int):
                blue

        Returns:

            str:
                A hexadecimal color value
        \"\"\"
        r_ = int(r * 255)
        g_ = int(g * 255)
        b_ = int(b * 255)
        return colorutils.color_to_hex((r_, g_, b_))

    @staticmethod
    def update_hsv(color, hd=0, sd=0, vd=0):
        \"\"\"Modify the hue, saturation, and/or value of a given hex
        color value by specifying the _delta_.

        Parameters:

            color (str):
                A hexadecimal color value to adjust.

            hd (float):
                % change in hue, _hue delta_.

            sd (float):
                % change in saturation, _saturation delta_.

            vd (float):
                % change in value, _value delta_.

        Returns:

            str:
                The resulting hexadecimal color value
        \"\"\"
        r, g, b = Colors.hex_to_rgb(color)
        h, s, v = colorsys.rgb_to_hsv(r, g, b)

        # hue
        if h * (1 + hd) > 1:
            h = 1
        elif h * (1 + hd) < 0:
            h = 0
        else:
            h *= 1 + hd

        # saturation
        if s * (1 + sd) > 1:
            s = 1
        elif s * (1 + sd) < 0:
            s = 0
        else:
            s *= 1 + sd

        # value
        if v * (1 + vd) > 1:
            v = 0.95
        elif v * (1 + vd) < 0.05:
            v = 0.05
        else:
            v *= 1 + vd

        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        return Colors.rgb_to_hex(r, g, b)


class ThemeDefinition:
    \"\"\"A class to provide defined name, colors, and font settings for a
    ttkbootstrap theme.\"\"\"

    def __init__(self, name, colors, themetype=LIGHT):
        \"\"\"
        Parameters:

            name (str):
                The name of the theme.

            colors (Colors):
                An object that defines the color scheme for a theme.

            themetype (str):
                Specifies whether the theme is **light** or **dark**.
        \"\"\"
        self.name = name
        self.colors = Colors(**colors)
        self.type = themetype

    def __repr__(self):

        return \" \".join(
            [
                f\"name={self.name},\",
                f\"type={self.type},\",
                f\"colors={self.colors}\",
            ]
        )


class Style(ttk.Style):
    \"\"\"A singleton class for creating and managing the application
    theme and widget styles.

    This class is meant to be a drop-in replacement for `ttk.Style` and
    inherits all of it's methods and properties. However, in
    ttkbootstrap, this class is implemented as a singleton. Subclassing
    is not recommended and may have unintended consequences.

    Examples:

        ```python
        # instantiate the style with default theme
        style = Style()

        # instantiate the style with another theme
        style = Style(theme='superhero')

        # check all available themes
        for theme in style.theme_names():
            print(theme)
        ```

    See the [Python documentation](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Style)
    on this class for more details.
    \"\"\"

    instance = None

    def __new__(cls, theme=None):
        if Style.instance is None:
            return object.__new__(cls)
        else:
            return Style.instance

    def __init__(self, theme=DEFAULT_THEME):
        \"\"\"
        Parameters:

            theme (str):
                The name of the theme to use when styling the widget.
        \"\"\"
        if Style.instance is not None:
            if theme != DEFAULT_THEME:
                Style.instance.theme_use(theme)
            return
        self._theme_objects = {}
        self._theme_definitions = {}
        self._style_registry = set()  # all styles used
        self._theme_styles = {}  # styles used in theme
        self._theme_names = set()
        self._load_themes()
        super().__init__()

        Style.instance = self
        self.theme_use(theme)

        # apply localization
        from ttkbootstrap import localization
        localization.initialize_localities()

    @property
    def colors(self):
        \"\"\"An object that contains the colors used for the current
        theme.

        Returns:

            Colors:
                The colors object for the current theme.
        \"\"\"
        theme = self.theme.name
        if theme in list(self._theme_names):
            definition = self._theme_definitions.get(theme)
            if not definition:
                return []  # TODO refactor this
            else:
                return definition.colors
        else:
            return []  # TODO refactor this

    def configure(self, style, query_opt: Any = None, **kw):
        if query_opt:
            return super().configure(style, query_opt=query_opt, **kw)

        if not self.style_exists_in_theme(style):
            ttkstyle = Bootstyle.update_ttk_widget_style(None, style)
        else:
            ttkstyle = style

        if ttkstyle == style:
            # configure an existing ttkbootrap theme
            return super().configure(style, query_opt=query_opt, **kw)
        else:
            # subclass a ttkbootstrap theme
            result = super().configure(style, query_opt=query_opt, **kw)
            self._register_ttkstyle(style)
            return result

    def theme_names(self):
        \"\"\"Return a list of all ttkbootstrap themes.

        Returns:

            List[str, ...]:
                A list of theme names.
        \"\"\"
        return list(self._theme_definitions.keys())

    def register_theme(self, definition):
        \"\"\"Register a theme definition for use by the `Style`
        object. This makes the definition and name available at
        run-time so that the assets and styles can be created when
        needed.

        Parameters:

            definition (ThemeDefinition):
                A `ThemeDefinition` object.
        \"\"\"
        theme = definition.name
        self._theme_names.add(theme)
        self._theme_definitions[theme] = definition
        self._theme_styles[theme] = set()

    def theme_use(self, themename=None):
        \"\"\"Changes the theme used in rendering the application widgets.

        If themename is None, returns the theme in use, otherwise, set
        the current theme to themename, refreshes all widgets and emits
        a ``<<ThemeChanged>>`` event.

        Only use this method if you are changing the theme *during*
        runtime. Otherwise, pass the theme name into the Style
        constructor to instantiate the style with a theme.

        Parameters:

            themename (str):
                The name of the theme to apply when creating new widgets

        Returns:

            Union[str, None]:
                The name of the current theme if `themename` is None
                otherwise, `None`.
        \"\"\"
        if not themename:
            # return current theme
            return super().theme_use()

        # change to an existing theme
        existing_themes = super().theme_names()
        if themename in existing_themes:
            self.theme = self._theme_definitions.get(themename)
            super().theme_use(themename)
            self._create_ttk_styles_on_theme_change()
            Publisher.publish_message(Channel.STD)
        # setup a new theme
        elif themename in self._theme_names:
            self.theme = self._theme_definitions.get(themename)
            self._theme_objects[themename] = StyleBuilderTTK()
            self._create_ttk_styles_on_theme_change()
            Publisher.publish_message(Channel.STD)
        else:
            raise TclError(themename, \"is not a valid theme.\")

    def style_exists_in_theme(self, ttkstyle: str):
        \"\"\"Check if a style exists in the current theme.

        Parameters:

            ttkstyle (str):
                The ttk style to check.

        Returns:

            bool:
                `True` if the style exists, otherwise `False`.
        \"\"\"
        theme_styles = self._theme_styles.get(self.theme.name)
        exists_in_theme = ttkstyle in theme_styles
        exists_in_registry = ttkstyle in self._style_registry
        return exists_in_theme and exists_in_registry

    @staticmethod
    def get_instance():
        \"\"\"Returns and instance of the style class\"\"\"
        return Style.instance

    @staticmethod
    def _get_builder():
        \"\"\"Get the object that builds the widget styles for the current
        theme.

        Returns:

            ThemeBuilderTTK:
                The theme builder object that builds the ttk styles for
                the current theme.
        \"\"\"
        style: Style = Style.get_instance()
        theme_name = style.theme.name
        return style._theme_objects[theme_name]

    @staticmethod
    def _get_builder_tk():
        \"\"\"Get the object that builds the widget styles for the current
        theme.

        Returns:

            ThemeBuilderTK:
                The theme builder object that builds the ttk styles for
                the current theme.
        \"\"\"
        builder = Style._get_builder()
        return builder.builder_tk

    def _build_configure(self, style, **kw):
        \"\"\"Calls configure of superclass; used by style builder classes.\"\"\"
        super().configure(style, **kw)

    def _load_themes(self):
        \"\"\"Load all ttkbootstrap defined themes\"\"\"
        # create a theme definition object for each theme, this will be
        # used to generate the theme in tkinter along with any assets
        # at run-time
        if USER_THEMES:
            STANDARD_THEMES.update(USER_THEMES)
        theme_settings = {\"themes\": STANDARD_THEMES}
        for name, definition in theme_settings[\"themes\"].items():
            self.register_theme(
                ThemeDefinition(
                    name=name,
                    themetype=definition[\"type\"],
                    colors=definition[\"colors\"],
                )
            )

    def _register_ttkstyle(self, ttkstyle):
        \"\"\"Register that a ttk style name. This ensures that the
        builder will not attempt to build a style that has already
        been created.

        Parameters:

            ttkstyle (str):
                The name of the ttk style to register.
        \"\"\"
        self._style_registry.add(ttkstyle)
        theme = self.theme.name
        self._theme_styles[theme].add(ttkstyle)

    def _create_ttk_styles_on_theme_change(self):
        \"\"\"Create existing styles when the theme changes\"\"\"
        for ttkstyle in self._style_registry:
            if not self.style_exists_in_theme(ttkstyle):
                color = Bootstyle.ttkstyle_widget_color(ttkstyle)
                method_name = Bootstyle.ttkstyle_method_name(string=ttkstyle)
                builder: StyleBuilderTTK = self._get_builder()
                method: Callable = builder.name_to_method(method_name)
                method(builder, color)

    def load_user_themes(self, file):
        \"\"\"Load user themes saved in json format\"\"\"
        with open(file, encoding='utf-8') as f:
            data = json.load(f)
            themes = data['themes']
        for theme in themes:
            for name, definition in theme.items():
                self.register_theme(
                    ThemeDefinition(
                        name=name,
                        themetype=definition[\"type\"],
                        colors=definition[\"colors\"],
                    )
                )


class StyleBuilderTK:
    \"\"\"A class for styling legacy tkinter widgets (not ttk).

    The methods in this classed are used internally to update tk widget
    style configurations and are not intended to be called by the end
    user.

    All legacy tkinter widgets are updated with a callback whenever the
    theme is changed. The color configuration of the widget is updated
    to match the current theme. Legacy ttk widgets are not the primary
    focus of this library, however, an attempt was made to make sure they
    did not stick out amongst ttk widgets if used.

    Some ttk widgets contain legacy components that must be updated
    such as the Combobox popdown, so this ensures they are styled
    completely to match the current theme.
    \"\"\"

    def __init__(self):
        self.style = Style.get_instance()
        self.master = self.style.master

    @property
    def theme(self) -> ThemeDefinition:
        \"\"\"A reference to the `ThemeDefinition` object for the current
        theme.\"\"\"
        return self.style.theme

    @property
    def colors(self) -> Colors:
        \"\"\"A reference to the `Colors` object for the current theme.\"\"\"
        return self.style.colors

    @property
    def is_light_theme(self) -> bool:
        \"\"\"Returns `True` if the theme is _light_, otherwise `False`.\"\"\"
        return self.style.theme.type == LIGHT

    def update_tk_style(self, widget: tk.Tk):
        \"\"\"Update the window style.

        Parameters:

            widget (tkinter.Tk):
                The tk object to update.
        \"\"\"
        widget.configure(background=self.colors.bg)
        # add default initial font for text widget
        widget.option_add('*Text*Font', 'TkDefaultFont')

    def update_toplevel_style(self, widget: tk.Toplevel):
        \"\"\"Update the toplevel style.

        Parameters:

            widget (tkinter.Toplevel):
                The toplevel object to update.
        \"\"\"
        widget.configure(background=self.colors.bg)

    def update_canvas_style(self, widget: tk.Canvas):
        \"\"\"Update the canvas style.

        Parameters:

            widget (tkinter.Canvas):
                The canvas object to update.
        \"\"\"
        # if self.is_light_theme:
        #     bordercolor = self.colors.border
        # else:
        #     bordercolor = self.colors.selectbg

        widget.configure(
            background=self.colors.bg,
            highlightthickness=0,
            # highlightbackground=bordercolor,
        )

    def update_button_style(self, widget: tk.Button):
        \"\"\"Update the button style.

        Parameters:

            widget (tkinter.Button):
                The button object to update.
        \"\"\"
        background = self.colors.primary
        foreground = self.colors.selectfg
        activebackground = Colors.update_hsv(self.colors.primary, vd=-0.1)

        widget.configure(
            background=background,
            foreground=foreground,
            relief=tk.FLAT,
            borderwidth=0,
            activebackground=activebackground,
            highlightbackground=self.colors.selectfg,
        )

    def update_label_style(self, widget: tk.Label):
        \"\"\"Update the label style.

        Parameters:

            widget (tkinter.Label):
                The label object to update.
        \"\"\"
        widget.configure(foreground=self.colors.fg, background=self.colors.bg)

    def update_frame_style(self, widget: tk.Frame):
        \"\"\"Update the frame style.

        Parameters:

            widget (tkinter.Frame):
                The frame object to update.
        \"\"\"
        widget.configure(background=self.colors.bg)

    def update_checkbutton_style(self, widget: tk.Checkbutton):
        \"\"\"Update the checkbutton style.

        Parameters:

            widget (tkinter.Checkbutton):
                The checkbutton object to update.
        \"\"\"
        widget.configure(
            activebackground=self.colors.bg,
            activeforeground=self.colors.primary,
            background=self.colors.bg,
            foreground=self.colors.fg,
            selectcolor=self.colors.bg,
        )

    def update_radiobutton_style(self, widget: tk.Radiobutton):
        \"\"\"Update the radiobutton style.

        Parameters:

            widget (tkinter.Radiobutton):
                The radiobutton object to update.
        \"\"\"
        widget.configure(
            activebackground=self.colors.bg,
            activeforeground=self.colors.primary,
            background=self.colors.bg,
            foreground=self.colors.fg,
            selectcolor=self.colors.bg,
        )

    def update_entry_style(self, widget: tk.Entry):
        \"\"\"Update the entry style.

        Parameters:

            widget (tkinter.Entry):
                The entry object to update.
        \"\"\"
        if self.is_light_theme:
            bordercolor = self.colors.border
        else:
            bordercolor = self.colors.selectbg

        widget.configure(
            relief=tk.FLAT,
            highlightthickness=1,
            foreground=self.colors.inputfg,
            highlightbackground=bordercolor,
            highlightcolor=self.colors.primary,
            background=self.colors.inputbg,
            insertbackground=self.colors.inputfg,
            insertwidth=1,
        )

    def update_scale_style(self, widget: tk.Scale):
        \"\"\"Update the scale style.

        Parameters:

            widget (tkinter.scale):
                The scale object to update.
        \"\"\"
        if self.is_light_theme:
            bordercolor = self.colors.border
        else:
            bordercolor = self.colors.selectbg

        activecolor = Colors.update_hsv(self.colors.primary, vd=-0.2)
        widget.configure(
            background=self.colors.primary,
            showvalue=False,
            sliderrelief=tk.FLAT,
            borderwidth=0,
            activebackground=activecolor,
            highlightthickness=1,
            highlightcolor=bordercolor,
            highlightbackground=bordercolor,
            troughcolor=self.colors.inputbg,
        )

    def update_spinbox_style(self, widget: tk.Spinbox):
        \"\"\"Update the spinbox style.

        Parameters:

            widget (tkinter.Spinbox):
                THe spinbox object to update.
        \"\"\"
        if self.is_light_theme:
            bordercolor = self.colors.border
        else:
            bordercolor = self.colors.selectbg

        widget.configure(
            relief=tk.FLAT,
            highlightthickness=1,
            foreground=self.colors.inputfg,
            highlightbackground=bordercolor,
            highlightcolor=self.colors.primary,
            background=self.colors.inputbg,
            buttonbackground=self.colors.inputbg,
            insertbackground=self.colors.inputfg,
            insertwidth=1,
            # these options should work, but do not have any affect
            buttonuprelief=tk.FLAT,
            buttondownrelief=tk.SUNKEN,
        )

    def update_listbox_style(self, widget: tk.Listbox):
        \"\"\"Update the listbox style.

        Parameters:

            widget (tkinter.Listbox):
                The listbox object to update.
        \"\"\"
        if self.is_light_theme:
            bordercolor = self.colors.border
        else:
            bordercolor = self.colors.selectbg

        widget.configure(
            foreground=self.colors.inputfg,
            background=self.colors.inputbg,
            selectbackground=self.colors.selectbg,
            selectforeground=self.colors.selectfg,
            highlightcolor=self.colors.primary,
            highlightbackground=bordercolor,
            highlightthickness=1,
            activestyle=\"none\",
            relief=tk.FLAT,
        )

    def update_menubutton_style(self, widget: tk.Menubutton):
        \"\"\"Update the menubutton style.

        Parameters:

            widget (tkinter.Menubutton):
                The menubutton object to update.
        \"\"\"
        activebackground = Colors.update_hsv(self.colors.primary, vd=-0.2)
        widget.configure(
            background=self.colors.primary,
            foreground=self.colors.selectfg,
            activebackground=activebackground,
            activeforeground=self.colors.selectfg,
            borderwidth=0,
        )

    def update_menu_style(self, widget: tk.Menu):
        \"\"\"Update the menu style.

        Parameters:

            widget (tkinter.Menu):
                The menu object to update.
        \"\"\"
        widget.configure(
            tearoff=False,
            activebackground=self.colors.selectbg,
            activeforeground=self.colors.selectfg,
            foreground=self.colors.fg,
            selectcolor=self.colors.primary,
            background=self.colors.bg,
            relief=tk.FLAT,
            borderwidth=0,
        )

    def update_labelframe_style(self, widget: tk.LabelFrame):
        \"\"\"Update the labelframe style.

        Parameters:

            widget (tkinter.LabelFrame):
                The labelframe object to update.
        \"\"\"
        if self.is_light_theme:
            bordercolor = self.colors.border
        else:
            bordercolor = self.colors.selectbg

        widget.configure(
            highlightcolor=bordercolor,
            foreground=self.colors.fg,
            borderwidth=1,
            highlightthickness=0,
            background=self.colors.bg,
        )

    def update_text_style(self, widget: tk.Text):
        \"\"\"Update the text style.

        Parameters:

            widget (tkinter.Text):
                The text object to update.
        \"\"\"
        if self.is_light_theme:
            bordercolor = self.colors.border
        else:
            bordercolor = self.colors.selectbg

        focuscolor = widget.cget(\"highlightbackground\")

        if focuscolor in [\"SystemButtonFace\", bordercolor]:
            focuscolor = bordercolor

        widget.configure(
            background=self.colors.inputbg,
            foreground=self.colors.inputfg,
            highlightcolor=focuscolor,
            highlightbackground=bordercolor,
            insertbackground=self.colors.inputfg,
            selectbackground=self.colors.selectbg,
            selectforeground=self.colors.selectfg,
            insertwidth=1,
            highlightthickness=1,
            relief=tk.FLAT,
            padx=5,
            pady=5,
            #font=\"TkDefaultFont\",
        )


class StyleBuilderTTK:
    \"\"\"A class containing methods for building new ttk widget styles on
    demand.

    The methods in this classed are used internally to generate ttk
    widget styles on-demand and are not intended to be called by the end
    user.
    \"\"\"

    def __init__(self):
        self.style: Style = Style.get_instance()
        self.theme_images = {}
        self.builder_tk = StyleBuilderTK()
        self.create_theme()

    @staticmethod
    def name_to_method(method_name):
        \"\"\"Get a method by name.

        Parameters:

            method_name (str):
                The name of the style builder method.

        Returns:

            Callable:
                The method that is named by `method_name`
        \"\"\"
        func = getattr(StyleBuilderTTK, method_name)
        return func

    @property
    def colors(self) -> Colors:
        \"\"\"A reference to the `Colors` object of the current theme.\"\"\"
        return self.style.theme.colors

    @property
    def theme(self) -> ThemeDefinition:
        \"\"\"A reference to the `ThemeDefinition` object for the current
        theme.\"\"\"
        return self.style.theme

    @property
    def is_light_theme(self) -> bool:
        \"\"\"If the current theme is _light_, returns `True`, otherwise
        returns `False`.\"\"\"
        return self.style.theme.type == LIGHT

    def scale_size(self, size):
        \"\"\"Scale the size of images and other assets based on the
        scaling factor of ttk to ensure that the image matches the
        screen resolution.

        Parameters:

            size (Union[int, List, Tuple]):
                A single integer or an iterable of integers
        \"\"\"
        winsys = self.style.master.tk.call(\"tk\", \"windowingsystem\")
        if winsys == \"aqua\":
            BASELINE = 1.000492368291482
        else:
            BASELINE = 1.33398982438864281
        scaling = self.style.master.tk.call(\"tk\", \"scaling\")
        factor = scaling / BASELINE

        if isinstance(size, int) or isinstance(size, float):
            return ceil(size * factor)
        elif isinstance(size, tuple) or isinstance(size, list):
            return [ceil(x * factor) for x in size]

    def create_theme(self):
        \"\"\"Create and style a new ttk theme. A wrapper around internal
        style methods.
        \"\"\"
        self.style.theme_create(self.theme.name, TTK_CLAM)
        ttk.Style.theme_use(self.style, self.theme.name)
        self.update_ttk_theme_settings()

    def update_ttk_theme_settings(self):
        \"\"\"This method is called internally every time the theme is
        changed to update various components included in the body of
        the method.\"\"\"
        self.create_default_style()

    def create_default_style(self):
        \"\"\"Setup the default widget style configuration for the root
        ttk style \".\"; these defaults are applied to any widget that
        contains the configuration options updated by this style. This
        method should be called *first* before any other style is applied
        during theme creation.
        \"\"\"
        self.style._build_configure(
            style=\".\",
            background=self.colors.bg,
            darkcolor=self.colors.border,
            foreground=self.colors.fg,
            troughcolor=self.colors.bg,
            selectbg=self.colors.selectbg,
            selectfg=self.colors.selectfg,
            selectforeground=self.colors.selectfg,
            selectbackground=self.colors.selectbg,
            fieldbg=\"white\",
            borderwidth=1,
            focuscolor=\"\",
        )
        # this is general style applied to the tableview
        self.create_link_button_style()
        self.style.configure(\"symbol.Link.TButton\", font=\"-size 16\")

    def create_combobox_style(self, colorname=DEFAULT):
        \"\"\"Create a style for the ttk.Combobox widget.

        Parameters:

            colorname (str):
                The color label to use as the primary widget color.
        \"\"\"
        STYLE = \"TCombobox\"

        if self.is_light_theme:
            disabled_fg = self.colors.border
            bordercolor = self.colors.border
            readonly = self.colors.light
        else:
            disabled_fg = self.colors.selectbg
            bordercolor = self.colors.selectbg
            readonly = bordercolor

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE
            element = f\"{ttkstyle.replace('TC','C')}\"
            focuscolor = self.colors.primary
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"
            element = f\"{ttkstyle.replace('TC','C')}\"
            focuscolor = self.colors.get(colorname)

        self.style.element_create(f\"{element}.downarrow\", \"from\", TTK_DEFAULT)
        self.style.element_create(f\"{element}.padding\", \"from\", TTK_CLAM)
        self.style.element_create(f\"{element}.textarea\", \"from\", TTK_CLAM)

        if all([colorname, colorname != DEFAULT]):
            bordercolor = focuscolor

        self.style._build_configure(
            ttkstyle,
            bordercolor=bordercolor,
            darkcolor=self.colors.inputbg,
            lightcolor=self.colors.inputbg,
            arrowcolor=self.colors.inputfg,
            foreground=self.colors.inputfg,
            fieldbackground=self.colors.inputbg,
            background=self.colors.inputbg,
            insertcolor=self.colors.inputfg,
            relief=tk.FLAT,
            padding=5,
            arrowsize=self.scale_size(12),
        )
        self.style.map(
            ttkstyle,
            background=[(\"readonly\", readonly)],
            fieldbackground=[(\"readonly\", readonly)],
            foreground=[(\"disabled\", disabled_fg)],
            bordercolor=[
                (\"invalid\", self.colors.danger),
                (\"focus !disabled\", focuscolor),
                (\"hover !disabled\", focuscolor),
            ],
            lightcolor=[
                (\"focus invalid\", self.colors.danger),
                (\"focus !disabled\", focuscolor),
                (\"pressed !disabled\", focuscolor),
                (\"readonly\", readonly),
            ],
            darkcolor=[
                (\"focus invalid\", self.colors.danger),
                (\"focus !disabled\", focuscolor),
                (\"pressed !disabled\", focuscolor),
                (\"readonly\", readonly),
            ],
            arrowcolor=[
                (\"disabled\", disabled_fg),
                (\"pressed !disabled\", focuscolor),
                (\"focus !disabled\", focuscolor),
                (\"hover !disabled\", focuscolor),
            ],
        )
        self.style.layout(
            ttkstyle,
            [
                (
                    \"combo.Spinbox.field\",
                    {
                        \"side\": tk.TOP,
                        \"sticky\": tk.EW,
                        \"children\": [
                            (
                                \"Combobox.downarrow\",
                                {\"side\": tk.RIGHT, \"sticky\": tk.NS},
                            ),
                            (
                                \"Combobox.padding\",
                                {
                                    \"expand\": \"1\",
                                    \"sticky\": tk.NSEW,
                                    \"children\": [
                                        (
                                            \"Combobox.textarea\",
                                            {\"sticky\": tk.NSEW},
                                        )
                                    ],
                                },
                            ),
                        ],
                    },
                )
            ],
        )
        self.style._register_ttkstyle(ttkstyle)

    def create_separator_style(self, colorname=DEFAULT):
        \"\"\"Create a style for the ttk.Separator widget.

        Parameters:

            colorname (str):
                The primary widget color.
        \"\"\"
        HSTYLE = \"Horizontal.TSeparator\"
        VSTYLE = \"Vertical.TSeparator\"

        hsize = [40, 1]
        vsize = [1, 40]

        # style colors
        if self.is_light_theme:
            default_color = self.colors.border
        else:
            default_color = self.colors.selectbg

        if any([colorname == DEFAULT, colorname == \"\"]):
            background = default_color
            h_ttkstyle = HSTYLE
            v_ttkstyle = VSTYLE
        else:
            background = self.colors.get(colorname)
            h_ttkstyle = f\"{colorname}.{HSTYLE}\"
            v_ttkstyle = f\"{colorname}.{VSTYLE}\"

        # horizontal separator
        h_element = h_ttkstyle.replace(\".TS\", \".S\")
        h_img = ImageTk.PhotoImage(Image.new(\"RGB\", hsize, background))
        h_name = util.get_image_name(h_img)
        self.theme_images[h_name] = h_img

        self.style.element_create(f\"{h_element}.separator\", \"image\", h_name)
        self.style.layout(
            h_ttkstyle, [(f\"{h_element}.separator\", {\"sticky\": tk.EW})]
        )

        # vertical separator
        v_element = v_ttkstyle.replace(\".TS\", \".S\")
        v_img = ImageTk.PhotoImage(Image.new(\"RGB\", vsize, background))
        v_name = util.get_image_name(v_img)
        self.theme_images[v_name] = v_img
        self.style.element_create(f\"{v_element}.separator\", \"image\", v_name)
        self.style.layout(
            v_ttkstyle, [(f\"{v_element}.separator\", {\"sticky\": tk.NS})]
        )
        self.style._register_ttkstyle(h_ttkstyle)
        self.style._register_ttkstyle(v_ttkstyle)

    def create_striped_progressbar_assets(self, thickness, colorname=DEFAULT):
        \"\"\"Create the striped progressbar image and return as a
        `PhotoImage`

        Parameters:

            colorname (str):
                The color label used to style the widget.

        Returns:

            Tuple[str]:
                A list of photoimage names.
        \"\"\"
        if any([colorname == DEFAULT, colorname == \"\"]):
            barcolor = self.colors.primary
        else:
            barcolor = self.colors.get(colorname)

        # calculate value of the light color
        brightness = Colors.rgb_to_hsv(*Colors.hex_to_rgb(barcolor))[2]
        if brightness < 0.4:
            value_delta = 0.3
        elif brightness > 0.8:
            value_delta = 0
        else:
            value_delta = 0.1

        barcolor_light = Colors.update_hsv(barcolor, sd=-0.2, vd=value_delta)

        # horizontal progressbar
        img = Image.new(\"RGBA\", (100, 100), barcolor_light)
        draw = ImageDraw.Draw(img)
        draw.polygon(
            xy=[(0, 0), (48, 0), (100, 52), (100, 100)],
            fill=barcolor,
        )
        draw.polygon(xy=[(0, 52), (48, 100), (0, 100)], fill=barcolor)

        _resized = img.resize((thickness, thickness), Image.LANCZOS)
        h_img = ImageTk.PhotoImage(_resized)
        h_name = h_img._PhotoImage__photo.name
        v_img = ImageTk.PhotoImage(_resized.rotate(90))
        v_name = v_img._PhotoImage__photo.name

        self.theme_images[h_name] = h_img
        self.theme_images[v_name] = v_img
        return h_name, v_name

    def create_striped_progressbar_style(self, colorname=DEFAULT):
        \"\"\"Create a striped style for the ttk.Progressbar widget.

        Parameters:

            colorname (str):
                The primary widget color label.
        \"\"\"
        HSTYLE = \"Striped.Horizontal.TProgressbar\"
        VSTYLE = \"Striped.Vertical.TProgressbar\"

        thickness = self.scale_size(12)

        if any([colorname == DEFAULT, colorname == \"\"]):
            h_ttkstyle = HSTYLE
            v_ttkstyle = VSTYLE
        else:
            h_ttkstyle = f\"{colorname}.{HSTYLE}\"
            v_ttkstyle = f\"{colorname}.{VSTYLE}\"

        if self.is_light_theme:
            if colorname == LIGHT:
                troughcolor = self.colors.bg
                bordercolor = self.colors.light
            else:
                troughcolor = self.colors.light
                bordercolor = troughcolor
        else:
            troughcolor = Colors.update_hsv(self.colors.selectbg, vd=-0.2)
            bordercolor = troughcolor

        # ( horizontal, vertical )
        images = self.create_striped_progressbar_assets(thickness, colorname)

        # horizontal progressbar
        h_element = h_ttkstyle.replace(\".TP\", \".P\")
        self.style.element_create(
            f\"{h_element}.pbar\",
            \"image\",
            images[0],
            width=thickness,
            sticky=tk.EW,
        )
        self.style.layout(
            h_ttkstyle,
            [
                (
                    f\"{h_element}.trough\",
                    {
                        \"sticky\": tk.NSEW,
                        \"children\": [
                            (
                                f\"{h_element}.pbar\",
                                {\"side\": tk.LEFT, \"sticky\": tk.NS},
                            )
                        ],
                    },
                )
            ],
        )
        self.style._build_configure(
            h_ttkstyle,
            troughcolor=troughcolor,
            thickness=thickness,
            bordercolor=bordercolor,
            borderwidth=1,
        )

        # vertical progressbar
        v_element = v_ttkstyle.replace(\".TP\", \".P\")
        self.style.element_create(
            f\"{v_element}.pbar\",
            \"image\",
            images[1],
            width=thickness,
            sticky=tk.NS,
        )
        self.style.layout(
            v_ttkstyle,
            [
                (
                    f\"{v_element}.trough\",
                    {
                        \"sticky\": tk.NSEW,
                        \"children\": [
                            (
                                f\"{v_element}.pbar\",
                                {\"side\": tk.BOTTOM, \"sticky\": tk.EW},
                            )
                        ],
                    },
                )
            ],
        )
        self.style._build_configure(
            v_ttkstyle,
            troughcolor=troughcolor,
            bordercolor=bordercolor,
            thickness=thickness,
            borderwidth=1,
        )
        self.style._register_ttkstyle(h_ttkstyle)
        self.style._register_ttkstyle(v_ttkstyle)

    def create_progressbar_style(self, colorname=DEFAULT):
        \"\"\"Create a solid ttk style for the ttk.Progressbar widget.

        Parameters:

            colorname (str):
                The primary widget color.
        \"\"\"
        H_STYLE = \"Horizontal.TProgressbar\"
        V_STYLE = \"Vertical.TProgressbar\"

        thickness = self.scale_size(10)

        if self.is_light_theme:
            if colorname == LIGHT:
                troughcolor = self.colors.bg
                bordercolor = self.colors.light
            else:
                troughcolor = self.colors.light
                bordercolor = troughcolor
        else:
            troughcolor = Colors.update_hsv(self.colors.selectbg, vd=-0.2)
            bordercolor = troughcolor

        if any([colorname == DEFAULT, colorname == \"\"]):
            background = self.colors.primary
            h_ttkstyle = H_STYLE
            v_ttkstyle = V_STYLE
        else:
            background = self.colors.get(colorname)
            h_ttkstyle = f\"{colorname}.{H_STYLE}\"
            v_ttkstyle = f\"{colorname}.{V_STYLE}\"

        self.style._build_configure(
            h_ttkstyle,
            thickness=thickness,
            borderwidth=1,
            bordercolor=bordercolor,
            lightcolor=self.colors.border,
            pbarrelief=tk.FLAT,
            troughcolor=troughcolor,
        )
        existing_elements = self.style.element_names()

        self.style._build_configure(
            v_ttkstyle,
            thickness=thickness,
            borderwidth=1,
            bordercolor=bordercolor,
            lightcolor=self.colors.border,
            pbarrelief=tk.FLAT,
            troughcolor=troughcolor,
        )
        existing_elements = self.style.element_names()

        # horizontal progressbar
        h_element = h_ttkstyle.replace(\".TP\", \".P\")
        trough_element = f\"{h_element}.trough\"
        pbar_element = f\"{h_element}.pbar\"
        if trough_element not in existing_elements:
            self.style.element_create(trough_element, \"from\", TTK_CLAM)
            self.style.element_create(pbar_element, \"from\", TTK_DEFAULT)

        self.style.layout(
            h_ttkstyle,
            [
                (
                    trough_element,
                    {
                        \"sticky\": \"nswe\",
                        \"children\": [
                            (pbar_element, {\"side\": \"left\", \"sticky\": \"ns\"})
                        ],
                    },
                )
            ],
        )
        self.style._build_configure(h_ttkstyle, background=background)

        # vertical progressbar
        v_element = v_ttkstyle.replace(\".TP\", \".P\")
        trough_element = f\"{v_element}.trough\"
        pbar_element = f\"{v_element}.pbar\"
        if trough_element not in existing_elements:
            self.style.element_create(trough_element, \"from\", TTK_CLAM)
            self.style.element_create(pbar_element, \"from\", TTK_DEFAULT)
            self.style._build_configure(v_ttkstyle, background=background)
        self.style.layout(
            v_ttkstyle,
            [
                (
                    trough_element,
                    {
                        \"sticky\": \"nswe\",
                        \"children\": [
                            (pbar_element, {\"side\": \"bottom\", \"sticky\": \"we\"})
                        ],
                    },
                )
            ],
        )

        # register ttkstyles
        self.style._register_ttkstyle(h_ttkstyle)
        self.style._register_ttkstyle(v_ttkstyle)

    def create_scale_assets(self, colorname=DEFAULT, size=14):
        \"\"\"Create the assets used for the ttk.Scale widget.

        The slider handle is automatically adjusted to fit the
        screen resolution.

        Parameters:

            colorname (str):
                The color label.

            size (int):
                The size diameter of the slider circle; default=16.

        Returns:

            Tuple[str]:
                A tuple of PhotoImage names to be used in the image
                layout when building the style.
        \"\"\"
        size = self.scale_size(size)
        if self.is_light_theme:
            disabled_color = self.colors.border
            if colorname == LIGHT:
                track_color = self.colors.bg
            else:
                track_color = self.colors.light
        else:
            disabled_color = self.colors.selectbg
            track_color = Colors.update_hsv(self.colors.selectbg, vd=-0.2)

        if any([colorname == DEFAULT, colorname == \"\"]):
            normal_color = self.colors.primary
        else:
            normal_color = self.colors.get(colorname)

        pressed_color = Colors.update_hsv(normal_color, vd=-0.1)
        hover_color = Colors.update_hsv(normal_color, vd=0.1)

        # normal state
        _normal = Image.new(\"RGBA\", (100, 100))
        draw = ImageDraw.Draw(_normal)
        draw.ellipse((0, 0, 95, 95), fill=normal_color)
        normal_img = ImageTk.PhotoImage(
            _normal.resize((size, size), Image.LANCZOS)
        )
        normal_name = util.get_image_name(normal_img)
        self.theme_images[normal_name] = normal_img

        # pressed state
        _pressed = Image.new(\"RGBA\", (100, 100))
        draw = ImageDraw.Draw(_pressed)
        draw.ellipse((0, 0, 95, 95), fill=pressed_color)
        pressed_img = ImageTk.PhotoImage(
            _pressed.resize((size, size), Image.LANCZOS)
        )
        pressed_name = util.get_image_name(pressed_img)
        self.theme_images[pressed_name] = pressed_img

        # hover state
        _hover = Image.new(\"RGBA\", (100, 100))
        draw = ImageDraw.Draw(_hover)
        draw.ellipse((0, 0, 95, 95), fill=hover_color)
        hover_img = ImageTk.PhotoImage(
            _hover.resize((size, size), Image.LANCZOS)
        )
        hover_name = util.get_image_name(hover_img)
        self.theme_images[hover_name] = hover_img

        # disabled state
        _disabled = Image.new(\"RGBA\", (100, 100))
        draw = ImageDraw.Draw(_disabled)
        draw.ellipse((0, 0, 95, 95), fill=disabled_color)
        disabled_img = ImageTk.PhotoImage(
            _disabled.resize((size, size), Image.LANCZOS)
        )
        disabled_name = util.get_image_name(disabled_img)
        self.theme_images[disabled_name] = disabled_img

        # vertical track
        h_track_img = ImageTk.PhotoImage(
            Image.new(\"RGB\", self.scale_size((40, 5)), track_color)
        )
        h_track_name = util.get_image_name(h_track_img)
        self.theme_images[h_track_name] = h_track_img

        # horizontal track
        v_track_img = ImageTk.PhotoImage(
            Image.new(\"RGB\", self.scale_size((5, 40)), track_color)
        )
        v_track_name = util.get_image_name(v_track_img)
        self.theme_images[v_track_name] = v_track_img

        return (
            normal_name,
            pressed_name,
            hover_name,
            disabled_name,
            h_track_name,
            v_track_name,
        )

    def create_scale_style(self, colorname=DEFAULT):
        \"\"\"Create a style for the ttk.Scale widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"TScale\"

        if any([colorname == DEFAULT, colorname == \"\"]):
            h_ttkstyle = f\"Horizontal.{STYLE}\"
            v_ttkstyle = f\"Vertical.{STYLE}\"
        else:
            h_ttkstyle = f\"{colorname}.Horizontal.{STYLE}\"
            v_ttkstyle = f\"{colorname}.Vertical.{STYLE}\"

        # ( normal, pressed, hover, disabled, htrack, vtrack )
        images = self.create_scale_assets(colorname)

        # horizontal scale
        h_element = h_ttkstyle.replace(\".TS\", \".S\")
        self.style.element_create(
            f\"{h_element}.slider\",
            \"image\",
            images[0],
            (\"disabled\", images[3]),
            (\"pressed\", images[1]),
            (\"hover\", images[2]),
        )
        self.style.element_create(f\"{h_element}.track\", \"image\", images[4])
        self.style.layout(
            h_ttkstyle,
            [
                (
                    f\"{h_element}.focus\",
                    {
                        \"expand\": \"1\",
                        \"sticky\": tk.NSEW,
                        \"children\": [
                            (f\"{h_element}.track\", {\"sticky\": tk.EW}),
                            (
                                f\"{h_element}.slider\",
                                {\"side\": tk.LEFT, \"sticky\": \"\"},
                            ),
                        ],
                    },
                )
            ],
        )
        # vertical scale
        v_element = v_ttkstyle.replace(\".TS\", \".S\")
        self.style.element_create(
            f\"{v_element}.slider\",
            \"image\",
            images[0],
            (\"disabled\", images[3]),
            (\"pressed\", images[1]),
            (\"hover\", images[2]),
        )
        self.style.element_create(f\"{v_element}.track\", \"image\", images[5])
        self.style.layout(
            v_ttkstyle,
            [
                (
                    f\"{v_element}.focus\",
                    {
                        \"expand\": \"1\",
                        \"sticky\": tk.NSEW,
                        \"children\": [
                            (f\"{v_element}.track\", {\"sticky\": tk.NS}),
                            (
                                f\"{v_element}.slider\",
                                {\"side\": tk.TOP, \"sticky\": \"\"},
                            ),
                        ],
                    },
                )
            ],
        )
        # register ttkstyles
        self.style._register_ttkstyle(h_ttkstyle)
        self.style._register_ttkstyle(v_ttkstyle)

    def create_floodgauge_style(self, colorname=DEFAULT):
        \"\"\"Create a ttk style for the ttkbootstrap.widgets.Floodgauge
        widget. This is a custom widget style that uses components of
        the progressbar and label.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        HSTYLE = \"Horizontal.TFloodgauge\"
        VSTYLE = \"Vertical.TFloodgauge\"
        FLOOD_FONT = \"-size 14\"

        if any([colorname == DEFAULT, colorname == \"\"]):
            h_ttkstyle = HSTYLE
            v_ttkstyle = VSTYLE
            background = self.colors.primary
        else:
            h_ttkstyle = f\"{colorname}.{HSTYLE}\"
            v_ttkstyle = f\"{colorname}.{VSTYLE}\"
            background = self.colors.get(colorname)

        if colorname == LIGHT:
            foreground = self.colors.fg
            troughcolor = self.colors.bg
        else:
            troughcolor = Colors.update_hsv(background, sd=-0.3, vd=0.8)
            foreground = self.colors.selectfg

        # horizontal floodgauge
        h_element = h_ttkstyle.replace(\".TF\", \".F\")
        self.style.element_create(f\"{h_element}.trough\", \"from\", TTK_CLAM)
        self.style.element_create(f\"{h_element}.pbar\", \"from\", TTK_DEFAULT)
        self.style.layout(
            h_ttkstyle,
            [
                (
                    f\"{h_element}.trough\",
                    {
                        \"children\": [
                            (f\"{h_element}.pbar\", {\"sticky\": tk.NS}),
                            (\"Floodgauge.label\", {\"sticky\": \"\"}),
                        ],
                        \"sticky\": tk.NSEW,
                    },
                )
            ],
        )
        self.style._build_configure(
            h_ttkstyle,
            thickness=50,
            borderwidth=1,
            bordercolor=background,
            lightcolor=background,
            pbarrelief=tk.FLAT,
            troughcolor=troughcolor,
            background=background,
            foreground=foreground,
            justify=tk.CENTER,
            anchor=tk.CENTER,
            font=FLOOD_FONT,
        )
        # vertical floodgauge
        v_element = v_ttkstyle.replace(\".TF\", \".F\")
        self.style.element_create(f\"{v_element}.trough\", \"from\", TTK_CLAM)
        self.style.element_create(f\"{v_element}.pbar\", \"from\", TTK_DEFAULT)
        self.style.layout(
            v_ttkstyle,
            [
                (
                    f\"{v_element}.trough\",
                    {
                        \"children\": [
                            (f\"{v_element}.pbar\", {\"sticky\": tk.EW}),
                            (\"Floodgauge.label\", {\"sticky\": \"\"}),
                        ],
                        \"sticky\": tk.NSEW,
                    },
                )
            ],
        )
        self.style._build_configure(
            v_ttkstyle,
            thickness=50,
            borderwidth=1,
            bordercolor=background,
            lightcolor=background,
            pbarrelief=tk.FLAT,
            troughcolor=troughcolor,
            background=background,
            foreground=foreground,
            justify=tk.CENTER,
            anchor=tk.CENTER,
            font=FLOOD_FONT,
        )
        # register ttkstyles
        self.style._register_ttkstyle(h_ttkstyle)
        self.style._register_ttkstyle(v_ttkstyle)

    def create_arrow_assets(self, arrowcolor, pressed, active):
        \"\"\"Create arrow assets used for various widget buttons.

        !!! note
            This method is currently not being utilized.

        Parameters:

            arrowcolor (str):
                The color value to use as the arrow fill color.

            pressed (str):
                The color value to use when the arrow is pressed.

            active (str):
                The color value to use when the arrow is active or
                hovered.
        \"\"\"

        def draw_arrow(color: str):

            img = Image.new(\"RGBA\", (11, 11))
            draw = ImageDraw.Draw(img)
            size = self.scale_size([11, 11])

            draw.line([2, 6, 2, 9], fill=color)
            draw.line([3, 5, 3, 8], fill=color)
            draw.line([4, 4, 4, 7], fill=color)
            draw.line([5, 3, 5, 6], fill=color)
            draw.line([6, 4, 6, 7], fill=color)
            draw.line([7, 5, 7, 8], fill=color)
            draw.line([8, 6, 8, 9], fill=color)

            img = img.resize(size, Image.BICUBIC)

            up_img = ImageTk.PhotoImage(img)
            up_name = util.get_image_name(up_img)
            self.theme_images[up_name] = up_img

            down_img = ImageTk.PhotoImage(img.rotate(180))
            down_name = util.get_image_name(down_img)
            self.theme_images[down_name] = down_img

            left_img = ImageTk.PhotoImage(img.rotate(90))
            left_name = util.get_image_name(left_img)
            self.theme_images[left_name] = left_img

            right_img = ImageTk.PhotoImage(img.rotate(-90))
            right_name = util.get_image_name(right_img)
            self.theme_images[right_name] = right_img

            return up_name, down_name, left_name, right_name

        normal_names = draw_arrow(arrowcolor)
        pressed_names = draw_arrow(pressed)
        active_names = draw_arrow(active)

        return normal_names, pressed_names, active_names

    def create_round_scrollbar_assets(self, thumbcolor, pressed, active):
        \"\"\"Create image assets to be used when building the round
        scrollbar style.

        Parameters:

            thumbcolor (str):
                The color value of the thumb in normal state.

            pressed (str):
                The color value to use when the thumb is pressed.

            active (str):
                The color value to use when the thumb is active or
                hovered.
        \"\"\"
        vsize = self.scale_size([9, 28])
        hsize = self.scale_size([28, 9])

        def rounded_rect(size, fill):
            x = size[0] * 10
            y = size[1] * 10
            img = Image.new(\"RGBA\", (x, y))
            draw = ImageDraw.Draw(img)
            radius = min([x, y]) // 2
            draw.rounded_rectangle([0, 0, x - 1, y - 1], radius, fill)
            image = ImageTk.PhotoImage(img.resize(size, Image.BICUBIC))
            name = util.get_image_name(image)
            self.theme_images[name] = image
            return name

        # create images
        h_normal_img = rounded_rect(hsize, thumbcolor)
        h_pressed_img = rounded_rect(hsize, pressed)
        h_active_img = rounded_rect(hsize, active)

        v_normal_img = rounded_rect(vsize, thumbcolor)
        v_pressed_img = rounded_rect(vsize, pressed)
        v_active_img = rounded_rect(vsize, active)

        return (
            h_normal_img,
            h_pressed_img,
            h_active_img,
            v_normal_img,
            v_pressed_img,
            v_active_img,
        )

    def create_round_scrollbar_style(self, colorname=DEFAULT):
        \"\"\"Create a round style for the ttk.Scrollbar widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"TScrollbar\"

        if any([colorname == DEFAULT, colorname == \"\"]):
            h_ttkstyle = f\"Round.Horizontal.{STYLE}\"
            v_ttkstyle = f\"Round.Vertical.{STYLE}\"

            if self.is_light_theme:
                background = self.colors.border
            else:
                background = self.colors.selectbg

        else:
            h_ttkstyle = f\"{colorname}.Round.Horizontal.{STYLE}\"
            v_ttkstyle = f\"{colorname}.Round.Vertical.{STYLE}\"
            background = self.colors.get(colorname)

        if self.is_light_theme:
            if colorname == LIGHT:
                troughcolor = self.colors.bg
            else:
                troughcolor = self.colors.light
        else:
            troughcolor = Colors.update_hsv(self.colors.selectbg, vd=-0.2)

        pressed = Colors.update_hsv(background, vd=-0.05)
        active = Colors.update_hsv(background, vd=0.05)

        scroll_images = self.create_round_scrollbar_assets(
            background, pressed, active
        )

        # horizontal scrollbar
        self.style._build_configure(
            h_ttkstyle,
            troughcolor=troughcolor,
            darkcolor=troughcolor,
            bordercolor=troughcolor,
            lightcolor=troughcolor,
            arrowcolor=background,
            arrowsize=self.scale_size(11),
            background=troughcolor,
            relief=tk.FLAT,
            borderwidth=0,
        )
        self.style.element_create(
            f\"{h_ttkstyle}.thumb\",
            \"image\",
            scroll_images[0],
            (\"pressed\", scroll_images[1]),
            (\"active\", scroll_images[2]),
            border=self.scale_size(9),
            padding=0,
            sticky=tk.EW,
        )
        self.style.layout(
            h_ttkstyle,
            [
                (
                    \"Horizontal.Scrollbar.trough\",
                    {
                        \"sticky\": \"we\",
                        \"children\": [
                            (
                                \"Horizontal.Scrollbar.leftarrow\",
                                {\"side\": \"left\", \"sticky\": \"\"},
                            ),
                            (
                                \"Horizontal.Scrollbar.rightarrow\",
                                {\"side\": \"right\", \"sticky\": \"\"},
                            ),
                            (
                                f\"{h_ttkstyle}.thumb\",
                                {\"expand\": \"1\", \"sticky\": \"nswe\"},
                            ),
                        ],
                    },
                )
            ],
        )
        self.style._build_configure(h_ttkstyle, arrowcolor=background)
        self.style.map(
            h_ttkstyle, arrowcolor=[(\"pressed\", pressed), (\"active\", active)]
        )

        # vertical scrollbar
        self.style._build_configure(
            v_ttkstyle,
            troughcolor=troughcolor,
            darkcolor=troughcolor,
            bordercolor=troughcolor,
            lightcolor=troughcolor,
            arrowcolor=background,
            arrowsize=self.scale_size(11),
            background=troughcolor,
            relief=tk.FLAT,
        )
        self.style.element_create(
            f\"{v_ttkstyle}.thumb\",
            \"image\",
            scroll_images[3],
            (\"pressed\", scroll_images[4]),
            (\"active\", scroll_images[5]),
            border=self.scale_size(9),
            padding=0,
            sticky=tk.NS,
        )
        self.style.layout(
            v_ttkstyle,
            [
                (
                    \"Vertical.Scrollbar.trough\",
                    {
                        \"sticky\": \"ns\",
                        \"children\": [
                            (
                                \"Vertical.Scrollbar.uparrow\",
                                {\"side\": \"top\", \"sticky\": \"\"},
                            ),
                            (
                                \"Vertical.Scrollbar.downarrow\",
                                {\"side\": \"bottom\", \"sticky\": \"\"},
                            ),
                            (
                                f\"{v_ttkstyle}.thumb\",
                                {\"expand\": \"1\", \"sticky\": \"nswe\"},
                            ),
                        ],
                    },
                )
            ],
        )
        self.style._build_configure(v_ttkstyle, arrowcolor=background)
        self.style.map(
            v_ttkstyle, arrowcolor=[(\"pressed\", pressed), (\"active\", active)]
        )

        # register ttkstyles
        self.style._register_ttkstyle(h_ttkstyle)
        self.style._register_ttkstyle(v_ttkstyle)

    def create_scrollbar_assets(self, thumbcolor, pressed, active):
        \"\"\"Create the image assets used to build the standard scrollbar
        style.

        Parameters:

            thumbcolor (str):
                The primary color value used to color the thumb.

            pressed (str):
                The color value to use when the thumb is pressed.

            active (str):
                The color value to use when the thumb is active or
                hovered.
        \"\"\"
        vsize = self.scale_size([9, 28])
        hsize = self.scale_size([28, 9])

        def draw_rect(size, fill):
            x = size[0] * 10
            y = size[1] * 10
            img = Image.new(\"RGBA\", (x, y), fill)
            image = ImageTk.PhotoImage(img.resize(size), Image.BICUBIC)
            name = util.get_image_name(image)
            self.theme_images[name] = image
            return name

        # create images
        h_normal_img = draw_rect(hsize, thumbcolor)
        h_pressed_img = draw_rect(hsize, pressed)
        h_active_img = draw_rect(hsize, active)

        v_normal_img = draw_rect(vsize, thumbcolor)
        v_pressed_img = draw_rect(vsize, pressed)
        v_active_img = draw_rect(vsize, active)

        return (
            h_normal_img,
            h_pressed_img,
            h_active_img,
            v_normal_img,
            v_pressed_img,
            v_active_img,
        )

    def create_scrollbar_style(self, colorname=DEFAULT):
        \"\"\"Create a standard style for the ttk.Scrollbar widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"TScrollbar\"

        if any([colorname == DEFAULT, colorname == \"\"]):
            h_ttkstyle = f\"Horizontal.{STYLE}\"
            v_ttkstyle = f\"Vertical.{STYLE}\"

            if self.is_light_theme:
                background = self.colors.border
            else:
                background = self.colors.selectbg

        else:
            h_ttkstyle = f\"{colorname}.Horizontal.{STYLE}\"
            v_ttkstyle = f\"{colorname}.Vertical.{STYLE}\"
            background = self.colors.get(colorname)

        if self.is_light_theme:
            if colorname == LIGHT:
                troughcolor = self.colors.bg
            else:
                troughcolor = self.colors.light
        else:
            troughcolor = Colors.update_hsv(self.colors.selectbg, vd=-0.2)

        pressed = Colors.update_hsv(background, vd=-0.05)
        active = Colors.update_hsv(background, vd=0.05)

        scroll_images = self.create_scrollbar_assets(
            background, pressed, active
        )

        # horizontal scrollbar
        self.style._build_configure(
            h_ttkstyle,
            troughcolor=troughcolor,
            darkcolor=troughcolor,
            bordercolor=troughcolor,
            lightcolor=troughcolor,
            arrowcolor=background,
            arrowsize=self.scale_size(11),
            background=troughcolor,
            relief=tk.FLAT,
            borderwidth=0,
        )
        self.style.element_create(
            f\"{h_ttkstyle}.thumb\",
            \"image\",
            scroll_images[0],
            (\"pressed\", scroll_images[1]),
            (\"active\", scroll_images[2]),
            border=(3, 0),
            sticky=tk.NSEW,
        )
        self.style.layout(
            h_ttkstyle,
            [
                (
                    \"Horizontal.Scrollbar.trough\",
                    {
                        \"sticky\": \"we\",
                        \"children\": [
                            (
                                \"Horizontal.Scrollbar.leftarrow\",
                                {\"side\": \"left\", \"sticky\": \"\"},
                            ),
                            (
                                \"Horizontal.Scrollbar.rightarrow\",
                                {\"side\": \"right\", \"sticky\": \"\"},
                            ),
                            (
                                f\"{h_ttkstyle}.thumb\",
                                {\"expand\": \"1\", \"sticky\": \"nswe\"},
                            ),
                        ],
                    },
                )
            ],
        )
        self.style._build_configure(h_ttkstyle, arrowcolor=background)
        self.style.map(
            h_ttkstyle, arrowcolor=[(\"pressed\", pressed), (\"active\", active)]
        )

        # vertical scrollbar
        self.style._build_configure(
            v_ttkstyle,
            troughcolor=troughcolor,
            darkcolor=troughcolor,
            bordercolor=troughcolor,
            lightcolor=troughcolor,
            arrowcolor=background,
            arrowsize=self.scale_size(11),
            background=troughcolor,
            relief=tk.FLAT,
            borderwidth=0,
        )
        self.style.element_create(
            f\"{v_ttkstyle}.thumb\",
            \"image\",
            scroll_images[3],
            (\"pressed\", scroll_images[4]),
            (\"active\", scroll_images[5]),
            border=(0, 3),
            sticky=tk.NSEW,
        )
        self.style.layout(
            v_ttkstyle,
            [
                (
                    \"Vertical.Scrollbar.trough\",
                    {
                        \"sticky\": \"ns\",
                        \"children\": [
                            (
                                \"Vertical.Scrollbar.uparrow\",
                                {\"side\": \"top\", \"sticky\": \"\"},
                            ),
                            (
                                \"Vertical.Scrollbar.downarrow\",
                                {\"side\": \"bottom\", \"sticky\": \"\"},
                            ),
                            (
                                f\"{v_ttkstyle}.thumb\",
                                {\"expand\": \"1\", \"sticky\": \"nswe\"},
                            ),
                        ],
                    },
                )
            ],
        )
        self.style._build_configure(v_ttkstyle, arrowcolor=background)
        self.style.map(
            v_ttkstyle, arrowcolor=[(\"pressed\", pressed), (\"active\", active)]
        )

        # register ttkstyles
        self.style._register_ttkstyle(h_ttkstyle)
        self.style._register_ttkstyle(v_ttkstyle)

    def create_spinbox_style(self, colorname=DEFAULT):
        \"\"\"Create a style for the ttk.Spinbox widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"TSpinbox\"

        if self.is_light_theme:
            disabled_fg = self.colors.border
            bordercolor = self.colors.border
            readonly = self.colors.light
        else:
            disabled_fg = self.colors.selectbg
            bordercolor = self.colors.selectbg
            readonly = bordercolor

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE
            focuscolor = self.colors.primary
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"
            focuscolor = self.colors.get(colorname)

        if all([colorname, colorname != DEFAULT]):
            bordercolor = focuscolor

        if colorname == \"light\":
            arrowfocus = self.colors.fg
        else:
            arrowfocus = focuscolor

        element = ttkstyle.replace(\".TS\", \".S\")
        self.style.element_create(f\"{element}.uparrow\", \"from\", TTK_DEFAULT)
        self.style.element_create(f\"{element}.downarrow\", \"from\", TTK_DEFAULT)
        self.style.layout(
            ttkstyle,
            [
                (
                    f\"{element}.field\",
                    {
                        \"side\": tk.TOP,
                        \"sticky\": tk.EW,
                        \"children\": [
                            (
                                \"null\",
                                {
                                    \"side\": tk.RIGHT,
                                    \"sticky\": \"\",
                                    \"children\": [
                                        (
                                            f\"{element}.uparrow\",
                                            {\"side\": tk.TOP, \"sticky\": tk.E},
                                        ),
                                        (
                                            f\"{element}.downarrow\",
                                            {
                                                \"side\": tk.BOTTOM,
                                                \"sticky\": tk.E,
                                            },
                                        ),
                                    ],
                                },
                            ),
                            (
                                f\"{element}.padding\",
                                {
                                    \"sticky\": tk.NSEW,
                                    \"children\": [
                                        (
                                            f\"{element}.textarea\",
                                            {\"sticky\": tk.NSEW},
                                        )
                                    ],
                                },
                            ),
                        ],
                    },
                )
            ],
        )
        self.style._build_configure(
            ttkstyle,
            bordercolor=bordercolor,
            darkcolor=self.colors.inputbg,
            lightcolor=self.colors.inputbg,
            fieldbackground=self.colors.inputbg,
            foreground=self.colors.inputfg,
            borderwidth=0,
            background=self.colors.inputbg,
            relief=tk.FLAT,
            arrowcolor=self.colors.inputfg,
            insertcolor=self.colors.inputfg,
            arrowsize=self.scale_size(12),
            padding=(10, 5),
        )
        self.style.map(
            ttkstyle,
            foreground=[(\"disabled\", disabled_fg)],
            fieldbackground=[(\"readonly\", readonly)],
            background=[(\"readonly\", readonly)],
            lightcolor=[
                (\"focus invalid\", self.colors.danger),
                (\"focus !disabled\", focuscolor),
                (\"readonly\", readonly),
            ],
            darkcolor=[
                (\"focus invalid\", self.colors.danger),
                (\"focus !disabled\", focuscolor),
                (\"readonly\", readonly),
            ],
            bordercolor=[
                (\"invalid\", self.colors.danger),
                (\"focus !disabled\", focuscolor),
                (\"hover !disabled\", focuscolor),
            ],
            arrowcolor=[
                (\"disabled !disabled\", disabled_fg),
                (\"pressed !disabled\", arrowfocus),
                (\"hover !disabled\", arrowfocus),
            ],
        )
        # register ttkstyles
        self.style._register_ttkstyle(ttkstyle)

    def create_table_treeview_style(self, colorname=DEFAULT):
        \"\"\"Create a style for the Tableview widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"Table.Treeview\"

        f = font.nametofont(\"TkDefaultFont\")
        rowheight = f.metrics()[\"linespace\"]

        if self.is_light_theme:
            disabled_fg = Colors.update_hsv(self.colors.inputbg, vd=-0.2)
            bordercolor = self.colors.border
            hover = Colors.update_hsv(self.colors.light, vd=-0.1)
        else:
            disabled_fg = Colors.update_hsv(self.colors.inputbg, vd=-0.3)
            bordercolor = self.colors.selectbg
            hover = Colors.update_hsv(self.colors.dark, vd=0.1)

        if any([colorname == DEFAULT, colorname == \"\"]):
            background = self.colors.inputbg
            foreground = self.colors.inputfg
            body_style = STYLE
            header_style = f\"{STYLE}.Heading\"
        elif colorname == LIGHT and self.is_light_theme:
            background = self.colors.get(colorname)
            foreground = self.colors.fg
            body_style = f\"{colorname}.{STYLE}\"
            header_style = f\"{colorname}.{STYLE}.Heading\"
            hover = Colors.update_hsv(background, vd=-0.1)
        else:
            background = self.colors.get(colorname)
            foreground = self.colors.selectfg
            body_style = f\"{colorname}.{STYLE}\"
            header_style = f\"{colorname}.{STYLE}.Heading\"
            hover = Colors.update_hsv(background, vd=0.1)


        # treeview header
        self.style._build_configure(
            header_style,
            background=background,
            foreground=foreground,
            relief=RAISED,
            borderwidth=1,
            darkcolor=background,
            bordercolor=bordercolor,
            lightcolor=background,
            padding=5,
        )
        self.style.map(
            header_style,
            foreground=[(\"disabled\", disabled_fg)],
            background=[
                (\"active !disabled\", hover),
            ],
            darkcolor=[
                (\"active !disabled\", hover),
            ],
            lightcolor=[
                (\"active !disabled\", hover),
            ],
        )
        self.style._build_configure(
            body_style,
            background=self.colors.inputbg,
            fieldbackground=self.colors.inputbg,
            foreground=self.colors.inputfg,
            bordercolor=bordercolor,
            lightcolor=self.colors.inputbg,
            darkcolor=self.colors.inputbg,
            borderwidth=2,
            padding=0,
            rowheight=rowheight,
            relief=tk.RAISED,
        )
        self.style.map(
            body_style,
            background=[(\"selected\", self.colors.selectbg)],
            foreground=[
                (\"disabled\", disabled_fg),
                (\"selected\", self.colors.selectfg),
            ],
        )
        self.style.layout(
            body_style,
            [
                (
                    \"Button.border\",
                    {
                        \"sticky\": tk.NSEW,
                        \"border\": \"1\",
                        \"children\": [
                            (
                                \"Treeview.padding\",
                                {
                                    \"sticky\": tk.NSEW,
                                    \"children\": [
                                        (
                                            \"Treeview.treearea\",
                                            {\"sticky\": tk.NSEW},
                                        )
                                    ],
                                },
                            )
                        ],
                    },
                )
            ],
        )
        # register ttkstyles
        self.style._register_ttkstyle(body_style)

    def create_treeview_style(self, colorname=DEFAULT):
        \"\"\"Create a style for the ttk.Treeview widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"Treeview\"

        f = font.nametofont(\"TkDefaultFont\")
        rowheight = f.metrics()[\"linespace\"]

        if self.is_light_theme:
            disabled_fg = Colors.update_hsv(self.colors.inputbg, vd=-0.2)
            bordercolor = self.colors.border
        else:
            disabled_fg = Colors.update_hsv(self.colors.inputbg, vd=-0.3)
            bordercolor = self.colors.selectbg

        if any([colorname == DEFAULT, colorname == \"\"]):
            background = self.colors.inputbg
            foreground = self.colors.inputfg
            body_style = STYLE
            header_style = f\"{STYLE}.Heading\"
            focuscolor = self.colors.primary
        elif colorname == LIGHT and self.is_light_theme:
            background = self.colors.get(colorname)
            foreground = self.colors.fg
            body_style = f\"{colorname}.{STYLE}\"
            header_style = f\"{colorname}.{STYLE}.Heading\"
            focuscolor = background
            bordercolor = focuscolor
        else:
            background = self.colors.get(colorname)
            foreground = self.colors.selectfg
            body_style = f\"{colorname}.{STYLE}\"
            header_style = f\"{colorname}.{STYLE}.Heading\"
            focuscolor = background
            bordercolor = focuscolor

        # treeview header
        self.style._build_configure(
            header_style,
            background=background,
            foreground=foreground,
            relief=tk.FLAT,
            padding=5,
        )
        self.style.map(
            header_style,
            foreground=[(\"disabled\", disabled_fg)],
            bordercolor=[(\"focus !disabled\", background)],
        )
        # treeview body
        self.style._build_configure(
            body_style,
            background=self.colors.inputbg,
            fieldbackground=self.colors.inputbg,
            foreground=self.colors.inputfg,
            bordercolor=bordercolor,
            lightcolor=self.colors.inputbg,
            darkcolor=self.colors.inputbg,
            borderwidth=2,
            padding=0,
            rowheight=rowheight,
            relief=tk.RAISED,
        )
        self.style.map(
            body_style,
            background=[(\"selected\", self.colors.selectbg)],
            foreground=[
                (\"disabled\", disabled_fg),
                (\"selected\", self.colors.selectfg),
            ],
            bordercolor=[
                (\"disabled\", bordercolor),
                (\"focus\", focuscolor),
                (\"pressed\", focuscolor),
                (\"hover\", focuscolor),
            ],
            lightcolor=[(\"focus\", focuscolor)],
            darkcolor=[(\"focus\", focuscolor)],
        )
        self.style.layout(
            body_style,
            [
                (
                    \"Button.border\",
                    {
                        \"sticky\": tk.NSEW,
                        \"border\": \"1\",
                        \"children\": [
                            (
                                \"Treeview.padding\",
                                {
                                    \"sticky\": tk.NSEW,
                                    \"children\": [
                                        (
                                            \"Treeview.treearea\",
                                            {\"sticky\": tk.NSEW},
                                        )
                                    ],
                                },
                            )
                        ],
                    },
                )
            ],
        )

        try:
            self.style.element_create(\"Treeitem.indicator\", \"from\", TTK_ALT)
        except:
            pass

        # register ttkstyles
        self.style._register_ttkstyle(body_style)

    def create_frame_style(self, colorname=DEFAULT):
        \"\"\"Create a style for the ttk.Frame widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"TFrame\"

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE
            background = self.colors.bg
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"
            background = self.colors.get(colorname)

        self.style._build_configure(ttkstyle, background=background)

        # register style
        self.style._register_ttkstyle(ttkstyle)

    def create_button_style(self, colorname=DEFAULT):
        \"\"\"Create a solid style for the ttk.Button widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"TButton\"

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE
            foreground = self.colors.get_foreground(PRIMARY)
            background = self.colors.primary
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"
            foreground = self.colors.get_foreground(colorname)
            background = self.colors.get(colorname)

        bordercolor = background
        disabled_bg = Colors.make_transparent(0.10, self.colors.fg, self.colors.bg)
        disabled_fg = Colors.make_transparent(0.30, self.colors.fg, self.colors.bg)
        pressed = Colors.make_transparent(0.80, background, self.colors.bg)
        hover = Colors.make_transparent(0.90, background, self.colors.bg)        

        self.style._build_configure(
            ttkstyle,
            foreground=foreground,
            background=background,
            bordercolor=bordercolor,
            darkcolor=background,
            lightcolor=background,
            relief=tk.RAISED,
            focusthickness=0,
            focuscolor=foreground,
            padding=(10, 5),
            anchor=tk.CENTER,
        )
        self.style.map(
            ttkstyle,
            foreground=[(\"disabled\", disabled_fg)],
            background=[
                (\"disabled\", disabled_bg),
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            bordercolor=[(\"disabled\", disabled_bg)],
            darkcolor=[
                (\"disabled\", disabled_bg),
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            lightcolor=[
                (\"disabled\", disabled_bg),
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_outline_button_style(self, colorname=DEFAULT):
        \"\"\"Create an outline style for the ttk.Button widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"Outline.TButton\"

        disabled_fg = Colors.make_transparent(0.30, self.colors.fg, self.colors.bg)

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE
            colorname = PRIMARY
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"

        foreground = self.colors.get(colorname)
        background = self.colors.get_foreground(colorname)
        foreground_pressed = background
        bordercolor = foreground
        pressed = foreground
        hover = foreground

        self.style._build_configure(
            ttkstyle,
            foreground=foreground,
            background=self.colors.bg,
            bordercolor=bordercolor,
            darkcolor=self.colors.bg,
            lightcolor=self.colors.bg,
            relief=tk.RAISED,
            focusthickness=0,
            focuscolor=foreground,
            padding=(10, 5),
            anchor=tk.CENTER,
        )
        self.style.map(
            ttkstyle,
            foreground=[
                (\"disabled\", disabled_fg),
                (\"pressed !disabled\", foreground_pressed),
                (\"hover !disabled\", foreground_pressed),
            ],
            background=[
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            bordercolor=[
                (\"disabled\", disabled_fg),
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            focuscolor=[
                (\"pressed !disabled\", foreground_pressed),
                (\"hover !disabled\", foreground_pressed),
            ],
            darkcolor=[
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            lightcolor=[
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_link_button_style(self, colorname=DEFAULT):
        \"\"\"Create a link button style for the ttk.Button widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"Link.TButton\"

        pressed = self.colors.info
        hover = self.colors.info

        if any([colorname == DEFAULT, colorname == \"\"]):
            foreground = self.colors.fg
            ttkstyle = STYLE
        elif colorname == LIGHT:
            foreground = self.colors.fg
            ttkstyle = f\"{colorname}.{STYLE}\"
        else:
            foreground = self.colors.get(colorname)
            ttkstyle = f\"{colorname}.{STYLE}\"

        disabled_fg = Colors.make_transparent(0.30, self.colors.fg, self.colors.bg)  

        self.style._build_configure(
            ttkstyle,
            foreground=foreground,
            background=self.colors.bg,
            bordercolor=self.colors.bg,
            darkcolor=self.colors.bg,
            lightcolor=self.colors.bg,
            relief=tk.RAISED,
            focusthickness=0,
            focuscolor=foreground,
            anchor=tk.CENTER,
            padding=(10, 5),
        )
        self.style.map(
            ttkstyle,
            shiftrelief=[(\"pressed !disabled\", -1)],
            foreground=[
                (\"disabled\", disabled_fg),
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            focuscolor=[
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", pressed),
            ],
            background=[
                (\"disabled\", self.colors.bg),
                (\"pressed !disabled\", self.colors.bg),
                (\"hover !disabled\", self.colors.bg),
            ],
            bordercolor=[
                (\"disabled\", self.colors.bg),
                (\"pressed !disabled\", self.colors.bg),
                (\"hover !disabled\", self.colors.bg),
            ],
            darkcolor=[
                (\"disabled\", self.colors.bg),
                (\"pressed !disabled\", self.colors.bg),
                (\"hover !disabled\", self.colors.bg),
            ],
            lightcolor=[
                (\"disabled\", self.colors.bg),
                (\"pressed !disabled\", self.colors.bg),
                (\"hover !disabled\", self.colors.bg),
            ],
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_square_toggle_assets(self, colorname=DEFAULT):
        \"\"\"Create the image assets used to build a square toggle
        style.

        Parameters:

            colorname (str):
                The color label used to style the widget.

        Returns:

            Tuple[str]:
                A tuple of PhotoImage names.
        \"\"\"
        size = self.scale_size([24, 15])
        if any([colorname == DEFAULT, colorname == \"\"]):
            colorname = PRIMARY

        # set default style color values
        prime_color = self.colors.get(colorname)
        on_border = prime_color
        on_indicator = self.colors.selectfg
        on_fill = prime_color
        off_fill = self.colors.bg
        disabled_fg = Colors.make_transparent(0.3, self.colors.fg, self.colors.bg)  
        off_border = Colors.make_transparent(0.4, self.colors.fg, self.colors.bg)
        off_indicator = Colors.make_transparent(0.4, self.colors.fg, self.colors.bg)     

        # override defaults for light and dark colors
        if colorname == LIGHT:
            on_border = self.colors.dark
            on_indicator = on_border
        elif colorname == DARK:
            on_border = self.colors.light
            on_indicator = on_border

        # toggle off
        _off = Image.new(\"RGBA\", (226, 130))
        draw = ImageDraw.Draw(_off)
        draw.rectangle(
            xy=[1, 1, 225, 129], outline=off_border, width=6, fill=off_fill
        )
        draw.rectangle([18, 18, 110, 110], fill=off_indicator)

        off_img = ImageTk.PhotoImage(_off.resize(size, Image.LANCZOS))
        off_name = util.get_image_name(off_img)
        self.theme_images[off_name] = off_img

        # toggle on
        toggle_on = Image.new(\"RGBA\", (226, 130))
        draw = ImageDraw.Draw(toggle_on)
        draw.rectangle(
            xy=[1, 1, 225, 129], outline=on_border, width=6, fill=on_fill
        )
        draw.rectangle([18, 18, 110, 110], fill=on_indicator)
        _on = toggle_on.transpose(Image.ROTATE_180)
        on_img = ImageTk.PhotoImage(_on.resize(size, Image.LANCZOS))
        on_name = util.get_image_name(on_img)
        self.theme_images[on_name] = on_img

        # toggle disabled
        _disabled = Image.new(\"RGBA\", (226, 130))
        draw = ImageDraw.Draw(_disabled)
        draw.rectangle([1, 1, 225, 129], outline=disabled_fg, width=6)
        draw.rectangle([18, 18, 110, 110], fill=disabled_fg)
        disabled_img = ImageTk.PhotoImage(
            _disabled.resize(size, Image.LANCZOS)
        )
        disabled_name = util.get_image_name(disabled_img)
        self.theme_images[disabled_name] = disabled_img

        # toggle on / disabled
        toggle_on_disabled = Image.new(\"RGBA\", (226, 130))
        draw = ImageDraw.Draw(toggle_on_disabled)
        draw.rectangle(
            xy=[1, 1, 225, 129], outline=disabled_fg, width=6, fill=off_fill
        )
        draw.rectangle([18, 18, 110, 110], fill=disabled_fg)
        _on_disabled = toggle_on_disabled.transpose(Image.ROTATE_180)
        on_dis_img = ImageTk.PhotoImage(_on_disabled.resize(size, Image.LANCZOS))
        on_disabled_name = util.get_image_name(on_dis_img)
        self.theme_images[on_disabled_name] = on_dis_img


        return off_name, on_name, disabled_name, on_disabled_name

    def create_toggle_style(self, colorname=DEFAULT):
        \"\"\"Create a round toggle style for the ttk.Checkbutton widget.

        Parameters:

            colorname (str):
        \"\"\"
        self.create_round_toggle_style(colorname)

    def create_round_toggle_assets(self, colorname=DEFAULT):
        \"\"\"Create image assets for the round toggle style.

        Parameters:

            colorname (str):
                The color label assigned to the colors property.

        Returns:

            Tuple[str]:
                A tuple of PhotoImage names.
        \"\"\"
        size = self.scale_size([24, 15])

        if any([colorname == DEFAULT, colorname == \"\"]):
            colorname = PRIMARY

        # set default style color values
        prime_color = self.colors.get(colorname)
        on_border = prime_color
        on_indicator = self.colors.selectfg
        on_fill = prime_color
        off_fill = self.colors.bg

        disabled_fg = Colors.make_transparent(0.3, self.colors.fg, self.colors.bg)  
        off_border = Colors.make_transparent(0.4, self.colors.fg, self.colors.bg)
        off_indicator = Colors.make_transparent(0.4, self.colors.fg, self.colors.bg)  

        # override defaults for light and dark colors
        if colorname == LIGHT:
            on_border = self.colors.dark
            on_indicator = on_border
        elif colorname == DARK:
            on_border = self.colors.light
            on_indicator = on_border

        # toggle off
        _off = Image.new(\"RGBA\", (226, 130))
        draw = ImageDraw.Draw(_off)
        draw.rounded_rectangle(
            xy=[1, 1, 225, 129],
            radius=(128 / 2),
            outline=off_border,
            width=6,
            fill=off_fill,
        )
        draw.ellipse([20, 18, 112, 110], fill=off_indicator)
        off_img = ImageTk.PhotoImage(_off.resize(size, Image.LANCZOS))
        off_name = util.get_image_name(off_img)
        self.theme_images[off_name] = off_img

        # toggle on
        _on = Image.new(\"RGBA\", (226, 130))
        draw = ImageDraw.Draw(_on)
        draw.rounded_rectangle(
            xy=[1, 1, 225, 129],
            radius=(128 / 2),
            outline=on_border,
            width=6,
            fill=on_fill,
        )
        draw.ellipse([20, 18, 112, 110], fill=on_indicator)
        _on = _on.transpose(Image.ROTATE_180)
        on_img = ImageTk.PhotoImage(_on.resize(size, Image.LANCZOS))
        on_name = util.get_image_name(on_img)
        self.theme_images[on_name] = on_img

        # toggle on / disabled
        _on_disabled = Image.new(\"RGBA\", (226, 130))
        draw = ImageDraw.Draw(_on_disabled)
        draw.rounded_rectangle(
            xy=[1, 1, 225, 129],
            radius=(128 / 2),
            outline=disabled_fg,
            width=6,
            fill=off_fill,
        )
        draw.ellipse([20, 18, 112, 110], fill=disabled_fg)
        _on_disabled = _on_disabled.transpose(Image.ROTATE_180)
        on_dis_img = ImageTk.PhotoImage(_on_disabled.resize(size, Image.LANCZOS))
        on_disabled_name = util.get_image_name(on_dis_img)
        self.theme_images[on_disabled_name] = on_dis_img        

        # toggle disabled
        _disabled = Image.new(\"RGBA\", (226, 130))
        draw = ImageDraw.Draw(_disabled)
        draw.rounded_rectangle(
            xy=[1, 1, 225, 129], radius=(128 / 2), outline=disabled_fg, width=6
        )
        draw.ellipse([20, 18, 112, 110], fill=disabled_fg)
        disabled_img = ImageTk.PhotoImage(
            _disabled.resize(size, Image.LANCZOS)
        )
        disabled_name = util.get_image_name(disabled_img)
        self.theme_images[disabled_name] = disabled_img

        return off_name, on_name, disabled_name, on_disabled_name

    def create_round_toggle_style(self, colorname=DEFAULT):
        \"\"\"Create a round toggle style for the ttk.Checkbutton widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"Round.Toggle\"

        disabled_fg = Colors.make_transparent(0.30, self.colors.fg, self.colors.bg)  

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE
            colorname = PRIMARY
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"

        # ( off, on, disabled )
        images = self.create_round_toggle_assets(colorname)

        try:
            width = self.scale_size(28)
            borderpad = self.scale_size(4)
            self.style.element_create(
                f\"{ttkstyle}.indicator\",
                \"image\",
                images[1],
                (\"disabled selected\", images[3]),
                (\"disabled\", images[2]),
                (\"!selected\", images[0]),
                width=width,
                border=borderpad,
                sticky=tk.W,
            )
        except:
            \"\"\"This method is used as the default Toggle style, so it
            is neccessary to catch Tcl Errors when it tries to create
            and element that was already created by the Toggle or
            Round Toggle style\"\"\"
            pass

        self.style._build_configure(
            ttkstyle,
            relief=tk.FLAT,
            borderwidth=0,
            padding=0,
            foreground=self.colors.fg,
            background=self.colors.bg,
        )
        self.style.map(
            ttkstyle,
            foreground=[(\"disabled\", disabled_fg)],
            background=[(\"selected\", self.colors.bg)],
        )
        self.style.layout(
            ttkstyle,
            [
                (
                    \"Toolbutton.border\",
                    {
                        \"sticky\": tk.NSEW,
                        \"children\": [
                            (
                                \"Toolbutton.padding\",
                                {
                                    \"sticky\": tk.NSEW,
                                    \"children\": [
                                        (
                                            f\"{ttkstyle}.indicator\",
                                            {\"side\": tk.LEFT},
                                        ),
                                        (
                                            \"Toolbutton.label\",
                                            {\"side\": tk.LEFT},
                                        ),
                                    ],
                                },
                            )
                        ],
                    },
                )
            ],
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_square_toggle_style(self, colorname=DEFAULT):
        \"\"\"Create a square toggle style for the ttk.Checkbutton widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"

        STYLE = \"Square.Toggle\"

        disabled_fg = Colors.make_transparent(0.30, self.colors.fg, self.colors.bg)  

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"

        # ( off, on, disabled )
        images = self.create_square_toggle_assets(colorname)

        width = self.scale_size(28)
        borderpad = self.scale_size(4)

        self.style.element_create(
            f\"{ttkstyle}.indicator\",
            \"image\",
            images[1],
            (\"disabled selected\", images[3]),
            (\"disabled\", images[2]),
            (\"!selected\", images[0]),
            width=width,
            border=borderpad,
            sticky=tk.W,
        )
        self.style.layout(
            ttkstyle,
            [
                (
                    \"Toolbutton.border\",
                    {
                        \"sticky\": tk.NSEW,
                        \"children\": [
                            (
                                \"Toolbutton.padding\",
                                {
                                    \"sticky\": tk.NSEW,
                                    \"children\": [
                                        (
                                            f\"{ttkstyle}.indicator\",
                                            {\"side\": tk.LEFT},
                                        ),
                                        (
                                            \"Toolbutton.label\",
                                            {\"side\": tk.LEFT},
                                        ),
                                    ],
                                },
                            )
                        ],
                    },
                )
            ],
        )
        self.style._build_configure(
            ttkstyle, relief=tk.FLAT, borderwidth=0, foreground=self.colors.fg
        )
        self.style.map(
            ttkstyle,
            foreground=[(\"disabled\", disabled_fg)],
            background=[
                (\"selected\", self.colors.bg),
                (\"!selected\", self.colors.bg),
            ],
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_toolbutton_style(self, colorname=DEFAULT):
        \"\"\"Create a solid toolbutton style for the ttk.Checkbutton
        and ttk.Radiobutton widgets.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"Toolbutton\"

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE
            toggle_on = self.colors.primary
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"
            toggle_on = self.colors.get(colorname)

        foreground = self.colors.get_foreground(colorname)

        if self.is_light_theme:
            toggle_off = self.colors.border
        else:
            toggle_off = self.colors.selectbg

        disabled_bg = Colors.make_transparent(0.10, self.colors.fg, self.colors.bg)
        disabled_fg = Colors.make_transparent(0.30, self.colors.fg, self.colors.bg)

        self.style._build_configure(
            ttkstyle,
            foreground=self.colors.selectfg,
            background=toggle_off,
            bordercolor=toggle_off,
            darkcolor=toggle_off,
            lightcolor=toggle_off,
            relief=tk.RAISED,
            focusthickness=0,
            focuscolor=\"\",
            padding=(10, 5),
            anchor=tk.CENTER,
        )
        self.style.map(
            ttkstyle,
            foreground=[
                (\"disabled\", disabled_fg),
                (\"hover\", foreground),
                (\"selected\", foreground),
            ],
            background=[
                (\"disabled\", disabled_bg),
                (\"pressed !disabled\", toggle_on),
                (\"selected !disabled\", toggle_on),
                (\"hover !disabled\", toggle_on),
            ],
            bordercolor=[
                (\"disabled\", disabled_bg),
                (\"pressed !disabled\", toggle_on),
                (\"selected !disabled\", toggle_on),
                (\"hover !disabled\", toggle_on),
            ],
            darkcolor=[
                (\"disabled\", disabled_bg),
                (\"pressed !disabled\", toggle_on),
                (\"selected !disabled\", toggle_on),
                (\"hover !disabled\", toggle_on),
            ],
            lightcolor=[
                (\"disabled\", disabled_bg),
                (\"pressed !disabled\", toggle_on),
                (\"selected !disabled\", toggle_on),
                (\"hover !disabled\", toggle_on),
            ],
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_outline_toolbutton_style(self, colorname=DEFAULT):
        \"\"\"Create an outline toolbutton style for the ttk.Checkbutton
        and ttk.Radiobutton widgets.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"Outline.Toolbutton\"

        disabled_fg = Colors.make_transparent(0.30, self.colors.fg, self.colors.bg)   

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE
            colorname = PRIMARY
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"

        foreground = self.colors.get(colorname)
        background = self.colors.get_foreground(colorname)
        foreground_pressed = background
        bordercolor = foreground
        pressed = foreground
        hover = foreground

        self.style._build_configure(
            ttkstyle,
            foreground=foreground,
            background=self.colors.bg,
            bordercolor=bordercolor,
            darkcolor=self.colors.bg,
            lightcolor=self.colors.bg,
            relief=tk.RAISED,
            focusthickness=0,
            focuscolor=foreground,
            padding=(10, 5),
            anchor=tk.CENTER,
            arrowcolor=foreground,
            arrowpadding=(0, 0, 15, 0),
            arrowsize=3,
        )
        self.style.map(
            ttkstyle,
            foreground=[
                (\"disabled\", disabled_fg),
                (\"pressed !disabled\", foreground_pressed),
                (\"selected !disabled\", foreground_pressed),
                (\"hover !disabled\", foreground_pressed),
            ],
            background=[
                (\"pressed !disabled\", pressed),
                (\"selected !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            bordercolor=[
                (\"disabled\", disabled_fg),
                (\"pressed !disabled\", pressed),
                (\"selected !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            darkcolor=[
                (\"disabled\", self.colors.bg),
                (\"pressed !disabled\", pressed),
                (\"selected !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            lightcolor=[
                (\"disabled\", self.colors.bg),
                (\"pressed !disabled\", pressed),
                (\"selected !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_entry_style(self, colorname=DEFAULT):
        \"\"\"Create a style for the ttk.Entry widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"TEntry\"

        # general default colors
        if self.is_light_theme:
            disabled_fg = self.colors.border
            bordercolor = self.colors.border
            readonly = self.colors.light
        else:
            disabled_fg = self.colors.selectbg
            bordercolor = self.colors.selectbg
            readonly = bordercolor

        if any([colorname == DEFAULT, not colorname]):
            # default style
            ttkstyle = STYLE
            focuscolor = self.colors.primary
        else:
            # colored style
            ttkstyle = f\"{colorname}.{STYLE}\"
            focuscolor = self.colors.get(colorname)
            bordercolor = focuscolor

        self.style._build_configure(
            ttkstyle,
            bordercolor=bordercolor,
            darkcolor=self.colors.inputbg,
            lightcolor=self.colors.inputbg,
            fieldbackground=self.colors.inputbg,
            foreground=self.colors.inputfg,
            insertcolor=self.colors.inputfg,
            padding=5,
        )
        self.style.map(
            ttkstyle,
            foreground=[(\"disabled\", disabled_fg)],
            fieldbackground=[(\"readonly\", readonly)],
            bordercolor=[
                (\"invalid\", self.colors.danger),
                (\"focus !disabled\", focuscolor),
                (\"hover !disabled\", focuscolor),
            ],
            lightcolor=[
                (\"focus invalid\", self.colors.danger),
                (\"focus !disabled\", focuscolor),
                (\"readonly\", readonly),
            ],
            darkcolor=[
                (\"focus invalid\", self.colors.danger),
                (\"focus !disabled\", focuscolor),
                (\"readonly\", readonly),
            ],
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_radiobutton_assets(self, colorname=DEFAULT):
        \"\"\"Create the image assets used to build the radiobutton style.

        Parameters:

            colorname (str):

        Returns:

            Tuple[str]:
                A tuple of PhotoImage names
        \"\"\"
        prime_color = self.colors.get(colorname)
        on_fill = prime_color
        off_fill = self.colors.bg
        on_indicator = self.colors.selectfg
        size = self.scale_size([14, 14])
        off_border = Colors.make_transparent(0.4, self.colors.fg, self.colors.bg)
        disabled = Colors.make_transparent(0.3, self.colors.fg, self.colors.bg)

        if self.is_light_theme:
            if colorname == LIGHT:
                on_indicator = self.colors.dark

        # radio off
        _off = Image.new(\"RGBA\", (134, 134))
        draw = ImageDraw.Draw(_off)
        draw.ellipse(
            xy=[1, 1, 133, 133], outline=off_border, width=6, fill=off_fill
        )
        off_img = ImageTk.PhotoImage(_off.resize(size, Image.LANCZOS))
        off_name = util.get_image_name(off_img)
        self.theme_images[off_name] = off_img

        # radio on
        _on = Image.new(\"RGBA\", (134, 134))
        draw = ImageDraw.Draw(_on)
        if colorname == LIGHT and self.is_light_theme:
            draw.ellipse(xy=[1, 1, 133, 133], outline=off_border, width=6)
        else:
            draw.ellipse(xy=[1, 1, 133, 133], fill=on_fill)
        draw.ellipse([40, 40, 94, 94], fill=on_indicator)
        on_img = ImageTk.PhotoImage(_on.resize(size, Image.LANCZOS))
        on_name = util.get_image_name(on_img)
        self.theme_images[on_name] = on_img

        # radio on/disabled
        _on_dis = Image.new(\"RGBA\", (134, 134))
        draw = ImageDraw.Draw(_on_dis)
        if colorname == LIGHT and self.is_light_theme:
            draw.ellipse(xy=[1, 1, 133, 133], outline=off_border, width=6)
        else:
            draw.ellipse(xy=[1, 1, 133, 133], fill=disabled)
        draw.ellipse([40, 40, 94, 94], fill=off_fill)
        on_dis_img = ImageTk.PhotoImage(_on_dis.resize(size, Image.LANCZOS))
        on_disabled_name = util.get_image_name(on_dis_img)
        self.theme_images[on_disabled_name] = on_dis_img        

        # radio disabled
        _disabled = Image.new(\"RGBA\", (134, 134))
        draw = ImageDraw.Draw(_disabled)
        draw.ellipse(
            xy=[1, 1, 133, 133], outline=disabled, width=3, fill=off_fill
        )
        disabled_img = ImageTk.PhotoImage(
            _disabled.resize(size, Image.LANCZOS)
        )
        disabled_name = util.get_image_name(disabled_img)
        self.theme_images[disabled_name] = disabled_img

        return off_name, on_name, disabled_name, on_disabled_name

    def create_radiobutton_style(self, colorname=DEFAULT):
        \"\"\"Create a style for the ttk.Radiobutton widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"

        STYLE = \"TRadiobutton\"

        disabled_fg = Colors.make_transparent(0.30, self.colors.fg, self.colors.bg)

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE
            colorname = PRIMARY
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"

        # ( off, on, disabled )
        images = self.create_radiobutton_assets(colorname)
        width = self.scale_size(20)
        borderpad = self.scale_size(4)
        self.style.element_create(
            f\"{ttkstyle}.indicator\",
            \"image\",
            images[1],
            (\"disabled selected\", images[3]),
            (\"disabled\", images[2]),
            (\"!selected\", images[0]),
            width=width,
            border=borderpad,
            sticky=tk.W,
        )
        self.style.map(ttkstyle, foreground=[(\"disabled\", disabled_fg)])
        self.style._build_configure(ttkstyle)
        self.style.layout(
            ttkstyle,
            [
                (
                    \"Radiobutton.padding\",
                    {
                        \"children\": [
                            (
                                f\"{ttkstyle}.indicator\",
                                {\"side\": tk.LEFT, \"sticky\": \"\"},
                            ),
                            (
                                \"Radiobutton.focus\",
                                {
                                    \"children\": [
                                        (
                                            \"Radiobutton.label\",
                                            {\"sticky\": tk.NSEW},
                                        )
                                    ],
                                    \"side\": tk.LEFT,
                                    \"sticky\": \"\",
                                },
                            ),
                        ],
                        \"sticky\": tk.NSEW,
                    },
                )
            ],
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_date_button_assets(self, foreground):
        \"\"\"Create the image assets used to build the date button
        style. This button style applied to the button in the
        ttkbootstrap.widgets.DateEntry.

        Parameters:

            foreground (str):
                The color value used to draw the calendar image.

        Returns:

            str:
                The PhotoImage name.
        \"\"\"
        fill = foreground
        image = Image.new(\"RGBA\", (210, 220))
        draw = ImageDraw.Draw(image)

        draw.rounded_rectangle(
            [10, 30, 200, 210], radius=20, outline=fill, width=10
        )

        calendar_image_coordinates = [
            # page spirals
            [40, 10, 50, 50],
            [100, 10, 110, 50],
            [160, 10, 170, 50],
            # row 1
            [70, 90, 90, 110],
            [110, 90, 130, 110],
            [150, 90, 170, 110],
            # row 2
            [30, 130, 50, 150],
            [70, 130, 90, 150],
            [110, 130, 130, 150],
            [150, 130, 170, 150],
            # row 3
            [30, 170, 50, 190],
            [70, 170, 90, 190],
            [110, 170, 130, 190],
        ]
        for xy in calendar_image_coordinates:
            draw.rectangle(xy=xy, fill=fill)

        size = self.scale_size([21, 22])
        tk_img = ImageTk.PhotoImage(image.resize(size, Image.LANCZOS))
        tk_name = util.get_image_name(tk_img)
        self.theme_images[tk_name] = tk_img
        return tk_name

    def create_date_button_style(self, colorname=DEFAULT):
        \"\"\"Create a date button style for the ttk.Button widget.

        Parameters:

            colorname (str):
                The color label used to style widget.
        \"\"\"
        STYLE = \"Date.TButton\"

        if self.is_light_theme:
            disabled_fg = self.colors.border
        else:
            disabled_fg = self.colors.selectbg

        btn_foreground = Colors.get_foreground(self.colors, colorname)

        img_normal = self.create_date_button_assets(btn_foreground)

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE
            foreground = self.colors.get_foreground(PRIMARY)
            background = self.colors.primary
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"
            foreground = self.colors.get_foreground(colorname)
            background = self.colors.get(colorname)

        pressed = Colors.update_hsv(background, vd=-0.1)
        hover = Colors.update_hsv(background, vd=0.10)

        self.style._build_configure(
            ttkstyle,
            foreground=foreground,
            background=background,
            bordercolor=background,
            darkcolor=background,
            lightcolor=background,
            relief=tk.RAISED,
            focusthickness=0,
            focuscolor=foreground,
            padding=(2, 2),
            anchor=tk.CENTER,
            image=img_normal,
        )
        self.style.map(
            ttkstyle,
            foreground=[(\"disabled\", disabled_fg)],
            background=[
                (\"disabled\", disabled_fg),
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            bordercolor=[(\"disabled\", disabled_fg)],
            darkcolor=[
                (\"disabled\", disabled_fg),
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            lightcolor=[
                (\"disabled\", disabled_fg),
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
        )

        self.style._register_ttkstyle(ttkstyle)

    def create_calendar_style(self, colorname=DEFAULT):
        \"\"\"Create a style for the
        ttkbootstrap.dialogs.DatePickerPopup widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"

        STYLE = \"TCalendar\"

        if any([colorname == DEFAULT, colorname == \"\"]):
            prime_color = self.colors.primary
            ttkstyle = STYLE
            chevron_style = \"Chevron.TButton\"
        else:
            prime_color = self.colors.get(colorname)
            ttkstyle = f\"{colorname}.{STYLE}\"
            chevron_style = f\"Chevron.{colorname}.TButton\"

        if self.is_light_theme:
            disabled_fg = Colors.update_hsv(self.colors.inputbg, vd=-0.2)
            pressed = Colors.update_hsv(prime_color, vd=-0.1)
        else:
            disabled_fg = Colors.update_hsv(self.colors.inputbg, vd=-0.3)
            pressed = Colors.update_hsv(prime_color, vd=0.1)

        self.style._build_configure(
            ttkstyle,
            foreground=self.colors.fg,
            background=self.colors.bg,
            bordercolor=self.colors.bg,
            darkcolor=self.colors.bg,
            lightcolor=self.colors.bg,
            relief=tk.RAISED,
            focusthickness=0,
            focuscolor=\"\",
            borderwidth=1,
            padding=(10, 5),
            anchor=tk.CENTER,
        )
        self.style.layout(
            ttkstyle,
            [
                (
                    \"Toolbutton.border\",
                    {
                        \"sticky\": tk.NSEW,
                        \"children\": [
                            (
                                \"Toolbutton.padding\",
                                {
                                    \"sticky\": tk.NSEW,
                                    \"children\": [
                                        (
                                            \"Toolbutton.label\",
                                            {\"sticky\": tk.NSEW},
                                        )
                                    ],
                                },
                            )
                        ],
                    },
                )
            ],
        )
        self.style.map(
            ttkstyle,
            foreground=[
                (\"disabled\", disabled_fg),
                (\"pressed !disabled\", self.colors.selectfg),
                (\"selected !disabled\", self.colors.selectfg),
                (\"hover !disabled\", self.colors.selectfg),
            ],
            background=[
                (\"pressed !disabled\", pressed),
                (\"selected !disabled\", pressed),
                (\"hover !disabled\", pressed),
            ],
            bordercolor=[
                (\"disabled\", disabled_fg),
                (\"pressed !disabled\", pressed),
                (\"selected !disabled\", pressed),
                (\"hover !disabled\", pressed),
            ],
            darkcolor=[
                (\"pressed !disabled\", pressed),
                (\"selected !disabled\", pressed),
                (\"hover !disabled\", pressed),
            ],
            lightcolor=[
                (\"pressed !disabled\", pressed),
                (\"selected !disabled\", pressed),
                (\"hover !disabled\", pressed),
            ],
        )
        self.style._build_configure(
            chevron_style, font=\"-size 14\", focuscolor=\"\"
        )

        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)
        self.style._register_ttkstyle(chevron_style)

    def create_metersubtxt_label_style(self, colorname=DEFAULT):
        \"\"\"Create a subtext label style for the
        ttkbootstrap.widgets.Meter widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"Metersubtxt.TLabel\"

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE
            if self.is_light_theme:
                foreground = self.colors.secondary
            else:
                foreground = self.colors.light
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"
            foreground = self.colors.get(colorname)

        background = self.colors.bg

        self.style._build_configure(
            ttkstyle, foreground=foreground, background=background
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_meter_label_style(self, colorname=DEFAULT):
        \"\"\"Create a label style for the
        ttkbootstrap.widgets.Meter widget. This style also stores some
        metadata that is called by the Meter class to lookup relevant
        colors for the trough and bar when the new image is drawn.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"

        STYLE = \"Meter.TLabel\"

        # text color = `foreground`
        # trough color = `space`

        if self.is_light_theme:
            if colorname == LIGHT:
                troughcolor = self.colors.bg
            else:
                troughcolor = self.colors.light
        else:
            troughcolor = Colors.update_hsv(self.colors.selectbg, vd=-0.2)

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE
            background = self.colors.bg
            textcolor = self.colors.primary
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"
            textcolor = self.colors.get(colorname)
            background = self.colors.bg

        self.style._build_configure(
            ttkstyle,
            foreground=textcolor,
            background=background,
            space=troughcolor,
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_label_style(self, colorname=DEFAULT):
        \"\"\"Create a standard style for the ttk.Label widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"TLabel\"

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE
            foreground = self.colors.fg
            background = self.colors.bg
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"
            foreground = self.colors.get(colorname)
            background = self.colors.bg

        # standard label
        self.style._build_configure(
            ttkstyle, foreground=foreground, background=background
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_inverse_label_style(self, colorname=DEFAULT):
        \"\"\"Create an inverted style for the ttk.Label.

        The foreground and background are inverted versions of that
        used in the standard label style.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE_INVERSE = \"Inverse.TLabel\"

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE_INVERSE
            background = self.colors.fg
            foreground = self.colors.bg
        else:
            ttkstyle = f\"{colorname}.{STYLE_INVERSE}\"
            background = self.colors.get(colorname)
            foreground = self.colors.get_foreground(colorname)

        self.style._build_configure(
            ttkstyle, foreground=foreground, background=background
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_labelframe_style(self, colorname=DEFAULT):
        \"\"\"Create a style for the ttk.Labelframe widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"TLabelframe\"

        background = self.colors.bg

        if any([colorname == DEFAULT, colorname == \"\"]):
            foreground = self.colors.fg
            ttkstyle = STYLE

            if self.is_light_theme:
                bordercolor = self.colors.border
            else:
                bordercolor = self.colors.selectbg

        else:
            foreground = self.colors.get(colorname)
            bordercolor = foreground
            ttkstyle = f\"{colorname}.{STYLE}\"

        # create widget style
        self.style._build_configure(
            f\"{ttkstyle}.Label\",
            foreground=foreground,
            background=background,
        )
        self.style._build_configure(
            ttkstyle,
            relief=tk.RAISED,
            borderwidth=1,
            bordercolor=bordercolor,
            lightcolor=background,
            darkcolor=background,
            background=background,
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_checkbutton_style(self, colorname=DEFAULT):
        \"\"\"Create a standard style for the ttk.Checkbutton widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"TCheckbutton\"

        disabled_fg = Colors.make_transparent(0.3, self.colors.fg, self.colors.bg)

        if any([colorname == DEFAULT, colorname == \"\"]):
            colorname = PRIMARY
            ttkstyle = STYLE
        else:
            ttkstyle = f\"{colorname}.TCheckbutton\"

        # ( off, on, disabled )
        images = self.create_checkbutton_assets(colorname)

        element = ttkstyle.replace(\".TC\", \".C\")
        width = self.scale_size(20)
        borderpad = self.scale_size(4)
        self.style.element_create(
            f\"{element}.indicator\",
            \"image\",
            images[1],
            (\"disabled selected\", images[4]),
            (\"disabled alternate\", images[5]),
            (\"disabled\", images[2]),
            (\"alternate\", images[3]),
            (\"!selected\", images[0]),
            width=width,
            border=borderpad,
            sticky=tk.W,
        )
        self.style._build_configure(ttkstyle, foreground=self.colors.fg)
        self.style.map(ttkstyle, foreground=[(\"disabled\", disabled_fg)])
        self.style.layout(
            ttkstyle,
            [
                (
                    \"Checkbutton.padding\",
                    {
                        \"children\": [
                            (
                                f\"{element}.indicator\",
                                {\"side\": tk.LEFT, \"sticky\": \"\"},
                            ),
                            (
                                \"Checkbutton.focus\",
                                {
                                    \"children\": [
                                        (
                                            \"Checkbutton.label\",
                                            {\"sticky\": tk.NSEW},
                                        )
                                    ],
                                    \"side\": tk.LEFT,
                                    \"sticky\": \"\",
                                },
                            ),
                        ],
                        \"sticky\": tk.NSEW,
                    },
                )
            ],
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_checkbutton_assets(self, colorname=DEFAULT):
        \"\"\"Create the image assets used to build the standard
        checkbutton style.

        Parameters:

            colorname (str):
                The color label used to style the widget.

        Returns:

            Tuple[str]:
                A tuple of PhotoImage names.
        \"\"\"
        # set platform specific checkfont
        winsys = self.style.tk.call(\"tk\", \"windowingsystem\")
        indicator = \"✓\"
        if winsys == \"win32\":
            # Windows font
            fnt = ImageFont.truetype(\"seguisym.ttf\", 120)
            font_offset = -20
            # TODO consider using ImageFont.getsize for offsets
        elif winsys == \"x11\":
            # Linux fonts
            try:
                # this should be available on most Linux distros
                fnt = ImageFont.truetype(\"FreeSerif.ttf\", 130)
                font_offset = 10
            except:
                try:
                    # this should be available as a backup on Linux 
                    # distros that don't have the FreeSerif.ttf file
                    fnt = ImageFont.truetype(\"DejaVuSans.ttf\", 160)
                    font_offset = -15
                except:
                    # If all else fails, use the default ImageFont
                    # this won't actually show anything in practice 
                    # because of how I'm scaling the image, but it 
                    # will prevent the program from crashing. I need 
                    # a better solution for a missing font
                    fnt = ImageFont.load_default()
                    font_offset = 0        
                    indicator = \"x\"
        else:
            # Mac OS font
            fnt = ImageFont.truetype(\"LucidaGrande.ttc\", 120)
            font_offset = -10

        prime_color = self.colors.get(colorname)
        on_border = prime_color
        on_fill = prime_color
        off_fill = self.colors.bg
        off_border = self.colors.selectbg
        off_border = Colors.make_transparent(0.4, self.colors.fg, self.colors.bg)
        disabled_fg = Colors.make_transparent(0.3, self.colors.fg, self.colors.bg)        

        if colorname == LIGHT:
            check_color = self.colors.dark
            on_border = check_color
        elif colorname == DARK:
            check_color = self.colors.light
            on_border = check_color
        else:
            check_color = self.colors.selectfg

        size = self.scale_size([14, 14])

        # checkbutton off
        checkbutton_off = Image.new(\"RGBA\", (134, 134))
        draw = ImageDraw.Draw(checkbutton_off)
        draw.rounded_rectangle(
            [2, 2, 132, 132],
            radius=16,
            outline=off_border,
            width=6,
            fill=off_fill,
        )
        off_img = ImageTk.PhotoImage(
            checkbutton_off.resize(size, Image.LANCZOS)
        )
        off_name = util.get_image_name(off_img)
        self.theme_images[off_name] = off_img

        # checkbutton on
        checkbutton_on = Image.new(\"RGBA\", (134, 134))
        draw = ImageDraw.Draw(checkbutton_on)
        draw.rounded_rectangle(
            [2, 2, 132, 132],
            radius=16,
            fill=on_fill,
            outline=on_border,
            width=3,
        )

        draw.text((20, font_offset), indicator, font=fnt, fill=check_color)
        on_img = ImageTk.PhotoImage(checkbutton_on.resize(size, Image.LANCZOS))
        on_name = util.get_image_name(on_img)
        self.theme_images[on_name] = on_img

       # checkbutton on/disabled
        checkbutton_on_disabled = Image.new(\"RGBA\", (134, 134))
        draw = ImageDraw.Draw(checkbutton_on_disabled)
        draw.rounded_rectangle(
            [2, 2, 132, 132],
            radius=16,
            fill=disabled_fg,
            outline=disabled_fg,
            width=3,
        )

        draw.text((20, font_offset), indicator, font=fnt, fill=off_fill)
        on_dis_img = ImageTk.PhotoImage(checkbutton_on_disabled.resize(size, Image.LANCZOS))
        on_dis_name = util.get_image_name(on_dis_img)
        self.theme_images[on_dis_name] = on_dis_img

        # checkbutton alt
        checkbutton_alt = Image.new(\"RGBA\", (134, 134))
        draw = ImageDraw.Draw(checkbutton_alt)
        draw.rounded_rectangle(
            [2, 2, 132, 132],
            radius=16,
            fill=on_fill,
            outline=on_border,
            width=3,
        )        
        draw.line([36, 67, 100, 67], fill=check_color, width=12)
        alt_img = ImageTk.PhotoImage(
            checkbutton_alt.resize(size, Image.LANCZOS)
        )
        alt_name = util.get_image_name(alt_img)
        self.theme_images[alt_name] = alt_img

        # checkbutton alt/disabled
        checkbutton_alt_disabled = Image.new(\"RGBA\", (134, 134))
        draw = ImageDraw.Draw(checkbutton_alt_disabled)
        draw.rounded_rectangle(
            [2, 2, 132, 132],
            radius=16,
            fill=disabled_fg,
            outline=disabled_fg,
            width=3,
        )        
        draw.line([36, 67, 100, 67], fill=off_fill, width=12)
        alt_dis_img = ImageTk.PhotoImage(
            checkbutton_alt_disabled.resize(size, Image.LANCZOS)
        )
        alt_dis_name = util.get_image_name(alt_dis_img)
        self.theme_images[alt_dis_name] = alt_dis_img        

        # checkbutton disabled
        checkbutton_disabled = Image.new(\"RGBA\", (134, 134))
        draw = ImageDraw.Draw(checkbutton_disabled)
        draw.rounded_rectangle(
            [2, 2, 132, 132], radius=16, outline=disabled_fg, width=3
        )
        disabled_img = ImageTk.PhotoImage(
            checkbutton_disabled.resize(size, Image.LANCZOS)
        )
        disabled_name = util.get_image_name(disabled_img)
        self.theme_images[disabled_name] = disabled_img

        return off_name, on_name, disabled_name, alt_name, on_dis_name, alt_dis_name

    def create_menubutton_style(self, colorname=DEFAULT):
        \"\"\"Create a solid style for the ttk.Menubutton widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"TMenubutton\"

        foreground = self.colors.get_foreground(colorname)

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE
            background = self.colors.primary
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"
            background = self.colors.get(colorname)

        disabled_bg = Colors.make_transparent(0.10, self.colors.fg, self.colors.bg)
        disabled_fg = Colors.make_transparent(0.30, self.colors.fg, self.colors.bg)
        pressed = Colors.make_transparent(0.80, background, self.colors.bg)
        hover = Colors.make_transparent(0.90, background, self.colors.bg)    

        self.style._build_configure(
            ttkstyle,
            foreground=foreground,
            background=background,
            bordercolor=background,
            darkcolor=background,
            lightcolor=background,
            arrowsize=self.scale_size(4),
            arrowcolor=foreground,
            arrowpadding=(0, 0, 15, 0),
            relief=tk.RAISED,
            focusthickness=0,
            focuscolor=self.colors.selectfg,
            padding=(10, 5),
        )
        self.style.map(
            ttkstyle,
            arrowcolor=[(\"disabled\", disabled_fg)],
            foreground=[(\"disabled\", disabled_fg)],
            background=[
                (\"disabled\", disabled_bg),
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            bordercolor=[
                (\"disabled\", disabled_bg),
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            darkcolor=[
                (\"disabled\", disabled_bg),
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            lightcolor=[
                (\"disabled\", disabled_bg),
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_outline_menubutton_style(self, colorname=DEFAULT):
        \"\"\"Create an outline button style for the ttk.Menubutton widget

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"Outline.TMenubutton\"

        disabled_fg = Colors.make_transparent(0.30, self.colors.fg, self.colors.bg)

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE
            colorname = PRIMARY
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"

        foreground = self.colors.get(colorname)
        background = self.colors.get_foreground(colorname)
        foreground_pressed = background
        bordercolor = foreground
        pressed = foreground
        hover = foreground

        self.style._build_configure(
            ttkstyle,
            foreground=foreground,
            background=self.colors.bg,
            bordercolor=bordercolor,
            darkcolor=self.colors.bg,
            lightcolor=self.colors.bg,
            relief=tk.RAISED,
            focusthickness=0,
            focuscolor=foreground,
            padding=(10, 5),
            arrowcolor=foreground,
            arrowpadding=(0, 0, 15, 0),
            arrowsize=self.scale_size(4),
        )
        self.style.map(
            ttkstyle,
            foreground=[
                (\"disabled\", disabled_fg),
                (\"pressed !disabled\", foreground_pressed),
                (\"hover !disabled\", foreground_pressed),
            ],
            background=[
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            bordercolor=[
                (\"disabled\", disabled_fg),
                (\"pressed\", pressed),
                (\"hover\", hover),
            ],
            darkcolor=[
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            lightcolor=[
                (\"pressed !disabled\", pressed),
                (\"hover !disabled\", hover),
            ],
            arrowcolor=[
                (\"disabled\", disabled_fg),
                (\"pressed\", foreground_pressed),
                (\"hover\", foreground_pressed),
            ],
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_notebook_style(self, colorname=DEFAULT):
        \"\"\"Create a standard style for the ttk.Notebook widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"TNotebook\"

        if self.is_light_theme:
            bordercolor = self.colors.border
            foreground = self.colors.inputfg
        else:
            bordercolor = self.colors.selectbg
            foreground = self.colors.selectfg

        if any([colorname == DEFAULT, colorname == \"\"]):
            background = self.colors.inputbg
            selectfg = self.colors.fg
            ttkstyle = STYLE
        else:
            selectfg = self.colors.get_foreground(colorname)
            background = self.colors.get(colorname)
            ttkstyle = f\"{colorname}.{STYLE}\"

        ttkstyle_tab = f\"{ttkstyle}.Tab\"

        # create widget style
        self.style._build_configure(
            ttkstyle,
            background=self.colors.bg,
            bordercolor=bordercolor,
            lightcolor=self.colors.bg,
            darkcolor=self.colors.bg,
            tabmargins=(0, 1, 1, 0),
        )
        self.style._build_configure(
            ttkstyle_tab, focuscolor=\"\", foreground=foreground, padding=(6, 5)
        )
        self.style.map(
            ttkstyle_tab,
            background=[
                (\"selected\", self.colors.bg),
                (\"!selected\", background),
            ],
            lightcolor=[
                (\"selected\", self.colors.bg),
                (\"!selected\", background),
            ],
            bordercolor=[
                (\"selected\", bordercolor),
                (\"!selected\", bordercolor),
            ],
            padding=[(\"selected\", (6, 5)), (\"!selected\", (6, 5))],
            foreground=[(\"selected\", foreground), (\"!selected\", selectfg)],
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def create_panedwindow_style(self, colorname=DEFAULT):
        \"\"\"Create a standard style for the ttk.Panedwindow widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        H_STYLE = \"Horizontal.TPanedwindow\"
        V_STYLE = \"Vertical.TPanedwindow\"

        if self.is_light_theme:
            default_color = self.colors.border
        else:
            default_color = self.colors.selectbg

        if any([colorname == DEFAULT, colorname == \"\"]):
            sashcolor = default_color
            h_ttkstyle = H_STYLE
            v_ttkstyle = V_STYLE
        else:
            sashcolor = self.colors.get(colorname)
            h_ttkstyle = f\"{colorname}.{H_STYLE}\"
            v_ttkstyle = f\"{colorname}.{V_STYLE}\"

        self.style._build_configure(
            \"Sash\", gripcount=0, sashthickness=self.scale_size(2)
        )
        self.style._build_configure(h_ttkstyle, background=sashcolor)
        self.style._build_configure(v_ttkstyle, background=sashcolor)

        # register ttkstyle
        self.style._register_ttkstyle(h_ttkstyle)
        self.style._register_ttkstyle(v_ttkstyle)

    def create_sizegrip_assets(self, color):
        \"\"\"Create image assets used to build the sizegrip style.

        Parameters:

            color (str):
                The color _value_ used to draw the image.

        Returns:

            str:
                The PhotoImage name.
        \"\"\"
        from math import ceil

        box = self.scale_size(1)
        pad = box * 2
        chunk = box + pad  # 4

        w = chunk * 3 + pad  # 14
        h = chunk * 3 + pad  # 14

        size = [w, h]

        im = Image.new(\"RGBA\", size)
        draw = ImageDraw.Draw(im)

        draw.rectangle((chunk * 2 + pad, pad, chunk * 3, chunk), fill=color)
        draw.rectangle(
            (chunk * 2 + pad, chunk + pad, chunk * 3, chunk * 2), fill=color
        )
        draw.rectangle(
            (chunk * 2 + pad, chunk * 2 + pad, chunk * 3, chunk * 3),
            fill=color,
        )

        draw.rectangle(
            (chunk + pad, chunk + pad, chunk * 2, chunk * 2), fill=color
        )
        draw.rectangle(
            (chunk + pad, chunk * 2 + pad, chunk * 2, chunk * 3), fill=color
        )

        draw.rectangle((pad, chunk * 2 + pad, chunk, chunk * 3), fill=color)

        _img = ImageTk.PhotoImage(im)
        _name = util.get_image_name(_img)
        self.theme_images[_name] = _img
        return _name

    def create_sizegrip_style(self, colorname=DEFAULT):
        \"\"\"Create a style for the ttk.Sizegrip widget.

        Parameters:

            colorname (str):
                The color label used to style the widget.
        \"\"\"
        STYLE = \"TSizegrip\"

        if any([colorname == DEFAULT, colorname == \"\"]):
            ttkstyle = STYLE

            if self.is_light_theme:
                grip_color = self.colors.border
            else:
                grip_color = self.colors.inputbg
        else:
            ttkstyle = f\"{colorname}.{STYLE}\"
            grip_color = self.colors.get(colorname)

        image = self.create_sizegrip_assets(grip_color)

        self.style.element_create(
            f\"{ttkstyle}.Sizegrip.sizegrip\", \"image\", image
        )
        self.style.layout(
            ttkstyle,
            [
                (
                    f\"{ttkstyle}.Sizegrip.sizegrip\",
                    {\"side\": tk.BOTTOM, \"sticky\": tk.SE},
                )
            ],
        )
        # register ttkstyle
        self.style._register_ttkstyle(ttkstyle)

    def update_combobox_popdown_style(self, widget):
        \"\"\"Update the legacy ttk.Combobox elements. This method is
        called every time the theme is changed in order to ensure
        that the legacy tkinter components embedded in this ttk widget
        are styled appropriate to the current theme.

        The ttk.Combobox contains several elements that are not styled
        using the ttk theme engine. This includes the **popdownwindow**
        and the **scrollbar**. Both of these widgets are configured
        manually using calls to tcl/tk.

        Parameters:

            widget (ttk.Combobox):
                The combobox element to be updated.
        \"\"\"
        if self.is_light_theme:
            bordercolor = self.colors.border
        else:
            bordercolor = self.colors.selectbg

        tk_settings = []
        tk_settings.extend([\"-borderwidth\", 2])
        tk_settings.extend([\"-highlightthickness\", 1])
        tk_settings.extend([\"-highlightcolor\", bordercolor])
        tk_settings.extend([\"-background\", self.colors.inputbg])
        tk_settings.extend([\"-foreground\", self.colors.inputfg])
        tk_settings.extend([\"-selectbackground\", self.colors.selectbg])
        tk_settings.extend([\"-selectforeground\", self.colors.selectfg])

        # set popdown style
        popdown = widget.tk.eval(f\"ttk::combobox::PopdownWindow {widget}\")
        widget.tk.call(f\"{popdown}.f.l\", \"configure\", *tk_settings)

        # set scrollbar style
        sb_style = \"TCombobox.Vertical.TScrollbar\"
        widget.tk.call(f\"{popdown}.f.sb\", \"configure\", \"-style\", sb_style)


class Keywords:

    # TODO possibly refactor the bootstyle keyword methods into this class?
    #   Leave for now.

    COLORS = [
        \"primary\",
        \"secondary\",
        \"success\",
        \"info\",
        \"warning\",
        \"danger\",
        \"light\",
        \"dark\",
    ]
    ORIENTS = [\"horizontal\", \"vertical\"]
    TYPES = [
        \"outline\",
        \"link\",
        \"inverse\",
        \"round\",
        \"square\",
        \"striped\",
        \"focus\",
        \"input\",
        \"date\",
        \"metersubtxt\",
        \"meter\",
        \"table\"
    ]
    CLASSES = [
        \"button\",
        \"progressbar\",
        \"checkbutton\",
        \"combobox\",
        \"entry\",
        \"labelframe\",
        \"label\",
        \"frame\",
        \"floodgauge\",
        \"sizegrip\",
        \"optionmenu\",
        \"menubutton\",
        \"menu\",
        \"notebook\",
        \"panedwindow\",
        \"radiobutton\",
        \"separator\",
        \"scrollbar\",
        \"spinbox\",
        \"scale\",
        \"text\",
        \"toolbutton\",
        \"treeview\",
        \"toggle\",
        \"tk\",
        \"calendar\",
        \"listbox\",
        \"canvas\",
        \"toplevel\",
    ]
    COLOR_PATTERN = re.compile(\"|\".join(COLORS))
    ORIENT_PATTERN = re.compile(\"|\".join(ORIENTS))
    CLASS_PATTERN = re.compile(\"|\".join(CLASSES))
    TYPE_PATTERN = re.compile(\"|\".join(TYPES))


class Bootstyle:
    @staticmethod
    def ttkstyle_widget_class(widget=None, string=\"\"):
        \"\"\"Find and return the widget class

        Parameters:

            widget (Widget):
                The widget object.

            string (str):
                A keyword string to parse.

        Returns:

            str:
                A widget class keyword.
        \"\"\"
        # find widget class from string pattern
        match = re.search(Keywords.CLASS_PATTERN, string.lower())
        if match is not None:
            widget_class = match.group(0)
            return widget_class

        # find widget class from tkinter/tcl method
        if widget is None:
            return \"\"
        _class = widget.winfo_class()
        match = re.search(Keywords.CLASS_PATTERN, _class.lower())
        if match is not None:
            widget_class = match.group(0)
            return widget_class
        else:
            return \"\"

    @staticmethod
    def ttkstyle_widget_type(string):
        \"\"\"Find and return the widget type.

        Parameters:

            string (str):
                A keyword string to parse.

        Returns:

            str:
                A widget type keyword.
        \"\"\"
        match = re.search(Keywords.TYPE_PATTERN, string.lower())
        if match is None:
            return \"\"
        else:
            widget_type = match.group(0)
            return widget_type

    @staticmethod
    def ttkstyle_widget_orient(widget=None, string=\"\", **kwargs):
        \"\"\"Find and return widget orient, or default orient for widget if
        a widget with orientation.

        Parameters:

            widget (Widget):
                The widget object.

            string (str):
                A keyword string to parse.

            **kwargs:
                Optional keyword arguments passed in the widget constructor.

        Returns:

            str:
                A widget orientation keyword.
        \"\"\"
        # string method (priority)
        match = re.search(Keywords.ORIENT_PATTERN, string)
        widget_orient = \"\"

        if match is not None:
            widget_orient = match.group(0)
            return widget_orient

        # orient from kwargs
        if \"orient\" in kwargs:
            _orient = kwargs.pop(\"orient\")
            if _orient == \"h\":
                widget_orient = \"horizontal\"
            elif _orient == \"v\":
                widget_orient = \"vertical\"
            else:
                widget_orient = _orient
            return widget_orient

        # orient from settings
        if widget is None:
            return widget_orient
        try:
            widget_orient = str(widget.cget(\"orient\"))
        except:
            pass

        return widget_orient

    @staticmethod
    def ttkstyle_widget_color(string):
        \"\"\"Find and return widget color

        Parameters:

            string (str):
                A keyword string to parse.

        Returns:

            str:
                A color keyword.
        \"\"\"
        _color = re.search(Keywords.COLOR_PATTERN, string.lower())
        if _color is None:
            return \"\"
        else:
            widget_color = _color.group(0)
            return widget_color

    @staticmethod
    def ttkstyle_name(widget=None, string=\"\", **kwargs):
        \"\"\"Parse a string to build and return a ttkstyle name.

        Parameters:

            widget (Widget):
                The widget object.

            string (str):
                A keyword string to parse.

            **kwargs:
                Other keyword arguments to parse widget orientation.

        Returns:

            str:
                A ttk style name
        \"\"\"
        style_string = \"\".join(string).lower()
        widget_color = Bootstyle.ttkstyle_widget_color(style_string)
        widget_type = Bootstyle.ttkstyle_widget_type(style_string)
        widget_orient = Bootstyle.ttkstyle_widget_orient(
            widget, style_string, **kwargs
        )
        widget_class = Bootstyle.ttkstyle_widget_class(widget, style_string)

        if widget_color:
            widget_color = f\"{widget_color}.\"

        if widget_type:
            widget_type = f\"{widget_type.title()}.\"

        if widget_orient:
            widget_orient = f\"{widget_orient.title()}.\"

        if widget_class.startswith(\"t\"):
            widget_class = widget_class.title()
        else:
            widget_class = f\"T{widget_class.title()}\"

        ttkstyle = f\"{widget_color}{widget_type}{widget_orient}{widget_class}\"
        return ttkstyle

    @staticmethod
    def ttkstyle_method_name(widget=None, string=\"\"):
        \"\"\"Parse a string to build and return the name of the
        `StyleBuilderTTK` method that creates the ttk style for the
        target widget.

        Parameters:

            widget (Widget):
                The widget object to lookup.

            string (str):
                The keyword string to parse.

        Returns:

            str:
                The name of the update method used to update the widget.
        \"\"\"
        style_string = \"\".join(string).lower()
        widget_type = Bootstyle.ttkstyle_widget_type(style_string)
        widget_class = Bootstyle.ttkstyle_widget_class(widget, style_string)

        if widget_type:
            widget_type = f\"_{widget_type}\"

        if widget_class:
            widget_class = f\"_{widget_class}\"

        if not widget_type and not widget_class:
            return \"\"
        else:
            method_name = f\"create{widget_type}{widget_class}_style\"
            return method_name

    @staticmethod
    def tkupdate_method_name(widget):
        \"\"\"Lookup the tkinter style update method from the widget class

        Parameters:

            widget (Widget):
                The widget object to lookup.

        Returns:

            str:
                The name of the method used to update the widget object.
        \"\"\"
        widget_class = Bootstyle.ttkstyle_widget_class(widget)

        if widget_class:
            widget_class = f\"_{widget_class}\"

        method_name = f\"update{widget_class}_style\"
        return method_name

    @staticmethod
    def override_ttk_widget_constructor(func):
        \"\"\"Override widget constructors with bootstyle api options.

        Parameters:

            func (Callable):
                The widget class `__init__` method
        \"\"\"

        def __init__(self, *args, **kwargs):

            # capture bootstyle and style arguments
            if \"bootstyle\" in kwargs:
                bootstyle = kwargs.pop(\"bootstyle\")
            else:
                bootstyle = \"\"

            if \"style\" in kwargs:
                style = kwargs.pop(\"style\") or \"\"
            else:
                style = \"\"

            # instantiate the widget
            func(self, *args, **kwargs)

            # must be called AFTER instantiation in order to use winfo_class
            #    in the `get_ttkstyle_name` method

            if style:
                if Style.get_instance().style_exists_in_theme(style):
                    self.configure(style=style)
                else:
                    ttkstyle = Bootstyle.update_ttk_widget_style(
                        self, style, **kwargs
                    )
                    self.configure(style=ttkstyle)
            elif bootstyle:
                ttkstyle = Bootstyle.update_ttk_widget_style(
                    self, bootstyle, **kwargs
                )
                self.configure(style=ttkstyle)
            else:
                ttkstyle = Bootstyle.update_ttk_widget_style(
                    self, \"default\", **kwargs
                )
                self.configure(style=ttkstyle)

        return __init__

    @staticmethod
    def override_ttk_widget_configure(func):
        \"\"\"Overrides the configure method on a ttk widget.

        Parameters:

            func (Callable):
                The widget class `configure` method
        \"\"\"

        def configure(self, cnf=None, **kwargs):
            # get configuration
            if cnf in (\"bootstyle\", \"style\"):
                return self.cget(\"style\")

            # set configuration
            if \"bootstyle\" in kwargs:
                bootstyle = kwargs.pop(\"bootstyle\")
            else:
                bootstyle = \"\"

            if \"style\" in kwargs:
                style = kwargs.get(\"style\")
                ttkstyle = Bootstyle.update_ttk_widget_style(
                    self, style, **kwargs
                )
            elif bootstyle:
                ttkstyle = Bootstyle.update_ttk_widget_style(
                    self, bootstyle, **kwargs
                )
                kwargs.update(style=ttkstyle)

            # update widget configuration
            func(self, cnf, **kwargs)

        return configure

    @staticmethod
    def update_ttk_widget_style(
        widget: ttk.Widget = None, style_string: str = None, **kwargs
    ):
        \"\"\"Update the ttk style or create if not existing.

        Parameters:

            widget (ttk.Widget):
                The widget instance being updated.

            style_string (str):
                The style string to evalulate. May be the `style`, `ttkstyle`
                or `bootstyle` argument depending on the context and scenario.

            **kwargs:
                Other optional keyword arguments.

        Returns:

            str:
                The ttkstyle or empty string if there is none.
        \"\"\"
        style: Style = Style.get_instance() or Style()

        # get existing widget style if not provided
        if style_string is None:
            style_string = widget.cget(\"style\")

        # do nothing if the style has not been set
        if not style_string:
            return \"\"

        if style_string == '.':
            return '.'

        # build style if not existing (example: theme changed)
        ttkstyle = Bootstyle.ttkstyle_name(widget, style_string, **kwargs)
        if not style.style_exists_in_theme(ttkstyle):
            widget_color = Bootstyle.ttkstyle_widget_color(ttkstyle)
            method_name = Bootstyle.ttkstyle_method_name(widget, ttkstyle)
            builder: StyleBuilderTTK = style._get_builder()
            builder_method = builder.name_to_method(method_name)
            builder_method(builder, widget_color)

        # subscribe popdown style to theme changes
        try:
            if widget.winfo_class() == \"TCombobox\":
                builder: StyleBuilderTTK = style._get_builder()
                winfo_id = hex(widget.winfo_id())
                winfo_pathname = widget.winfo_pathname(winfo_id)
                Publisher.subscribe(
                    name=winfo_pathname,
                    func=lambda w=widget: builder.update_combobox_popdown_style(
                        w
                    ),
                    channel=Channel.STD,
                )
                builder.update_combobox_popdown_style(widget)
        except:
            pass

        return ttkstyle

    @staticmethod
    def setup_ttkbootstap_api():
        \"\"\"Setup ttkbootstrap for use with tkinter and ttk. This method
        is called when ttkbootstrap is imported to perform all of the
        necessary method overrides that implement the bootstyle api.\"\"\"
        from ttkbootstrap.widgets import TTK_WIDGETS
        from ttkbootstrap.widgets import TK_WIDGETS

        # TTK WIDGETS
        for widget in TTK_WIDGETS:
            try:
                # override widget constructor
                _init = Bootstyle.override_ttk_widget_constructor(
                    widget.__init__
                )
                widget.__init__ = _init

                # override configure method
                _configure = Bootstyle.override_ttk_widget_configure(
                    widget.configure
                )
                widget.configure = _configure
                widget.config = widget.configure

                # override get and set methods
                _orig_getitem = widget.__getitem
                _orig_setitem = widget.__setitem

                def __setitem(self, key, val):
                    if key in (\"bootstyle\", \"style\"):
                        return _configure(self, **{key: val})
                    return _orig_setitem(key, val)

                def __getitem(self, key):
                    if key in (\"bootstyle\", \"style\"):
                        return _configure(self, cnf=key)
                    return _orig_getitem(key)

                if (
                    widget.__name__ != \"OptionMenu\"
                ):  # this has it's own override
                    widget.__setitem__ = __setitem
                    widget.__getitem__ = __getitem
            except:
                # this may fail in python 3.6 for ttk widgets that do not exist
                #   in that version.
                continue

        # TK WIDGETS
        for widget in TK_WIDGETS:
            # override widget constructor
            _init = Bootstyle.override_tk_widget_constructor(widget.__init__)
            widget.__init__ = _init

    @staticmethod
    def update_tk_widget_style(widget):
        \"\"\"Lookup the widget name and call the appropriate update
        method

        Parameters:

            widget (object):
                The tcl/tk name given by `tkinter.Widget.winfo_name()`
        \"\"\"
        try:
            style = Style.get_instance()
            method_name = Bootstyle.tkupdate_method_name(widget)
            builder = style._get_builder_tk()
            builder_method = getattr(StyleBuilderTK, method_name)
            builder_method(builder, widget)
        except:
            \"\"\"Must pass here to prevent a failure when the user calls
            the `Style`method BEFORE an instance of `Tk` is instantiated.
            This will defer the update of the `Tk` background until the end
            of the `BootStyle` object instantiation (created by the `Style`
            method)\"\"\"
            pass

    @staticmethod
    def override_tk_widget_constructor(func):
        \"\"\"Override widget constructors to apply default style for tk
        widgets.

        Parameters:

            func (Callable):
                The `__init__` method for this widget.
        \"\"\"

        def __init__wrapper(self, *args, **kwargs):

            # check for autostyle flag
            if \"autostyle\" in kwargs:
                autostyle = kwargs.pop(\"autostyle\")
            else:
                autostyle = True

            # instantiate the widget
            func(self, *args, **kwargs)

            if autostyle:
                Publisher.subscribe(
                    name=str(self),
                    func=lambda w=self: Bootstyle.update_tk_widget_style(w),
                    channel=Channel.STD,
                )
                Bootstyle.update_tk_widget_style(self)

        return __init__wrapper
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/tableview.py": """import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from math import ceil
from datetime import datetime
from tkinter import font
from ttkbootstrap import utility
from typing import Any, Dict, List, Union
from ttkbootstrap.localization import MessageCatalog

UPARROW = \"⬆\"
DOWNARROW = \"⬇\"
ASCENDING = 0
DESCENDING = 1


class TableColumn:
    \"\"\"Represents a column in a Tableview object\"\"\"

    def __init__(
            self,
            tableview,
            cid,
            text,
            image=\"\",
            command=\"\",
            anchor=W,
            width=200,
            minwidth=20,
            stretch=False,
    ):
        \"\"\"
        Parameters:

            tableview (Tableview):
                The parent tableview object.

            cid (str):
                The column id.

            text (str):
                The header text.

            image (PhotoImage):
                An image that is displayed to the left of the header text.

            command (Callable):
                A function called whenever the header button is clicked.

            anchor (str):
                The position of the header text within the header. One
                of \"e\", \"w\", \"center\".

            width (int):
                Specifies the width of the column in pixels.

            minwidth (int):
                Specifies the minimum width of the column in pixels.

            stretch (bool):
                Specifies whether or not the column width should be
                adjusted whenever the widget is resized or the user
                drags the column separator.
        \"\"\"
        self._table = tableview
        self._cid = cid
        self._headertext = text
        self._sort = ASCENDING
        self._settings_column = {}
        self._settings_heading = {}

        self.view: ttk.Treeview = tableview.view
        self.view.column(
            self._cid,
            width=width,
            minwidth=minwidth,
            stretch=stretch,
            anchor=anchor,
        )
        self.view.heading(
            self._cid,
            text=text,
            anchor=anchor,
            image=image,
            command=command,
        )
        self._capture_settings()
        self._table._cidmap[self._cid] = self

    @property
    def headertext(self):
        \"\"\"The text on the header label\"\"\"
        return self._headertext

    @property
    def columnsort(self):
        \"\"\"Indicates how the column is to be sorted when the sorting
        method is invoked.\"\"\"
        return self._sort

    @columnsort.setter
    def columnsort(self, value):
        self._sort = value

    @property
    def cid(self):
        \"\"\"A unique column identifier\"\"\"
        return str(self._cid)

    @property
    def tableindex(self):
        \"\"\"The index of the column as it is in the table configuration.\"\"\"
        cols = self.view.configure(\"columns\")
        if cols is None:
            return
        try:
            return cols.index(self.cid)
        except IndexError:
            return

    @property
    def displayindex(self):
        \"\"\"The index of the column as it is displayed\"\"\"
        cols = self.view.configure(\"displaycolumns\")
        if \"#all\" in cols:
            return self.tableindex
        else:
            return cols.index(self.cid)

    def configure(self, opt=None, **kwargs):
        \"\"\"Configure the column. If opt is provided, the
        current value is returned, otherwise, sets the widget
        options specified in kwargs. See the documentation for
        `Tableview.insert_column` for configurable options.

        Parameters:

            opt (str):
                A configuration option to query.

            **kwargs (Dict):
                Optional keyword arguments used to configure the
                column and headers.
        \"\"\"
        # return queried options
        if opt is not None:
            if opt in (\"anchor\", \"width\", \"minwidth\", \"stretch\"):
                return self.view.column(self.cid, opt)
            elif opt in (\"command\", \"text\", \"image\"):
                return self.view.heading(self.cid, opt)
            else:
                return

        # configure column and heading
        for k, v in kwargs.items():
            if k in (\"anchor\", \"width\", \"minwidth\", \"stretch\"):
                self._settings_column[k] = v
            elif k in (\"command\", \"text\", \"image\"):
                self._settings_heading[k] = v
        self.view.column(self._cid, **self._settings_column)
        self.view.heading(self._cid, **self._settings_heading)
        if \"text\" in kwargs:
            self._headertext = kwargs[\"text\"]

    def show(self):
        \"\"\"Make the column visible in the tableview\"\"\"
        displaycols = list(self.view.configure(\"displaycolumns\"))
        if \"#all\" in displaycols:
            return
        if self.cid in displaycols:
            return
        columns = list(self.view.configure(\"columns\"))
        index = columns.index(self.cid)
        displaycols.insert(index, self.cid)
        self.view.configure(displaycolumns=displaycols)

    def hide(self):
        \"\"\"Hide the column in the tableview\"\"\"
        displaycols = list(self.view.configure(\"displaycolumns\"))
        cols = list(self.view.configure(\"columns\"))
        if \"#all\" in displaycols:
            displaycols = cols
        displaycols.remove(self.cid)
        self.view.configure(displaycolumns=displaycols)

    def delete(self):
        \"\"\"Remove the column from the tableview permanently.\"\"\"
        # update the tablerow columns
        index = self.tableindex
        if index is None:
            return

        for row in self._table.tablerows:
            row.values.pop(index)
            row.refresh()

        # actual columns
        cols = list(self.view.cget(\"columns\"))
        cols.remove(self.cid)
        self._table.tablecolumns.remove(self)

        # visible columns
        dcols = list(self.view.cget(\"displaycolumns\"))
        if \"#all\" in dcols:
            dcols = cols
        else:
            dcols.remove(self.cid)

        # remove cid mapping
        self._table.cidmap.pop(self._cid)

        # reconfigure the tableview column and displaycolumns
        self.view.configure(columns=cols, displaycolumns=dcols)

        # remove the internal object references
        for i, column in enumerate(self._table.tablecolumns):
            if column.cid == self.cid:
                self._table.tablecolumns.pop(i)
            else:
                column.restore_settings()

    def restore_settings(self):
        \"\"\"Update the configuration based on stored settings\"\"\"
        self.view.column(self.cid, **self._settings_column)
        self.view.heading(self.cid, **self._settings_heading)

    def _capture_settings(self):
        \"\"\"Update the stored settings for the column and heading.
        This is required because the settings are erased whenever
        the `columns` parameter is configured in the underlying
        Treeview widget.\"\"\"
        self._settings_heading = self.view.heading(self.cid)
        self._settings_heading.pop(\"state\")
        self._settings_column = self.view.column(self.cid)
        self._settings_column.pop(\"id\")


class TableRow:
    \"\"\"Represents a row in a Tableview object\"\"\"

    _cnt = 0

    def __init__(self, tableview, values):
        \"\"\"
        Parameters:

            tableview (Tableview):
                The Tableview widget that contains this row

            values (List[Any, ...]):
                A list of values to display in the row
        \"\"\"
        self.view: ttk.Treeview = tableview.view
        self._values = values
        self._iid = None
        self._sort = TableRow._cnt + 1
        self._table = tableview

        # increment cnt
        TableRow._cnt += 1

    @property
    def values(self):
        \"\"\"The table row values\"\"\"
        return self._values

    @values.setter
    def values(self, values):
        self._values = values
        self.refresh()

    @property
    def iid(self):
        \"\"\"A unique record identifier\"\"\"
        return str(self._iid)

    def configure(self, opt=None, **kwargs):
        \"\"\"Configure the row. If opt is provided, the
        current value is returned, otherwise, sets the widget
        options specified in kwargs. See the documentation for
        `Tableview.insert_row` for configurable options.

        Parameters:

            opt (str):
                A configuration option to query.

            **kwargs { values, tags }:
                Optional keyword arguments used to configure the
                row.
        \"\"\"
        if self._iid is None:
            self.build()

        if opt is not None:
            return self.view.item(self.iid, opt)
        elif 'values' in kwargs:
            values = kwargs.pop('values')
            self.values = values
        else:
            self.view.item(self.iid, **kwargs)

    def show(self, striped=False):
        \"\"\"Show the row in the data table view\"\"\"
        if self._iid is None:
            self.build()
        self.view.reattach(self.iid, \"\", END)

        # remove existing stripes
        tags = list(self.view.item(self.iid, \"tags\"))
        try:
            tags.remove(\"striped\")
        except ValueError:
            pass

        # add stripes (if needed)
        if striped:
            tags.append(\"striped\")
        self.view.item(self.iid, tags=tags)

    def delete(self):
        \"\"\"Delete the row from the dataset\"\"\"
        if self.iid:
            self._table.iidmap.pop(self.iid)
            self._table.tablerows_visible.remove(self)
            self._table._tablerows.remove(self)
            self._table.load_table_data()
            self.view.delete(self.iid)

    def hide(self):
        \"\"\"Remove the row from the data table view\"\"\"
        self.view.detach(self.iid)

    def refresh(self):
        \"\"\"Syncs the tableview values with the object values\"\"\"
        if self._iid:
            self.view.item(self.iid, values=self.values)

    def build(self):
        \"\"\"Create the row object in the `Treeview` and capture
        the resulting item id (iid).
        \"\"\"
        if self._iid is None:
            self._iid = self.view.insert(\"\", END, values=self.values)
            self._table.iidmap[self.iid] = self


class TableEvent:
    \"\"\"A container class for holding table event objects\"\"\"

    def __init__(self, column: TableColumn, row: TableRow):
        self.column = column
        self.row = row


class Tableview(ttk.Frame):
    \"\"\"A class built on the `ttk.Treeview` widget for arranging data in
    rows and columns. The underlying Treeview object and its methods are
    exposed in the `Tableview.view` property.

    A Tableview object contains various features such has striped rows,
    pagination, and autosized and autoaligned columns.

    The pagination option is recommended when loading a lot of data as
    the table records are inserted on-demand. Table records are only
    created when requested to be in a page view. This allows the table
    to be loaded very quickly even with hundreds of thousands of
    records.

    All table columns are sortable. Clicking a column header will toggle
    between sorting \"ascending\" and \"descending\".

    Columns are configurable by passing a simple list of header names or
    by passing in a dictionary of column names with settings. You can
    use both as well, as in the example below, where a column header
    name is use for one column, and a dictionary of settings is used
    for another.

    The object has a right-click menu on the header and the cells that
    allow you to configure various settings.

    ![](../../assets/widgets/tableview-1.png)
    ![](../../assets/widgets/tableview-2.png)

    Examples:

        Adding data with the constructor
        ```python
        import ttkbootstrap as ttk
        from ttkbootstrap.tableview import Tableview
        from ttkbootstrap.constants import *

        app = ttk.Window()
        colors = app.style.colors

        coldata = [
            {\"text\": \"LicenseNumber\", \"stretch\": False},
            \"CompanyName\",
            {\"text\": \"UserCount\", \"stretch\": False},
        ]

        rowdata = [
            ('A123', 'IzzyCo', 12),
            ('A136', 'Kimdee Inc.', 45),
            ('A158', 'Farmadding Co.', 36)
        ]

        dt = Tableview(
            master=app,
            coldata=coldata,
            rowdata=rowdata,
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(colors.light, None),
        )
        dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        app.mainloop()
        ```

        Add data with methods
        ```python
        dt.insert_row('end', ['Marzale LLC', 26])
        ```
    \"\"\"

    def __init__(
            self,
            master=None,
            bootstyle=DEFAULT,
            coldata=[],
            rowdata=[],
            paginated=False,
            searchable=False,
            autofit=False,
            autoalign=True,
            stripecolor=None,
            pagesize=10,
            height=10,
            delimiter=\",\",
    ):
        \"\"\"
        Parameters:

            master (Widget):
                The parent widget.

            bootstyle (str):
                A style keyword used to set the focus color of the entry
                and the background color of the date button. Available
                options include -> primary, secondary, success, info,
                warning, danger, dark, light.

            coldata (List[str | Dict]):
                An iterable containing either the heading name or a
                dictionary of column settings. Configurable settings
                include >> text, image, command, anchor, width, minwidth,
                maxwidth, stretch. Also see `Tableview.insert_column`.

            rowdata (List):
                An iterable of row data. The lenth of each row of data
                must match the number of columns. Also see
                `Tableview.insert_row`.

            paginated (bool):
                Specifies that the data is to be paginated. A pagination
                frame will be created below the table with controls that
                enable the user to page forward and backwards in the
                data set.

            pagesize (int):
                When `paginated=True`, this specifies the number of rows
                to show per page.

            searchable (bool):
                If `True`, a searchbar will be created above the table.
                Press the <Return> key to initiate a search. Searching
                with an empty string will reset the search criteria, or
                pressing the reset button to the right of the search
                bar. Currently, the search method looks for any row
                that contains the search text. The filtered results
                are displayed in the table view.

            autofit (bool):
                If `True`, the table columns will be automatically sized
                when loaded based on the records in the current view.
                Also see `Tableview.autofit_columns`.

            autoalign (bool):
                If `True`, the column headers and data are automatically
                aligned. Numbers and number headers are right-aligned
                and all other data types are left-aligned. The auto
                align method evaluates the first record in each column
                to determine the data type for alignment. Also see
                `Tableview.autoalign_columns`.

            stripecolor (Tuple[str, str]):
                If provided, even numbered rows will be color using the
                (background, foreground) specified. You may specify one
                or the other by passing in **None**. For example,
                `stripecolor=('green', None)` will set the stripe
                background as green, but the foreground will remain as
                default. You may use standand color names, hexadecimal
                color codes, or bootstyle color keywords. For example,
                ('light', '#222') will set the background to the \"light\"
                themed ttkbootstrap color and the foreground to the
                specified hexadecimal color. Also see
                `Tableview.apply_table_stripes`.

            height (int):
                Specifies how many rows will appear in the table's viewport.
                If the number of records extends beyond the table height,
                the user may use the mousewheel or scrollbar to navigate
                the data.

            delimiter (str):
                The character to use as a delimiter when exporting data
                to CSV.
        \"\"\"
        super().__init__(master)
        self._tablecols = []
        self._tablerows = []
        self._tablerows_filtered = []
        self._viewdata = []
        self._rowindex = tk.IntVar(value=0)
        self._pageindex = tk.IntVar(value=1)
        self._pagelimit = tk.IntVar(value=0)
        self._height = height
        self._pagesize = tk.IntVar(value=pagesize)
        self._paginated = paginated
        self._searchable = searchable
        self._stripecolor = stripecolor
        self._autofit = autofit
        self._autoalign = autoalign
        self._filtered = False
        self._sorted = False
        self._searchcriteria = tk.StringVar()
        self._rightclickmenu_cell = None
        self._delimiter = delimiter
        self._iidmap = {}  # maps iid to row object
        self._cidmap = {}  # maps cid to col object

        self.view: ttk.Treeview = None
        self._build_tableview_widget(coldata, rowdata, bootstyle)

    @property
    def tablerows(self):
        \"\"\"A list of all tablerow objects\"\"\"
        return self._tablerows

    @property
    def tablerows_filtered(self):
        \"\"\"A list of filtered tablerow objects\"\"\"
        return self._tablerows_filtered

    @property
    def tablerows_visible(self):
        \"\"\"A list of visible tablerow objects\"\"\"
        return self._viewdata

    @property
    def tablecolumns(self):
        \"\"\"A list of table column objects\"\"\"
        return self._tablecols

    @property
    def tablecolumns_visible(self):
        \"\"\"A list of visible table column objects\"\"\"
        cids = list(self.view.cget(\"displaycolumns\"))
        if \"#all\" in cids:
            return self._tablecols
        columns = []
        for cid in cids:
            # the cidmap expects an integer
            columns.append(self.cidmap.get(int(cid)))
        return columns

    @property
    def is_filtered(self):
        \"\"\"Indicates whether the table is currently filtered\"\"\"
        return self._filtered

    @property
    def searchcriteria(self):
        \"\"\"The criteria used to filter the records when the search
        method is invoked\"\"\"
        return self._searchcriteria.get()

    @searchcriteria.setter
    def searchcriteria(self, value):
        self._searchcriteria.set(value)

    @property
    def pagesize(self):
        \"\"\"The number of records visible on a single page\"\"\"
        return self._pagesize.get()

    @pagesize.setter
    def pagesize(self, value):
        self._pagesize.set(value)

    @property
    def iidmap(self) -> Dict[str, TableRow]:
        \"\"\"A map of iid to tablerow object\"\"\"
        return self._iidmap

    @property
    def cidmap(self) -> Dict[str, TableColumn]:
        \"\"\"A map of cid to tablecolumn object\"\"\"
        return self._cidmap

    def configure(self, cnf=None, **kwargs) -> Union[Any, None]:
        \"\"\"Configure the internal `Treeview` widget. If cnf is provided,
        value of the option is return. Otherwise the widget is
        configured via kwargs.

        Parameters:

            cnf (Any):
                An option to query.

            **kwargs (Dict):
                Optional keyword arguments used to configure the internal
                Treeview widget.

        Returns:

            Union[Any, None]:
                The value of cnf or None.
        \"\"\"
        try:
            if \"pagesize\" in kwargs:
                pagesize: int = kwargs.pop(\"pagesize\")
                self._pagesize.set(value=pagesize)

            self.view.configure(cnf, **kwargs)
        except:
            super().configure(cnf, **kwargs)

    # DATA HANDLING

    def build_table_data(self, coldata, rowdata):
        \"\"\"Insert the specified column and row data.

        The coldata can be either a string column name or a dictionary
        of column settings that are passed to the `insert_column`
        method. You may use a mixture of string and dictionary in
        the list of coldata.

        !!!warning \"Existing table data will be erased.
            This method will completely rebuild the underlying table
            with the new column and row data. Any existing data will
            be lost.

        Parameters:

            coldata (List[Union[str, Dict]]):
                An iterable of column names and/or settings.

            rowdata (List):
                An iterable of row values.
        \"\"\"
        # destroy the existing data if existing
        self.purge_table_data()

        # build the table columns
        for i, col in enumerate(coldata):
            if isinstance(col, str):
                # just a column name
                self.insert_column(i, col)
            else:
                # a dictionary of column settings
                self.insert_column(i, **col)

        # build the table rows
        for values in rowdata:
            self.insert_row(values=values)

        # load the table data
        self.load_table_data()

        # apply table formatting
        if self._autofit:
            self.autofit_columns()

        if self._autoalign:
            self.autoalign_columns()

        if self._stripecolor is not None:
            self.apply_table_stripes(self._stripecolor)

        self.goto_first_page()

    def insert_row(self, index=END, values=[]) -> TableRow:
        \"\"\"Insert a row into the tableview at index.

        You must call `Tableview.load_table_data()` to update the
        current view. If the data is filtered, you will need to call
        `Tableview.load_table_data(clear_filters=True)`.

        Parameters:

            index (Union[int, str]):
                A numerical index that specifieds where to insert
                the record in the dataset. You may also use the string
                'end' to append the record to the end of the data set.
                If the index exceeds the record count, it will be
                appended to the end of the dataset.

            values (Iterable):
                An iterable of values to insert into the data set.
                The number of columns implied by the list of values
                must match the number of columns in the data set for
                the values to be visible.

        Returns:

            TableRow:
                A table row object.
        \"\"\"
        rowcount = len(self._tablerows)

        # validate the index
        if len(values) == 0:
            return
        if index == END:
            index = -1
        elif index > rowcount - 1:
            index = -1

        record = TableRow(self, values)
        if rowcount == 0 or index == -1:
            self._tablerows.append(record)
        else:
            self._tablerows.insert(index, record)

        return record

    def insert_rows(self, index, rowdata):
        \"\"\"Insert row after index for each row in *row. If index does
        not exist then the records are appended to the end of the table.
        You can also use the string 'end' to append records at the end
        of the table.

        Parameters:

            index (Union[int, str]):
                The location in the data set after where the records
                will be inserted. You may use a numerical index or
                the string 'end', which will append the records to the
                end of the data set.

            rowdata (List[Any, List]):
                A list of row values to be inserted into the table.

        Examples:

            ```python
            Tableview.insert_rows('end', ['one', 1], ['two', 2])
            ```
        \"\"\"
        if len(rowdata) == 0:
            return
        for values in reversed(rowdata):
            self.insert_row(index, values)

    def delete_column(self, index=None, cid=None, visible=True):
        \"\"\"Delete the specified column based on the column index or the
        unique cid.

        Unless otherwise specified, the index refers to the column index
        as displayed in the tableview.

        If cid is provided, the column associated with the cid is deleted
        regardless of whether it is in the visible data sets.

        Parameters:

            index (int):
                The numerical index of the column.

            cid (str):
                A unique column indentifier.

            visible (bool):
                Specifies that the index should refer to the visible
                columns. Otherwise, if False, the original column
                position is used.
        \"\"\"
        if cid is not None:
            column: TableColumn = self.cidmap(int(cid))
            column.delete()

        elif index is not None and visible:
            self.tablecolumns_visible[int(index)].delete()

        elif index is None and not visible:
            self.tablecolumns[int(index)].delete()

    def delete_columns(self, indices=None, cids=None, visible=True):
        \"\"\"Delete columns specified by indices or cids.

        Unless specified otherwise, the index refers to the position
        of the columns in the table from left to right starting with
        index 0.

        !!!Warning \"Use this method with caution!
            This method may or may not suffer performance issues.
            Internally, this method calls the `delete_column` method
            on each column specified in the list. The `delete_column`
            method deletes the related column from each record in
            the table data. So, if there are a lot of records this
            could be problematic. It may be more beneficial to use
            the `build_table_data` if you plan on changing the
            structure of the table dramatically.

        Parameters:

            indices (List[int]):
                A list of column indices to delete from the table.

            cids (List[str]):
                A list of unique column identifiers to delete from the
                table.

            visible (bool):
                If True, the index refers to the visible position of the
                column in the stable, from left to right starting at
                index 0.
        \"\"\"
        if cids is not None:
            for cid in cids:
                self.delete_column(cid=cid)
        elif indices is not None:
            for index in indices:
                self.delete_column(index=index, visible=visible)

    def delete_row(self, index=None, iid=None, visible=True):
        \"\"\"Delete a record from the data set.

        Unless specified otherwise, the index refers to the record
        position within the visible data set from top to bottom
        starting with index 0.

        If iid is provided, the record associated with the cid is deleted
        regardless of whether it is in the visible data set.

        Parameters:

            index (int):
                The numerical index of the record within the data set.

            iid (str):
                A unique record identifier.

            visible (bool):
                Indicates that the record index is relative to the current
                records in view, otherwise, the original data set index is
                used if False.
        \"\"\"
        # delete from iid
        if iid is not None:
            record: TableRow = self.iidmap.get(iid)
            record.delete()
        elif index is not None:
            # visible index
            if visible:
                record = self.tablerows_visible[index]
                record.delete()
            # original index
            else:
                for record in self.tablerows:
                    if record._sort == index:
                        record.delete()

    def delete_rows(self, indices=None, iids=None, visible=True):
        \"\"\"Delete rows specified by indices or iids.

        If both indices and iids are None, then all records in the
        table will be deleted.
        \"\"\"
        # remove records by iid
        if iids is not None:
            for iid in iids:
                self.delete_row(iid=iid)
        # remove records by index
        elif indices is not None:
            for index in indices:
                self.delete_row(index=index, visible=visible)
        # remove ALL records
        else:
            self._tablerows.clear()
            self._tablerows_filtered.clear()
            self._viewdata.clear()
            self._iidmap.clear()
            records = self.view.get_children()
            self.view.delete(*records)
        # route to new page if no records visible
        if len(self._viewdata) == 0:
            self.goto_page()

    def insert_column(
            self,
            index,
            text=\"\",
            image=\"\",
            command=\"\",
            anchor=W,
            width=200,
            minwidth=20,
            stretch=False,
    ) -> TableColumn:
        \"\"\"
        Parameters:

            index (Union[int, str]):
                A numerical index that specifieds where to insert
                the column. You may also use the string 'end' to
                insert the column in the right-most position. If the
                index exceeds the column count, it will be inserted
                at the right-most position.

            text (str):
                The header text.

            image (PhotoImage):
                An image that is displayed to the left of the header text.

            command (Callable):
                A function called whenever the header button is clicked.

            anchor (str):
                The position of the header text within the header. One
                of \"e\", \"w\", \"center\".

            width (int):
                Specifies the width of the column in pixels.

            minwidth (int):
                Specifies the minimum width of the column in pixels.

            stretch (bool):
                Specifies whether or not the column width should be
                adjusted whenever the widget is resized or the user
                drags the column separator.

        Returns:

            TableColumn:
                A table column object.
        \"\"\"
        self.reset_table()
        colcount = len(self.tablecolumns)
        cid = colcount
        if index == END:
            index = -1
        elif index > colcount - 1:
            index = -1

        # actual columns
        cols = self.view.cget(\"columns\")
        if len(cols) > 0:
            cols = [int(x) for x in cols]
            cols.append(cid)
        else:
            cols = [cid]

        # visible columns
        dcols = self.view.cget(\"displaycolumns\")
        if \"#all\" in dcols:
            dcols = cols
        elif len(dcols) > 0:
            dcols = [int(x) for x in dcols]
            if index == -1:
                dcols.append(cid)
            else:
                dcols.insert(index, cid)
        else:
            dcols = [cid]

        self.view.configure(columns=cols, displaycolumns=dcols)

        # configure new column
        column = TableColumn(
            tableview=self,
            cid=cid,
            text=text,
            image=image,
            command=command,
            anchor=anchor,
            width=width,
            minwidth=minwidth,
            stretch=stretch,
        )
        self._tablecols.append(column)
        # must be called to show the header after initially creating it
        # ad hoc, not sure why this should be the case;
        self._column_sort_header_reset()

        # update settings after they are erased when a column is
        #   inserted
        for column in self._tablecols:
            column.restore_settings()

        return column

    def purge_table_data(self):
        \"\"\"Erase all table and column data.

        This method will completely destroy the table data structure.
        The table will need to be completely rebuilt after using this
        method.
        \"\"\"
        self.delete_rows()
        self.cidmap.clear()
        self.tablecolumns.clear()
        self.view.configure(columns=[], displaycolumns=[])

    def unload_table_data(self):
        \"\"\"Unload all data from the table\"\"\"
        for row in self.tablerows_visible:
            row.hide()
        self.tablerows_visible.clear()

    def load_table_data(self, clear_filters=False):
        \"\"\"Load records into the tableview.

        Parameters:

            clear_filters (bool):
                Specifies that the table filters should be cleared
                before loading the data into the view.
        \"\"\"
        if len(self.tablerows) == 0:
            return

        if clear_filters:
            self.reset_table()

        self.unload_table_data()

        if self._paginated:
            page_start = self._rowindex.get()
            page_end = self._rowindex.get() + self._pagesize.get()
        else:
            page_start = 0
            page_end = len(self._tablerows)

        if self._filtered:
            rowdata = self._tablerows_filtered[page_start:page_end]
            rowcount = len(self._tablerows_filtered)
        else:
            rowdata = self._tablerows[page_start:page_end]
            rowcount = len(self._tablerows)

        self._pagelimit.set(ceil(rowcount / self._pagesize.get()))

        pageindex = ceil(page_end / self._pagesize.get())
        pagelimit = self._pagelimit.get()
        self._pageindex.set(min([pagelimit, pageindex]))

        for i, row in enumerate(rowdata):
            if self._stripecolor is not None and i % 2 == 0:
                row.show(True)
            else:
                row.show(False)
            self._viewdata.append(row)

    def fill_empty_columns(self, fillvalue=\"\"):
        \"\"\"Fill empty columns with the fillvalue.

        This method can be used to fill in missing values when a column
        column is inserted after data has already been inserted into
        the tableview.

        Parameters:

            fillvalue (Any):
                A value to insert into an empty column
        \"\"\"
        rowcount = len(self._tablerows)
        if rowcount == 0:
            return
        colcount = len(self._tablecols)
        for row in self._tablerows:
            var = colcount - len(row._values)
            if var <= 0:
                return
            else:
                for _ in range(var):
                    row._values.append(fillvalue)
                row.configure(values=row._values)

    # CONFIGURATION

    def get_columns(self) -> List[TableColumn]:
        \"\"\"Returns a list of all column objects. Same as using the
        `Tableview.tablecolumns` property.\"\"\"
        return self._tablecols

    def get_column(
            self, index=None, visible=False, cid=None
    ) -> TableColumn:
        \"\"\"Returns the `TableColumn` object from an index or a cid.

        If index is specified, the column index refers to the index
        within the original, unless the visible flag is set, in which
        case the index is relative to the visible columns in view.

        If cid is specified, the column associated with the cid is
        return regardless of whether it is visible.

        Parameters:

            index (int):
                The numerical index of the column.

            visible (bool):
                Use the index of the visible columns as they appear
                in the table.

        Returns:

            Union[TableColumn, None]:
                The table column object if found, otherwise None.
        \"\"\"
        if cid is not None:
            return self._cidmap.get(cid)

        if not visible:
            # original column index
            try:
                return self._tablecols[index]
            except IndexError:
                return None
        else:
            # visible column index
            cols = self.view.cget(\"columns\")
            if len(cols) > 0:
                cols = [int(x) for x in cols]
            else:
                cols = []

            dcols = self.view.cget(\"displaycolumns\")
            if \"#all\" in dcols:
                dcols = cols
            else:
                try:
                    x = int(dcols[index])
                    for c in self._tablecols:
                        if c.cid == x:
                            return c
                except ValueError:
                    return None

    def get_rows(self, visible=False, filtered=False, selected=False) -> List[TableRow]:
        \"\"\"Return a list of TableRow objects.

        Return a subset of rows based on optional flags. Only ONE flag can be used
        at a time. If more than one flag is set to `True`, then the first flag will
        be used to return the data.

        Parameters:

            visible (bool):
                If true, only records in the current view will be returned.

            filtered (bool):
                If True, only rows in the filtered dataset will be returned.

            selected (bool):
                If True, only rows that are currently selected will be returned.

        Returns:

            List[TableRow]:
                A list of TableRow objects.
        \"\"\"
        if visible:
            return self._viewdata
        elif filtered:
            return self._tablerows_filtered
        elif selected:
            return [row for row in self._viewdata if row.iid in self.view.selection()]
        else:
            return self._tablerows

    def get_row(self, index=None, visible=False, filtered=False, iid=None) -> TableRow:
        \"\"\"Returns the `TableRow` object from an index or the iid.

        If an index is specified, the row index refers to the index
        within the original dataset. When choosing a subset of data,
        the visible data takes priority over filtered if both flags
        are set.

        If an iid is specified, the object attached to that iid is
        returned regardless of whether or not it is visible or
        filtered.

        Parameters:

            index (int):
                The numerical index of the column.

            iid (str):
                A unique column identifier.

            visible (bool):
                Use the index of the visible rows as they appear
                in the current table view.

            filtered (bool):
                Use the index of the rows within the filtered data
                set.

        Returns:

            Union[TableRow, None]:
                The table column object if found, otherwise None
        \"\"\"
        if iid is not None:
            return self.iidmap.get(iid)

        if visible:
            try:
                return self.tablerows_visible[index]
            except IndexError:
                return None
        elif filtered:
            try:
                return self.tablerows_filtered[index]
            except IndexError:
                return None
        else:
            try:
                return self.tablerows[index]
            except IndexError:
                return None

    # PAGE NAVIGATION

    def _select_first_visible_item(self):
        try:
            iid = self.tablerows_visible[0].iid
            self.view.selection_set(iid)
            # must force focus, sometimes just focus on iid doesn't work
            self.view.focus_force()
            # this sets the focus on the specific row item
            self.view.focus(iid)
            # make sure the row is visible
            self.view.see(iid)
        except:
            pass

    def goto_first_page(self):
        \"\"\"Update table with first page of data\"\"\"
        self._rowindex.set(0)
        self.load_table_data()
        self._select_first_visible_item()

    def goto_last_page(self):
        \"\"\"Update table with the last page of data\"\"\"
        pagelimit = self._pagelimit.get() - 1
        self._rowindex.set(self.pagesize * pagelimit)
        self.load_table_data()
        self._select_first_visible_item()

    def goto_next_page(self):
        \"\"\"Update table with next page of data\"\"\"
        if self._pageindex.get() >= self._pagelimit.get():
            return
        rowindex = self._rowindex.get()
        self._rowindex.set(rowindex + self.pagesize)
        self.load_table_data()
        self._select_first_visible_item()

    def goto_prev_page(self):
        \"\"\"Update table with prev page of data\"\"\"
        if self._pageindex.get() <= 1:
            return
        rowindex = self._rowindex.get()
        self._rowindex.set(rowindex - self.pagesize)
        self.load_table_data()
        self._select_first_visible_item()

    def goto_page(self, *_):
        \"\"\"Go to a specific page indicated by the page entry widget.\"\"\"
        pagelimit = self._pagelimit.get()
        pageindex = self._pageindex.get()
        if pageindex > pagelimit:
            pageindex = pagelimit
            self._pageindex.set(pageindex)
        elif pageindex <= 0:
            pageindex = 1
            self._pageindex.set(pageindex)
        rowindex = (pageindex * self.pagesize) - self.pagesize
        self._rowindex.set(rowindex)
        self.load_table_data()
        self._select_first_visible_item()

    # COLUMN SORTING

    def sort_column_data(self, event=None, cid=None, sort=None):
        \"\"\"Sort the table rows by the specified column. This method
        may be trigged by an event or manually.

        Parameters:

            event (Event):
                A window event.

            cid (int):
                A unique column identifier; typically the numerical
                index of the column relative to the original data set.

            sort (int):
                Determines the sort direction. 0 = ASCENDING. 1 = DESCENDING.
        \"\"\"
        if event is not None:
            eo = self._get_event_objects(event)
            column = eo.column
            index = column.tableindex
        elif cid is not None:
            column: TableColumn = self.cidmap.get(int(cid))
            index = column.tableindex
        else:
            return

        # update table data
        if self.is_filtered:
            tablerows = self.tablerows_filtered
        else:
            tablerows = self.tablerows

        if sort is not None:
            columnsort = sort
        else:
            columnsort = self.tablecolumns[index].columnsort

        if columnsort == ASCENDING:
            self._tablecols[index].columnsort = DESCENDING
        else:
            self._tablecols[index].columnsort = ASCENDING

        try:
            sortedrows = sorted(
                tablerows, reverse=columnsort, key=lambda x: x.values[index]
            )
        except:
            # when data is missing, or sometimes with numbers
            # this is still not right, but it works most of the time
            # fix sometime down the road when I have time
            self.fill_empty_columns()
            sortedrows = sorted(
                tablerows, reverse=columnsort, key=lambda x: int(x.values[index])
            )
        if self.is_filtered:
            self._tablerows_filtered = sortedrows
        else:
            self._tablerows = sortedrows

        # update headers
        self._column_sort_header_reset()
        self._column_sort_header_update(column.cid)

        self.unload_table_data()
        self.load_table_data()
        self._select_first_visible_item()

    # DATA SEARCH & FILTERING

    def reset_row_filters(self):
        \"\"\"Remove all row level filters; unhide all rows.\"\"\"
        self._filtered = False
        self.searchcriteria = \"\"
        self.unload_table_data()
        self.load_table_data()

    def reset_column_filters(self):
        \"\"\"Remove all column level filters; unhide all columns.\"\"\"
        cols = [col.cid for col in self.tablecolumns]
        self.view.configure(displaycolumns=cols)

    def reset_row_sort(self):
        \"\"\"Display all table rows by original insert index\"\"\"
        ...

    def reset_column_sort(self):
        \"\"\"Display all columns by original insert index\"\"\"
        cols = sorted([col.cid for col in self.tablecolumns_visible])
        self.view.configure(displaycolumns=cols)

    def reset_table(self):
        \"\"\"Remove all table data filters and column sorts\"\"\"
        self._filtered = False
        self.searchcriteria = \"\"
        try:
            sortedrows = sorted(self.tablerows, key=lambda x: x._sort)
        except IndexError:
            self.fill_empty_columns()
            sortedrows = sorted(self.tablerows, key=lambda x: x._sort)
        self._tablerows = sortedrows
        self.unload_table_data()

        # reset the columns
        self.reset_column_filters()
        self.reset_column_sort()

        self._column_sort_header_reset()
        self.goto_first_page()  # needed?

    def filter_column_to_value(self, event=None, cid=None, value=None):
        \"\"\"Hide all records except for records where the current
        column exactly matches the provided value. This method may
        be triggered by a window event or by specifying the column id.

        Parameters:

            event (Event):
                A window click event.

            cid (int):
                A unique column identifier; typically the numerical
                index of the column within the original dataset.

            value (Any):
                The criteria used to filter the column.
        \"\"\"
        if event is not None:
            eo = self._get_event_objects(event)
            index = eo.column.tableindex
            value = value or eo.row.values[index]
        elif cid is not None:
            column: TableColumn = self.cidmap.get(cid)
            index = column.tableindex
        else:
            return

        self._filtered = True
        self.tablerows_filtered.clear()
        self.unload_table_data()

        for row in self.tablerows:
            if row.values[index] == value:
                self.tablerows_filtered.append(row)

        self._rowindex.set(0)
        self.load_table_data()

    def filter_to_selected_rows(self):
        \"\"\"Hide all records except for the selected rows\"\"\"
        criteria = self.view.selection()
        if len(criteria) == 0:
            return  # nothing is selected

        if self.is_filtered:
            for row in self.tablerows_visible:
                if row.iid not in criteria:
                    row.hide()
                    self.tablerows_filtered.remove(row)
        else:
            self._filtered = True
            self.tablerows_filtered.clear()
            for row in self.tablerows_visible:
                if row.iid in criteria:
                    self.tablerows_filtered.append(row)
        self._rowindex.set(0)
        self.load_table_data()

    def hide_selected_rows(self):
        \"\"\"Hide the currently selected rows\"\"\"
        selected = self.view.selection()
        view_cnt = len(self._viewdata)
        hide_cnt = len(selected)
        self.view.detach(*selected)

        tablerows = []
        for row in self.tablerows_visible:
            if row.iid in selected:
                tablerows.append(row)

        if not self.is_filtered:
            self._filtered = True
            self._tablerows_filtered = self.tablerows.copy()

        for row in tablerows:
            if self.is_filtered:
                self.tablerows_filtered.remove(row)

        if hide_cnt == view_cnt:
            # assuming that if the count of the records on the page are
            #   selected for hiding, then need to go to the next page
            # The call to `load_table_data` is duplicative, but currently
            #   this is the only way to get this to work until I've
            #   refactored this bit.
            self.load_table_data()
            self.goto_page()
        else:
            self.load_table_data()

    def hide_selected_column(self, event=None, cid=None):
        \"\"\"Detach the selected column from the tableview. This method
        may be triggered by a window event or by specifying the column
        id.

        Parameters:

            event (Event):
                A window click event

            cid (int):
                A unique column identifier; typically the numerical
                index of the column within the original dataset.
        \"\"\"
        if event is not None:
            eo = self._get_event_objects(event)
            column = eo.column.hide()
        elif cid is not None:
            column: TableColumn = self.cidmap.get(cid)
            column.hide()

    def unhide_selected_column(self, event=None, cid=None):
        \"\"\"Attach the selected column to the tableview. This method
        may be triggered by a window event or by specifying the column
        id. The column is reinserted at the index in the original data
        set.

        Parameters:

            event (Event):
                An application click event

            cid (int):
                A unique column identifier; typically the numerical
                index of the column within the original dataset.
        \"\"\"
        if event is not None:
            eo = self._get_event_objects(event)
            eo.column.show()
        elif cid is not None:
            column = self.cidmap.get(cid)
            column.show()

    # DATA EXPORT

    def export_all_records(self):
        \"\"\"Export all records to a csv file\"\"\"
        headers = [col.headertext for col in self.tablecolumns]
        records = [row.values for row in self.tablerows]
        self.save_data_to_csv(headers, records, self._delimiter)

    def export_current_page(self):
        \"\"\"Export records on current page to csv file\"\"\"
        headers = [col.headertext for col in self.tablecolumns]
        records = [row.values for row in self.tablerows_visible]
        self.save_data_to_csv(headers, records, self._delimiter)

    def export_current_selection(self):
        \"\"\"Export rows currently selected to csv file\"\"\"
        headers = [col.headertext for col in self.tablecolumns]
        selected = self.view.selection()
        records = []
        for iid in selected:
            record: TableRow = self.iidmap.get(iid)
            records.append(record.values)
        self.save_data_to_csv(headers, records, self._delimiter)

    def export_records_in_filter(self):
        \"\"\"Export rows currently filtered to csv file\"\"\"
        headers = [col.headertext for col in self.tablecolumns]
        if not self.is_filtered:
            return
        records = [row.values for row in self.tablerows_filtered]
        self.save_data_to_csv(headers, records, self._delimiter)

    def save_data_to_csv(self, headers, records, delimiter=\",\"):
        \"\"\"Save data records to a csv file.

        Parameters:

            headers (List[str]):
                A list of header labels.

            records (List[Tuple[...]]):
                A list of table records.

            delimiter (str):
                The character to use for delimiting the values.
        \"\"\"
        from tkinter.filedialog import asksaveasfilename
        import csv

        timestamp = datetime.now().strftime(\"%Y%m%d_%H%M%S\")
        initialfile = f\"tabledata_{timestamp}.csv\"
        filetypes = [
            (\"CSV UTF-8 (Comma delimited)\", \"*.csv\"),
            (\"All file types\", \"*.*\"),
        ]
        filename = asksaveasfilename(
            confirmoverwrite=True,
            filetypes=filetypes,
            defaultextension=\"csv\",
            initialfile=initialfile,
        )
        if filename:
            with open(filename, \"w\", encoding=\"utf-8\", newline=\"\") as f:
                writer = csv.writer(f, delimiter=delimiter)
                writer.writerow(headers)
                writer.writerows(records)

    # ROW MOVEMENT

    def move_selected_rows_to_top(self):
        \"\"\"Move the selected rows to the top of the data set\"\"\"
        selected = self.view.selection()
        if len(selected) == 0:
            return

        if self.is_filtered:
            tablerows = self.tablerows_filtered.copy()
        else:
            tablerows = self.tablerows.copy()

        for i, iid in enumerate(selected):
            row = self.iidmap.get(iid)
            tablerows.remove(row)
            tablerows.insert(i, row)

        if self.is_filtered:
            self._tablerows_filtered = tablerows
        else:
            self._tablerows = tablerows

        # refresh the table data
        self.unload_table_data()
        self.load_table_data()

    def move_selected_rows_to_bottom(self):
        \"\"\"Move the selected rows to the bottom of the dataset\"\"\"
        selected = self.view.selection()
        if len(selected) == 0:
            return

        if self.is_filtered:
            tablerows = self.tablerows_filtered.copy()
        else:
            tablerows = self.tablerows.copy()

        for iid in selected:
            row = self.iidmap.get(iid)
            tablerows.remove(row)
            tablerows.append(row)

        if self.is_filtered:
            self._tablerows_filtered = tablerows
        else:
            self._tablerows = tablerows

        # refresh the table data
        self.unload_table_data()
        self.load_table_data()

    def move_selected_row_up(self):
        \"\"\"Move the selected rows up one position in the dataset\"\"\"
        selected = self.view.selection()
        if len(selected) == 0:
            return

        if self.is_filtered:
            tablerows = self._tablerows_filtered.copy()
        else:
            tablerows = self.tablerows.copy()

        for iid in selected:
            row = self.iidmap.get(iid)
            index = tablerows.index(row) - 1
            tablerows.remove(row)
            tablerows.insert(index, row)

        if self.is_filtered:
            self._tablerows_filtered = tablerows
        else:
            self._tablerows = tablerows

        # refresh the table data
        self.unload_table_data()
        self.load_table_data()

    def move_row_down(self):
        \"\"\"Move the selected rows down one position in the dataset\"\"\"
        selected = self.view.selection()
        if len(selected) == 0:
            return

        if self._filtered:
            tablerows = self._tablerows_filtered
        else:
            tablerows = self._tablerows

        for iid in selected:
            row = self.iidmap.get(iid)
            index = tablerows.index(row) + 1
            tablerows.remove(row)
            tablerows.insert(index, row)

        if self._filtered:
            self._tablerows_filtered = tablerows
        else:
            self._tablerows = tablerows

        # refresh the table data
        self.unload_table_data()
        self.load_table_data()

    # COLUMN MOVEMENT

    def move_column_left(self, event=None, cid=None):
        \"\"\"Move column one position to the left. This can be triggered
        by either an event, or by passing in the `cid`, which is the
        index of the column relative to the original data set.

        Parameters:

            event (Event):
                An application click event.

            cid (int):
                A unique column identifier; typically the index of the
                column relative to the original dataset.
        \"\"\"
        if event is not None:
            eo = self._get_event_objects(event)
            column = eo.column
        elif cid is not None:
            column = self.cidmap.get(cid)
        else:
            return

        displaycols = [x.cid for x in self.tablecolumns_visible]
        old_index = column.displayindex
        if old_index == 0:
            return

        new_index = column.displayindex - 1
        displaycols.insert(new_index, displaycols.pop(old_index))
        self.view.configure(displaycolumns=displaycols)

    def move_column_right(self, event=None, cid=None):
        \"\"\"Move column one position to the right. This can be triggered
        by either an event, or by passing in the `cid`, which is the
        index of the column relative to the original data set.

        Parameters:

            event (Event):
                An application click event.

            cid (int):
                A unique column identifier; typically the index of the
                column relative to the original dataset.
        \"\"\"
        if event is not None:
            eo = self._get_event_objects(event)
            column = eo.column
        elif cid is not None:
            column = self.cidmap.get(cid)
        else:
            return

        displaycols = [x.cid for x in self.tablecolumns_visible]
        old_index = column.displayindex
        if old_index == len(displaycols) - 1:
            return

        new_index = old_index + 1
        displaycols.insert(new_index, displaycols.pop(old_index))
        self.view.configure(displaycolumns=displaycols)

    def move_column_to_first(self, event=None, cid=None):
        \"\"\"Move column to leftmost position. This can be triggered by
        either an event, or by passing in the `cid`, which is the index
        of the column relative to the original data set.

        Parameters:

            event (Event):
                An application click event.

            cid (int):
                A unique column identifier; typically the index of the
                column relative to the original dataset.
        \"\"\"
        if event is not None:
            eo = self._get_event_objects(event)
            column = eo.column
        elif cid is not None:
            column = self.cidmap.get(cid)
        else:
            return

        displaycols = [x.cid for x in self.tablecolumns_visible]
        old_index = column.displayindex
        if old_index == 0:
            return

        displaycols.insert(0, displaycols.pop(old_index))
        self.view.configure(displaycolumns=displaycols)

    def move_column_to_last(self, event=None, cid=None):
        \"\"\"Move column to the rightmost position. This can be triggered
        by either an event, or by passing in the `cid`, which is the
        index of the column relative to the original data set.

        Parameters:

            event (Event):
                An application click event.

            cid (int):
                A unique column identifier; typically the index of the
                column relative to the original dataset.
        \"\"\"
        if event is not None:
            eo = self._get_event_objects(event)
            column = eo.column
        elif cid is not None:
            column = self.cidmap.get(cid)
        else:
            return

        displaycols = [x.cid for x in self.tablecolumns_visible]
        old_index = column.displayindex
        if old_index == len(displaycols) - 1:
            return

        new_index = len(displaycols) - 1
        displaycols.insert(new_index, displaycols.pop(old_index))
        self.view.configure(displaycolumns=displaycols)

    # OTHER FORMATTING

    def apply_table_stripes(self, stripecolor):
        \"\"\"Add stripes to even-numbered table rows as indicated by the
        `stripecolor` of (background, foreground). Either element may be
        specified as `None`, but both elements must be present.

        Parameters:

            stripecolor (Tuple[str, str]):
                A tuple of colors to apply to the table stripe. The
                tuple represents (background, foreground).
        \"\"\"
        style: ttk.Style = ttk.Style.get_instance()
        colors = style.colors
        if len(stripecolor) == 2:
            self._stripecolor = stripecolor
            bg, fg = stripecolor
            kw = {}
            if bg is None:
                kw[\"background\"] = colors.active
            else:
                kw[\"background\"] = bg
            if fg is None:
                kw[\"foreground\"] = colors.inputfg
            else:
                kw[\"foreground\"] = fg
            self.view.tag_configure(\"striped\", **kw)

    def autofit_columns(self):
        \"\"\"Autofit all columns in the current view\"\"\"
        f = font.nametofont(\"TkDefaultFont\")
        pad = utility.scale_size(self, 20)
        col_widths = []

        # measure header sizes
        for col in self.tablecolumns:
            width = f.measure(f\"{col._headertext} {DOWNARROW}\") + pad
            col_widths.append(width)

        for row in self.tablerows_visible:
            values = row.values
            for i, value in enumerate(values):
                old_width = col_widths[i]
                new_width = f.measure(str(value)) + pad
                width = max(old_width, new_width)
                col_widths[i] = width

        for i, width in enumerate(col_widths):
            self.view.column(i, width=width)

    # COLUMN AND HEADER ALIGNMENT

    def autoalign_columns(self):
        \"\"\"Align the columns and headers based on the data type of the
        values. Text is left-aligned; numbers are right-aligned. This
        method will have no effect if there is no data in the tables.\"\"\"
        if len(self._tablerows) == 0:
            return

        values = self._tablerows[0]._values
        for i, value in enumerate(values):
            if str(value).isnumeric():
                self.view.column(i, anchor=E)
                self.view.heading(i, anchor=E)
            else:
                self.view.column(i, anchor=W)
                self.view.heading(i, anchor=W)

    def align_column_left(self, event=None, cid=None):
        \"\"\"Left align the column text. This can be triggered by
        either an event, or by passing in the `cid`, which is the index
        of the column relative to the original data set.

        Parameters:

            event (Event):
                An application click event.

            cid (int):
                A unique column identifier; typically the index of the
                column relative to the original dataset.
        \"\"\"
        if event is not None:
            eo = self._get_event_objects(event)
            self.view.column(eo.column.cid, anchor=W)
        elif cid is not None:
            self.view.column(cid, anchor=W)

    def align_column_right(self, event=None, cid=None):
        \"\"\"Right align the column text. This can be triggered by
        either an event, or by passing in the `cid`, which is the index
        of the column relative to the original data set.

        Parameters:

            event (Event):
                An application event.

            cid (int):
                A unique column identifier; typically the index of the
                column relative to the original dataset.
        \"\"\"
        if event is not None:
            eo = self._get_event_objects(event)
            self.view.column(eo.column.cid, anchor=E)
        elif cid is not None:
            self.view.column(cid, anchor=E)

    def align_column_center(self, event=None, cid=None):
        \"\"\"Center align the column text. This can be triggered by
        either an event, or by passing in the `cid`, which is the index
        of the column relative to the original data set.

        Parameters:

            event (Event):
                An application event.

            cid (int):
                A unique column identifier; typically the index of the
                column relative to the original dataset.
        \"\"\"
        if event is not None:
            eo = self._get_event_objects(event)
            self.view.column(eo.column.cid, anchor=CENTER)
        elif cid is not None:
            self.view.column(cid, anchor=CENTER)

    def align_heading_left(self, event=None, cid=None):
        \"\"\"Left align the heading text. This can be triggered by
        either an event, or by passing in the `cid`, which is the index
        of the heading relative to the original data set.

        Parameters:

            event (Event):
                An application event.

            cid (int):
                A unique heading identifier; typically the index of the
                heading relative to the original dataset.
        \"\"\"
        if event is not None:
            eo = self._get_event_objects(event)
            self.view.heading(eo.column.cid, anchor=W)
        elif cid is not None:
            self.view.heading(cid, anchor=W)

    def align_heading_right(self, event=None, cid=None):
        \"\"\"Right align the heading text. This can be triggered by
        either an event, or by passing in the `cid`, which is the index
        of the heading relative to the original data set.

        Parameters:

            event (Event):
                An application event.

            cid (int):
                A unique heading identifier; typically the index of the
                heading relative to the original dataset.
        \"\"\"
        if event is not None:
            eo = self._get_event_objects(event)
            self.view.heading(eo.column.cid, anchor=E)
        elif cid is not None:
            self.view.heading(cid, anchor=E)

    def align_heading_center(self, event=None, cid=None):
        \"\"\"Center align the heading text. This can be triggered by
        either an event, or by passing in the `cid`, which is the index
        of the heading relative to the original data set.

        Parameters:

            event (Event):
                An application event.

            cid (int):
                A unique heading identifier; typically the index of the
                heading relative to the original dataset.
        \"\"\"
        if event is not None:
            eo = self._get_event_objects(event)
            self.view.heading(eo.column.cid, anchor=CENTER)
        elif cid is not None:
            self.view.heading(cid, anchor=CENTER)

    # PRIVATE METHODS

    def _get_event_objects(self, event):
        iid = self.view.identify_row(event.y)
        col = self.view.identify_column(event.x)
        cid = int(self.view.column(col, \"id\"))
        column: TableColumn = self.cidmap.get(cid)
        row: TableRow = self.iidmap.get(iid)
        data = TableEvent(column, row)
        return data

    def _search_table_data(self, _):
        \"\"\"Search the table data for records that meet search criteria.
        Currently, this search locates any records that contain the
        specified text; it is also case insensitive.
        \"\"\"
        criteria = self._searchcriteria.get()
        self._filtered = True
        self.tablerows_filtered.clear()
        self.unload_table_data()
        for row in self.tablerows:
            for col in row.values:
                if str(criteria).lower() in str(col).lower():
                    self.tablerows_filtered.append(row)
                    break
        self._rowindex.set(0)
        self.load_table_data()

    # PRIVATE METHODS - SORTING

    def _column_sort_header_reset(self):
        \"\"\"Remove the sort character from the column headers\"\"\"
        for col in self.tablecolumns:
            self.view.heading(col.cid, text=col.headertext)

    def _column_sort_header_update(self, cid):
        \"\"\"Add sort character to the sorted column\"\"\"
        column: TableColumn = self.cidmap.get(int(cid))
        arrow = UPARROW if column.columnsort == ASCENDING else DOWNARROW
        headertext = f\"{column.headertext} {arrow}\"
        self.view.heading(column.cid, text=headertext)

    # PRIVATE METHODS - WIDGET BUILDERS

    def _build_tableview_widget(self, coldata, rowdata, bootstyle):
        \"\"\"Build the data table\"\"\"
        if self._searchable:
            self._build_search_frame()

        self.view = ttk.Treeview(
            master=self,
            columns=[x for x in range(len(coldata))],
            height=self._height,
            selectmode=EXTENDED,
            show=HEADINGS,
            bootstyle=f\"{bootstyle}-table\",
        )
        self.view.pack(fill=BOTH, expand=YES, side=TOP)
        self.hbar = ttk.Scrollbar(
            master=self, command=self.view.xview, orient=HORIZONTAL
        )
        self.hbar.pack(fill=X)
        self.view.configure(xscrollcommand=self.hbar.set)

        if self._paginated:
            self._build_pagination_frame()

        self.build_table_data(coldata, rowdata)

        self._rightclickmenu_cell = TableCellRightClickMenu(self)
        self._rightclickmenu_head = TableHeaderRightClickMenu(self)
        self._set_widget_binding()

    def _build_search_frame(self):
        \"\"\"Build the search frame containing the search widgets. This
        frame is only created if `searchable=True` when creating the
        widget.
        \"\"\"
        frame = ttk.Frame(self, padding=5)
        frame.pack(fill=X, side=TOP)
        ttk.Label(frame, text=MessageCatalog.translate(\"Search\")).pack(side=LEFT, padx=5)
        searchterm = ttk.Entry(frame, textvariable=self._searchcriteria)
        searchterm.pack(fill=X, side=LEFT, expand=YES)
        searchterm.bind(\"<Return>\", self._search_table_data)
        searchterm.bind(\"<KP_Enter>\", self._search_table_data)
        if not self._paginated:
            ttk.Button(
                frame,
                text=MessageCatalog.translate(\"⎌\"),
                command=self.reset_table,
                style=\"symbol.Link.TButton\",
            ).pack(side=LEFT)

    def _build_pagination_frame(self):
        \"\"\"Build the frame containing the pagination widgets. This
        frame is only built if `pagination=True` when creating the
        widget.
        \"\"\"
        pageframe = ttk.Frame(self)
        pageframe.pack(fill=X, anchor=N)

        ttk.Button(
            pageframe,
            text=MessageCatalog.translate(\"⎌\"),
            command=self.reset_table,
            style=\"symbol.Link.TButton\",
        ).pack(side=RIGHT)

        ttk.Separator(pageframe, orient=VERTICAL).pack(side=RIGHT, padx=10)

        ttk.Button(
            master=pageframe,
            text=\"»\",
            command=self.goto_last_page,
            style=\"symbol.Link.TButton\",
        ).pack(side=RIGHT, fill=Y)
        ttk.Button(
            master=pageframe,
            text=\"›\",
            command=self.goto_next_page,
            style=\"symbol.Link.TButton\",
        ).pack(side=RIGHT, fill=Y)

        ttk.Button(
            master=pageframe,
            text=\"‹\",
            command=self.goto_prev_page,
            style=\"symbol.Link.TButton\",
        ).pack(side=RIGHT, fill=Y)
        ttk.Button(
            master=pageframe,
            text=\"«\",
            command=self.goto_first_page,
            style=\"symbol.Link.TButton\",
        ).pack(side=RIGHT, fill=Y)

        ttk.Separator(pageframe, orient=VERTICAL).pack(side=RIGHT, padx=10)

        lbl = ttk.Label(pageframe, textvariable=self._pagelimit)
        lbl.pack(side=RIGHT, padx=(0, 5))
        ttk.Label(pageframe, text=MessageCatalog.translate(\"of\")).pack(side=RIGHT, padx=(5, 0))

        index = ttk.Entry(pageframe, textvariable=self._pageindex, width=4)
        index.pack(side=RIGHT)
        index.bind(\"<Return>\", self.goto_page, \"+\")
        index.bind(\"<KP_Enter>\", self.goto_page, \"+\")

        ttk.Label(pageframe, text=MessageCatalog.translate(\"Page\")).pack(side=RIGHT, padx=5)

    def _build_table_rows(self, rowdata):
        \"\"\"Build, load, and configure the DataTableRow objects

        Parameters:

            rowdata (List):
                An iterable of row data
        \"\"\"
        for row in rowdata:
            self.insert_row(END, row)

    def _build_table_columns(self, coldata):
        \"\"\"Build, load, and configure the DataTableColumn objects

        Parameters:

            coldata (List[str|Dict[str, Any]]):
                An iterable of column names or a dictionary of column
                configuration settings.
        \"\"\"
        for cid, col in enumerate(coldata):
            if isinstance(col, str):
                self.tablecolumns.append(
                    TableColumn(
                        tableview=self,
                        cid=cid,
                        text=col,
                    )
                )
            else:
                if \"text\" not in col:
                    col[\"text\"] = f\"Column {cid}\"
                self.tablecolumns.append(
                    TableColumn(tableview=self, cid=cid, **col)
                )

    # PRIVATE METHODS - WIDGET BINDING

    def _set_widget_binding(self):
        \"\"\"Setup the widget binding\"\"\"
        self.view.bind(\"<Double-Button-1>\", self._header_double_leftclick)
        self.view.bind(\"<Button-1>\", self._header_leftclick)
        if self.tk.call(\"tk\", \"windowingsystem\") == \"aqua\":
            sequence = \"<Button-2>\"
        else:
            sequence = \"<Button-3>\"
        self.view.bind(sequence, self._table_rightclick)

        # add trace to track pagesize changes
        self._pagesize.trace_add(\"write\", self._trace_pagesize)

    # def _select_pagesize(self, event):
    #     cbo: ttk.Combobox = self.nametowidget(event.widget)
    #     cbo.select_clear()
    #     self.goto_first_page()

    def _trace_pagesize(self, *_):
        \"\"\"Callback for changes to page size\"\"\"
        self.goto_first_page()

    def _header_double_leftclick(self, event):
        \"\"\"Callback for double-click events on the tableview header\"\"\"
        region = self.view.identify_region(event.x, event.y)
        if region == \"separator\":
            self.autofit_columns()

    def _header_leftclick(self, event):
        \"\"\"Callback for left-click events\"\"\"
        region = self.view.identify_region(event.x, event.y)
        if region == \"heading\":
            self.sort_column_data(event)

    def _table_rightclick(self, event):
        \"\"\"Callback for right-click events\"\"\"
        region = self.view.identify_region(event.x, event.y)
        if region == \"heading\":
            self._rightclickmenu_head.tk_popup(event)
        elif region != \"separator\":
            self._rightclickmenu_cell.tk_popup(event)


class TableCellRightClickMenu(tk.Menu):
    \"\"\"A right-click menu object for the tableview cells - INTERNAL\"\"\"

    def __init__(self, master: Tableview):
        \"\"\"
        Parameters:

            master (Tableview):
                The parent object
        \"\"\"
        super().__init__(master, tearoff=False)
        self.master: Tableview = master
        self.view: ttk.Treeview = master.view
        self.cid = None
        self.iid = None

        config = {
            \"sortascending\": {
                \"label\": f'''⬆  {MessageCatalog.translate(\"Sort Ascending\")}''',
                \"command\": self.sort_column_ascending,
            },
            \"sortdescending\": {
                \"label\": f'''⬇  {MessageCatalog.translate(\"Sort Descending\")}''',
                \"command\": self.sort_column_descending,
            },
            \"clearfilter\": {
                \"label\": f'''{MessageCatalog.translate(\"⎌\")} {MessageCatalog.translate(\"Clear filters\")}''',
                \"command\": self.master.reset_row_filters,
            },
            \"filterbyvalue\": {
                \"label\": f'''{MessageCatalog.translate(\"Filter by cell's value\")}''',
                \"command\": self.filter_to_cell_value,
            },
            \"hiderows\": {
                \"label\": f'''{MessageCatalog.translate(\"Hide select rows\")}''',
                \"command\": self.hide_selected_rows,
            },
            \"showrows\": {
                \"label\": f'''{MessageCatalog.translate(\"Show only select rows\")}''',
                \"command\": self.filter_to_selected_rows,
            },
            \"exportall\": {
                \"label\": f'''{MessageCatalog.translate(\"Export all records\")}''',
                \"command\": self.export_all_records,
            },
            \"exportpage\": {
                \"label\": f'''{MessageCatalog.translate(\"Export current page\")}''',
                \"command\": self.export_current_page,
            },
            \"exportselection\": {
                \"label\": f'''{MessageCatalog.translate(\"Export current selection\")}''',
                \"command\": self.export_current_selection,
            },
            \"exportfiltered\": {
                \"label\": f'''{MessageCatalog.translate(\"Export records in filter\")}''',
                \"command\": self.export_records_in_filter,
            },
            \"moveup\": {
                \"label\": f'''↑ {MessageCatalog.translate(\"Move up\")}''',
                \"command\": self.move_row_up
            },
            \"movedown\": {
                \"label\": f'''↓ {MessageCatalog.translate(\"Move down\")}''',
                \"command\": self.move_row_down,
            },
            \"movetotop\": {
                \"label\": f'''⤒ {MessageCatalog.translate(\"Move to top\")}''',
                \"command\": self.move_row_to_top,
            },
            \"movetobottom\": {
                \"label\": f'''⤓ {MessageCatalog.translate(\"Move to bottom\")}''',
                \"command\": self.move_row_to_bottom,
            },
            \"alignleft\": {
                \"label\": f'''◧  {MessageCatalog.translate(\"Align left\")}''',
                \"command\": self.align_column_left,
            },
            \"aligncenter\": {
                \"label\": f'''◫  {MessageCatalog.translate(\"Align center\")}''',
                \"command\": self.align_column_center,
            },
            \"alignright\": {
                \"label\": f'''◨  {MessageCatalog.translate(\"Align right\")}''',
                \"command\": self.align_column_right,
            },
            \"deleterows\": {
                \"label\": f'''🞨  {MessageCatalog.translate(\"Delete selected rows\")}''',
                \"command\": self.delete_selected_rows,
            },
        }
        sort_menu = tk.Menu(self, tearoff=False)
        sort_menu.add_command(cnf=config[\"sortascending\"])
        sort_menu.add_command(cnf=config[\"sortdescending\"])
        self.add_cascade(menu=sort_menu, label=f'''⇅  {MessageCatalog.translate(\"Sort\")}''')

        filter_menu = tk.Menu(self, tearoff=False)
        filter_menu.add_command(cnf=config[\"clearfilter\"])
        filter_menu.add_separator()
        filter_menu.add_command(cnf=config[\"filterbyvalue\"])
        filter_menu.add_command(cnf=config[\"hiderows\"])
        filter_menu.add_command(cnf=config[\"showrows\"])
        self.add_cascade(menu=filter_menu, label=f'''⧨  {MessageCatalog.translate(\"Filter\")}''')

        export_menu = tk.Menu(self, tearoff=False)
        export_menu.add_command(cnf=config[\"exportall\"])
        export_menu.add_command(cnf=config[\"exportpage\"])
        export_menu.add_command(cnf=config[\"exportselection\"])
        export_menu.add_command(cnf=config[\"exportfiltered\"])
        self.add_cascade(menu=export_menu, label=f'''↔  {MessageCatalog.translate(\"Export\")}''')

        move_menu = tk.Menu(self, tearoff=False)
        move_menu.add_command(cnf=config[\"moveup\"])
        move_menu.add_command(cnf=config[\"movedown\"])
        move_menu.add_command(cnf=config[\"movetotop\"])
        move_menu.add_command(cnf=config[\"movetobottom\"])
        self.add_cascade(menu=move_menu, label=f'''⇵  {MessageCatalog.translate(\"Move\")}''')

        align_menu = tk.Menu(self, tearoff=False)
        align_menu.add_command(cnf=config[\"alignleft\"])
        align_menu.add_command(cnf=config[\"aligncenter\"])
        align_menu.add_command(cnf=config[\"alignright\"])
        self.add_cascade(menu=align_menu, label=f'''↦  {MessageCatalog.translate(\"Align\")}''')
        self.add_command(cnf=config[\"deleterows\"])

    def tk_popup(self, event):
        \"\"\"Display the menu below the selected cell.

        Parameters:

            event (Event):
                The click event that triggers menu.
        \"\"\"
        # capture the column and item that invoked the menu
        self.event = event
        iid = self.view.identify_row(event.y)
        col = self.view.identify_column(event.x)

        # show the menu below the invoking cell
        rootx = self.view.winfo_rootx()
        rooty = self.view.winfo_rooty()
        try:
            bbox = self.view.bbox(iid, col)
        except:
            return
        try:
            super().tk_popup(rootx + bbox[0], rooty + bbox[1] + bbox[3])
        except IndexError:
            pass

    def sort_column_ascending(self):
        \"\"\"Sort the column in ascending order.\"\"\"
        self.master.sort_column_data(self.event, sort=ASCENDING)

    def sort_column_descending(self):
        \"\"\"Sort the column in descending order.\"\"\"
        self.master.sort_column_data(self.event, sort=DESCENDING)

    def filter_to_cell_value(self):
        \"\"\"Hide all records except for records where the current
        column exactly matches the current cell value.\"\"\"
        self.master.filter_column_to_value(self.event)

    def filter_to_selected_rows(self):
        \"\"\"Hide all records except for the selected rows.\"\"\"
        self.master.filter_to_selected_rows()

    def export_all_records(self):
        \"\"\"Export all records to a csv file\"\"\"
        self.master.export_all_records()

    def export_current_page(self):
        \"\"\"Export records on current page\"\"\"
        self.master.export_current_page()

    def export_current_selection(self):
        \"\"\"Export rows currently selected\"\"\"
        self.master.export_current_selection()

    def export_records_in_filter(self):
        \"\"\"Export rows currently filtered\"\"\"
        self.master.export_records_in_filter()

    def hide_selected_rows(self):
        \"\"\"Hide the selected rows\"\"\"
        self.master.hide_selected_rows()

    def move_row_to_top(self):
        \"\"\"Move the row to the top of the data set\"\"\"
        self.master.move_selected_rows_to_top()

    def move_row_to_bottom(self):
        \"\"\"Move the row to the bottom of the dataset\"\"\"
        self.master.move_selected_rows_to_bottom()

    def move_row_up(self):
        \"\"\"Move the selected above the previous sibling\"\"\"
        self.master.move_selected_row_up()

    def move_row_down(self):
        \"\"\"Move the selected row below the next sibling\"\"\"
        self.master.move_row_down()

    def align_column_left(self):
        \"Left align the column text\"
        self.master.align_column_left(self.event)

    def align_column_right(self):
        \"\"\"Right align the column text\"\"\"
        self.master.align_column_right(self.event)

    def align_column_center(self):
        \"\"\"Center align the column text\"\"\"
        self.master.align_column_center(self.event)

    def delete_selected_rows(self):
        \"\"\"Delete the selected rows\"\"\"
        iids = self.view.selection()
        if len(iids) > 0:
            # setting to prev should be in master?
            prev_item = self.view.prev(iids[0])
            self.master.delete_rows(iids=iids)
            self.view.focus(prev_item)
            self.view.selection_set(prev_item)


class TableHeaderRightClickMenu(tk.Menu):
    \"\"\"A right-click menu object for the tableview header - INTERNAL\"\"\"

    def __init__(self, master: Tableview):
        \"\"\"
        Parameters:

            master (Tableview):
                The parent object
        \"\"\"
        super().__init__(master, tearoff=False)
        self.master: Tableview = self.master
        self.view: ttk.Treeview = master.view
        self.event = None
        self.columnvars = []
        self._show_menu = None

        config = {
            \"movetoright\": {
                \"label\": f'''→  {MessageCatalog.translate(\"Move to right\")}''',
                \"command\": self.move_column_right,
            },
            \"movetoleft\": {
                \"label\": f'''←  {MessageCatalog.translate(\"Move to left\")}''',
                \"command\": self.move_column_left,
            },
            \"movetofirst\": {
                \"label\": f'''⇤  {MessageCatalog.translate(\"Move to first\")}''',
                \"command\": self.move_column_to_first,
            },
            \"movetolast\": {
                \"label\": f'''⇥  {MessageCatalog.translate(\"Move to last\")}''',
                \"command\": self.move_column_to_last,
            },
            \"alignleft\": {
                \"label\": f'''◧  {MessageCatalog.translate(\"Align left\")}''',
                \"command\": self.align_heading_left,
            },
            \"alignright\": {
                \"label\": f'''◨  {MessageCatalog.translate(\"Align right\")}''',
                \"command\": self.align_heading_right,
            },
            \"aligncenter\": {
                \"label\": f'''◫  {MessageCatalog.translate(\"Align center\")}''',
                \"command\": self.align_heading_center,
            },
            \"resettable\": {
                \"label\": f'''{MessageCatalog.translate(\"⎌\")}  {MessageCatalog.translate(\"Reset table\")}''',
                \"command\": self.master.reset_table,
            },
            \"deletecolumn\": {
                \"label\": f'''🞨  {MessageCatalog.translate(\"Delete column\")}''',
                \"command\": self.delete_column,
            },
            \"hidecolumn\": {
                \"label\": f'''◑  {MessageCatalog.translate(\"Hide column\")}''',
                \"command\": self.hide_column,
            },
        }

        self.add_command(cnf=config[\"resettable\"])

        # HIDE & SHOW
        self._build_show_menu()
        self.add_cascade(menu=self._show_menu, label=f'''±  {MessageCatalog.translate(\"Columns\")}''')
        self.add_separator()

        # MOVE MENU
        move_menu = tk.Menu(self, tearoff=False)
        move_menu.add_command(cnf=config[\"movetoleft\"])
        move_menu.add_command(cnf=config[\"movetoright\"])
        move_menu.add_command(cnf=config[\"movetofirst\"])
        move_menu.add_command(cnf=config[\"movetolast\"])
        self.add_cascade(menu=move_menu, label=f'''⇄  {MessageCatalog.translate(\"Move\")}''')

        align_menu = tk.Menu(self, tearoff=False)
        align_menu.add_command(cnf=config[\"alignleft\"])
        align_menu.add_command(cnf=config[\"aligncenter\"])
        align_menu.add_command(cnf=config[\"alignright\"])
        self.add_cascade(menu=align_menu, label=f'''↦  {MessageCatalog.translate(\"Align\")}''')
        self.add_command(cnf=config[\"hidecolumn\"])
        self.add_command(cnf=config[\"deletecolumn\"])

    def tk_popup(self, event):
        # capture the column and item that invoked the menu
        self.event = event
        self._build_show_menu()

        # show the menu below the invoking cell
        rootx = self.view.winfo_rootx()
        rooty = self.view.winfo_rooty()
        super().tk_popup(rootx + event.x, rooty + event.y + 10)

    def _build_show_menu(self):
        \"\"\"Build the show menu based on currently available columns\"\"\"
        if self._show_menu is not None:
            self._show_menu.delete(0, END)
        else:
            self._show_menu = tk.Menu(self, tearoff=False)

        self._show_menu.add_command(
            label=MessageCatalog.translate(\"Show All\"), command=self.show_all_columns
        )
        self._show_menu.add_separator()

        displaycolumns = [x.cid for x in self.master.tablecolumns_visible]
        for column in self.master.tablecolumns:
            varname = f\"column_{column.cid}\"
            # self.columnvars.append(tk.Variable(name=varname, value=True))
            self._show_menu.add_checkbutton(
                label=column._headertext,
                command=lambda w=column: self.toggle_columns(w.cid),
                variable=varname,
                onvalue=True,
                offvalue=False,
            )
            if column.cid in displaycolumns:
                self.setvar(varname, True)
            else:
                self.setvar(varname, False)

    def toggle_columns(self, cid):
        \"\"\"Toggles the visibility of the selected column\"\"\"
        variable = f\"column_{cid}\"
        toggled = self.getvar(variable)
        if toggled:
            self.master.unhide_selected_column(cid=int(cid))
        else:
            self.master.hide_selected_column(cid=int(cid))

    def show_all_columns(self):
        \"\"\"Show all columns\"\"\"
        for var in self.columnvars:
            var.set(value=True)
        self.master.reset_column_filters()

    def move_column_left(self):
        \"\"\"Move column one position to the left\"\"\"
        self.master.move_column_left(self.event)

    def move_column_right(self):
        \"\"\"Move column on position to the right\"\"\"
        self.master.move_column_right(self.event)

    def move_column_to_first(self):
        \"\"\"Move column to leftmost position\"\"\"
        self.master.move_column_to_first(self.event)

    def move_column_to_last(self):
        \"\"\"Move column to rightmost position\"\"\"
        self.master.move_column_to_last(self.event)

    def align_heading_left(self):
        \"\"\"Left align the column header\"\"\"
        self.master.align_heading_left(self.event)

    def align_heading_right(self):
        \"\"\"Right align the column header\"\"\"
        self.master.align_heading_right(self.event)

    def align_heading_center(self):
        \"\"\"Center align the column header\"\"\"
        self.master.align_heading_center(self.event)

    def delete_column(self):
        \"\"\"Delete the selected column\"\"\"
        eo = self.master._get_event_objects(self.event)
        eo.column.delete()

    def hide_column(self):
        \"\"\"Hide the selected column\"\"\"
        eo = self.master._get_event_objects(self.event)
        eo.column.hide()
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/publisher.py": """from enum import Enum
from typing import List


class Channel(Enum):
    \"\"\"A grouping for Publisher subscribers. Indicates whether the
    widget is a legacy `STD` tk widget or a styled `TTK` widget.

    Attributes:

        STD (1):
            Legacy tkinter widgets.

        TTK (2):
            Themed tkinter widgets.
    \"\"\"

    STD = 1
    TTK = 2


class Subscriber:
    \"\"\"A subcriber data class used to store information about a specific
    subcriber to the `Publisher`.\"\"\"

    def __init__(self, name, func, channel):
        \"\"\"Create a subscriber.

        Parameters:

            name (str):
                The name of the subscriber

            func (Callable):
                The function to call when messaging.

            channel (Channel):
                The subscription channel.
        \"\"\"
        self.name = name
        self.func = func
        self.channel = channel


class Publisher:
    \"\"\"A class used to publish events for widget updates for theme changes
    or configurations\"\"\"

    __subscribers = {}

    @staticmethod
    def subscriber_count():
        return len(Publisher.__subscribers)

    @staticmethod
    def subscribe(name, func, channel):
        \"\"\"Subscribe to an event.

        Parameters:

            name (str):
                The widget's tkinter/tcl name.

            func (Callable):
                A function to call when passing a message.

            channel (Channel):
                Indicates the channel grouping the subscribers.
        \"\"\"
        subs = Publisher.__subscribers
        subs[name] = Subscriber(name, func, channel)

    @staticmethod
    def unsubscribe(name):
        \"\"\"Remove a subscriber

        Parameters:

            name (str):
                The widget's tkinter/tcl name.
        \"\"\"
        subs = Publisher.__subscribers
        try:
            del subs[str(name)]
        except:
            pass

    def get_subscribers(channel):
        \"\"\"Return a list of subscribers

        Returns:

            List:
                List of key-value tuples
        \"\"\"
        subs = Publisher.__subscribers.values()
        channel_subs = [s for s in subs if s.channel == channel]
        return channel_subs

    def publish_message(channel, *args):
        \"\"\"Publish a message to all subscribers

        Parameters:

            channel (Channel):
                The name of the channel to subscribe.

            **args:
                optional arguments to pass to the subscribers.
        \"\"\"
        subs: List[Subscriber] = Publisher.get_subscribers(channel)
        for sub in subs:
            sub.func(*args)

    @staticmethod
    def clear_subscribers():
        \"\"\"Reset all subscriptions.\"\"\"
        Publisher.__subscribers.clear()
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/icons.py": """\"\"\"
    A module various classes that can be used either in text as `Emoji` 
    or in the tkinter.PhotoImage class as in `Icon`.
\"\"\"


class Icon:
    \"\"\"A container class that contains base64 image attributes that can
    be used in the `PhotoImage` class using the `data` parameter.

    Attributes:

        icon (str): The ttkbootstrap icon.
        error (str): An error image.
        warning (str): A warning image.
        question (str): A question image.
        info (str): An info image.

    Examples:

        ```python
        img = tk.PhotoImage(data=Icon.warning)
        ```
    \"\"\"

    icon = \"iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFxEAABcRAcom8z8AAAT/SURBVFhHzZd9TNR1HMff/O64BwKOp+NRnkIScJI2n7ZqFmqjVhkrHExrrDFZLnPkqmEyW2WtlQ1SQawWPSAYiJLNGvK0VhJOaDgVBDPCw0PwEOUQfsfd/fp+v/cFbt0Bd6yxXvfP5+F79/l+P9+H+3w8wMnO3r40I+P5vOCQ4I1ymVzrQeCu/wSJYDabB/sHbp45XlnzQUnJgcvcBRQUHEjX6/vH6aCFQK/XjxcWHnyBxpbRle/Ysf3n0NAQJTWMmiRUnB/FNy1GNHaNYdwsIS7IE4JdPqxWKxoam3D0aAVq6+rR39+P2NhYKBQKPsJGx3Abyq8dxGldBbrvXkSoVyR8Pf3g7e0tj46O2mQ0Gqs96urqv1u/PmUL/cLfQ2a8/O0t9A2b2Q9MsjpGicOZQfBSeEAURbyZtxstLee410awVovCgk8RGxPD9NLuT1B6dT+TJ/EUFMhL/gwpYZuYXl/fUCbQPaeKVQJyqwwOwSnnekR8VDvM5JIjnzsEpwwMDmL32/mwWCxoHqhzCE6ZsJrw4YWduHGvh+k0tkAPHFXadSZc1k8whzNOtt+DcWwCJ2p+4BZH/urpwfnWNpzs/YpbHJmwivjxehmTaWxh8rTT9M+GSM7CpZ5BjI2NcYtzdH069PEVzsSkn8YWmETQek+JTpER9/3h/pDL5dzinKDAQAQqg7nmHHv/VNRV5KCFaWRcc2RdvBpajRopjz/GLY4EBARgzerVeCKc3TCneJDPxohp/9QEFDIPfJwWwE76v1nkL8fep/yYnLvzNURFRTLZHqVSib35e6BSqfDkokysC32ae6ahwbPidyFRs4JbiK2jo1NKSFjCVaDHYMaRX0fQ3mcikwIeiVMh+2EfaNTTW2Q0jqKsvBxnzzaza5mYmICXXtw6dQUpVslK7n85ztyogkEcQIRXLNKis7BWu4GPADo7rzhOYCGZ9wQmxi249NN19P5xCxaTFdo4XyQ/Gw3fEDUf4RrzmoA4MoFT77RiqNfILTY8VTKk5i1HWJI/t8wNncDsd88JzV93OQSn0Kw0FF5kGXEHtyZgJj/+5283uebI6JAI3QUD11zDrQmIIyZYzLOvcNQgcsk13JqASqOAXDnzY0XxcfMgujUBmVzAkpRwrjmiCfNCxLIArrmG24dwzZbFTk+6mmRnw+vLIJAX1R3m9Q5IpHjo/kWP3jYDOZgW9g4sTY2EyseTj3CN/8VL6PYWMO70A1W7gHeTgfzFwBcZpBpp4U7OuAl4jxQm8ZvJ/pB/0IeygC9P0fKYD7DhfgaGeoFDzwAjA9zAEcjtyDwEPEjqPZFUVqm5QFMbd9rxShpQ9AYT55eBmj2OwSlWC1D9Fln5XaC42nlwSvEJoLGVK+7eApE8wVcauOKEsTtAVxPwfT03zMCxab9AGwUuz834iG2lszF6GzCQLMzGkM1PYwu0XWKaK/iQAlqt4coMhDwAJE0XJk7hfhpboL0a01xBIAXpo9u44oRIUmrFriV1G7kV9q2UPb73AdueYyKNLfNSazpXrlyRTdslZp2LmFXAbR2gn+4tGSHkJmWVkgz5AtGhpOsgT3ItaWBIGzeFnw9QuQ9YHk/bObG4qGgrs9NGkTaMdE9c5trvknR6nyTV5EtS23HS+pq4w46rOkl6v1SSXt0vSQXHJGlwmJltzWkhK42n8pSTk5OUnr5598K055WkPS8hKQT+AVyRrtzM5URAAAAAAElFTkSuQmCC\"
    error = \"iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAABmJLR0QA/wD/AP+gvaeTAAAEc0lEQVRIDcVXbU8bRxCee7MxkGBTSIJt0UAjRES+tKDKUfoFm5I0UVuFUKr+h/ZTf0Wr/pK2BFlKKkUmqOqHJKC8NFKiJKqJAEGNgRIIAcy97PWZde8EfgGnQcLy7M0+MzvP7e3ezB7REf2UWnnvDAx8qKrqkKZpl1zXPSWECJPrkqppa6Qoi2Tbv1lEYxcymT9ribkvsUukTKZSXyua9pNmGMcj8Xhd04kThh4Mkm4YMr5tWWTv7NDrfN5cXVgwhW2vOY7zfWJ8/BcERwjpVtbAVoZJAIRdrqalA6FQPN7T03istVXiBzWvl5dp4enTN2ahMOdY1hcXJiamK42pSDyZTCZJ19PR7u76lo4OtdLAg7Clly/F4osXW1iSz8+Pj/9OJb8y4nupVD8e7c2Ovr5QrbMsiel3efYz9+9v27Z9CTP/wzdA2UM81d/f4+r65AeJRENDczPM7/7fXF2l7NTUBgnRm8hk/vIiqp6CXaBQMPhz7Ny50GGRcmyOFcOS4W34VXIwCPGJ7w4MfBOsr29/r73dx2A/lH/L6dOaEQp13hscHPECShK+E9zRD21nzzZ6htKrduYMKXV1pbDfV0IhYh8fKFE4tqYoP3qwJL6TSvXhPW061tLi4XuuWlcXGVeuUODaNWKCPUZ0GGMb+7AvoLL/cbyOqmFE7iaTH7FREuua9lUkFqs6HTE7S2JpiRQMDoyMkNLQwGOlsC4x3DT7OPCVhgpNpK0tiDdmmE2SGJ1PMdtiKmK0RFxkJvP6dRL5PCmRCAWGhyW5JGUdGNvYh+BbMtzv4vUM4MkOMqBzg61+ChlKqlUbBOTAgaEhUk+eJJ4l+ypNTfKG2LYfKftig5ErRJR1OWN0Ipx/GdhX/iMXSItMyOJCr4WU4xrYnK7jNLMuiVmpVRQUBxbfn/t68cH5WA2KJFZUdZUrzEH+SmNjcX3DYbnZeDMp0L01P2i8hScGrn/YzyPOW9vb3K8qe0gXF8kcHZUioPsbDjdWNQAM1tYWYSPnoJIkRv28sYZ6ykAlKSMdGyO5kTADE3qt5KjZBdTrG8xRJHbd0fVczmSgkqjRKHkbyUqni6SeI8gZc1dWpA/7eqbS66tcznGEGGVcVidOmVMXL8519PbG8a4xXiacDsX8PLmFQpmNAc5eaixGTjbL3TLhEjn74MHcx7duvc9GOWOwu45tfzf/5MkbnKcYLxMOWI2UnV3sEfZhvVQ45vzjx5s4kXzr2SQxd87fvp22TXNueWZGcP8wZWV62hGOM52YmJDry7F9Yp61ZZqXc8+ebawjNbLxMGQduz6Xza7vOM5nzOHF9IkZwPEE1UBcnX34cHsDGYmxdxG5ro8ebeMkevWTTObv3bFwE7u7RV0e9jRtrK27u661szNQRN+uxWHPzD1/XsD6flnTYc8LfyTHW4/c3XWgV3U9HI5GAyjoRgD12KtmJrLRzuYm4bFanAtQBF4hIf3/A71H7l13fcJcRjWLYpe2sA2fMCv4tFlARrppvcUnDI89EvkXuxHzVm+w/WUAAAAASUVORK5CYII=\"
    warning = \"iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAABmJLR0QA/wD/AP+gvaeTAAADO0lEQVRIDe1V3UtTYRh/P87HPo815+zoNlHb5tzUbTmnQiUU6QZGBN4UBBURIgR1E9TNkkIi8SIw2BKi226iG5cfMKiLoIT+hO4qRSIIg3Tb6TxHtpbbzs4RIogO5znvc37P7/n9zns+3oPQX9rwfnyz8yOWvMl8nyAs7dDtm6MXlrf06jB6G4BfMAtPmhziOEIS2tz42CxjE3Lo2okutkxeWkgcIwTHg9EhPhAd5gmhccDkkq5dl3EymSQMJQu+3n4ToRRROSAHDGp6nHUZDzvfXjJbG0TR3VZ6NyA3WQVxyPXu4h8xXkmdbJBv8aw/PGBBCJd5YNQdjlkYgmeBU1ZQTTXPmLLGaYfTzQkHbRWCgDW1unjCGZNI46bJeDWd8EpYuuLrCRtr6e7WpKvArcUpxzUZE54+6vAFOY7/5Rs7+wxBFMWg1uELcIRn5ouY2ljXeCU9NkopG3N7/VRNCGpubzelDDMIPXCuFqrGa6kjLGGZtD/UbyFElap4AKerL2qBnmxyRHVxUlX7yjZPCgdstqYWlyKs5eBocSLoybnMk2r8msbZ1LgdY3LXH4nJn4+aRGXNHxmwEIzvrT490VhZ3UVqGhd4NCO621mzVdhl6jjKiwwS29pZjIwztdqqGq+kEj3y+n/ucCBkqNVYD1d6C/i8olWFXNWYGuhjT7DPwHJclRZtEPR6gr0GytN0tY4K4+X02GmWMwScHd6KWjUBNczZ4SMszweXFuLje3nliy5afBjnOYH5EB48Ltoc8JvdS9d//mVjHb1/k/20/a3QnriW+VFU+G1WnAXfsDXaBS2mnze/I4iiUK0RtGyNDoG34uvlnJLxy9SoiBG51RUaMJcTquVgODG1iCamMmhdvoBqnHKsKyxrSuQ2eBTxkjFn4GZdnV7WaNbw2UpSsV9++UtpzQQ0nZ0eluP5B0WS8oxX02NRynPZo/EzZsqwxZrqCLMGwiG7CYa6kc/toFeZ51u5XH7k1OXFNWXGhOPmPMGQUaspuIAhBORaArS9gYiRpcwc8BXjQj4fsYutSg7gnwrwyBdyEdBX/iCUkOnXmRfTUqGw/xUD1OoEJmSbEuZOHdr/8j9yB34CUBepV8n7RlcAAAAASUVORK5CYII=\"
    question = \"iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAABmJLR0QA/wD/AP+gvaeTAAAEvElEQVRIDcVX208cVRj/5sxlB1j2Aiyy2lpgEZVaUvXBeIvERCOwC1Qlvhj/gcYnE1PAR1tsU598bOK7sV6A3ZVEX9pqE32yFzDKdlkS6ILslUXYmT0z4zlnmbLtzt76oJPznXO+y+/7zsy5fQPwPz1cvXEnpkMnDZ4/JSA0AobRpem6i2J5hDKAuLiGtTAu4O+C5wM3qLwW1QhscIHp8KTAo88FQXR2dnps7rY2SRIFEAWB+S5gDGoBQzqVVLf+TigYa2kDax/NzQ5/A8AZzMiiqhh47MxiHxKNOZvNdsTn8zncLqcFvFyUTmcgEo3m1Ly6RgY1HvrMHy23IkOyEk58sjDEceL33d3HWr1eL+IqDs8KTWUGbGzEtVhsbdfQtMDcrP8alZZSmcvAVPg1XkTzJ5453upobS3Tl4Jr9bM7OWNpaXkHa7p/4ezwz6X29zk+NRXqB4H/dXDwhMtubym1e+j+7u4u3Lh5K40N/ELw08CK6UgwOwAGB/zi1729PS3VgjpkBENPy3DUXYSupzFc+TMPmT390FVJz263Q09Pt31tNfYVADxHiBXEalKNTYfea25ufryr6xGRsJallQT94GU79BOTJokDSk+Q/vsv2oHqLEFE+KjXK9pkuXd8KvwuYVk5CGxwCAkXen09bG8yjUX1OnlTWeQguo3h0pUcXLqaY30qG3pKtkAcinx9PifiuYumhAUemwk/L0mCgzym3LI91l78vD8u7UN2X4cs+bw/Le8z2+6Ooo4xFpXT4QBRFF1jZ8LPUjULjBA36fF4mqmgGklCcS3m8ofzWdAOzoiDphre0+lpQgI3SW3YMBEnvOFyuyrOLTWkdHExS5v76ORRifFbOY211Sqn0yltxjffJDbT7I3B0L02SSJ8Y8XXKcJLfcW5/S2q1ATLsg3It/JSQxaYHPhuSbJRvm5qa0EwOtgE9FS7HslDLIFrYiXycrqmtVNDFph2GqVX+2Wgc35rXYXrEaUBeHGdsMCI51Oq2ggY4GgbWx5w9a983UEVRQHEoyQFFANzsKWoKuXrJrp3qfG+WsdypoaEFEUFEjBOusCGXcB6MJlIDbjIqqPCeshqhdfCpVKpPFlPQWpHBgCgY3w5kdhu7JUpukHaTmxrBV27TGEscPC8/6amGelMtnyfUiMr6rDzQMlKZyWjCYKO9UTonP821bPAJB8wsI4/jKxEdow6poxuJXpZUHKTbUUdVScDViJ3cpqunTbtDgIDLJwdmVcVNba1tVkwlfW0xc1R3fJufLOgFdTI/Dl/yLRki6vIcIamzg1H76z+Tq6wDrfLVdFn6h8dvryWY7BK9zBTkiqZShmrq7Es0rhRwt4rZc5Z6sNzoYHjA80kwSvT30PW0UlnMsby0h975B55q2rqY/oKzPzwCrmI5rpJ5kCSPYkei6auvtaA9Y14PrZGkj1sTMzPjvzyII57UGDyb38cPgIy+laUpCcfJr3FamEJ5/PvzF8Yv2v6LG0rBjaNAjOhcQEJX/A8cne0t5OE3iXKsgyUqI2i5GF/Lw+pTEZNJhIFklEmyV/F6YXZ0SDVV6KagU2g+Qsj8tyorhmPkROogySIwCM+QVKaDUxOv0Z+YUy//3n7L6y2u/Lkn4gSAAAAAElFTkSuQmCC\"
    info = \"iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAABmJLR0QA/wD/AP+gvaeTAAADzElEQVRIDcWXzXPbRBTAn7SSrJbEH8Vp4rjFjjPDUCgz0PbMDMwAwRknE4aP4dpe4QSHEigHSDNDp/9C+wfQr6RNTLgxvXGDoaEpxDSJmzYhtpSPUluydpd9InJE4yTqpCYaPe3Te2/fb3dlrZ8A9uiQgnL7TudfVQh/V1LUHuC8gzIWxb5ElpdBkhYcxvISpddGhnt/RvtOsgOYS32D4x8SQs4TRQ23H4zrsQPPqpqqgKoobu6a40DNroFhmvbi4l82pXTZofTTG8PZSwASd4MaXLYED3w+/jwoZFTT1EPd3d0tsVi0QffNJtM0oVC4+9CyrTmxMn0jQ9nC5igxpEbG3Jf5NxSQR1Pp1P5kskPeIqxR13Ubh/n5+2x2pviIQy03MpT7ER47Ns24b3DsdSKT8SMvHtkXdJaP5azf4uxv/zZVoZz1XD/be7PuEMp/wLkzEy8Rzn86+vLRZyLhVuHe/bm6sgq3JifXatw5PjaU+8PLKHsKAJcUCb7LZLr2BYGGdRlQNvo31sKRMKS60vs1Wb2MDC+qDu4/k/9ID+nPJRL4TD134xaBp15rhZNCWsUAGkdtWJOJBAmF9Ez/F99/4FnXwVySgXybyaRbPMe2re8B+dRtu3R1pVokIp/zglxw7vTECaIokWg02CuzWmFw4eYaXBSyWmVerm3bWCwm3k4llhu8cQwDXbCssPfbD7bpaAgqCEQJGo9x7W1tISIr76Hubj+KrL4ppquiIYh81hOph52fWKnrOymRaERbWFh4S8QNujPmnHXoIU3cBzufBObPqOshYJx3os0Fiw0/pmkhvG+qaJoGjPEDCHHBqPzf4oJlQgzbtprOtiwLZCKXEfQvWIJFy7bxvqliWTYI4AOEiBaAOmzMKBlNJxumURW/p7E6GDi7slQqNR28tLREucSu1MEjw9lfsHIwzWW0NUVMwwTKeHn0m95fEeAutfij547DPpmeLjzkfMtqBeNd8W8gft11NrhgzunCn39zyj723L49nksDX/1wK3X48AvJQ8n1AXlhu2uL9+bpvWJx8urXb7+Ck8RsPoDELUqzM7Nza4ZYFnQ+DSmXDSjOFVecqvWOB8W8PjBA/mzvLGN0YOr275Wn8byx9LkzdadCRc7r5/rvI9AT31J7JgAs9sSIrmXSab0zmdDESDecgTQs9h7Yd2dmqhLQ/kDFnpd3T8pbD441Ur2gJyQaj8c1UXmquq4DCsZZVhUqj6qioF+ulcslUdAzc1cFPSb1y8YnjJLljHeKHSiOfvEJU5KJNF+jfPxJPmGw757IPxpVi5HvZ9PZAAAAAElFTkSuQmCC\"


class EmojiItem:

    \"\"\"A container for an emoji character used by the Emoji class\"\"\"

    def __init__(self, name, category, subcategory, char):
        \"\"\"
        Parameters:

            name (str):
                The name of the emoji character.

            category (str):
                The major category of the emoji character.

            subcategory (str):
                The subcategory of the emoji character.

            char (str):
                The unicode character.
        \"\"\"
        self.name = name
        self.category = category
        self.subcategory = subcategory
        self.char = char

    def __repr__(self) -> str:
        return self.char


class Emoji:
    \"\"\"A class that contains emoji characters that can be used in the
    `text` parameter in any tkinter widget with the option.
    \"\"\"

    _ITEMS = [
        EmojiItem(\"KNOT\", \"activities\", \"arts & crafts\", \"🪢\"),
        EmojiItem(\"SEWING NEEDLE\", \"activities\", \"arts & crafts\", \"🪡\"),
        EmojiItem(\"BALL OF YARN\", \"activities\", \"arts & crafts\", \"🧶\"),
        EmojiItem(\"SPOOL OF THREAD\", \"activities\", \"arts & crafts\", \"🧵\"),
        EmojiItem(\"FRAME WITH PICTURE\", \"activities\", \"arts & crafts\", \"🖼\"),
        EmojiItem(\"PERFORMING ARTS\", \"activities\", \"arts & crafts\", \"🎭\"),
        EmojiItem(\"ARTIST PALETTE\", \"activities\", \"arts & crafts\", \"🎨\"),
        EmojiItem(\"THIRD PLACE MEDAL\", \"activities\", \"award-medal\", \"🥉\"),
        EmojiItem(\"SECOND PLACE MEDAL\", \"activities\", \"award-medal\", \"🥈\"),
        EmojiItem(\"FIRST PLACE MEDAL\", \"activities\", \"award-medal\", \"🥇\"),
        EmojiItem(\"TROPHY\", \"activities\", \"award-medal\", \"🏆\"),
        EmojiItem(\"SPORTS MEDAL\", \"activities\", \"award-medal\", \"🏅\"),
        EmojiItem(\"MILITARY MEDAL\", \"activities\", \"award-medal\", \"🎖\"),
        EmojiItem(\"SPARKLES\", \"activities\", \"event\", \"✨\"),
        EmojiItem(\"FIRECRACKER\", \"activities\", \"event\", \"🧨\"),
        EmojiItem(\"RED GIFT ENVELOPE\", \"activities\", \"event\", \"🧧\"),
        EmojiItem(\"TICKET\", \"activities\", \"event\", \"🎫\"),
        EmojiItem(\"ADMISSION TICKETS\", \"activities\", \"event\", \"🎟\"),
        EmojiItem(\"REMINDER RIBBON\", \"activities\", \"event\", \"🎗\"),
        EmojiItem(\"MOON VIEWING CEREMONY\", \"activities\", \"event\", \"🎑\"),
        EmojiItem(\"WIND CHIME\", \"activities\", \"event\", \"🎐\"),
        EmojiItem(\"CARP STREAMER\", \"activities\", \"event\", \"🎏\"),
        EmojiItem(\"JAPANESE DOLLS\", \"activities\", \"event\", \"🎎\"),
        EmojiItem(\"PINE DECORATION\", \"activities\", \"event\", \"🎍\"),
        EmojiItem(\"TANABATA TREE\", \"activities\", \"event\", \"🎋\"),
        EmojiItem(\"CONFETTI BALL\", \"activities\", \"event\", \"🎊\"),
        EmojiItem(\"PARTY POPPER\", \"activities\", \"event\", \"🎉\"),
        EmojiItem(\"BALLOON\", \"activities\", \"event\", \"🎈\"),
        EmojiItem(\"FIREWORK SPARKLER\", \"activities\", \"event\", \"🎇\"),
        EmojiItem(\"FIREWORKS\", \"activities\", \"event\", \"🎆\"),
        EmojiItem(\"CHRISTMAS TREE\", \"activities\", \"event\", \"🎄\"),
        EmojiItem(\"JACK-O-LANTERN\", \"activities\", \"event\", \"🎃\"),
        EmojiItem(\"WRAPPED PRESENT\", \"activities\", \"event\", \"🎁\"),
        EmojiItem(\"RIBBON\", \"activities\", \"event\", \"🎀\"),
        EmojiItem(\"BLACK CHESS PAWN\", \"activities\", \"game\", \"♟\"),
        EmojiItem(\"BLACK DIAMOND SUIT\", \"activities\", \"game\", \"♦\"),
        EmojiItem(\"BLACK HEART SUIT\", \"activities\", \"game\", \"♥\"),
        EmojiItem(\"BLACK CLUB SUIT\", \"activities\", \"game\", \"♣\"),
        EmojiItem(\"BLACK SPADE SUIT\", \"activities\", \"game\", \"♠\"),
        EmojiItem(\"NESTING DOLLS\", \"activities\", \"game\", \"🪆\"),
        EmojiItem(\"PINATA\", \"activities\", \"game\", \"🪅\"),
        EmojiItem(\"MAGIC WAND\", \"activities\", \"game\", \"🪄\"),
        EmojiItem(\"KITE\", \"activities\", \"game\", \"🪁\"),
        EmojiItem(\"YO-YO\", \"activities\", \"game\", \"🪀\"),
        EmojiItem(\"NAZAR AMULET\", \"activities\", \"game\", \"🧿\"),
        EmojiItem(\"TEDDY BEAR\", \"activities\", \"game\", \"🧸\"),
        EmojiItem(\"JIGSAW PUZZLE PIECE\", \"activities\", \"game\", \"🧩\"),
        EmojiItem(\"JOYSTICK\", \"activities\", \"game\", \"🕹\"),
        EmojiItem(\"CRYSTAL BALL\", \"activities\", \"game\", \"🔮\"),
        EmojiItem(\"FLOWER PLAYING CARDS\", \"activities\", \"game\", \"🎴\"),
        EmojiItem(\"GAME DIE\", \"activities\", \"game\", \"🎲\"),
        EmojiItem(\"BILLIARDS\", \"activities\", \"game\", \"🎱\"),
        EmojiItem(\"SLOT MACHINE\", \"activities\", \"game\", \"🎰\"),
        EmojiItem(\"DIRECT HIT\", \"activities\", \"game\", \"🎯\"),
        EmojiItem(\"VIDEO GAME\", \"activities\", \"game\", \"🎮\"),
        EmojiItem(\"PLAYING CARD BLACK JOKER\", \"activities\", \"game\", \"🃏\"),
        EmojiItem(\"MAHJONG TILE RED DRAGON\", \"activities\", \"game\", \"🀄\"),
        EmojiItem(\"ICE SKATE\", \"activities\", \"sport\", \"⛸\"),
        EmojiItem(\"FLAG IN HOLE\", \"activities\", \"sport\", \"⛳\"),
        EmojiItem(\"BASEBALL\", \"activities\", \"sport\", \"⚾\"),
        EmojiItem(\"SOCCER BALL\", \"activities\", \"sport\", \"⚽\"),
        EmojiItem(\"FLYING DISC\", \"activities\", \"sport\", \"🥏\"),
        EmojiItem(\"SOFTBALL\", \"activities\", \"sport\", \"🥎\"),
        EmojiItem(\"LACROSSE STICK AND BALL\", \"activities\", \"sport\", \"🥍\"),
        EmojiItem(\"CURLING STONE\", \"activities\", \"sport\", \"🥌\"),
        EmojiItem(\"MARTIAL ARTS UNIFORM\", \"activities\", \"sport\", \"🥋\"),
        EmojiItem(\"BOXING GLOVE\", \"activities\", \"sport\", \"🥊\"),
        EmojiItem(\"GOAL NET\", \"activities\", \"sport\", \"🥅\"),
        EmojiItem(\"DIVING MASK\", \"activities\", \"sport\", \"🤿\"),
        EmojiItem(\"SLED\", \"activities\", \"sport\", \"🛷\"),
        EmojiItem(
            \"BADMINTON RACQUET AND SHUTTLECOCK\", \"activities\", \"sport\", \"🏸\"
        ),
        EmojiItem(\"TABLE TENNIS PADDLE AND BALL\", \"activities\", \"sport\", \"🏓\"),
        EmojiItem(\"ICE HOCKEY STICK AND PUCK\", \"activities\", \"sport\", \"🏒\"),
        EmojiItem(\"FIELD HOCKEY STICK AND BALL\", \"activities\", \"sport\", \"🏑\"),
        EmojiItem(\"VOLLEYBALL\", \"activities\", \"sport\", \"🏐\"),
        EmojiItem(\"CRICKET BAT AND BALL\", \"activities\", \"sport\", \"🏏\"),
        EmojiItem(\"RUGBY FOOTBALL\", \"activities\", \"sport\", \"🏉\"),
        EmojiItem(\"AMERICAN FOOTBALL\", \"activities\", \"sport\", \"🏈\"),
        EmojiItem(\"BASKETBALL AND HOOP\", \"activities\", \"sport\", \"🏀\"),
        EmojiItem(\"SKI AND SKI BOOT\", \"activities\", \"sport\", \"🎿\"),
        EmojiItem(\"TENNIS RACQUET AND BALL\", \"activities\", \"sport\", \"🎾\"),
        EmojiItem(\"RUNNING SHIRT WITH SASH\", \"activities\", \"sport\", \"🎽\"),
        EmojiItem(\"BOWLING\", \"activities\", \"sport\", \"🎳\"),
        EmojiItem(\"FISHING POLE AND FISH\", \"activities\", \"sport\", \"🎣\"),
        EmojiItem(\"FROG FACE\", \"animal-nature\", \"animal-amphibian\", \"🐸\"),
        EmojiItem(\"FEATHER\", \"animal-nature\", \"animal-bird\", \"🪶\"),
        EmojiItem(\"FLAMINGO\", \"animal-nature\", \"animal-bird\", \"🦩\"),
        EmojiItem(\"DODO\", \"animal-nature\", \"animal-bird\", \"🦤\"),
        EmojiItem(\"SWAN\", \"animal-nature\", \"animal-bird\", \"🦢\"),
        EmojiItem(\"PARROT\", \"animal-nature\", \"animal-bird\", \"🦜\"),
        EmojiItem(\"PEACOCK\", \"animal-nature\", \"animal-bird\", \"🦚\"),
        EmojiItem(\"OWL\", \"animal-nature\", \"animal-bird\", \"🦉\"),
        EmojiItem(\"DUCK\", \"animal-nature\", \"animal-bird\", \"🦆\"),
        EmojiItem(\"EAGLE\", \"animal-nature\", \"animal-bird\", \"🦅\"),
        EmojiItem(\"TURKEY\", \"animal-nature\", \"animal-bird\", \"🦃\"),
        EmojiItem(\"DOVE OF PEACE\", \"animal-nature\", \"animal-bird\", \"🕊\"),
        EmojiItem(\"PENGUIN\", \"animal-nature\", \"animal-bird\", \"🐧\"),
        EmojiItem(\"BIRD\", \"animal-nature\", \"animal-bird\", \"🐦\"),
        EmojiItem(
            \"FRONT-FACING BABY CHICK\", \"animal-nature\", \"animal-bird\", \"🐥\"
        ),
        EmojiItem(\"BABY CHICK\", \"animal-nature\", \"animal-bird\", \"🐤\"),
        EmojiItem(\"HATCHING CHICK\", \"animal-nature\", \"animal-bird\", \"🐣\"),
        EmojiItem(\"CHICKEN\", \"animal-nature\", \"animal-bird\", \"🐔\"),
        EmojiItem(\"ROOSTER\", \"animal-nature\", \"animal-bird\", \"🐓\"),
        EmojiItem(\"COCKROACH\", \"animal-nature\", \"animal-bug\", \"🪳\"),
        EmojiItem(\"BEETLE\", \"animal-nature\", \"animal-bug\", \"🪲\"),
        EmojiItem(\"WORM\", \"animal-nature\", \"animal-bug\", \"🪱\"),
        EmojiItem(\"FLY\", \"animal-nature\", \"animal-bug\", \"🪰\"),
        EmojiItem(\"MICROBE\", \"animal-nature\", \"animal-bug\", \"🦠\"),
        EmojiItem(\"MOSQUITO\", \"animal-nature\", \"animal-bug\", \"🦟\"),
        EmojiItem(\"CRICKET\", \"animal-nature\", \"animal-bug\", \"🦗\"),
        EmojiItem(\"BUTTERFLY\", \"animal-nature\", \"animal-bug\", \"🦋\"),
        EmojiItem(\"SCORPION\", \"animal-nature\", \"animal-bug\", \"🦂\"),
        EmojiItem(\"SPIDER WEB\", \"animal-nature\", \"animal-bug\", \"🕸\"),
        EmojiItem(\"SPIDER\", \"animal-nature\", \"animal-bug\", \"🕷\"),
        EmojiItem(\"LADY BEETLE\", \"animal-nature\", \"animal-bug\", \"🐞\"),
        EmojiItem(\"HONEYBEE\", \"animal-nature\", \"animal-bug\", \"🐝\"),
        EmojiItem(\"ANT\", \"animal-nature\", \"animal-bug\", \"🐜\"),
        EmojiItem(\"BUG\", \"animal-nature\", \"animal-bug\", \"🐛\"),
        EmojiItem(\"SNAIL\", \"animal-nature\", \"animal-bug\", \"🐌\"),
        EmojiItem(\"GUIDE DOG\", \"animal-nature\", \"animal-mammal\", \"🦮\"),
        EmojiItem(\"BISON\", \"animal-nature\", \"animal-mammal\", \"🦬\"),
        EmojiItem(\"BEAVER\", \"animal-nature\", \"animal-mammal\", \"🦫\"),
        EmojiItem(\"SKUNK\", \"animal-nature\", \"animal-mammal\", \"🦨\"),
        EmojiItem(\"ORANGUTAN\", \"animal-nature\", \"animal-mammal\", \"🦧\"),
        EmojiItem(\"OTTER\", \"animal-nature\", \"animal-mammal\", \"🦦\"),
        EmojiItem(\"SLOTH\", \"animal-nature\", \"animal-mammal\", \"🦥\"),
        EmojiItem(\"MAMMOTH\", \"animal-nature\", \"animal-mammal\", \"🦣\"),
        EmojiItem(\"BADGER\", \"animal-nature\", \"animal-mammal\", \"🦡\"),
        EmojiItem(\"RACCOON\", \"animal-nature\", \"animal-mammal\", \"🦝\"),
        EmojiItem(\"HIPPOPOTAMUS\", \"animal-nature\", \"animal-mammal\", \"🦛\"),
        EmojiItem(\"LLAMA\", \"animal-nature\", \"animal-mammal\", \"🦙\"),
        EmojiItem(\"KANGAROO\", \"animal-nature\", \"animal-mammal\", \"🦘\"),
        EmojiItem(\"HEDGEHOG\", \"animal-nature\", \"animal-mammal\", \"🦔\"),
        EmojiItem(\"ZEBRA FACE\", \"animal-nature\", \"animal-mammal\", \"🦓\"),
        EmojiItem(\"GIRAFFE FACE\", \"animal-nature\", \"animal-mammal\", \"🦒\"),
        EmojiItem(\"RHINOCEROS\", \"animal-nature\", \"animal-mammal\", \"🦏\"),
        EmojiItem(\"GORILLA\", \"animal-nature\", \"animal-mammal\", \"🦍\"),
        EmojiItem(\"DEER\", \"animal-nature\", \"animal-mammal\", \"🦌\"),
        EmojiItem(\"FOX FACE\", \"animal-nature\", \"animal-mammal\", \"🦊\"),
        EmojiItem(\"BAT\", \"animal-nature\", \"animal-mammal\", \"🦇\"),
        EmojiItem(\"UNICORN FACE\", \"animal-nature\", \"animal-mammal\", \"🦄\"),
        EmojiItem(\"LION FACE\", \"animal-nature\", \"animal-mammal\", \"🦁\"),
        EmojiItem(\"CHIPMUNK\", \"animal-nature\", \"animal-mammal\", \"🐿\"),
        EmojiItem(\"PAW PRINTS\", \"animal-nature\", \"animal-mammal\", \"🐾\"),
        EmojiItem(\"PIG NOSE\", \"animal-nature\", \"animal-mammal\", \"🐽\"),
        EmojiItem(\"PANDA FACE\", \"animal-nature\", \"animal-mammal\", \"🐼\"),
        EmojiItem(\"BEAR FACE\", \"animal-nature\", \"animal-mammal\", \"🐻\"),
        EmojiItem(\"WOLF FACE\", \"animal-nature\", \"animal-mammal\", \"🐺\"),
        EmojiItem(\"HAMSTER FACE\", \"animal-nature\", \"animal-mammal\", \"🐹\"),
        EmojiItem(\"PIG FACE\", \"animal-nature\", \"animal-mammal\", \"🐷\"),
        EmojiItem(\"DOG FACE\", \"animal-nature\", \"animal-mammal\", \"🐶\"),
        EmojiItem(\"MONKEY FACE\", \"animal-nature\", \"animal-mammal\", \"🐵\"),
        EmojiItem(\"HORSE FACE\", \"animal-nature\", \"animal-mammal\", \"🐴\"),
        EmojiItem(\"CAT FACE\", \"animal-nature\", \"animal-mammal\", \"🐱\"),
        EmojiItem(\"RABBIT FACE\", \"animal-nature\", \"animal-mammal\", \"🐰\"),
        EmojiItem(\"TIGER FACE\", \"animal-nature\", \"animal-mammal\", \"🐯\"),
        EmojiItem(\"COW FACE\", \"animal-nature\", \"animal-mammal\", \"🐮\"),
        EmojiItem(\"MOUSE FACE\", \"animal-nature\", \"animal-mammal\", \"🐭\"),
        EmojiItem(\"BACTRIAN CAMEL\", \"animal-nature\", \"animal-mammal\", \"🐫\"),
        EmojiItem(\"DROMEDARY CAMEL\", \"animal-nature\", \"animal-mammal\", \"🐪\"),
        EmojiItem(\"POODLE\", \"animal-nature\", \"animal-mammal\", \"🐩\"),
        EmojiItem(\"KOALA\", \"animal-nature\", \"animal-mammal\", \"🐨\"),
        EmojiItem(\"ELEPHANT\", \"animal-nature\", \"animal-mammal\", \"🐘\"),
        EmojiItem(\"BOAR\", \"animal-nature\", \"animal-mammal\", \"🐗\"),
        EmojiItem(\"PIG\", \"animal-nature\", \"animal-mammal\", \"🐖\"),
        EmojiItem(\"DOG\", \"animal-nature\", \"animal-mammal\", \"🐕\"),
        EmojiItem(\"MONKEY\", \"animal-nature\", \"animal-mammal\", \"🐒\"),
        EmojiItem(\"SHEEP\", \"animal-nature\", \"animal-mammal\", \"🐑\"),
        EmojiItem(\"GOAT\", \"animal-nature\", \"animal-mammal\", \"🐐\"),
        EmojiItem(\"RAM\", \"animal-nature\", \"animal-mammal\", \"🐏\"),
        EmojiItem(\"HORSE\", \"animal-nature\", \"animal-mammal\", \"🐎\"),
        EmojiItem(\"CAT\", \"animal-nature\", \"animal-mammal\", \"🐈\"),
        EmojiItem(\"RABBIT\", \"animal-nature\", \"animal-mammal\", \"🐇\"),
        EmojiItem(\"LEOPARD\", \"animal-nature\", \"animal-mammal\", \"🐆\"),
        EmojiItem(\"TIGER\", \"animal-nature\", \"animal-mammal\", \"🐅\"),
        EmojiItem(\"COW\", \"animal-nature\", \"animal-mammal\", \"🐄\"),
        EmojiItem(\"WATER BUFFALO\", \"animal-nature\", \"animal-mammal\", \"🐃\"),
        EmojiItem(\"OX\", \"animal-nature\", \"animal-mammal\", \"🐂\"),
        EmojiItem(\"MOUSE\", \"animal-nature\", \"animal-mammal\", \"🐁\"),
        EmojiItem(\"RAT\", \"animal-nature\", \"animal-mammal\", \"🐀\"),
        EmojiItem(\"SEAL\", \"animal-nature\", \"animal-marine\", \"🦭\"),
        EmojiItem(\"SHARK\", \"animal-nature\", \"animal-marine\", \"🦈\"),
        EmojiItem(\"SPOUTING WHALE\", \"animal-nature\", \"animal-marine\", \"🐳\"),
        EmojiItem(\"DOLPHIN\", \"animal-nature\", \"animal-marine\", \"🐬\"),
        EmojiItem(\"BLOWFISH\", \"animal-nature\", \"animal-marine\", \"🐡\"),
        EmojiItem(\"TROPICAL FISH\", \"animal-nature\", \"animal-marine\", \"🐠\"),
        EmojiItem(\"FISH\", \"animal-nature\", \"animal-marine\", \"🐟\"),
        EmojiItem(\"SPIRAL SHELL\", \"animal-nature\", \"animal-marine\", \"🐚\"),
        EmojiItem(\"OCTOPUS\", \"animal-nature\", \"animal-marine\", \"🐙\"),
        EmojiItem(\"WHALE\", \"animal-nature\", \"animal-marine\", \"🐋\"),
        EmojiItem(\"T-REX\", \"animal-nature\", \"animal-reptile\", \"🦖\"),
        EmojiItem(\"SAUROPOD\", \"animal-nature\", \"animal-reptile\", \"🦕\"),
        EmojiItem(\"LIZARD\", \"animal-nature\", \"animal-reptile\", \"🦎\"),
        EmojiItem(\"DRAGON FACE\", \"animal-nature\", \"animal-reptile\", \"🐲\"),
        EmojiItem(\"TURTLE\", \"animal-nature\", \"animal-reptile\", \"🐢\"),
        EmojiItem(\"SNAKE\", \"animal-nature\", \"animal-reptile\", \"🐍\"),
        EmojiItem(\"CROCODILE\", \"animal-nature\", \"animal-reptile\", \"🐊\"),
        EmojiItem(\"DRAGON\", \"animal-nature\", \"animal-reptile\", \"🐉\"),
        EmojiItem(\"WILTED FLOWER\", \"animal-nature\", \"plant-flower\", \"🥀\"),
        EmojiItem(\"WHITE FLOWER\", \"animal-nature\", \"plant-flower\", \"💮\"),
        EmojiItem(\"BOUQUET\", \"animal-nature\", \"plant-flower\", \"💐\"),
        EmojiItem(\"ROSETTE\", \"animal-nature\", \"plant-flower\", \"🏵\"),
        EmojiItem(\"BLOSSOM\", \"animal-nature\", \"plant-flower\", \"🌼\"),
        EmojiItem(\"SUNFLOWER\", \"animal-nature\", \"plant-flower\", \"🌻\"),
        EmojiItem(\"HIBISCUS\", \"animal-nature\", \"plant-flower\", \"🌺\"),
        EmojiItem(\"ROSE\", \"animal-nature\", \"plant-flower\", \"🌹\"),
        EmojiItem(\"CHERRY BLOSSOM\", \"animal-nature\", \"plant-flower\", \"🌸\"),
        EmojiItem(\"TULIP\", \"animal-nature\", \"plant-flower\", \"🌷\"),
        EmojiItem(\"SHAMROCK\", \"animal-nature\", \"plant-other\", \"☘\"),
        EmojiItem(\"POTTED PLANT\", \"animal-nature\", \"plant-other\", \"🪴\"),
        EmojiItem(
            \"LEAF FLUTTERING IN WIND\", \"animal-nature\", \"plant-other\", \"🍃\"
        ),
        EmojiItem(\"FALLEN LEAF\", \"animal-nature\", \"plant-other\", \"🍂\"),
        EmojiItem(\"MAPLE LEAF\", \"animal-nature\", \"plant-other\", \"🍁\"),
        EmojiItem(\"FOUR LEAF CLOVER\", \"animal-nature\", \"plant-other\", \"🍀\"),
        EmojiItem(\"HERB\", \"animal-nature\", \"plant-other\", \"🌿\"),
        EmojiItem(\"EAR OF RICE\", \"animal-nature\", \"plant-other\", \"🌾\"),
        EmojiItem(\"CACTUS\", \"animal-nature\", \"plant-other\", \"🌵\"),
        EmojiItem(\"PALM TREE\", \"animal-nature\", \"plant-other\", \"🌴\"),
        EmojiItem(\"DECIDUOUS TREE\", \"animal-nature\", \"plant-other\", \"🌳\"),
        EmojiItem(\"EVERGREEN TREE\", \"animal-nature\", \"plant-other\", \"🌲\"),
        EmojiItem(\"SEEDLING\", \"animal-nature\", \"plant-other\", \"🌱\"),
        EmojiItem(
            \"EMOJI COMPONENT WHITE HAIR\", \"component\", \"hair-style\", \"🦳\"
        ),
        EmojiItem(\"EMOJI COMPONENT BALD\", \"component\", \"hair-style\", \"🦲\"),
        EmojiItem(
            \"EMOJI COMPONENT CURLY HAIR\", \"component\", \"hair-style\", \"🦱\"
        ),
        EmojiItem(\"EMOJI COMPONENT RED HAIR\", \"component\", \"hair-style\", \"🦰\"),
        EmojiItem(
            \"EMOJI MODIFIER FITZPATRICK TYPE-6\", \"component\", \"skin-tone\", \"🏿\"
        ),
        EmojiItem(
            \"EMOJI MODIFIER FITZPATRICK TYPE-5\", \"component\", \"skin-tone\", \"🏾\"
        ),
        EmojiItem(
            \"EMOJI MODIFIER FITZPATRICK TYPE-4\", \"component\", \"skin-tone\", \"🏽\"
        ),
        EmojiItem(
            \"EMOJI MODIFIER FITZPATRICK TYPE-3\", \"component\", \"skin-tone\", \"🏼\"
        ),
        EmojiItem(
            \"EMOJI MODIFIER FITZPATRICK TYPE-1-2\",
            \"component\",
            \"skin-tone\",
            \"🏻\",
        ),
        EmojiItem(\"TRIANGULAR FLAG ON POST\", \"flags\", \"flag\", \"🚩\"),
        EmojiItem(\"WAVING BLACK FLAG\", \"flags\", \"flag\", \"🏴\"),
        EmojiItem(\"WAVING WHITE FLAG\", \"flags\", \"flag\", \"🏳\"),
        EmojiItem(\"CHEQUERED FLAG\", \"flags\", \"flag\", \"🏁\"),
        EmojiItem(\"CROSSED FLAGS\", \"flags\", \"flag\", \"🎌\"),
        EmojiItem(\"CHOPSTICKS\", \"food-drink\", \"dishware\", \"🥢\"),
        EmojiItem(\"SPOON\", \"food-drink\", \"dishware\", \"🥄\"),
        EmojiItem(\"HOCHO\", \"food-drink\", \"dishware\", \"🔪\"),
        EmojiItem(\"AMPHORA\", \"food-drink\", \"dishware\", \"🏺\"),
        EmojiItem(\"FORK AND KNIFE WITH PLATE\", \"food-drink\", \"dishware\", \"🍽\"),
        EmojiItem(\"FORK AND KNIFE\", \"food-drink\", \"dishware\", \"🍴\"),
        EmojiItem(\"HOT BEVERAGE\", \"food-drink\", \"drink\", \"☕\"),
        EmojiItem(\"TEAPOT\", \"food-drink\", \"drink\", \"🫖\"),
        EmojiItem(\"BUBBLE TEA\", \"food-drink\", \"drink\", \"🧋\"),
        EmojiItem(\"ICE CUBE\", \"food-drink\", \"drink\", \"🧊\"),
        EmojiItem(\"MATE DRINK\", \"food-drink\", \"drink\", \"🧉\"),
        EmojiItem(\"BEVERAGE BOX\", \"food-drink\", \"drink\", \"🧃\"),
        EmojiItem(\"CUP WITH STRAW\", \"food-drink\", \"drink\", \"🥤\"),
        EmojiItem(\"GLASS OF MILK\", \"food-drink\", \"drink\", \"🥛\"),
        EmojiItem(\"TUMBLER GLASS\", \"food-drink\", \"drink\", \"🥃\"),
        EmojiItem(\"CLINKING GLASSES\", \"food-drink\", \"drink\", \"🥂\"),
        EmojiItem(\"BOTTLE WITH POPPING CORK\", \"food-drink\", \"drink\", \"🍾\"),
        EmojiItem(\"BABY BOTTLE\", \"food-drink\", \"drink\", \"🍼\"),
        EmojiItem(\"CLINKING BEER MUGS\", \"food-drink\", \"drink\", \"🍻\"),
        EmojiItem(\"BEER MUG\", \"food-drink\", \"drink\", \"🍺\"),
        EmojiItem(\"TROPICAL DRINK\", \"food-drink\", \"drink\", \"🍹\"),
        EmojiItem(\"COCKTAIL GLASS\", \"food-drink\", \"drink\", \"🍸\"),
        EmojiItem(\"WINE GLASS\", \"food-drink\", \"drink\", \"🍷\"),
        EmojiItem(\"SAKE BOTTLE AND CUP\", \"food-drink\", \"drink\", \"🍶\"),
        EmojiItem(\"TEACUP WITHOUT HANDLE\", \"food-drink\", \"drink\", \"🍵\"),
        EmojiItem(\"MOON CAKE\", \"food-drink\", \"food-asian\", \"🥮\"),
        EmojiItem(\"TAKEOUT BOX\", \"food-drink\", \"food-asian\", \"🥡\"),
        EmojiItem(\"FORTUNE COOKIE\", \"food-drink\", \"food-asian\", \"🥠\"),
        EmojiItem(\"DUMPLING\", \"food-drink\", \"food-asian\", \"🥟\"),
        EmojiItem(\"BENTO BOX\", \"food-drink\", \"food-asian\", \"🍱\"),
        EmojiItem(
            \"FISH CAKE WITH SWIRL DESIGN\", \"food-drink\", \"food-asian\", \"🍥\"
        ),
        EmojiItem(\"FRIED SHRIMP\", \"food-drink\", \"food-asian\", \"🍤\"),
        EmojiItem(\"SUSHI\", \"food-drink\", \"food-asian\", \"🍣\"),
        EmojiItem(\"ODEN\", \"food-drink\", \"food-asian\", \"🍢\"),
        EmojiItem(\"DANGO\", \"food-drink\", \"food-asian\", \"🍡\"),
        EmojiItem(\"ROASTED SWEET POTATO\", \"food-drink\", \"food-asian\", \"🍠\"),
        EmojiItem(\"SPAGHETTI\", \"food-drink\", \"food-asian\", \"🍝\"),
        EmojiItem(\"STEAMING BOWL\", \"food-drink\", \"food-asian\", \"🍜\"),
        EmojiItem(\"CURRY AND RICE\", \"food-drink\", \"food-asian\", \"🍛\"),
        EmojiItem(\"COOKED RICE\", \"food-drink\", \"food-asian\", \"🍚\"),
        EmojiItem(\"RICE BALL\", \"food-drink\", \"food-asian\", \"🍙\"),
        EmojiItem(\"RICE CRACKER\", \"food-drink\", \"food-asian\", \"🍘\"),
        EmojiItem(\"OLIVE\", \"food-drink\", \"food-fruit\", \"🫒\"),
        EmojiItem(\"BLUEBERRIES\", \"food-drink\", \"food-fruit\", \"🫐\"),
        EmojiItem(\"MANGO\", \"food-drink\", \"food-fruit\", \"🥭\"),
        EmojiItem(\"COCONUT\", \"food-drink\", \"food-fruit\", \"🥥\"),
        EmojiItem(\"KIWIFRUIT\", \"food-drink\", \"food-fruit\", \"🥝\"),
        EmojiItem(\"STRAWBERRY\", \"food-drink\", \"food-fruit\", \"🍓\"),
        EmojiItem(\"CHERRIES\", \"food-drink\", \"food-fruit\", \"🍒\"),
        EmojiItem(\"PEACH\", \"food-drink\", \"food-fruit\", \"🍑\"),
        EmojiItem(\"PEAR\", \"food-drink\", \"food-fruit\", \"🍐\"),
        EmojiItem(\"GREEN APPLE\", \"food-drink\", \"food-fruit\", \"🍏\"),
        EmojiItem(\"RED APPLE\", \"food-drink\", \"food-fruit\", \"🍎\"),
        EmojiItem(\"PINEAPPLE\", \"food-drink\", \"food-fruit\", \"🍍\"),
        EmojiItem(\"BANANA\", \"food-drink\", \"food-fruit\", \"🍌\"),
        EmojiItem(\"LEMON\", \"food-drink\", \"food-fruit\", \"🍋\"),
        EmojiItem(\"TANGERINE\", \"food-drink\", \"food-fruit\", \"🍊\"),
        EmojiItem(\"WATERMELON\", \"food-drink\", \"food-fruit\", \"🍉\"),
        EmojiItem(\"MELON\", \"food-drink\", \"food-fruit\", \"🍈\"),
        EmojiItem(\"GRAPES\", \"food-drink\", \"food-fruit\", \"🍇\"),
        EmojiItem(\"TOMATO\", \"food-drink\", \"food-fruit\", \"🍅\"),
        EmojiItem(\"OYSTER\", \"food-drink\", \"food-marine\", \"🦪\"),
        EmojiItem(\"LOBSTER\", \"food-drink\", \"food-marine\", \"🦞\"),
        EmojiItem(\"SQUID\", \"food-drink\", \"food-marine\", \"🦑\"),
        EmojiItem(\"SHRIMP\", \"food-drink\", \"food-marine\", \"🦐\"),
        EmojiItem(\"CRAB\", \"food-drink\", \"food-marine\", \"🦀\"),
        EmojiItem(\"FONDUE\", \"food-drink\", \"food-prepared\", \"🫕\"),
        EmojiItem(\"TAMALE\", \"food-drink\", \"food-prepared\", \"🫔\"),
        EmojiItem(\"FLATBREAD\", \"food-drink\", \"food-prepared\", \"🫓\"),
        EmojiItem(\"BUTTER\", \"food-drink\", \"food-prepared\", \"🧈\"),
        EmojiItem(\"WAFFLE\", \"food-drink\", \"food-prepared\", \"🧇\"),
        EmojiItem(\"FALAFEL\", \"food-drink\", \"food-prepared\", \"🧆\"),
        EmojiItem(\"SALT SHAKER\", \"food-drink\", \"food-prepared\", \"🧂\"),
        EmojiItem(\"CHEESE WEDGE\", \"food-drink\", \"food-prepared\", \"🧀\"),
        EmojiItem(\"BAGEL\", \"food-drink\", \"food-prepared\", \"🥯\"),
        EmojiItem(\"CANNED FOOD\", \"food-drink\", \"food-prepared\", \"🥫\"),
        EmojiItem(\"SANDWICH\", \"food-drink\", \"food-prepared\", \"🥪\"),
        EmojiItem(\"CUT OF MEAT\", \"food-drink\", \"food-prepared\", \"🥩\"),
        EmojiItem(\"PRETZEL\", \"food-drink\", \"food-prepared\", \"🥨\"),
        EmojiItem(\"BOWL WITH SPOON\", \"food-drink\", \"food-prepared\", \"🥣\"),
        EmojiItem(\"PANCAKES\", \"food-drink\", \"food-prepared\", \"🥞\"),
        EmojiItem(\"EGG\", \"food-drink\", \"food-prepared\", \"🥚\"),
        EmojiItem(\"STUFFED FLATBREAD\", \"food-drink\", \"food-prepared\", \"🥙\"),
        EmojiItem(\"SHALLOW PAN OF FOOD\", \"food-drink\", \"food-prepared\", \"🥘\"),
        EmojiItem(\"GREEN SALAD\", \"food-drink\", \"food-prepared\", \"🥗\"),
        EmojiItem(\"BAGUETTE BREAD\", \"food-drink\", \"food-prepared\", \"🥖\"),
        EmojiItem(\"BACON\", \"food-drink\", \"food-prepared\", \"🥓\"),
        EmojiItem(\"CROISSANT\", \"food-drink\", \"food-prepared\", \"🥐\"),
        EmojiItem(\"POPCORN\", \"food-drink\", \"food-prepared\", \"🍿\"),
        EmojiItem(\"COOKING\", \"food-drink\", \"food-prepared\", \"🍳\"),
        EmojiItem(\"POT OF FOOD\", \"food-drink\", \"food-prepared\", \"🍲\"),
        EmojiItem(\"FRENCH FRIES\", \"food-drink\", \"food-prepared\", \"🍟\"),
        EmojiItem(\"BREAD\", \"food-drink\", \"food-prepared\", \"🍞\"),
        EmojiItem(\"POULTRY LEG\", \"food-drink\", \"food-prepared\", \"🍗\"),
        EmojiItem(\"MEAT ON BONE\", \"food-drink\", \"food-prepared\", \"🍖\"),
        EmojiItem(\"SLICE OF PIZZA\", \"food-drink\", \"food-prepared\", \"🍕\"),
        EmojiItem(\"HAMBURGER\", \"food-drink\", \"food-prepared\", \"🍔\"),
        EmojiItem(\"BURRITO\", \"food-drink\", \"food-prepared\", \"🌯\"),
        EmojiItem(\"TACO\", \"food-drink\", \"food-prepared\", \"🌮\"),
        EmojiItem(\"HOT DOG\", \"food-drink\", \"food-prepared\", \"🌭\"),
        EmojiItem(\"CUPCAKE\", \"food-drink\", \"food-sweet\", \"🧁\"),
        EmojiItem(\"PIE\", \"food-drink\", \"food-sweet\", \"🥧\"),
        EmojiItem(\"BIRTHDAY CAKE\", \"food-drink\", \"food-sweet\", \"🎂\"),
        EmojiItem(\"SHORTCAKE\", \"food-drink\", \"food-sweet\", \"🍰\"),
        EmojiItem(\"HONEY POT\", \"food-drink\", \"food-sweet\", \"🍯\"),
        EmojiItem(\"CUSTARD\", \"food-drink\", \"food-sweet\", \"🍮\"),
        EmojiItem(\"LOLLIPOP\", \"food-drink\", \"food-sweet\", \"🍭\"),
        EmojiItem(\"CANDY\", \"food-drink\", \"food-sweet\", \"🍬\"),
        EmojiItem(\"CHOCOLATE BAR\", \"food-drink\", \"food-sweet\", \"🍫\"),
        EmojiItem(\"COOKIE\", \"food-drink\", \"food-sweet\", \"🍪\"),
        EmojiItem(\"DOUGHNUT\", \"food-drink\", \"food-sweet\", \"🍩\"),
        EmojiItem(\"ICE CREAM\", \"food-drink\", \"food-sweet\", \"🍨\"),
        EmojiItem(\"SHAVED ICE\", \"food-drink\", \"food-sweet\", \"🍧\"),
        EmojiItem(\"SOFT ICE CREAM\", \"food-drink\", \"food-sweet\", \"🍦\"),
        EmojiItem(\"BELL PEPPER\", \"food-drink\", \"food-vegetable\", \"🫑\"),
        EmojiItem(\"ONION\", \"food-drink\", \"food-vegetable\", \"🧅\"),
        EmojiItem(\"GARLIC\", \"food-drink\", \"food-vegetable\", \"🧄\"),
        EmojiItem(\"LEAFY GREEN\", \"food-drink\", \"food-vegetable\", \"🥬\"),
        EmojiItem(\"BROCCOLI\", \"food-drink\", \"food-vegetable\", \"🥦\"),
        EmojiItem(\"PEANUTS\", \"food-drink\", \"food-vegetable\", \"🥜\"),
        EmojiItem(\"CARROT\", \"food-drink\", \"food-vegetable\", \"🥕\"),
        EmojiItem(\"POTATO\", \"food-drink\", \"food-vegetable\", \"🥔\"),
        EmojiItem(\"CUCUMBER\", \"food-drink\", \"food-vegetable\", \"🥒\"),
        EmojiItem(\"AVOCADO\", \"food-drink\", \"food-vegetable\", \"🥑\"),
        EmojiItem(\"AUBERGINE\", \"food-drink\", \"food-vegetable\", \"🍆\"),
        EmojiItem(\"MUSHROOM\", \"food-drink\", \"food-vegetable\", \"🍄\"),
        EmojiItem(\"EAR OF MAIZE\", \"food-drink\", \"food-vegetable\", \"🌽\"),
        EmojiItem(\"HOT PEPPER\", \"food-drink\", \"food-vegetable\", \"🌶\"),
        EmojiItem(\"CHESTNUT\", \"food-drink\", \"food-vegetable\", \"🌰\"),
        EmojiItem(\"ROLLED-UP NEWSPAPER\", \"objects\", \"book-paper\", \"🗞\"),
        EmojiItem(\"BOOKMARK\", \"objects\", \"book-paper\", \"🔖\"),
        EmojiItem(\"NEWSPAPER\", \"objects\", \"book-paper\", \"📰\"),
        EmojiItem(\"SCROLL\", \"objects\", \"book-paper\", \"📜\"),
        EmojiItem(\"BOOKS\", \"objects\", \"book-paper\", \"📚\"),
        EmojiItem(\"ORANGE BOOK\", \"objects\", \"book-paper\", \"📙\"),
        EmojiItem(\"BLUE BOOK\", \"objects\", \"book-paper\", \"📘\"),
        EmojiItem(\"GREEN BOOK\", \"objects\", \"book-paper\", \"📗\"),
        EmojiItem(\"OPEN BOOK\", \"objects\", \"book-paper\", \"📖\"),
        EmojiItem(\"CLOSED BOOK\", \"objects\", \"book-paper\", \"📕\"),
        EmojiItem(
            \"NOTEBOOK WITH DECORATIVE COVER\", \"objects\", \"book-paper\", \"📔\"
        ),
        EmojiItem(\"NOTEBOOK\", \"objects\", \"book-paper\", \"📓\"),
        EmojiItem(\"LEDGER\", \"objects\", \"book-paper\", \"📒\"),
        EmojiItem(\"BOOKMARK TABS\", \"objects\", \"book-paper\", \"📑\"),
        EmojiItem(\"PAGE FACING UP\", \"objects\", \"book-paper\", \"📄\"),
        EmojiItem(\"PAGE WITH CURL\", \"objects\", \"book-paper\", \"📃\"),
        EmojiItem(\"LABEL\", \"objects\", \"book-paper\", \"🏷\"),
        EmojiItem(\"HELMET WITH WHITE CROSS\", \"objects\", \"clothing\", \"⛑\"),
        EmojiItem(\"MILITARY HELMET\", \"objects\", \"clothing\", \"🪖\"),
        EmojiItem(\"THONG SANDAL\", \"objects\", \"clothing\", \"🩴\"),
        EmojiItem(\"SHORTS\", \"objects\", \"clothing\", \"🩳\"),
        EmojiItem(\"BRIEFS\", \"objects\", \"clothing\", \"🩲\"),
        EmojiItem(\"ONE-PIECE SWIMSUIT\", \"objects\", \"clothing\", \"🩱\"),
        EmojiItem(\"BALLET SHOES\", \"objects\", \"clothing\", \"🩰\"),
        EmojiItem(\"SOCKS\", \"objects\", \"clothing\", \"🧦\"),
        EmojiItem(\"COAT\", \"objects\", \"clothing\", \"🧥\"),
        EmojiItem(\"GLOVES\", \"objects\", \"clothing\", \"🧤\"),
        EmojiItem(\"SCARF\", \"objects\", \"clothing\", \"🧣\"),
        EmojiItem(\"BILLED CAP\", \"objects\", \"clothing\", \"🧢\"),
        EmojiItem(\"SAFETY VEST\", \"objects\", \"clothing\", \"🦺\"),
        EmojiItem(\"FLAT SHOE\", \"objects\", \"clothing\", \"🥿\"),
        EmojiItem(\"HIKING BOOT\", \"objects\", \"clothing\", \"🥾\"),
        EmojiItem(\"GOGGLES\", \"objects\", \"clothing\", \"🥽\"),
        EmojiItem(\"LAB COAT\", \"objects\", \"clothing\", \"🥼\"),
        EmojiItem(\"SARI\", \"objects\", \"clothing\", \"🥻\"),
        EmojiItem(\"SHOPPING BAGS\", \"objects\", \"clothing\", \"🛍\"),
        EmojiItem(\"DARK SUNGLASSES\", \"objects\", \"clothing\", \"🕶\"),
        EmojiItem(\"PRAYER BEADS\", \"objects\", \"clothing\", \"📿\"),
        EmojiItem(\"GEM STONE\", \"objects\", \"clothing\", \"💎\"),
        EmojiItem(\"RING\", \"objects\", \"clothing\", \"💍\"),
        EmojiItem(\"LIPSTICK\", \"objects\", \"clothing\", \"💄\"),
        EmojiItem(\"WOMANS BOOTS\", \"objects\", \"clothing\", \"👢\"),
        EmojiItem(\"WOMANS SANDAL\", \"objects\", \"clothing\", \"👡\"),
        EmojiItem(\"HIGH-HEELED SHOE\", \"objects\", \"clothing\", \"👠\"),
        EmojiItem(\"ATHLETIC SHOE\", \"objects\", \"clothing\", \"👟\"),
        EmojiItem(\"MANS SHOE\", \"objects\", \"clothing\", \"👞\"),
        EmojiItem(\"POUCH\", \"objects\", \"clothing\", \"👝\"),
        EmojiItem(\"HANDBAG\", \"objects\", \"clothing\", \"👜\"),
        EmojiItem(\"PURSE\", \"objects\", \"clothing\", \"👛\"),
        EmojiItem(\"WOMANS CLOTHES\", \"objects\", \"clothing\", \"👚\"),
        EmojiItem(\"BIKINI\", \"objects\", \"clothing\", \"👙\"),
        EmojiItem(\"KIMONO\", \"objects\", \"clothing\", \"👘\"),
        EmojiItem(\"DRESS\", \"objects\", \"clothing\", \"👗\"),
        EmojiItem(\"JEANS\", \"objects\", \"clothing\", \"👖\"),
        EmojiItem(\"T-SHIRT\", \"objects\", \"clothing\", \"👕\"),
        EmojiItem(\"NECKTIE\", \"objects\", \"clothing\", \"👔\"),
        EmojiItem(\"EYEGLASSES\", \"objects\", \"clothing\", \"👓\"),
        EmojiItem(\"WOMANS HAT\", \"objects\", \"clothing\", \"👒\"),
        EmojiItem(\"CROWN\", \"objects\", \"clothing\", \"👑\"),
        EmojiItem(\"TOP HAT\", \"objects\", \"clothing\", \"🎩\"),
        EmojiItem(\"GRADUATION CAP\", \"objects\", \"clothing\", \"🎓\"),
        EmojiItem(\"SCHOOL SATCHEL\", \"objects\", \"clothing\", \"🎒\"),
        EmojiItem(\"KEYBOARD\", \"objects\", \"computer\", \"⌨\"),
        EmojiItem(\"ABACUS\", \"objects\", \"computer\", \"🧮\"),
        EmojiItem(\"TRACKBALL\", \"objects\", \"computer\", \"🖲\"),
        EmojiItem(\"THREE BUTTON MOUSE\", \"objects\", \"computer\", \"🖱\"),
        EmojiItem(\"PRINTER\", \"objects\", \"computer\", \"🖨\"),
        EmojiItem(\"DESKTOP COMPUTER\", \"objects\", \"computer\", \"🖥\"),
        EmojiItem(\"ELECTRIC PLUG\", \"objects\", \"computer\", \"🔌\"),
        EmojiItem(\"BATTERY\", \"objects\", \"computer\", \"🔋\"),
        EmojiItem(\"DVD\", \"objects\", \"computer\", \"📀\"),
        EmojiItem(\"OPTICAL DISC\", \"objects\", \"computer\", \"💿\"),
        EmojiItem(\"FLOPPY DISK\", \"objects\", \"computer\", \"💾\"),
        EmojiItem(\"MINIDISC\", \"objects\", \"computer\", \"💽\"),
        EmojiItem(\"PERSONAL COMPUTER\", \"objects\", \"computer\", \"💻\"),
        EmojiItem(\"TOOTHBRUSH\", \"objects\", \"household\", \"🪥\"),
        EmojiItem(\"MOUSE TRAP\", \"objects\", \"household\", \"🪤\"),
        EmojiItem(\"BUCKET\", \"objects\", \"household\", \"🪣\"),
        EmojiItem(\"PLUNGER\", \"objects\", \"household\", \"🪠\"),
        EmojiItem(\"WINDOW\", \"objects\", \"household\", \"🪟\"),
        EmojiItem(\"MIRROR\", \"objects\", \"household\", \"🪞\"),
        EmojiItem(\"RAZOR\", \"objects\", \"household\", \"🪒\"),
        EmojiItem(\"CHAIR\", \"objects\", \"household\", \"🪑\"),
        EmojiItem(\"SPONGE\", \"objects\", \"household\", \"🧽\"),
        EmojiItem(\"BAR OF SOAP\", \"objects\", \"household\", \"🧼\"),
        EmojiItem(\"ROLL OF PAPER\", \"objects\", \"household\", \"🧻\"),
        EmojiItem(\"BASKET\", \"objects\", \"household\", \"🧺\"),
        EmojiItem(\"BROOM\", \"objects\", \"household\", \"🧹\"),
        EmojiItem(\"SAFETY PIN\", \"objects\", \"household\", \"🧷\"),
        EmojiItem(\"LOTION BOTTLE\", \"objects\", \"household\", \"🧴\"),
        EmojiItem(\"FIRE EXTINGUISHER\", \"objects\", \"household\", \"🧯\"),
        EmojiItem(\"ELEVATOR\", \"objects\", \"household\", \"🛗\"),
        EmojiItem(\"SHOPPING TROLLEY\", \"objects\", \"household\", \"🛒\"),
        EmojiItem(\"BED\", \"objects\", \"household\", \"🛏\"),
        EmojiItem(\"COUCH AND LAMP\", \"objects\", \"household\", \"🛋\"),
        EmojiItem(\"BATHTUB\", \"objects\", \"household\", \"🛁\"),
        EmojiItem(\"SHOWER\", \"objects\", \"household\", \"🚿\"),
        EmojiItem(\"TOILET\", \"objects\", \"household\", \"🚽\"),
        EmojiItem(\"DOOR\", \"objects\", \"household\", \"🚪\"),
        EmojiItem(\"DIYA LAMP\", \"objects\", \"light & video\", \"🪔\"),
        EmojiItem(\"CANDLE\", \"objects\", \"light & video\", \"🕯\"),
        EmojiItem(\"ELECTRIC TORCH\", \"objects\", \"light & video\", \"🔦\"),
        EmojiItem(
            \"RIGHT-POINTING MAGNIFYING GLASS\", \"objects\", \"light & video\", \"🔎\"
        ),
        EmojiItem(
            \"LEFT-POINTING MAGNIFYING GLASS\", \"objects\", \"light & video\", \"🔍\"
        ),
        EmojiItem(\"FILM PROJECTOR\", \"objects\", \"light & video\", \"📽\"),
        EmojiItem(\"VIDEOCASSETTE\", \"objects\", \"light & video\", \"📼\"),
        EmojiItem(\"TELEVISION\", \"objects\", \"light & video\", \"📺\"),
        EmojiItem(\"VIDEO CAMERA\", \"objects\", \"light & video\", \"📹\"),
        EmojiItem(\"CAMERA WITH FLASH\", \"objects\", \"light & video\", \"📸\"),
        EmojiItem(\"CAMERA\", \"objects\", \"light & video\", \"📷\"),
        EmojiItem(\"ELECTRIC LIGHT BULB\", \"objects\", \"light & video\", \"💡\"),
        EmojiItem(\"IZAKAYA LANTERN\", \"objects\", \"light & video\", \"🏮\"),
        EmojiItem(\"CLAPPER BOARD\", \"objects\", \"light & video\", \"🎬\"),
        EmojiItem(\"MOVIE CAMERA\", \"objects\", \"light & video\", \"🎥\"),
        EmojiItem(\"FILM FRAMES\", \"objects\", \"light & video\", \"🎞\"),
        EmojiItem(\"OLD KEY\", \"objects\", \"lock\", \"🗝\"),
        EmojiItem(\"OPEN LOCK\", \"objects\", \"lock\", \"🔓\"),
        EmojiItem(\"LOCK\", \"objects\", \"lock\", \"🔒\"),
        EmojiItem(\"KEY\", \"objects\", \"lock\", \"🔑\"),
        EmojiItem(\"CLOSED LOCK WITH KEY\", \"objects\", \"lock\", \"🔐\"),
        EmojiItem(\"LOCK WITH INK PEN\", \"objects\", \"lock\", \"🔏\"),
        EmojiItem(\"ENVELOPE\", \"objects\", \"mail\", \"✉\"),
        EmojiItem(\"BALLOT BOX WITH BALLOT\", \"objects\", \"mail\", \"🗳\"),
        EmojiItem(\"POSTBOX\", \"objects\", \"mail\", \"📮\"),
        EmojiItem(\"OPEN MAILBOX WITH LOWERED FLAG\", \"objects\", \"mail\", \"📭\"),
        EmojiItem(\"OPEN MAILBOX WITH RAISED FLAG\", \"objects\", \"mail\", \"📬\"),
        EmojiItem(\"CLOSED MAILBOX WITH RAISED FLAG\", \"objects\", \"mail\", \"📫\"),
        EmojiItem(\"CLOSED MAILBOX WITH LOWERED FLAG\", \"objects\", \"mail\", \"📪\"),
        EmojiItem(
            \"ENVELOPE WITH DOWNWARDS ARROW ABOVE\", \"objects\", \"mail\", \"📩\"
        ),
        EmojiItem(\"INCOMING ENVELOPE\", \"objects\", \"mail\", \"📨\"),
        EmojiItem(\"E-MAIL SYMBOL\", \"objects\", \"mail\", \"📧\"),
        EmojiItem(\"PACKAGE\", \"objects\", \"mail\", \"📦\"),
        EmojiItem(\"INBOX TRAY\", \"objects\", \"mail\", \"📥\"),
        EmojiItem(\"OUTBOX TRAY\", \"objects\", \"mail\", \"📤\"),
        EmojiItem(\"STETHOSCOPE\", \"objects\", \"medical\", \"🩺\"),
        EmojiItem(\"ADHESIVE BANDAGE\", \"objects\", \"medical\", \"🩹\"),
        EmojiItem(\"DROP OF BLOOD\", \"objects\", \"medical\", \"🩸\"),
        EmojiItem(\"PILL\", \"objects\", \"medical\", \"💊\"),
        EmojiItem(\"SYRINGE\", \"objects\", \"medical\", \"💉\"),
        EmojiItem(\"COIN\", \"objects\", \"money\", \"🪙\"),
        EmojiItem(\"RECEIPT\", \"objects\", \"money\", \"🧾\"),
        EmojiItem(
            \"CHART WITH UPWARDS TREND AND YEN SIGN\", \"objects\", \"money\", \"💹\"
        ),
        EmojiItem(\"MONEY WITH WINGS\", \"objects\", \"money\", \"💸\"),
        EmojiItem(\"BANKNOTE WITH POUND SIGN\", \"objects\", \"money\", \"💷\"),
        EmojiItem(\"BANKNOTE WITH EURO SIGN\", \"objects\", \"money\", \"💶\"),
        EmojiItem(\"BANKNOTE WITH DOLLAR SIGN\", \"objects\", \"money\", \"💵\"),
        EmojiItem(\"BANKNOTE WITH YEN SIGN\", \"objects\", \"money\", \"💴\"),
        EmojiItem(\"CREDIT CARD\", \"objects\", \"money\", \"💳\"),
        EmojiItem(\"MONEY BAG\", \"objects\", \"money\", \"💰\"),
        EmojiItem(\"RADIO\", \"objects\", \"music\", \"📻\"),
        EmojiItem(\"MUSICAL SCORE\", \"objects\", \"music\", \"🎼\"),
        EmojiItem(\"MULTIPLE MUSICAL NOTES\", \"objects\", \"music\", \"🎶\"),
        EmojiItem(\"MUSICAL NOTE\", \"objects\", \"music\", \"🎵\"),
        EmojiItem(\"HEADPHONE\", \"objects\", \"music\", \"🎧\"),
        EmojiItem(\"MICROPHONE\", \"objects\", \"music\", \"🎤\"),
        EmojiItem(\"CONTROL KNOBS\", \"objects\", \"music\", \"🎛\"),
        EmojiItem(\"LEVEL SLIDER\", \"objects\", \"music\", \"🎚\"),
        EmojiItem(\"STUDIO MICROPHONE\", \"objects\", \"music\", \"🎙\"),
        EmojiItem(\"LONG DRUM\", \"objects\", \"musical-instrument\", \"🪘\"),
        EmojiItem(\"ACCORDION\", \"objects\", \"musical-instrument\", \"🪗\"),
        EmojiItem(\"BANJO\", \"objects\", \"musical-instrument\", \"🪕\"),
        EmojiItem(
            \"DRUM WITH DRUMSTICKS\", \"objects\", \"musical-instrument\", \"🥁\"
        ),
        EmojiItem(\"VIOLIN\", \"objects\", \"musical-instrument\", \"🎻\"),
        EmojiItem(\"TRUMPET\", \"objects\", \"musical-instrument\", \"🎺\"),
        EmojiItem(\"MUSICAL KEYBOARD\", \"objects\", \"musical-instrument\", \"🎹\"),
        EmojiItem(\"GUITAR\", \"objects\", \"musical-instrument\", \"🎸\"),
        EmojiItem(\"SAXOPHONE\", \"objects\", \"musical-instrument\", \"🎷\"),
        EmojiItem(\"BLACK SCISSORS\", \"objects\", \"office\", \"✂\"),
        EmojiItem(\"SPIRAL CALENDAR PAD\", \"objects\", \"office\", \"🗓\"),
        EmojiItem(\"SPIRAL NOTE PAD\", \"objects\", \"office\", \"🗒\"),
        EmojiItem(\"WASTEBASKET\", \"objects\", \"office\", \"🗑\"),
        EmojiItem(\"FILE CABINET\", \"objects\", \"office\", \"🗄\"),
        EmojiItem(\"CARD FILE BOX\", \"objects\", \"office\", \"🗃\"),
        EmojiItem(\"CARD INDEX DIVIDERS\", \"objects\", \"office\", \"🗂\"),
        EmojiItem(\"LINKED PAPERCLIPS\", \"objects\", \"office\", \"🖇\"),
        EmojiItem(\"TRIANGULAR RULER\", \"objects\", \"office\", \"📐\"),
        EmojiItem(\"STRAIGHT RULER\", \"objects\", \"office\", \"📏\"),
        EmojiItem(\"PAPERCLIP\", \"objects\", \"office\", \"📎\"),
        EmojiItem(\"ROUND PUSHPIN\", \"objects\", \"office\", \"📍\"),
        EmojiItem(\"PUSHPIN\", \"objects\", \"office\", \"📌\"),
        EmojiItem(\"CLIPBOARD\", \"objects\", \"office\", \"📋\"),
        EmojiItem(\"BAR CHART\", \"objects\", \"office\", \"📊\"),
        EmojiItem(\"CHART WITH DOWNWARDS TREND\", \"objects\", \"office\", \"📉\"),
        EmojiItem(\"CHART WITH UPWARDS TREND\", \"objects\", \"office\", \"📈\"),
        EmojiItem(\"CARD INDEX\", \"objects\", \"office\", \"📇\"),
        EmojiItem(\"TEAR-OFF CALENDAR\", \"objects\", \"office\", \"📆\"),
        EmojiItem(\"CALENDAR\", \"objects\", \"office\", \"📅\"),
        EmojiItem(\"OPEN FILE FOLDER\", \"objects\", \"office\", \"📂\"),
        EmojiItem(\"FILE FOLDER\", \"objects\", \"office\", \"📁\"),
        EmojiItem(\"BRIEFCASE\", \"objects\", \"office\", \"💼\"),
        EmojiItem(\"FUNERAL URN\", \"objects\", \"other-object\", \"⚱\"),
        EmojiItem(\"COFFIN\", \"objects\", \"other-object\", \"⚰\"),
        EmojiItem(\"PLACARD\", \"objects\", \"other-object\", \"🪧\"),
        EmojiItem(\"HEADSTONE\", \"objects\", \"other-object\", \"🪦\"),
        EmojiItem(\"SMOKING SYMBOL\", \"objects\", \"other-object\", \"🚬\"),
        EmojiItem(\"MOYAI\", \"objects\", \"other-object\", \"🗿\"),
        EmojiItem(\"BLACK TELEPHONE\", \"objects\", \"phone\", \"☎\"),
        EmojiItem(
            \"MOBILE PHONE WITH RIGHTWARDS ARROW AT LEFT\",
            \"objects\",
            \"phone\",
            \"📲\",
        ),
        EmojiItem(\"MOBILE PHONE\", \"objects\", \"phone\", \"📱\"),
        EmojiItem(\"FAX MACHINE\", \"objects\", \"phone\", \"📠\"),
        EmojiItem(\"PAGER\", \"objects\", \"phone\", \"📟\"),
        EmojiItem(\"TELEPHONE RECEIVER\", \"objects\", \"phone\", \"📞\"),
        EmojiItem(\"ALEMBIC\", \"objects\", \"science\", \"⚗\"),
        EmojiItem(\"DNA DOUBLE HELIX\", \"objects\", \"science\", \"🧬\"),
        EmojiItem(\"PETRI DISH\", \"objects\", \"science\", \"🧫\"),
        EmojiItem(\"TEST TUBE\", \"objects\", \"science\", \"🧪\"),
        EmojiItem(\"TELESCOPE\", \"objects\", \"science\", \"🔭\"),
        EmojiItem(\"MICROSCOPE\", \"objects\", \"science\", \"🔬\"),
        EmojiItem(\"SATELLITE ANTENNA\", \"objects\", \"science\", \"📡\"),
        EmojiItem(\"BELL WITH CANCELLATION STROKE\", \"objects\", \"sound\", \"🔕\"),
        EmojiItem(\"BELL\", \"objects\", \"sound\", \"🔔\"),
        EmojiItem(\"SPEAKER WITH THREE SOUND WAVES\", \"objects\", \"sound\", \"🔊\"),
        EmojiItem(\"SPEAKER WITH ONE SOUND WAVE\", \"objects\", \"sound\", \"🔉\"),
        EmojiItem(\"SPEAKER\", \"objects\", \"sound\", \"🔈\"),
        EmojiItem(\"SPEAKER WITH CANCELLATION STROKE\", \"objects\", \"sound\", \"🔇\"),
        EmojiItem(\"POSTAL HORN\", \"objects\", \"sound\", \"📯\"),
        EmojiItem(\"CHEERING MEGAPHONE\", \"objects\", \"sound\", \"📣\"),
        EmojiItem(\"PUBLIC ADDRESS LOUDSPEAKER\", \"objects\", \"sound\", \"📢\"),
        EmojiItem(\"CHAINS\", \"objects\", \"tool\", \"⛓\"),
        EmojiItem(\"PICK\", \"objects\", \"tool\", \"⛏\"),
        EmojiItem(\"GEAR\", \"objects\", \"tool\", \"⚙\"),
        EmojiItem(\"SCALES\", \"objects\", \"tool\", \"⚖\"),
        EmojiItem(\"CROSSED SWORDS\", \"objects\", \"tool\", \"⚔\"),
        EmojiItem(\"HAMMER AND PICK\", \"objects\", \"tool\", \"⚒\"),
        EmojiItem(\"HOOK\", \"objects\", \"tool\", \"🪝\"),
        EmojiItem(\"LADDER\", \"objects\", \"tool\", \"🪜\"),
        EmojiItem(\"SCREWDRIVER\", \"objects\", \"tool\", \"🪛\"),
        EmojiItem(\"CARPENTRY SAW\", \"objects\", \"tool\", \"🪚\"),
        EmojiItem(\"AXE\", \"objects\", \"tool\", \"🪓\"),
        EmojiItem(\"BOOMERANG\", \"objects\", \"tool\", \"🪃\"),
        EmojiItem(\"MAGNET\", \"objects\", \"tool\", \"🧲\"),
        EmojiItem(\"TOOLBOX\", \"objects\", \"tool\", \"🧰\"),
        EmojiItem(\"PROBING CANE\", \"objects\", \"tool\", \"🦯\"),
        EmojiItem(\"SHIELD\", \"objects\", \"tool\", \"🛡\"),
        EmojiItem(\"HAMMER AND WRENCH\", \"objects\", \"tool\", \"🛠\"),
        EmojiItem(\"DAGGER KNIFE\", \"objects\", \"tool\", \"🗡\"),
        EmojiItem(\"COMPRESSION\", \"objects\", \"tool\", \"🗜\"),
        EmojiItem(\"PISTOL\", \"objects\", \"tool\", \"🔫\"),
        EmojiItem(\"NUT AND BOLT\", \"objects\", \"tool\", \"🔩\"),
        EmojiItem(\"HAMMER\", \"objects\", \"tool\", \"🔨\"),
        EmojiItem(\"WRENCH\", \"objects\", \"tool\", \"🔧\"),
        EmojiItem(\"LINK SYMBOL\", \"objects\", \"tool\", \"🔗\"),
        EmojiItem(\"BOW AND ARROW\", \"objects\", \"tool\", \"🏹\"),
        EmojiItem(\"PENCIL\", \"objects\", \"writing\", \"✏\"),
        EmojiItem(\"BLACK NIB\", \"objects\", \"writing\", \"✒\"),
        EmojiItem(\"LOWER LEFT CRAYON\", \"objects\", \"writing\", \"🖍\"),
        EmojiItem(\"LOWER LEFT PAINTBRUSH\", \"objects\", \"writing\", \"🖌\"),
        EmojiItem(\"LOWER LEFT FOUNTAIN PEN\", \"objects\", \"writing\", \"🖋\"),
        EmojiItem(\"LOWER LEFT BALLPOINT PEN\", \"objects\", \"writing\", \"🖊\"),
        EmojiItem(\"MEMO\", \"objects\", \"writing\", \"📝\"),
        EmojiItem(\"LUNGS\", \"people-body\", \"body-parts\", \"🫁\"),
        EmojiItem(\"ANATOMICAL HEART\", \"people-body\", \"body-parts\", \"🫀\"),
        EmojiItem(\"BRAIN\", \"people-body\", \"body-parts\", \"🧠\"),
        EmojiItem(\"MECHANICAL LEG\", \"people-body\", \"body-parts\", \"🦿\"),
        EmojiItem(\"MECHANICAL ARM\", \"people-body\", \"body-parts\", \"🦾\"),
        EmojiItem(\"EAR WITH HEARING AID\", \"people-body\", \"body-parts\", \"🦻\"),
        EmojiItem(\"TOOTH\", \"people-body\", \"body-parts\", \"🦷\"),
        EmojiItem(\"FOOT\", \"people-body\", \"body-parts\", \"🦶\"),
        EmojiItem(\"LEG\", \"people-body\", \"body-parts\", \"🦵\"),
        EmojiItem(\"BONE\", \"people-body\", \"body-parts\", \"🦴\"),
        EmojiItem(\"FLEXED BICEPS\", \"people-body\", \"body-parts\", \"💪\"),
        EmojiItem(\"TONGUE\", \"people-body\", \"body-parts\", \"👅\"),
        EmojiItem(\"MOUTH\", \"people-body\", \"body-parts\", \"👄\"),
        EmojiItem(\"NOSE\", \"people-body\", \"body-parts\", \"👃\"),
        EmojiItem(\"EAR\", \"people-body\", \"body-parts\", \"👂\"),
        EmojiItem(\"EYE\", \"people-body\", \"body-parts\", \"👁\"),
        EmojiItem(\"EYES\", \"people-body\", \"body-parts\", \"👀\"),
        EmojiItem(\"COUPLE WITH HEART\", \"people-body\", \"family\", \"💑\"),
        EmojiItem(\"KISS\", \"people-body\", \"family\", \"💏\"),
        EmojiItem(\"TWO WOMEN HOLDING HANDS\", \"people-body\", \"family\", \"👭\"),
        EmojiItem(\"TWO MEN HOLDING HANDS\", \"people-body\", \"family\", \"👬\"),
        EmojiItem(\"MAN AND WOMAN HOLDING HANDS\", \"people-body\", \"family\", \"👫\"),
        EmojiItem(\"FAMILY\", \"people-body\", \"family\", \"👪\"),
        EmojiItem(\"RAISED FIST\", \"people-body\", \"hand-fingers-closed\", \"✊\"),
        EmojiItem(
            \"RIGHT-FACING FIST\", \"people-body\", \"hand-fingers-closed\", \"🤜\"
        ),
        EmojiItem(
            \"LEFT-FACING FIST\", \"people-body\", \"hand-fingers-closed\", \"🤛\"
        ),
        EmojiItem(
            \"THUMBS DOWN SIGN\", \"people-body\", \"hand-fingers-closed\", \"👎\"
        ),
        EmojiItem(\"THUMBS UP SIGN\", \"people-body\", \"hand-fingers-closed\", \"👍\"),
        EmojiItem(
            \"FISTED HAND SIGN\", \"people-body\", \"hand-fingers-closed\", \"👊\"
        ),
        EmojiItem(\"RAISED HAND\", \"people-body\", \"hand-fingers-open\", \"✋\"),
        EmojiItem(
            \"RAISED BACK OF HAND\", \"people-body\", \"hand-fingers-open\", \"🤚\"
        ),
        EmojiItem(
            \"RAISED HAND WITH PART BETWEEN MIDDLE AND RING FINGERS\",
            \"people-body\",
            \"hand-fingers-open\",
            \"🖖\",
        ),
        EmojiItem(
            \"RAISED HAND WITH FINGERS SPLAYED\",
            \"people-body\",
            \"hand-fingers-open\",
            \"🖐\",
        ),
        EmojiItem(\"WAVING HAND SIGN\", \"people-body\", \"hand-fingers-open\", \"👋\"),
        EmojiItem(\"VICTORY HAND\", \"people-body\", \"hand-fingers-partial\", \"✌\"),
        EmojiItem(
            \"I LOVE YOU HAND SIGN\", \"people-body\", \"hand-fingers-partial\", \"🤟\"
        ),
        EmojiItem(
            \"HAND WITH INDEX AND MIDDLE FINGERS CROSSED\",
            \"people-body\",
            \"hand-fingers-partial\",
            \"🤞\",
        ),
        EmojiItem(\"CALL ME HAND\", \"people-body\", \"hand-fingers-partial\", \"🤙\"),
        EmojiItem(
            \"SIGN OF THE HORNS\", \"people-body\", \"hand-fingers-partial\", \"🤘\"
        ),
        EmojiItem(\"PINCHING HAND\", \"people-body\", \"hand-fingers-partial\", \"🤏\"),
        EmojiItem(
            \"PINCHED FINGERS\", \"people-body\", \"hand-fingers-partial\", \"🤌\"
        ),
        EmojiItem(\"OK HAND SIGN\", \"people-body\", \"hand-fingers-partial\", \"👌\"),
        EmojiItem(\"WRITING HAND\", \"people-body\", \"hand-prop\", \"✍\"),
        EmojiItem(\"SELFIE\", \"people-body\", \"hand-prop\", \"🤳\"),
        EmojiItem(\"NAIL POLISH\", \"people-body\", \"hand-prop\", \"💅\"),
        EmojiItem(\"PALMS UP TOGETHER\", \"people-body\", \"hands\", \"🤲\"),
        EmojiItem(\"HANDSHAKE\", \"people-body\", \"hands\", \"🤝\"),
        EmojiItem(\"PERSON WITH FOLDED HANDS\", \"people-body\", \"hands\", \"🙏\"),
        EmojiItem(
            \"PERSON RAISING BOTH HANDS IN CELEBRATION\",
            \"people-body\",
            \"hands\",
            \"🙌\",
        ),
        EmojiItem(\"OPEN HANDS SIGN\", \"people-body\", \"hands\", \"👐\"),
        EmojiItem(\"CLAPPING HANDS SIGN\", \"people-body\", \"hands\", \"👏\"),
        EmojiItem(
            \"WHITE UP POINTING INDEX\", \"people-body\", \"hand-single-finger\", \"☝\"
        ),
        EmojiItem(
            \"REVERSED HAND WITH MIDDLE FINGER EXTENDED\",
            \"people-body\",
            \"hand-single-finger\",
            \"🖕\",
        ),
        EmojiItem(
            \"WHITE RIGHT POINTING BACKHAND INDEX\",
            \"people-body\",
            \"hand-single-finger\",
            \"👉\",
        ),
        EmojiItem(
            \"WHITE LEFT POINTING BACKHAND INDEX\",
            \"people-body\",
            \"hand-single-finger\",
            \"👈\",
        ),
        EmojiItem(
            \"WHITE DOWN POINTING BACKHAND INDEX\",
            \"people-body\",
            \"hand-single-finger\",
            \"👇\",
        ),
        EmojiItem(
            \"WHITE UP POINTING BACKHAND INDEX\",
            \"people-body\",
            \"hand-single-finger\",
            \"👆\",
        ),
        EmojiItem(\"BEARDED PERSON\", \"people-body\", \"person\", \"🧔\"),
        EmojiItem(\"OLDER ADULT\", \"people-body\", \"person\", \"🧓\"),
        EmojiItem(\"CHILD\", \"people-body\", \"person\", \"🧒\"),
        EmojiItem(\"ADULT\", \"people-body\", \"person\", \"🧑\"),
        EmojiItem(\"BABY\", \"people-body\", \"person\", \"👶\"),
        EmojiItem(\"OLDER WOMAN\", \"people-body\", \"person\", \"👵\"),
        EmojiItem(\"OLDER MAN\", \"people-body\", \"person\", \"👴\"),
        EmojiItem(\"PERSON WITH BLOND HAIR\", \"people-body\", \"person\", \"👱\"),
        EmojiItem(\"WOMAN\", \"people-body\", \"person\", \"👩\"),
        EmojiItem(\"MAN\", \"people-body\", \"person\", \"👨\"),
        EmojiItem(\"GIRL\", \"people-body\", \"person\", \"👧\"),
        EmojiItem(\"BOY\", \"people-body\", \"person\", \"👦\"),
        EmojiItem(\"PERSON CLIMBING\", \"people-body\", \"person-activity\", \"🧗\"),
        EmojiItem(
            \"PERSON IN STEAMY ROOM\", \"people-body\", \"person-activity\", \"🧖\"
        ),
        EmojiItem(\"KNEELING PERSON\", \"people-body\", \"person-activity\", \"🧎\"),
        EmojiItem(\"STANDING PERSON\", \"people-body\", \"person-activity\", \"🧍\"),
        EmojiItem(\"PEDESTRIAN\", \"people-body\", \"person-activity\", \"🚶\"),
        EmojiItem(\"MAN DANCING\", \"people-body\", \"person-activity\", \"🕺\"),
        EmojiItem(
            \"MAN IN BUSINESS SUIT LEVITATING\",
            \"people-body\",
            \"person-activity\",
            \"🕴\",
        ),
        EmojiItem(\"HAIRCUT\", \"people-body\", \"person-activity\", \"💇\"),
        EmojiItem(\"FACE MASSAGE\", \"people-body\", \"person-activity\", \"💆\"),
        EmojiItem(\"DANCER\", \"people-body\", \"person-activity\", \"💃\"),
        EmojiItem(
            \"WOMAN WITH BUNNY EARS\", \"people-body\", \"person-activity\", \"👯\"
        ),
        EmojiItem(\"RUNNER\", \"people-body\", \"person-activity\", \"🏃\"),
        EmojiItem(\"ZOMBIE\", \"people-body\", \"person-fantasy\", \"🧟\"),
        EmojiItem(\"GENIE\", \"people-body\", \"person-fantasy\", \"🧞\"),
        EmojiItem(\"ELF\", \"people-body\", \"person-fantasy\", \"🧝\"),
        EmojiItem(\"MERPERSON\", \"people-body\", \"person-fantasy\", \"🧜\"),
        EmojiItem(\"VAMPIRE\", \"people-body\", \"person-fantasy\", \"🧛\"),
        EmojiItem(\"FAIRY\", \"people-body\", \"person-fantasy\", \"🧚\"),
        EmojiItem(\"MAGE\", \"people-body\", \"person-fantasy\", \"🧙\"),
        EmojiItem(\"SUPERVILLAIN\", \"people-body\", \"person-fantasy\", \"🦹\"),
        EmojiItem(\"SUPERHERO\", \"people-body\", \"person-fantasy\", \"🦸\"),
        EmojiItem(\"MOTHER CHRISTMAS\", \"people-body\", \"person-fantasy\", \"🤶\"),
        EmojiItem(\"BABY ANGEL\", \"people-body\", \"person-fantasy\", \"👼\"),
        EmojiItem(\"FATHER CHRISTMAS\", \"people-body\", \"person-fantasy\", \"🎅\"),
        EmojiItem(\"DEAF PERSON\", \"people-body\", \"person-gesture\", \"🧏\"),
        EmojiItem(\"SHRUG\", \"people-body\", \"person-gesture\", \"🤷\"),
        EmojiItem(\"FACE PALM\", \"people-body\", \"person-gesture\", \"🤦\"),
        EmojiItem(
            \"PERSON WITH POUTING FACE\", \"people-body\", \"person-gesture\", \"🙎\"
        ),
        EmojiItem(\"PERSON FROWNING\", \"people-body\", \"person-gesture\", \"🙍\"),
        EmojiItem(
            \"HAPPY PERSON RAISING ONE HAND\",
            \"people-body\",
            \"person-gesture\",
            \"🙋\",
        ),
        EmojiItem(
            \"PERSON BOWING DEEPLY\", \"people-body\", \"person-gesture\", \"🙇\"
        ),
        EmojiItem(
            \"FACE WITH OK GESTURE\", \"people-body\", \"person-gesture\", \"🙆\"
        ),
        EmojiItem(
            \"FACE WITH NO GOOD GESTURE\", \"people-body\", \"person-gesture\", \"🙅\"
        ),
        EmojiItem(
            \"INFORMATION DESK PERSON\", \"people-body\", \"person-gesture\", \"💁\"
        ),
        EmojiItem(
            \"PERSON IN LOTUS POSITION\", \"people-body\", \"person-resting\", \"🧘\"
        ),
        EmojiItem(
            \"SLEEPING ACCOMMODATION\", \"people-body\", \"person-resting\", \"🛌\"
        ),
        EmojiItem(\"BATH\", \"people-body\", \"person-resting\", \"🛀\"),
        EmojiItem(\"PERSON WITH HEADSCARF\", \"people-body\", \"person-role\", \"🧕\"),
        EmojiItem(\"NINJA\", \"people-body\", \"person-role\", \"🥷\"),
        EmojiItem(\"MAN IN TUXEDO\", \"people-body\", \"person-role\", \"🤵\"),
        EmojiItem(\"PRINCE\", \"people-body\", \"person-role\", \"🤴\"),
        EmojiItem(\"BREAST-FEEDING\", \"people-body\", \"person-role\", \"🤱\"),
        EmojiItem(\"PREGNANT WOMAN\", \"people-body\", \"person-role\", \"🤰\"),
        EmojiItem(\"SLEUTH OR SPY\", \"people-body\", \"person-role\", \"🕵\"),
        EmojiItem(\"GUARDSMAN\", \"people-body\", \"person-role\", \"💂\"),
        EmojiItem(\"PRINCESS\", \"people-body\", \"person-role\", \"👸\"),
        EmojiItem(\"CONSTRUCTION WORKER\", \"people-body\", \"person-role\", \"👷\"),
        EmojiItem(\"MAN WITH TURBAN\", \"people-body\", \"person-role\", \"👳\"),
        EmojiItem(\"MAN WITH GUA PI MAO\", \"people-body\", \"person-role\", \"👲\"),
        EmojiItem(\"BRIDE WITH VEIL\", \"people-body\", \"person-role\", \"👰\"),
        EmojiItem(\"POLICE OFFICER\", \"people-body\", \"person-role\", \"👮\"),
        EmojiItem(\"PERSON WITH BALL\", \"people-body\", \"person-sport\", \"⛹\"),
        EmojiItem(\"SKIER\", \"people-body\", \"person-sport\", \"⛷\"),
        EmojiItem(\"HANDBALL\", \"people-body\", \"person-sport\", \"🤾\"),
        EmojiItem(\"WATER POLO\", \"people-body\", \"person-sport\", \"🤽\"),
        EmojiItem(\"WRESTLERS\", \"people-body\", \"person-sport\", \"🤼\"),
        EmojiItem(\"FENCER\", \"people-body\", \"person-sport\", \"🤺\"),
        EmojiItem(\"JUGGLING\", \"people-body\", \"person-sport\", \"🤹\"),
        EmojiItem(
            \"PERSON DOING CARTWHEEL\", \"people-body\", \"person-sport\", \"🤸\"
        ),
        EmojiItem(\"MOUNTAIN BICYCLIST\", \"people-body\", \"person-sport\", \"🚵\"),
        EmojiItem(\"BICYCLIST\", \"people-body\", \"person-sport\", \"🚴\"),
        EmojiItem(\"ROWBOAT\", \"people-body\", \"person-sport\", \"🚣\"),
        EmojiItem(\"GOLFER\", \"people-body\", \"person-sport\", \"🏌\"),
        EmojiItem(\"WEIGHT LIFTER\", \"people-body\", \"person-sport\", \"🏋\"),
        EmojiItem(\"SWIMMER\", \"people-body\", \"person-sport\", \"🏊\"),
        EmojiItem(\"HORSE RACING\", \"people-body\", \"person-sport\", \"🏇\"),
        EmojiItem(\"SURFER\", \"people-body\", \"person-sport\", \"🏄\"),
        EmojiItem(\"SNOWBOARDER\", \"people-body\", \"person-sport\", \"🏂\"),
        EmojiItem(\"PEOPLE HUGGING\", \"people-body\", \"person-symbol\", \"🫂\"),
        EmojiItem(
            \"SPEAKING HEAD IN SILHOUETTE\", \"people-body\", \"person-symbol\", \"🗣\"
        ),
        EmojiItem(\"BUSTS IN SILHOUETTE\", \"people-body\", \"person-symbol\", \"👥\"),
        EmojiItem(\"BUST IN SILHOUETTE\", \"people-body\", \"person-symbol\", \"👤\"),
        EmojiItem(\"FOOTPRINTS\", \"people-body\", \"person-symbol\", \"👣\"),
        EmojiItem(
            \"CIRCLED LATIN CAPITAL LETTER M\", \"symbols\", \"alphanum\", \"Ⓜ\"
        ),
        EmojiItem(\"CIRCLED IDEOGRAPH SECRET\", \"symbols\", \"alphanum\", \"㊙\"),
        EmojiItem(
            \"CIRCLED IDEOGRAPH CONGRATULATION\", \"symbols\", \"alphanum\", \"㊗\"
        ),
        EmojiItem(\"INFORMATION SOURCE\", \"symbols\", \"alphanum\", \"ℹ\"),
        EmojiItem(
            \"INPUT SYMBOL FOR LATIN LETTERS\", \"symbols\", \"alphanum\", \"🔤\"
        ),
        EmojiItem(\"INPUT SYMBOL FOR SYMBOLS\", \"symbols\", \"alphanum\", \"🔣\"),
        EmojiItem(\"INPUT SYMBOL FOR NUMBERS\", \"symbols\", \"alphanum\", \"🔢\"),
        EmojiItem(
            \"INPUT SYMBOL FOR LATIN SMALL LETTERS\", \"symbols\", \"alphanum\", \"🔡\"
        ),
        EmojiItem(
            \"INPUT SYMBOL FOR LATIN CAPITAL LETTERS\",
            \"symbols\",
            \"alphanum\",
            \"🔠\",
        ),
        EmojiItem(\"CIRCLED IDEOGRAPH ACCEPT\", \"symbols\", \"alphanum\", \"🉑\"),
        EmojiItem(\"CIRCLED IDEOGRAPH ADVANTAGE\", \"symbols\", \"alphanum\", \"🉐\"),
        EmojiItem(
            \"SQUARED CJK UNIFIED IDEOGRAPH-55B6\", \"symbols\", \"alphanum\", \"🈺\"
        ),
        EmojiItem(
            \"SQUARED CJK UNIFIED IDEOGRAPH-5272\", \"symbols\", \"alphanum\", \"🈹\"
        ),
        EmojiItem(
            \"SQUARED CJK UNIFIED IDEOGRAPH-7533\", \"symbols\", \"alphanum\", \"🈸\"
        ),
        EmojiItem(
            \"SQUARED CJK UNIFIED IDEOGRAPH-6708\", \"symbols\", \"alphanum\", \"🈷\"
        ),
        EmojiItem(
            \"SQUARED CJK UNIFIED IDEOGRAPH-6709\", \"symbols\", \"alphanum\", \"🈶\"
        ),
        EmojiItem(
            \"SQUARED CJK UNIFIED IDEOGRAPH-6E80\", \"symbols\", \"alphanum\", \"🈵\"
        ),
        EmojiItem(
            \"SQUARED CJK UNIFIED IDEOGRAPH-5408\", \"symbols\", \"alphanum\", \"🈴\"
        ),
        EmojiItem(
            \"SQUARED CJK UNIFIED IDEOGRAPH-7A7A\", \"symbols\", \"alphanum\", \"🈳\"
        ),
        EmojiItem(
            \"SQUARED CJK UNIFIED IDEOGRAPH-7981\", \"symbols\", \"alphanum\", \"🈲\"
        ),
        EmojiItem(
            \"SQUARED CJK UNIFIED IDEOGRAPH-6307\", \"symbols\", \"alphanum\", \"🈯\"
        ),
        EmojiItem(
            \"SQUARED CJK UNIFIED IDEOGRAPH-7121\", \"symbols\", \"alphanum\", \"🈚\"
        ),
        EmojiItem(\"SQUARED KATAKANA SA\", \"symbols\", \"alphanum\", \"🈂\"),
        EmojiItem(\"SQUARED KATAKANA KOKO\", \"symbols\", \"alphanum\", \"🈁\"),
        EmojiItem(\"SQUARED VS\", \"symbols\", \"alphanum\", \"🆚\"),
        EmojiItem(
            \"SQUARED UP WITH EXCLAMATION MARK\", \"symbols\", \"alphanum\", \"🆙\"
        ),
        EmojiItem(\"SQUARED SOS\", \"symbols\", \"alphanum\", \"🆘\"),
        EmojiItem(\"SQUARED OK\", \"symbols\", \"alphanum\", \"🆗\"),
        EmojiItem(\"SQUARED NG\", \"symbols\", \"alphanum\", \"🆖\"),
        EmojiItem(\"SQUARED NEW\", \"symbols\", \"alphanum\", \"🆕\"),
        EmojiItem(\"SQUARED ID\", \"symbols\", \"alphanum\", \"🆔\"),
        EmojiItem(\"SQUARED FREE\", \"symbols\", \"alphanum\", \"🆓\"),
        EmojiItem(\"SQUARED COOL\", \"symbols\", \"alphanum\", \"🆒\"),
        EmojiItem(\"SQUARED CL\", \"symbols\", \"alphanum\", \"🆑\"),
        EmojiItem(\"NEGATIVE SQUARED AB\", \"symbols\", \"alphanum\", \"🆎\"),
        EmojiItem(
            \"NEGATIVE SQUARED LATIN CAPITAL LETTER P\",
            \"symbols\",
            \"alphanum\",
            \"🅿\",
        ),
        EmojiItem(
            \"NEGATIVE SQUARED LATIN CAPITAL LETTER O\",
            \"symbols\",
            \"alphanum\",
            \"🅾\",
        ),
        EmojiItem(
            \"NEGATIVE SQUARED LATIN CAPITAL LETTER B\",
            \"symbols\",
            \"alphanum\",
            \"🅱\",
        ),
        EmojiItem(
            \"NEGATIVE SQUARED LATIN CAPITAL LETTER A\",
            \"symbols\",
            \"alphanum\",
            \"🅰\",
        ),
        EmojiItem(\"DOWNWARDS BLACK ARROW\", \"symbols\", \"arrow\", \"⬇\"),
        EmojiItem(\"UPWARDS BLACK ARROW\", \"symbols\", \"arrow\", \"⬆\"),
        EmojiItem(\"LEFTWARDS BLACK ARROW\", \"symbols\", \"arrow\", \"⬅\"),
        EmojiItem(\"BLACK RIGHTWARDS ARROW\", \"symbols\", \"arrow\", \"➡\"),
        EmojiItem(\"RIGHTWARDS ARROW WITH HOOK\", \"symbols\", \"arrow\", \"↪\"),
        EmojiItem(\"LEFTWARDS ARROW WITH HOOK\", \"symbols\", \"arrow\", \"↩\"),
        EmojiItem(
            \"ARROW POINTING RIGHTWARDS THEN CURVING DOWNWARDS\",
            \"symbols\",
            \"arrow\",
            \"⤵\",
        ),
        EmojiItem(
            \"ARROW POINTING RIGHTWARDS THEN CURVING UPWARDS\",
            \"symbols\",
            \"arrow\",
            \"⤴\",
        ),
        EmojiItem(\"SOUTH WEST ARROW\", \"symbols\", \"arrow\", \"↙\"),
        EmojiItem(\"SOUTH EAST ARROW\", \"symbols\", \"arrow\", \"↘\"),
        EmojiItem(\"NORTH EAST ARROW\", \"symbols\", \"arrow\", \"↗\"),
        EmojiItem(\"NORTH WEST ARROW\", \"symbols\", \"arrow\", \"↖\"),
        EmojiItem(\"UP DOWN ARROW\", \"symbols\", \"arrow\", \"↕\"),
        EmojiItem(\"LEFT RIGHT ARROW\", \"symbols\", \"arrow\", \"↔\"),
        EmojiItem(\"TOP WITH UPWARDS ARROW ABOVE\", \"symbols\", \"arrow\", \"🔝\"),
        EmojiItem(\"SOON WITH RIGHTWARDS ARROW ABOVE\", \"symbols\", \"arrow\", \"🔜\"),
        EmojiItem(
            \"ON WITH EXCLAMATION MARK WITH LEFT RIGHT ARROW ABOVE\",
            \"symbols\",
            \"arrow\",
            \"🔛\",
        ),
        EmojiItem(\"END WITH LEFTWARDS ARROW ABOVE\", \"symbols\", \"arrow\", \"🔚\"),
        EmojiItem(\"BACK WITH LEFTWARDS ARROW ABOVE\", \"symbols\", \"arrow\", \"🔙\"),
        EmojiItem(
            \"ANTICLOCKWISE DOWNWARDS AND UPWARDS OPEN CIRCLE ARROWS\",
            \"symbols\",
            \"arrow\",
            \"🔄\",
        ),
        EmojiItem(
            \"CLOCKWISE DOWNWARDS AND UPWARDS OPEN CIRCLE ARROWS\",
            \"symbols\",
            \"arrow\",
            \"🔃\",
        ),
        EmojiItem(\"BLACK LEFT-POINTING TRIANGLE\", \"symbols\", \"av-symbol\", \"◀\"),
        EmojiItem(
            \"BLACK RIGHT-POINTING TRIANGLE\", \"symbols\", \"av-symbol\", \"▶\"
        ),
        EmojiItem(\"BLACK CIRCLE FOR RECORD\", \"symbols\", \"av-symbol\", \"⏺\"),
        EmojiItem(\"BLACK SQUARE FOR STOP\", \"symbols\", \"av-symbol\", \"⏹\"),
        EmojiItem(\"DOUBLE VERTICAL BAR\", \"symbols\", \"av-symbol\", \"⏸\"),
        EmojiItem(
            \"BLACK RIGHT-POINTING TRIANGLE WITH DOUBLE VERTICAL BAR\",
            \"symbols\",
            \"av-symbol\",
            \"⏯\",
        ),
        EmojiItem(
            \"BLACK LEFT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR\",
            \"symbols\",
            \"av-symbol\",
            \"⏮\",
        ),
        EmojiItem(
            \"BLACK RIGHT-POINTING DOUBLE TRIANGLE WITH VERTICAL BAR\",
            \"symbols\",
            \"av-symbol\",
            \"⏭\",
        ),
        EmojiItem(
            \"BLACK DOWN-POINTING DOUBLE TRIANGLE\", \"symbols\", \"av-symbol\", \"⏬\"
        ),
        EmojiItem(
            \"BLACK UP-POINTING DOUBLE TRIANGLE\", \"symbols\", \"av-symbol\", \"⏫\"
        ),
        EmojiItem(
            \"BLACK LEFT-POINTING DOUBLE TRIANGLE\", \"symbols\", \"av-symbol\", \"⏪\"
        ),
        EmojiItem(\"EJECT SYMBOL\", \"symbols\", \"av-symbol\", \"⏏\"),
        EmojiItem(
            \"DOWN-POINTING SMALL RED TRIANGLE\", \"symbols\", \"av-symbol\", \"🔽\"
        ),
        EmojiItem(
            \"UP-POINTING SMALL RED TRIANGLE\", \"symbols\", \"av-symbol\", \"🔼\"
        ),
        EmojiItem(\"HIGH BRIGHTNESS SYMBOL\", \"symbols\", \"av-symbol\", \"🔆\"),
        EmojiItem(\"LOW BRIGHTNESS SYMBOL\", \"symbols\", \"av-symbol\", \"🔅\"),
        EmojiItem(
            \"CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS WITH CIRCLED ONE OVERLAY\",
            \"symbols\",
            \"av-symbol\",
            \"🔂\",
        ),
        EmojiItem(
            \"CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS\",
            \"symbols\",
            \"av-symbol\",
            \"🔁\",
        ),
        EmojiItem(\"TWISTED RIGHTWARDS ARROWS\", \"symbols\", \"av-symbol\", \"🔀\"),
        EmojiItem(\"ANTENNA WITH BARS\", \"symbols\", \"av-symbol\", \"📶\"),
        EmojiItem(\"MOBILE PHONE OFF\", \"symbols\", \"av-symbol\", \"📴\"),
        EmojiItem(\"VIBRATION MODE\", \"symbols\", \"av-symbol\", \"📳\"),
        EmojiItem(\"CINEMA\", \"symbols\", \"av-symbol\", \"🎦\"),
        EmojiItem(\"HEAVY DOLLAR SIGN\", \"symbols\", \"currency\", \"💲\"),
        EmojiItem(\"CURRENCY EXCHANGE\", \"symbols\", \"currency\", \"💱\"),
        EmojiItem(
            \"MALE WITH STROKE AND MALE AND FEMALE SIGN\",
            \"symbols\",
            \"gender\",
            \"⚧\",
        ),
        EmojiItem(\"MALE SIGN\", \"symbols\", \"gender\", \"♂\"),
        EmojiItem(\"FEMALE SIGN\", \"symbols\", \"gender\", \"♀\"),
        EmojiItem(\"WHITE LARGE SQUARE\", \"symbols\", \"geometric\", \"⬜\"),
        EmojiItem(\"BLACK LARGE SQUARE\", \"symbols\", \"geometric\", \"⬛\"),
        EmojiItem(\"MEDIUM BLACK CIRCLE\", \"symbols\", \"geometric\", \"⚫\"),
        EmojiItem(\"MEDIUM WHITE CIRCLE\", \"symbols\", \"geometric\", \"⚪\"),
        EmojiItem(\"BLACK MEDIUM SMALL SQUARE\", \"symbols\", \"geometric\", \"◾\"),
        EmojiItem(\"WHITE MEDIUM SMALL SQUARE\", \"symbols\", \"geometric\", \"◽\"),
        EmojiItem(\"BLACK MEDIUM SQUARE\", \"symbols\", \"geometric\", \"◼\"),
        EmojiItem(\"WHITE MEDIUM SQUARE\", \"symbols\", \"geometric\", \"◻\"),
        EmojiItem(\"WHITE SMALL SQUARE\", \"symbols\", \"geometric\", \"▫\"),
        EmojiItem(\"BLACK SMALL SQUARE\", \"symbols\", \"geometric\", \"▪\"),
        EmojiItem(\"LARGE BROWN SQUARE\", \"symbols\", \"geometric\", \"🟫\"),
        EmojiItem(\"LARGE PURPLE SQUARE\", \"symbols\", \"geometric\", \"🟪\"),
        EmojiItem(\"LARGE GREEN SQUARE\", \"symbols\", \"geometric\", \"🟩\"),
        EmojiItem(\"LARGE YELLOW SQUARE\", \"symbols\", \"geometric\", \"🟨\"),
        EmojiItem(\"LARGE ORANGE SQUARE\", \"symbols\", \"geometric\", \"🟧\"),
        EmojiItem(\"LARGE BLUE SQUARE\", \"symbols\", \"geometric\", \"🟦\"),
        EmojiItem(\"LARGE RED SQUARE\", \"symbols\", \"geometric\", \"🟥\"),
        EmojiItem(\"LARGE BROWN CIRCLE\", \"symbols\", \"geometric\", \"🟤\"),
        EmojiItem(\"LARGE PURPLE CIRCLE\", \"symbols\", \"geometric\", \"🟣\"),
        EmojiItem(\"LARGE GREEN CIRCLE\", \"symbols\", \"geometric\", \"🟢\"),
        EmojiItem(\"LARGE YELLOW CIRCLE\", \"symbols\", \"geometric\", \"🟡\"),
        EmojiItem(\"LARGE ORANGE CIRCLE\", \"symbols\", \"geometric\", \"🟠\"),
        EmojiItem(\"DOWN-POINTING RED TRIANGLE\", \"symbols\", \"geometric\", \"🔻\"),
        EmojiItem(\"UP-POINTING RED TRIANGLE\", \"symbols\", \"geometric\", \"🔺\"),
        EmojiItem(\"SMALL BLUE DIAMOND\", \"symbols\", \"geometric\", \"🔹\"),
        EmojiItem(\"SMALL ORANGE DIAMOND\", \"symbols\", \"geometric\", \"🔸\"),
        EmojiItem(\"LARGE BLUE DIAMOND\", \"symbols\", \"geometric\", \"🔷\"),
        EmojiItem(\"LARGE ORANGE DIAMOND\", \"symbols\", \"geometric\", \"🔶\"),
        EmojiItem(\"LARGE BLUE CIRCLE\", \"symbols\", \"geometric\", \"🔵\"),
        EmojiItem(\"LARGE RED CIRCLE\", \"symbols\", \"geometric\", \"🔴\"),
        EmojiItem(\"WHITE SQUARE BUTTON\", \"symbols\", \"geometric\", \"🔳\"),
        EmojiItem(\"BLACK SQUARE BUTTON\", \"symbols\", \"geometric\", \"🔲\"),
        EmojiItem(\"RADIO BUTTON\", \"symbols\", \"geometric\", \"🔘\"),
        EmojiItem(
            \"DIAMOND SHAPE WITH A DOT INSIDE\", \"symbols\", \"geometric\", \"💠\"
        ),
        EmojiItem(\"KEYCAP TEN\", \"symbols\", \"keycap\", \"🔟\"),
        EmojiItem(\"PERMANENT PAPER SIGN\", \"symbols\", \"math\", \"♾\"),
        EmojiItem(\"HEAVY DIVISION SIGN\", \"symbols\", \"math\", \"➗\"),
        EmojiItem(\"HEAVY MINUS SIGN\", \"symbols\", \"math\", \"➖\"),
        EmojiItem(\"HEAVY PLUS SIGN\", \"symbols\", \"math\", \"➕\"),
        EmojiItem(\"HEAVY MULTIPLICATION X\", \"symbols\", \"math\", \"✖\"),
        EmojiItem(\"PART ALTERNATION MARK\", \"symbols\", \"other-symbol\", \"〽\"),
        EmojiItem(\"HEAVY LARGE CIRCLE\", \"symbols\", \"other-symbol\", \"⭕\"),
        EmojiItem(\"DOUBLE CURLY LOOP\", \"symbols\", \"other-symbol\", \"➿\"),
        EmojiItem(\"CURLY LOOP\", \"symbols\", \"other-symbol\", \"➰\"),
        EmojiItem(
            \"NEGATIVE SQUARED CROSS MARK\", \"symbols\", \"other-symbol\", \"❎\"
        ),
        EmojiItem(\"CROSS MARK\", \"symbols\", \"other-symbol\", \"❌\"),
        EmojiItem(\"FLEUR-DE-LIS\", \"symbols\", \"other-symbol\", \"⚜\"),
        EmojiItem(
            \"BLACK UNIVERSAL RECYCLING SYMBOL\", \"symbols\", \"other-symbol\", \"♻\"
        ),
        EmojiItem(\"REGISTERED SIGN\", \"symbols\", \"other-symbol\", \"®\"),
        EmojiItem(\"COPYRIGHT SIGN\", \"symbols\", \"other-symbol\", \"©\"),
        EmojiItem(\"SPARKLE\", \"symbols\", \"other-symbol\", \"❇\"),
        EmojiItem(\"EIGHT POINTED BLACK STAR\", \"symbols\", \"other-symbol\", \"✴\"),
        EmojiItem(\"EIGHT SPOKED ASTERISK\", \"symbols\", \"other-symbol\", \"✳\"),
        EmojiItem(\"HEAVY CHECK MARK\", \"symbols\", \"other-symbol\", \"✔\"),
        EmojiItem(\"WHITE HEAVY CHECK MARK\", \"symbols\", \"other-symbol\", \"✅\"),
        EmojiItem(\"STAFF OF AESCULAPIUS\", \"symbols\", \"other-symbol\", \"⚕\"),
        EmojiItem(\"BALLOT BOX WITH CHECK\", \"symbols\", \"other-symbol\", \"☑\"),
        EmojiItem(\"TRADE MARK SIGN\", \"symbols\", \"other-symbol\", \"™\"),
        EmojiItem(\"TRIDENT EMBLEM\", \"symbols\", \"other-symbol\", \"🔱\"),
        EmojiItem(
            \"JAPANESE SYMBOL FOR BEGINNER\", \"symbols\", \"other-symbol\", \"🔰\"
        ),
        EmojiItem(\"NAME BADGE\", \"symbols\", \"other-symbol\", \"📛\"),
        EmojiItem(\"DOUBLE EXCLAMATION MARK\", \"symbols\", \"punctuation\", \"‼\"),
        EmojiItem(\"WAVY DASH\", \"symbols\", \"punctuation\", \"〰\"),
        EmojiItem(
            \"HEAVY EXCLAMATION MARK SYMBOL\", \"symbols\", \"punctuation\", \"❗\"
        ),
        EmojiItem(
            \"WHITE EXCLAMATION MARK ORNAMENT\", \"symbols\", \"punctuation\", \"❕\"
        ),
        EmojiItem(
            \"WHITE QUESTION MARK ORNAMENT\", \"symbols\", \"punctuation\", \"❔\"
        ),
        EmojiItem(
            \"BLACK QUESTION MARK ORNAMENT\", \"symbols\", \"punctuation\", \"❓\"
        ),
        EmojiItem(\"EXCLAMATION QUESTION MARK\", \"symbols\", \"punctuation\", \"⁉\"),
        EmojiItem(\"LATIN CROSS\", \"symbols\", \"religion\", \"✝\"),
        EmojiItem(\"ATOM SYMBOL\", \"symbols\", \"religion\", \"⚛\"),
        EmojiItem(\"YIN YANG\", \"symbols\", \"religion\", \"☯\"),
        EmojiItem(\"PEACE SYMBOL\", \"symbols\", \"religion\", \"☮\"),
        EmojiItem(\"STAR AND CRESCENT\", \"symbols\", \"religion\", \"☪\"),
        EmojiItem(\"STAR OF DAVID\", \"symbols\", \"religion\", \"✡\"),
        EmojiItem(\"WHEEL OF DHARMA\", \"symbols\", \"religion\", \"☸\"),
        EmojiItem(\"ORTHODOX CROSS\", \"symbols\", \"religion\", \"☦\"),
        EmojiItem(\"PLACE OF WORSHIP\", \"symbols\", \"religion\", \"🛐\"),
        EmojiItem(\"MENORAH WITH NINE BRANCHES\", \"symbols\", \"religion\", \"🕎\"),
        EmojiItem(\"OM SYMBOL\", \"symbols\", \"religion\", \"🕉\"),
        EmojiItem(
            \"SIX POINTED STAR WITH MIDDLE DOT\", \"symbols\", \"religion\", \"🔯\"
        ),
        EmojiItem(\"WHEELCHAIR SYMBOL\", \"symbols\", \"transport-sign\", \"♿\"),
        EmojiItem(\"LEFT LUGGAGE\", \"symbols\", \"transport-sign\", \"🛅\"),
        EmojiItem(\"BAGGAGE CLAIM\", \"symbols\", \"transport-sign\", \"🛄\"),
        EmojiItem(\"CUSTOMS\", \"symbols\", \"transport-sign\", \"🛃\"),
        EmojiItem(\"PASSPORT CONTROL\", \"symbols\", \"transport-sign\", \"🛂\"),
        EmojiItem(\"WATER CLOSET\", \"symbols\", \"transport-sign\", \"🚾\"),
        EmojiItem(\"BABY SYMBOL\", \"symbols\", \"transport-sign\", \"🚼\"),
        EmojiItem(\"RESTROOM\", \"symbols\", \"transport-sign\", \"🚻\"),
        EmojiItem(\"WOMENS SYMBOL\", \"symbols\", \"transport-sign\", \"🚺\"),
        EmojiItem(\"MENS SYMBOL\", \"symbols\", \"transport-sign\", \"🚹\"),
        EmojiItem(\"POTABLE WATER SYMBOL\", \"symbols\", \"transport-sign\", \"🚰\"),
        EmojiItem(
            \"PUT LITTER IN ITS PLACE SYMBOL\", \"symbols\", \"transport-sign\", \"🚮\"
        ),
        EmojiItem(
            \"AUTOMATED TELLER MACHINE\", \"symbols\", \"transport-sign\", \"🏧\"
        ),
        EmojiItem(\"NO ENTRY\", \"symbols\", \"warning\", \"⛔\"),
        EmojiItem(\"WARNING SIGN\", \"symbols\", \"warning\", \"⚠\"),
        EmojiItem(\"BIOHAZARD SIGN\", \"symbols\", \"warning\", \"☣\"),
        EmojiItem(\"RADIOACTIVE SIGN\", \"symbols\", \"warning\", \"☢\"),
        EmojiItem(\"CHILDREN CROSSING\", \"symbols\", \"warning\", \"🚸\"),
        EmojiItem(\"NO PEDESTRIANS\", \"symbols\", \"warning\", \"🚷\"),
        EmojiItem(\"NO BICYCLES\", \"symbols\", \"warning\", \"🚳\"),
        EmojiItem(\"NON-POTABLE WATER SYMBOL\", \"symbols\", \"warning\", \"🚱\"),
        EmojiItem(\"DO NOT LITTER SYMBOL\", \"symbols\", \"warning\", \"🚯\"),
        EmojiItem(\"NO SMOKING SYMBOL\", \"symbols\", \"warning\", \"🚭\"),
        EmojiItem(\"NO ENTRY SIGN\", \"symbols\", \"warning\", \"🚫\"),
        EmojiItem(\"NO ONE UNDER EIGHTEEN SYMBOL\", \"symbols\", \"warning\", \"🔞\"),
        EmojiItem(\"NO MOBILE PHONES\", \"symbols\", \"warning\", \"📵\"),
        EmojiItem(\"OPHIUCHUS\", \"symbols\", \"zodiac\", \"⛎\"),
        EmojiItem(\"SCORPIUS\", \"symbols\", \"zodiac\", \"♏\"),
        EmojiItem(\"LIBRA\", \"symbols\", \"zodiac\", \"♎\"),
        EmojiItem(\"VIRGO\", \"symbols\", \"zodiac\", \"♍\"),
        EmojiItem(\"LEO\", \"symbols\", \"zodiac\", \"♌\"),
        EmojiItem(\"CANCER\", \"symbols\", \"zodiac\", \"♋\"),
        EmojiItem(\"GEMINI\", \"symbols\", \"zodiac\", \"♊\"),
        EmojiItem(\"PISCES\", \"symbols\", \"zodiac\", \"♓\"),
        EmojiItem(\"AQUARIUS\", \"symbols\", \"zodiac\", \"♒\"),
        EmojiItem(\"CAPRICORN\", \"symbols\", \"zodiac\", \"♑\"),
        EmojiItem(\"SAGITTARIUS\", \"symbols\", \"zodiac\", \"♐\"),
        EmojiItem(\"TAURUS\", \"symbols\", \"zodiac\", \"♉\"),
        EmojiItem(\"ARIES\", \"symbols\", \"zodiac\", \"♈\"),
        EmojiItem(\"LUGGAGE\", \"travel-places\", \"hotel\", \"🧳\"),
        EmojiItem(\"BELLHOP BELL\", \"travel-places\", \"hotel\", \"🛎\"),
        EmojiItem(\"WOOD\", \"travel-places\", \"place-building\", \"🪵\"),
        EmojiItem(\"ROCK\", \"travel-places\", \"place-building\", \"🪨\"),
        EmojiItem(\"BRICK\", \"travel-places\", \"place-building\", \"🧱\"),
        EmojiItem(\"HUT\", \"travel-places\", \"place-building\", \"🛖\"),
        EmojiItem(\"STATUE OF LIBERTY\", \"travel-places\", \"place-building\", \"🗽\"),
        EmojiItem(\"TOKYO TOWER\", \"travel-places\", \"place-building\", \"🗼\"),
        EmojiItem(\"WEDDING\", \"travel-places\", \"place-building\", \"💒\"),
        EmojiItem(\"EUROPEAN CASTLE\", \"travel-places\", \"place-building\", \"🏰\"),
        EmojiItem(\"JAPANESE CASTLE\", \"travel-places\", \"place-building\", \"🏯\"),
        EmojiItem(\"FACTORY\", \"travel-places\", \"place-building\", \"🏭\"),
        EmojiItem(\"DEPARTMENT STORE\", \"travel-places\", \"place-building\", \"🏬\"),
        EmojiItem(\"SCHOOL\", \"travel-places\", \"place-building\", \"🏫\"),
        EmojiItem(\"CONVENIENCE STORE\", \"travel-places\", \"place-building\", \"🏪\"),
        EmojiItem(\"LOVE HOTEL\", \"travel-places\", \"place-building\", \"🏩\"),
        EmojiItem(\"HOTEL\", \"travel-places\", \"place-building\", \"🏨\"),
        EmojiItem(\"BANK\", \"travel-places\", \"place-building\", \"🏦\"),
        EmojiItem(\"HOSPITAL\", \"travel-places\", \"place-building\", \"🏥\"),
        EmojiItem(
            \"EUROPEAN POST OFFICE\", \"travel-places\", \"place-building\", \"🏤\"
        ),
        EmojiItem(
            \"JAPANESE POST OFFICE\", \"travel-places\", \"place-building\", \"🏣\"
        ),
        EmojiItem(\"OFFICE BUILDING\", \"travel-places\", \"place-building\", \"🏢\"),
        EmojiItem(\"HOUSE WITH GARDEN\", \"travel-places\", \"place-building\", \"🏡\"),
        EmojiItem(\"HOUSE BUILDING\", \"travel-places\", \"place-building\", \"🏠\"),
        EmojiItem(\"STADIUM\", \"travel-places\", \"place-building\", \"🏟\"),
        EmojiItem(
            \"CLASSICAL BUILDING\", \"travel-places\", \"place-building\", \"🏛\"
        ),
        EmojiItem(
            \"DERELICT HOUSE BUILDING\", \"travel-places\", \"place-building\", \"🏚\"
        ),
        EmojiItem(\"HOUSE BUILDINGS\", \"travel-places\", \"place-building\", \"🏘\"),
        EmojiItem(
            \"BUILDING CONSTRUCTION\", \"travel-places\", \"place-building\", \"🏗\"
        ),
        EmojiItem(\"MOUNTAIN\", \"travel-places\", \"place-geographic\", \"⛰\"),
        EmojiItem(\"MOUNT FUJI\", \"travel-places\", \"place-geographic\", \"🗻\"),
        EmojiItem(\"NATIONAL PARK\", \"travel-places\", \"place-geographic\", \"🏞\"),
        EmojiItem(\"DESERT ISLAND\", \"travel-places\", \"place-geographic\", \"🏝\"),
        EmojiItem(\"DESERT\", \"travel-places\", \"place-geographic\", \"🏜\"),
        EmojiItem(
            \"BEACH WITH UMBRELLA\", \"travel-places\", \"place-geographic\", \"🏖\"
        ),
        EmojiItem(\"CAMPING\", \"travel-places\", \"place-geographic\", \"🏕\"),
        EmojiItem(
            \"SNOW CAPPED MOUNTAIN\", \"travel-places\", \"place-geographic\", \"🏔\"
        ),
        EmojiItem(\"VOLCANO\", \"travel-places\", \"place-geographic\", \"🌋\"),
        EmojiItem(\"COMPASS\", \"travel-places\", \"place-map\", \"🧭\"),
        EmojiItem(\"SILHOUETTE OF JAPAN\", \"travel-places\", \"place-map\", \"🗾\"),
        EmojiItem(\"WORLD MAP\", \"travel-places\", \"place-map\", \"🗺\"),
        EmojiItem(\"GLOBE WITH MERIDIANS\", \"travel-places\", \"place-map\", \"🌐\"),
        EmojiItem(
            \"EARTH GLOBE ASIA-AUSTRALIA\", \"travel-places\", \"place-map\", \"🌏\"
        ),
        EmojiItem(\"EARTH GLOBE AMERICAS\", \"travel-places\", \"place-map\", \"🌎\"),
        EmojiItem(
            \"EARTH GLOBE EUROPE-AFRICA\", \"travel-places\", \"place-map\", \"🌍\"
        ),
        EmojiItem(\"TENT\", \"travel-places\", \"place-other\", \"⛺\"),
        EmojiItem(\"FOUNTAIN\", \"travel-places\", \"place-other\", \"⛲\"),
        EmojiItem(\"HOT SPRINGS\", \"travel-places\", \"place-other\", \"♨\"),
        EmojiItem(\"BARBER POLE\", \"travel-places\", \"place-other\", \"💈\"),
        EmojiItem(\"CITYSCAPE\", \"travel-places\", \"place-other\", \"🏙\"),
        EmojiItem(\"CIRCUS TENT\", \"travel-places\", \"place-other\", \"🎪\"),
        EmojiItem(\"ROLLER COASTER\", \"travel-places\", \"place-other\", \"🎢\"),
        EmojiItem(\"FERRIS WHEEL\", \"travel-places\", \"place-other\", \"🎡\"),
        EmojiItem(\"CAROUSEL HORSE\", \"travel-places\", \"place-other\", \"🎠\"),
        EmojiItem(\"BRIDGE AT NIGHT\", \"travel-places\", \"place-other\", \"🌉\"),
        EmojiItem(
            \"SUNSET OVER BUILDINGS\", \"travel-places\", \"place-other\", \"🌇\"
        ),
        EmojiItem(\"CITYSCAPE AT DUSK\", \"travel-places\", \"place-other\", \"🌆\"),
        EmojiItem(\"SUNRISE\", \"travel-places\", \"place-other\", \"🌅\"),
        EmojiItem(
            \"SUNRISE OVER MOUNTAINS\", \"travel-places\", \"place-other\", \"🌄\"
        ),
        EmojiItem(\"NIGHT WITH STARS\", \"travel-places\", \"place-other\", \"🌃\"),
        EmojiItem(\"FOGGY\", \"travel-places\", \"place-other\", \"🌁\"),
        EmojiItem(\"CHURCH\", \"travel-places\", \"place-religious\", \"⛪\"),
        EmojiItem(\"HINDU TEMPLE\", \"travel-places\", \"place-religious\", \"🛕\"),
        EmojiItem(\"SYNAGOGUE\", \"travel-places\", \"place-religious\", \"🕍\"),
        EmojiItem(\"MOSQUE\", \"travel-places\", \"place-religious\", \"🕌\"),
        EmojiItem(\"KAABA\", \"travel-places\", \"place-religious\", \"🕋\"),
        EmojiItem(\"WHITE MEDIUM STAR\", \"travel-places\", \"sky & weather\", \"⭐\"),
        EmojiItem(\"UMBRELLA ON GROUND\", \"travel-places\", \"sky & weather\", \"⛱\"),
        EmojiItem(
            \"THUNDER CLOUD AND RAIN\", \"travel-places\", \"sky & weather\", \"⛈\"
        ),
        EmojiItem(\"SUN BEHIND CLOUD\", \"travel-places\", \"sky & weather\", \"⛅\"),
        EmojiItem(
            \"SNOWMAN WITHOUT SNOW\", \"travel-places\", \"sky & weather\", \"⛄\"
        ),
        EmojiItem(\"HIGH VOLTAGE SIGN\", \"travel-places\", \"sky & weather\", \"⚡\"),
        EmojiItem(\"SNOWFLAKE\", \"travel-places\", \"sky & weather\", \"❄\"),
        EmojiItem(
            \"UMBRELLA WITH RAIN DROPS\", \"travel-places\", \"sky & weather\", \"☔\"
        ),
        EmojiItem(\"COMET\", \"travel-places\", \"sky & weather\", \"☄\"),
        EmojiItem(\"SNOWMAN\", \"travel-places\", \"sky & weather\", \"☃\"),
        EmojiItem(\"UMBRELLA\", \"travel-places\", \"sky & weather\", \"☂\"),
        EmojiItem(\"CLOUD\", \"travel-places\", \"sky & weather\", \"☁\"),
        EmojiItem(
            \"BLACK SUN WITH RAYS\", \"travel-places\", \"sky & weather\", \"☀\"
        ),
        EmojiItem(\"RINGED PLANET\", \"travel-places\", \"sky & weather\", \"🪐\"),
        EmojiItem(\"FIRE\", \"travel-places\", \"sky & weather\", \"🔥\"),
        EmojiItem(\"DROPLET\", \"travel-places\", \"sky & weather\", \"💧\"),
        EmojiItem(\"WIND BLOWING FACE\", \"travel-places\", \"sky & weather\", \"🌬\"),
        EmojiItem(\"FOG\", \"travel-places\", \"sky & weather\", \"🌫\"),
        EmojiItem(\"CLOUD WITH TORNADO\", \"travel-places\", \"sky & weather\", \"🌪\"),
        EmojiItem(
            \"CLOUD WITH LIGHTNING\", \"travel-places\", \"sky & weather\", \"🌩\"
        ),
        EmojiItem(\"CLOUD WITH SNOW\", \"travel-places\", \"sky & weather\", \"🌨\"),
        EmojiItem(\"CLOUD WITH RAIN\", \"travel-places\", \"sky & weather\", \"🌧\"),
        EmojiItem(
            \"WHITE SUN BEHIND CLOUD WITH RAIN\",
            \"travel-places\",
            \"sky & weather\",
            \"🌦\",
        ),
        EmojiItem(
            \"WHITE SUN BEHIND CLOUD\", \"travel-places\", \"sky & weather\", \"🌥\"
        ),
        EmojiItem(
            \"WHITE SUN WITH SMALL CLOUD\", \"travel-places\", \"sky & weather\", \"🌤\"
        ),
        EmojiItem(\"THERMOMETER\", \"travel-places\", \"sky & weather\", \"🌡\"),
        EmojiItem(\"SHOOTING STAR\", \"travel-places\", \"sky & weather\", \"🌠\"),
        EmojiItem(\"GLOWING STAR\", \"travel-places\", \"sky & weather\", \"🌟\"),
        EmojiItem(\"SUN WITH FACE\", \"travel-places\", \"sky & weather\", \"🌞\"),
        EmojiItem(
            \"FULL MOON WITH FACE\", \"travel-places\", \"sky & weather\", \"🌝\"
        ),
        EmojiItem(
            \"LAST QUARTER MOON WITH FACE\",
            \"travel-places\",
            \"sky & weather\",
            \"🌜\",
        ),
        EmojiItem(
            \"FIRST QUARTER MOON WITH FACE\",
            \"travel-places\",
            \"sky & weather\",
            \"🌛\",
        ),
        EmojiItem(\"NEW MOON WITH FACE\", \"travel-places\", \"sky & weather\", \"🌚\"),
        EmojiItem(\"CRESCENT MOON\", \"travel-places\", \"sky & weather\", \"🌙\"),
        EmojiItem(
            \"WANING CRESCENT MOON SYMBOL\",
            \"travel-places\",
            \"sky & weather\",
            \"🌘\",
        ),
        EmojiItem(
            \"LAST QUARTER MOON SYMBOL\", \"travel-places\", \"sky & weather\", \"🌗\"
        ),
        EmojiItem(
            \"WANING GIBBOUS MOON SYMBOL\", \"travel-places\", \"sky & weather\", \"🌖\"
        ),
        EmojiItem(\"FULL MOON SYMBOL\", \"travel-places\", \"sky & weather\", \"🌕\"),
        EmojiItem(
            \"WAXING GIBBOUS MOON SYMBOL\", \"travel-places\", \"sky & weather\", \"🌔\"
        ),
        EmojiItem(
            \"FIRST QUARTER MOON SYMBOL\", \"travel-places\", \"sky & weather\", \"🌓\"
        ),
        EmojiItem(
            \"WAXING CRESCENT MOON SYMBOL\",
            \"travel-places\",
            \"sky & weather\",
            \"🌒\",
        ),
        EmojiItem(\"NEW MOON SYMBOL\", \"travel-places\", \"sky & weather\", \"🌑\"),
        EmojiItem(\"MILKY WAY\", \"travel-places\", \"sky & weather\", \"🌌\"),
        EmojiItem(\"WATER WAVE\", \"travel-places\", \"sky & weather\", \"🌊\"),
        EmojiItem(\"RAINBOW\", \"travel-places\", \"sky & weather\", \"🌈\"),
        EmojiItem(\"CLOSED UMBRELLA\", \"travel-places\", \"sky & weather\", \"🌂\"),
        EmojiItem(\"CYCLONE\", \"travel-places\", \"sky & weather\", \"🌀\"),
        EmojiItem(\"HOURGLASS WITH FLOWING SAND\", \"travel-places\", \"time\", \"⏳\"),
        EmojiItem(\"TIMER CLOCK\", \"travel-places\", \"time\", \"⏲\"),
        EmojiItem(\"STOPWATCH\", \"travel-places\", \"time\", \"⏱\"),
        EmojiItem(\"ALARM CLOCK\", \"travel-places\", \"time\", \"⏰\"),
        EmojiItem(\"HOURGLASS\", \"travel-places\", \"time\", \"⌛\"),
        EmojiItem(\"WATCH\", \"travel-places\", \"time\", \"⌚\"),
        EmojiItem(\"MANTELPIECE CLOCK\", \"travel-places\", \"time\", \"🕰\"),
        EmojiItem(\"CLOCK FACE TWELVE-THIRTY\", \"travel-places\", \"time\", \"🕧\"),
        EmojiItem(\"CLOCK FACE ELEVEN-THIRTY\", \"travel-places\", \"time\", \"🕦\"),
        EmojiItem(\"CLOCK FACE TEN-THIRTY\", \"travel-places\", \"time\", \"🕥\"),
        EmojiItem(\"CLOCK FACE NINE-THIRTY\", \"travel-places\", \"time\", \"🕤\"),
        EmojiItem(\"CLOCK FACE EIGHT-THIRTY\", \"travel-places\", \"time\", \"🕣\"),
        EmojiItem(\"CLOCK FACE SEVEN-THIRTY\", \"travel-places\", \"time\", \"🕢\"),
        EmojiItem(\"CLOCK FACE SIX-THIRTY\", \"travel-places\", \"time\", \"🕡\"),
        EmojiItem(\"CLOCK FACE FIVE-THIRTY\", \"travel-places\", \"time\", \"🕠\"),
        EmojiItem(\"CLOCK FACE FOUR-THIRTY\", \"travel-places\", \"time\", \"🕟\"),
        EmojiItem(\"CLOCK FACE THREE-THIRTY\", \"travel-places\", \"time\", \"🕞\"),
        EmojiItem(\"CLOCK FACE TWO-THIRTY\", \"travel-places\", \"time\", \"🕝\"),
        EmojiItem(\"CLOCK FACE ONE-THIRTY\", \"travel-places\", \"time\", \"🕜\"),
        EmojiItem(\"CLOCK FACE TWELVE OCLOCK\", \"travel-places\", \"time\", \"🕛\"),
        EmojiItem(\"CLOCK FACE ELEVEN OCLOCK\", \"travel-places\", \"time\", \"🕚\"),
        EmojiItem(\"CLOCK FACE TEN OCLOCK\", \"travel-places\", \"time\", \"🕙\"),
        EmojiItem(\"CLOCK FACE NINE OCLOCK\", \"travel-places\", \"time\", \"🕘\"),
        EmojiItem(\"CLOCK FACE EIGHT OCLOCK\", \"travel-places\", \"time\", \"🕗\"),
        EmojiItem(\"CLOCK FACE SEVEN OCLOCK\", \"travel-places\", \"time\", \"🕖\"),
        EmojiItem(\"CLOCK FACE SIX OCLOCK\", \"travel-places\", \"time\", \"🕕\"),
        EmojiItem(\"CLOCK FACE FIVE OCLOCK\", \"travel-places\", \"time\", \"🕔\"),
        EmojiItem(\"CLOCK FACE FOUR OCLOCK\", \"travel-places\", \"time\", \"🕓\"),
        EmojiItem(\"CLOCK FACE THREE OCLOCK\", \"travel-places\", \"time\", \"🕒\"),
        EmojiItem(\"CLOCK FACE TWO OCLOCK\", \"travel-places\", \"time\", \"🕑\"),
        EmojiItem(\"CLOCK FACE ONE OCLOCK\", \"travel-places\", \"time\", \"🕐\"),
        EmojiItem(\"AIRPLANE\", \"travel-places\", \"transport-air\", \"✈\"),
        EmojiItem(\"PARACHUTE\", \"travel-places\", \"transport-air\", \"🪂\"),
        EmojiItem(\"FLYING SAUCER\", \"travel-places\", \"transport-air\", \"🛸\"),
        EmojiItem(\"SATELLITE\", \"travel-places\", \"transport-air\", \"🛰\"),
        EmojiItem(\"AIRPLANE ARRIVING\", \"travel-places\", \"transport-air\", \"🛬\"),
        EmojiItem(\"AIRPLANE DEPARTURE\", \"travel-places\", \"transport-air\", \"🛫\"),
        EmojiItem(\"SMALL AIRPLANE\", \"travel-places\", \"transport-air\", \"🛩\"),
        EmojiItem(\"AERIAL TRAMWAY\", \"travel-places\", \"transport-air\", \"🚡\"),
        EmojiItem(\"MOUNTAIN CABLEWAY\", \"travel-places\", \"transport-air\", \"🚠\"),
        EmojiItem(\"SUSPENSION RAILWAY\", \"travel-places\", \"transport-air\", \"🚟\"),
        EmojiItem(\"HELICOPTER\", \"travel-places\", \"transport-air\", \"🚁\"),
        EmojiItem(\"ROCKET\", \"travel-places\", \"transport-air\", \"🚀\"),
        EmojiItem(\"SEAT\", \"travel-places\", \"transport-air\", \"💺\"),
        EmojiItem(\"FUEL PUMP\", \"travel-places\", \"transport-ground\", \"⛽\"),
        EmojiItem(
            \"MANUAL WHEELCHAIR\", \"travel-places\", \"transport-ground\", \"🦽\"
        ),
        EmojiItem(
            \"MOTORIZED WHEELCHAIR\", \"travel-places\", \"transport-ground\", \"🦼\"
        ),
        EmojiItem(\"ROLLER SKATE\", \"travel-places\", \"transport-ground\", \"🛼\"),
        EmojiItem(\"PICKUP TRUCK\", \"travel-places\", \"transport-ground\", \"🛻\"),
        EmojiItem(\"AUTO RICKSHAW\", \"travel-places\", \"transport-ground\", \"🛺\"),
        EmojiItem(\"SKATEBOARD\", \"travel-places\", \"transport-ground\", \"🛹\"),
        EmojiItem(\"MOTOR SCOOTER\", \"travel-places\", \"transport-ground\", \"🛵\"),
        EmojiItem(\"SCOOTER\", \"travel-places\", \"transport-ground\", \"🛴\"),
        EmojiItem(\"RAILWAY TRACK\", \"travel-places\", \"transport-ground\", \"🛤\"),
        EmojiItem(\"MOTORWAY\", \"travel-places\", \"transport-ground\", \"🛣\"),
        EmojiItem(\"OIL DRUM\", \"travel-places\", \"transport-ground\", \"🛢\"),
        EmojiItem(\"OCTAGONAL SIGN\", \"travel-places\", \"transport-ground\", \"🛑\"),
        EmojiItem(\"BICYCLE\", \"travel-places\", \"transport-ground\", \"🚲\"),
        EmojiItem(
            \"POLICE CARS REVOLVING LIGHT\",
            \"travel-places\",
            \"transport-ground\",
            \"🚨\",
        ),
        EmojiItem(
            \"CONSTRUCTION SIGN\", \"travel-places\", \"transport-ground\", \"🚧\"
        ),
        EmojiItem(
            \"VERTICAL TRAFFIC LIGHT\", \"travel-places\", \"transport-ground\", \"🚦\"
        ),
        EmojiItem(
            \"HORIZONTAL TRAFFIC LIGHT\",
            \"travel-places\",
            \"transport-ground\",
            \"🚥\",
        ),
        EmojiItem(
            \"MOUNTAIN RAILWAY\", \"travel-places\", \"transport-ground\", \"🚞\"
        ),
        EmojiItem(\"MONORAIL\", \"travel-places\", \"transport-ground\", \"🚝\"),
        EmojiItem(\"TRACTOR\", \"travel-places\", \"transport-ground\", \"🚜\"),
        EmojiItem(
            \"ARTICULATED LORRY\", \"travel-places\", \"transport-ground\", \"🚛\"
        ),
        EmojiItem(\"DELIVERY TRUCK\", \"travel-places\", \"transport-ground\", \"🚚\"),
        EmojiItem(
            \"RECREATIONAL VEHICLE\", \"travel-places\", \"transport-ground\", \"🚙\"
        ),
        EmojiItem(
            \"ONCOMING AUTOMOBILE\", \"travel-places\", \"transport-ground\", \"🚘\"
        ),
        EmojiItem(\"AUTOMOBILE\", \"travel-places\", \"transport-ground\", \"🚗\"),
        EmojiItem(\"ONCOMING TAXI\", \"travel-places\", \"transport-ground\", \"🚖\"),
        EmojiItem(\"TAXI\", \"travel-places\", \"transport-ground\", \"🚕\"),
        EmojiItem(
            \"ONCOMING POLICE CAR\", \"travel-places\", \"transport-ground\", \"🚔\"
        ),
        EmojiItem(\"POLICE CAR\", \"travel-places\", \"transport-ground\", \"🚓\"),
        EmojiItem(\"FIRE ENGINE\", \"travel-places\", \"transport-ground\", \"🚒\"),
        EmojiItem(\"AMBULANCE\", \"travel-places\", \"transport-ground\", \"🚑\"),
        EmojiItem(\"MINIBUS\", \"travel-places\", \"transport-ground\", \"🚐\"),
        EmojiItem(\"BUS STOP\", \"travel-places\", \"transport-ground\", \"🚏\"),
        EmojiItem(\"TROLLEYBUS\", \"travel-places\", \"transport-ground\", \"🚎\"),
        EmojiItem(\"ONCOMING BUS\", \"travel-places\", \"transport-ground\", \"🚍\"),
        EmojiItem(\"BUS\", \"travel-places\", \"transport-ground\", \"🚌\"),
        EmojiItem(\"TRAM CAR\", \"travel-places\", \"transport-ground\", \"🚋\"),
        EmojiItem(\"TRAM\", \"travel-places\", \"transport-ground\", \"🚊\"),
        EmojiItem(\"STATION\", \"travel-places\", \"transport-ground\", \"🚉\"),
        EmojiItem(\"LIGHT RAIL\", \"travel-places\", \"transport-ground\", \"🚈\"),
        EmojiItem(\"METRO\", \"travel-places\", \"transport-ground\", \"🚇\"),
        EmojiItem(\"TRAIN\", \"travel-places\", \"transport-ground\", \"🚆\"),
        EmojiItem(
            \"HIGH-SPEED TRAIN WITH BULLET NOSE\",
            \"travel-places\",
            \"transport-ground\",
            \"🚅\",
        ),
        EmojiItem(
            \"HIGH-SPEED TRAIN\", \"travel-places\", \"transport-ground\", \"🚄\"
        ),
        EmojiItem(\"RAILWAY CAR\", \"travel-places\", \"transport-ground\", \"🚃\"),
        EmojiItem(
            \"STEAM LOCOMOTIVE\", \"travel-places\", \"transport-ground\", \"🚂\"
        ),
        EmojiItem(\"RACING CAR\", \"travel-places\", \"transport-ground\", \"🏎\"),
        EmojiItem(
            \"RACING MOTORCYCLE\", \"travel-places\", \"transport-ground\", \"🏍\"
        ),
        EmojiItem(\"SAILBOAT\", \"travel-places\", \"transport-water\", \"⛵\"),
        EmojiItem(\"FERRY\", \"travel-places\", \"transport-water\", \"⛴\"),
        EmojiItem(\"ANCHOR\", \"travel-places\", \"transport-water\", \"⚓\"),
        EmojiItem(\"CANOE\", \"travel-places\", \"transport-water\", \"🛶\"),
        EmojiItem(\"PASSENGER SHIP\", \"travel-places\", \"transport-water\", \"🛳\"),
        EmojiItem(\"MOTOR BOAT\", \"travel-places\", \"transport-water\", \"🛥\"),
        EmojiItem(\"SPEEDBOAT\", \"travel-places\", \"transport-water\", \"🚤\"),
        EmojiItem(\"SHIP\", \"travel-places\", \"transport-water\", \"🚢\"),
        EmojiItem(\"WEARY CAT FACE\", \"smiley-emotion\", \"cat-face\", \"🙀\"),
        EmojiItem(\"CRYING CAT FACE\", \"smiley-emotion\", \"cat-face\", \"😿\"),
        EmojiItem(\"POUTING CAT FACE\", \"smiley-emotion\", \"cat-face\", \"😾\"),
        EmojiItem(
            \"KISSING CAT FACE WITH CLOSED EYES\",
            \"smiley-emotion\",
            \"cat-face\",
            \"😽\",
        ),
        EmojiItem(
            \"CAT FACE WITH WRY SMILE\", \"smiley-emotion\", \"cat-face\", \"😼\"
        ),
        EmojiItem(
            \"SMILING CAT FACE WITH HEART-SHAPED EYES\",
            \"smiley-emotion\",
            \"cat-face\",
            \"😻\",
        ),
        EmojiItem(
            \"SMILING CAT FACE WITH OPEN MOUTH\",
            \"smiley-emotion\",
            \"cat-face\",
            \"😺\",
        ),
        EmojiItem(
            \"CAT FACE WITH TEARS OF JOY\", \"smiley-emotion\", \"cat-face\", \"😹\"
        ),
        EmojiItem(
            \"GRINNING CAT FACE WITH SMILING EYES\",
            \"smiley-emotion\",
            \"cat-face\",
            \"😸\",
        ),
        EmojiItem(\"HEAVY BLACK HEART\", \"smiley-emotion\", \"emotion\", \"❤\"),
        EmojiItem(
            \"HEAVY HEART EXCLAMATION MARK ORNAMENT\",
            \"smiley-emotion\",
            \"emotion\",
            \"❣\",
        ),
        EmojiItem(\"ORANGE HEART\", \"smiley-emotion\", \"emotion\", \"🧡\"),
        EmojiItem(\"BROWN HEART\", \"smiley-emotion\", \"emotion\", \"🤎\"),
        EmojiItem(\"WHITE HEART\", \"smiley-emotion\", \"emotion\", \"🤍\"),
        EmojiItem(\"RIGHT ANGER BUBBLE\", \"smiley-emotion\", \"emotion\", \"🗯\"),
        EmojiItem(\"LEFT SPEECH BUBBLE\", \"smiley-emotion\", \"emotion\", \"🗨\"),
        EmojiItem(\"BLACK HEART\", \"smiley-emotion\", \"emotion\", \"🖤\"),
        EmojiItem(\"HOLE\", \"smiley-emotion\", \"emotion\", \"🕳\"),
        EmojiItem(\"HUNDRED POINTS SYMBOL\", \"smiley-emotion\", \"emotion\", \"💯\"),
        EmojiItem(\"THOUGHT BALLOON\", \"smiley-emotion\", \"emotion\", \"💭\"),
        EmojiItem(\"SPEECH BALLOON\", \"smiley-emotion\", \"emotion\", \"💬\"),
        EmojiItem(\"DIZZY SYMBOL\", \"smiley-emotion\", \"emotion\", \"💫\"),
        EmojiItem(\"DASH SYMBOL\", \"smiley-emotion\", \"emotion\", \"💨\"),
        EmojiItem(\"SPLASHING SWEAT SYMBOL\", \"smiley-emotion\", \"emotion\", \"💦\"),
        EmojiItem(\"COLLISION SYMBOL\", \"smiley-emotion\", \"emotion\", \"💥\"),
        EmojiItem(\"SLEEPING SYMBOL\", \"smiley-emotion\", \"emotion\", \"💤\"),
        EmojiItem(\"BOMB\", \"smiley-emotion\", \"emotion\", \"💣\"),
        EmojiItem(\"ANGER SYMBOL\", \"smiley-emotion\", \"emotion\", \"💢\"),
        EmojiItem(\"HEART DECORATION\", \"smiley-emotion\", \"emotion\", \"💟\"),
        EmojiItem(\"REVOLVING HEARTS\", \"smiley-emotion\", \"emotion\", \"💞\"),
        EmojiItem(\"HEART WITH RIBBON\", \"smiley-emotion\", \"emotion\", \"💝\"),
        EmojiItem(\"PURPLE HEART\", \"smiley-emotion\", \"emotion\", \"💜\"),
        EmojiItem(\"YELLOW HEART\", \"smiley-emotion\", \"emotion\", \"💛\"),
        EmojiItem(\"GREEN HEART\", \"smiley-emotion\", \"emotion\", \"💚\"),
        EmojiItem(\"BLUE HEART\", \"smiley-emotion\", \"emotion\", \"💙\"),
        EmojiItem(\"HEART WITH ARROW\", \"smiley-emotion\", \"emotion\", \"💘\"),
        EmojiItem(\"GROWING HEART\", \"smiley-emotion\", \"emotion\", \"💗\"),
        EmojiItem(\"SPARKLING HEART\", \"smiley-emotion\", \"emotion\", \"💖\"),
        EmojiItem(\"TWO HEARTS\", \"smiley-emotion\", \"emotion\", \"💕\"),
        EmojiItem(\"BROKEN HEART\", \"smiley-emotion\", \"emotion\", \"💔\"),
        EmojiItem(\"BEATING HEART\", \"smiley-emotion\", \"emotion\", \"💓\"),
        EmojiItem(\"LOVE LETTER\", \"smiley-emotion\", \"emotion\", \"💌\"),
        EmojiItem(\"KISS MARK\", \"smiley-emotion\", \"emotion\", \"💋\"),
        EmojiItem(
            \"WHITE SMILING FACE\", \"smiley-emotion\", \"face-affection\", \"☺\"
        ),
        EmojiItem(
            \"SMILING FACE WITH TEAR\", \"smiley-emotion\", \"face-affection\", \"🥲\"
        ),
        EmojiItem(
            \"SMILING FACE WITH SMILING EYES AND THREE HEARTS\",
            \"smiley-emotion\",
            \"face-affection\",
            \"🥰\",
        ),
        EmojiItem(
            \"GRINNING FACE WITH STAR EYES\",
            \"smiley-emotion\",
            \"face-affection\",
            \"🤩\",
        ),
        EmojiItem(
            \"KISSING FACE WITH CLOSED EYES\",
            \"smiley-emotion\",
            \"face-affection\",
            \"😚\",
        ),
        EmojiItem(
            \"KISSING FACE WITH SMILING EYES\",
            \"smiley-emotion\",
            \"face-affection\",
            \"😙\",
        ),
        EmojiItem(
            \"FACE THROWING A KISS\", \"smiley-emotion\", \"face-affection\", \"😘\"
        ),
        EmojiItem(\"KISSING FACE\", \"smiley-emotion\", \"face-affection\", \"😗\"),
        EmojiItem(
            \"SMILING FACE WITH HEART-SHAPED EYES\",
            \"smiley-emotion\",
            \"face-affection\",
            \"😍\",
        ),
        EmojiItem(
            \"WHITE FROWNING FACE\", \"smiley-emotion\", \"face-concerned\", \"☹\"
        ),
        EmojiItem(
            \"FACE WITH PLEADING EYES\", \"smiley-emotion\", \"face-concerned\", \"🥺\"
        ),
        EmojiItem(\"YAWNING FACE\", \"smiley-emotion\", \"face-concerned\", \"🥱\"),
        EmojiItem(
            \"SLIGHTLY FROWNING FACE\", \"smiley-emotion\", \"face-concerned\", \"🙁\"
        ),
        EmojiItem(\"FLUSHED FACE\", \"smiley-emotion\", \"face-concerned\", \"😳\"),
        EmojiItem(\"ASTONISHED FACE\", \"smiley-emotion\", \"face-concerned\", \"😲\"),
        EmojiItem(
            \"FACE SCREAMING IN FEAR\", \"smiley-emotion\", \"face-concerned\", \"😱\"
        ),
        EmojiItem(
            \"FACE WITH OPEN MOUTH AND COLD SWEAT\",
            \"smiley-emotion\",
            \"face-concerned\",
            \"😰\",
        ),
        EmojiItem(\"HUSHED FACE\", \"smiley-emotion\", \"face-concerned\", \"😯\"),
        EmojiItem(
            \"FACE WITH OPEN MOUTH\", \"smiley-emotion\", \"face-concerned\", \"😮\"
        ),
        EmojiItem(
            \"LOUDLY CRYING FACE\", \"smiley-emotion\", \"face-concerned\", \"😭\"
        ),
        EmojiItem(\"TIRED FACE\", \"smiley-emotion\", \"face-concerned\", \"😫\"),
        EmojiItem(\"WEARY FACE\", \"smiley-emotion\", \"face-concerned\", \"😩\"),
        EmojiItem(\"FEARFUL FACE\", \"smiley-emotion\", \"face-concerned\", \"😨\"),
        EmojiItem(\"ANGUISHED FACE\", \"smiley-emotion\", \"face-concerned\", \"😧\"),
        EmojiItem(
            \"FROWNING FACE WITH OPEN MOUTH\",
            \"smiley-emotion\",
            \"face-concerned\",
            \"😦\",
        ),
        EmojiItem(
            \"DISAPPOINTED BUT RELIEVED FACE\",
            \"smiley-emotion\",
            \"face-concerned\",
            \"😥\",
        ),
        EmojiItem(\"PERSEVERING FACE\", \"smiley-emotion\", \"face-concerned\", \"😣\"),
        EmojiItem(\"CRYING FACE\", \"smiley-emotion\", \"face-concerned\", \"😢\"),
        EmojiItem(\"WORRIED FACE\", \"smiley-emotion\", \"face-concerned\", \"😟\"),
        EmojiItem(
            \"DISAPPOINTED FACE\", \"smiley-emotion\", \"face-concerned\", \"😞\"
        ),
        EmojiItem(\"CONFOUNDED FACE\", \"smiley-emotion\", \"face-concerned\", \"😖\"),
        EmojiItem(\"CONFUSED FACE\", \"smiley-emotion\", \"face-concerned\", \"😕\"),
        EmojiItem(
            \"FACE WITH COLD SWEAT\", \"smiley-emotion\", \"face-concerned\", \"😓\"
        ),
        EmojiItem(\"CLOWN FACE\", \"smiley-emotion\", \"face-costume\", \"🤡\"),
        EmojiItem(\"ROBOT FACE\", \"smiley-emotion\", \"face-costume\", \"🤖\"),
        EmojiItem(\"PILE OF POO\", \"smiley-emotion\", \"face-costume\", \"💩\"),
        EmojiItem(\"ALIEN MONSTER\", \"smiley-emotion\", \"face-costume\", \"👾\"),
        EmojiItem(
            \"EXTRATERRESTRIAL ALIEN\", \"smiley-emotion\", \"face-costume\", \"👽\"
        ),
        EmojiItem(\"GHOST\", \"smiley-emotion\", \"face-costume\", \"👻\"),
        EmojiItem(\"JAPANESE GOBLIN\", \"smiley-emotion\", \"face-costume\", \"👺\"),
        EmojiItem(\"JAPANESE OGRE\", \"smiley-emotion\", \"face-costume\", \"👹\"),
        EmojiItem(\"FACE WITH MONOCLE\", \"smiley-emotion\", \"face-glasses\", \"🧐\"),
        EmojiItem(\"NERD FACE\", \"smiley-emotion\", \"face-glasses\", \"🤓\"),
        EmojiItem(
            \"SMILING FACE WITH SUNGLASSES\",
            \"smiley-emotion\",
            \"face-glasses\",
            \"😎\",
        ),
        EmojiItem(
            \"SMILING FACE WITH SMILING EYES AND HAND COVERING MOUTH\",
            \"smiley-emotion\",
            \"face-hand\",
            \"🤭\",
        ),
        EmojiItem(
            \"FACE WITH FINGER COVERING CLOSED LIPS\",
            \"smiley-emotion\",
            \"face-hand\",
            \"🤫\",
        ),
        EmojiItem(\"HUGGING FACE\", \"smiley-emotion\", \"face-hand\", \"🤗\"),
        EmojiItem(\"THINKING FACE\", \"smiley-emotion\", \"face-hand\", \"🤔\"),
        EmojiItem(\"DISGUISED FACE\", \"smiley-emotion\", \"face-hat\", \"🥸\"),
        EmojiItem(
            \"FACE WITH PARTY HORN AND PARTY HAT\",
            \"smiley-emotion\",
            \"face-hat\",
            \"🥳\",
        ),
        EmojiItem(\"FACE WITH COWBOY HAT\", \"smiley-emotion\", \"face-hat\", \"🤠\"),
        EmojiItem(
            \"SKULL AND CROSSBONES\", \"smiley-emotion\", \"face-negative\", \"☠\"
        ),
        EmojiItem(
            \"SERIOUS FACE WITH SYMBOLS COVERING MOUTH\",
            \"smiley-emotion\",
            \"face-negative\",
            \"🤬\",
        ),
        EmojiItem(
            \"FACE WITH LOOK OF TRIUMPH\", \"smiley-emotion\", \"face-negative\", \"😤\"
        ),
        EmojiItem(\"POUTING FACE\", \"smiley-emotion\", \"face-negative\", \"😡\"),
        EmojiItem(\"ANGRY FACE\", \"smiley-emotion\", \"face-negative\", \"😠\"),
        EmojiItem(
            \"SMILING FACE WITH HORNS\", \"smiley-emotion\", \"face-negative\", \"😈\"
        ),
        EmojiItem(\"SKULL\", \"smiley-emotion\", \"face-negative\", \"💀\"),
        EmojiItem(\"IMP\", \"smiley-emotion\", \"face-negative\", \"👿\"),
        EmojiItem(
            \"FACE WITH ONE EYEBROW RAISED\",
            \"smiley-emotion\",
            \"face-neutral-skeptical\",
            \"🤨\",
        ),
        EmojiItem(
            \"LYING FACE\", \"smiley-emotion\", \"face-neutral-skeptical\", \"🤥\"
        ),
        EmojiItem(
            \"ZIPPER-MOUTH FACE\",
            \"smiley-emotion\",
            \"face-neutral-skeptical\",
            \"🤐\",
        ),
        EmojiItem(
            \"FACE WITH ROLLING EYES\",
            \"smiley-emotion\",
            \"face-neutral-skeptical\",
            \"🙄\",
        ),
        EmojiItem(
            \"FACE WITHOUT MOUTH\",
            \"smiley-emotion\",
            \"face-neutral-skeptical\",
            \"😶\",
        ),
        EmojiItem(
            \"GRIMACING FACE\", \"smiley-emotion\", \"face-neutral-skeptical\", \"😬\"
        ),
        EmojiItem(
            \"UNAMUSED FACE\", \"smiley-emotion\", \"face-neutral-skeptical\", \"😒\"
        ),
        EmojiItem(
            \"EXPRESSIONLESS FACE\",
            \"smiley-emotion\",
            \"face-neutral-skeptical\",
            \"😑\",
        ),
        EmojiItem(
            \"NEUTRAL FACE\", \"smiley-emotion\", \"face-neutral-skeptical\", \"😐\"
        ),
        EmojiItem(
            \"SMIRKING FACE\", \"smiley-emotion\", \"face-neutral-skeptical\", \"😏\"
        ),
        EmojiItem(\"DROOLING FACE\", \"smiley-emotion\", \"face-sleepy\", \"🤤\"),
        EmojiItem(\"SLEEPING FACE\", \"smiley-emotion\", \"face-sleepy\", \"😴\"),
        EmojiItem(\"SLEEPY FACE\", \"smiley-emotion\", \"face-sleepy\", \"😪\"),
        EmojiItem(\"PENSIVE FACE\", \"smiley-emotion\", \"face-sleepy\", \"😔\"),
        EmojiItem(\"RELIEVED FACE\", \"smiley-emotion\", \"face-sleepy\", \"😌\"),
        EmojiItem(
            \"ROLLING ON THE FLOOR LAUGHING\",
            \"smiley-emotion\",
            \"face-smiling\",
            \"🤣\",
        ),
        EmojiItem(\"UPSIDE-DOWN FACE\", \"smiley-emotion\", \"face-smiling\", \"🙃\"),
        EmojiItem(
            \"SLIGHTLY SMILING FACE\", \"smiley-emotion\", \"face-smiling\", \"🙂\"
        ),
        EmojiItem(
            \"SMILING FACE WITH SMILING EYES\",
            \"smiley-emotion\",
            \"face-smiling\",
            \"😊\",
        ),
        EmojiItem(\"WINKING FACE\", \"smiley-emotion\", \"face-smiling\", \"😉\"),
        EmojiItem(
            \"SMILING FACE WITH HALO\", \"smiley-emotion\", \"face-smiling\", \"😇\"
        ),
        EmojiItem(
            \"SMILING FACE WITH OPEN MOUTH AND TIGHTLY-CLOSED EYES\",
            \"smiley-emotion\",
            \"face-smiling\",
            \"😆\",
        ),
        EmojiItem(
            \"SMILING FACE WITH OPEN MOUTH AND COLD SWEAT\",
            \"smiley-emotion\",
            \"face-smiling\",
            \"😅\",
        ),
        EmojiItem(
            \"SMILING FACE WITH OPEN MOUTH AND SMILING EYES\",
            \"smiley-emotion\",
            \"face-smiling\",
            \"😄\",
        ),
        EmojiItem(
            \"SMILING FACE WITH OPEN MOUTH\",
            \"smiley-emotion\",
            \"face-smiling\",
            \"😃\",
        ),
        EmojiItem(
            \"FACE WITH TEARS OF JOY\", \"smiley-emotion\", \"face-smiling\", \"😂\"
        ),
        EmojiItem(
            \"GRINNING FACE WITH SMILING EYES\",
            \"smiley-emotion\",
            \"face-smiling\",
            \"😁\",
        ),
        EmojiItem(\"GRINNING FACE\", \"smiley-emotion\", \"face-smiling\", \"😀\"),
        EmojiItem(
            \"GRINNING FACE WITH ONE LARGE AND ONE SMALL EYE\",
            \"smiley-emotion\",
            \"face-tongue\",
            \"🤪\",
        ),
        EmojiItem(\"MONEY-MOUTH FACE\", \"smiley-emotion\", \"face-tongue\", \"🤑\"),
        EmojiItem(
            \"FACE WITH STUCK-OUT TONGUE AND TIGHTLY-CLOSED EYES\",
            \"smiley-emotion\",
            \"face-tongue\",
            \"😝\",
        ),
        EmojiItem(
            \"FACE WITH STUCK-OUT TONGUE AND WINKING EYE\",
            \"smiley-emotion\",
            \"face-tongue\",
            \"😜\",
        ),
        EmojiItem(
            \"FACE WITH STUCK-OUT TONGUE\", \"smiley-emotion\", \"face-tongue\", \"😛\"
        ),
        EmojiItem(
            \"FACE SAVOURING DELICIOUS FOOD\",
            \"smiley-emotion\",
            \"face-tongue\",
            \"😋\",
        ),
        EmojiItem(\"FREEZING FACE\", \"smiley-emotion\", \"face-unwell\", \"🥶\"),
        EmojiItem(\"OVERHEATED FACE\", \"smiley-emotion\", \"face-unwell\", \"🥵\"),
        EmojiItem(
            \"FACE WITH UNEVEN EYES AND WAVY MOUTH\",
            \"smiley-emotion\",
            \"face-unwell\",
            \"🥴\",
        ),
        EmojiItem(
            \"SHOCKED FACE WITH EXPLODING HEAD\",
            \"smiley-emotion\",
            \"face-unwell\",
            \"🤯\",
        ),
        EmojiItem(
            \"FACE WITH OPEN MOUTH VOMITING\",
            \"smiley-emotion\",
            \"face-unwell\",
            \"🤮\",
        ),
        EmojiItem(\"SNEEZING FACE\", \"smiley-emotion\", \"face-unwell\", \"🤧\"),
        EmojiItem(\"NAUSEATED FACE\", \"smiley-emotion\", \"face-unwell\", \"🤢\"),
        EmojiItem(
            \"FACE WITH HEAD-BANDAGE\", \"smiley-emotion\", \"face-unwell\", \"🤕\"
        ),
        EmojiItem(
            \"FACE WITH THERMOMETER\", \"smiley-emotion\", \"face-unwell\", \"🤒\"
        ),
        EmojiItem(
            \"FACE WITH MEDICAL MASK\", \"smiley-emotion\", \"face-unwell\", \"😷\"
        ),
        EmojiItem(\"DIZZY FACE\", \"smiley-emotion\", \"face-unwell\", \"😵\"),
        EmojiItem(
            \"SPEAK-NO-EVIL MONKEY\", \"smiley-emotion\", \"monkey-face\", \"🙊\"
        ),
        EmojiItem(\"HEAR-NO-EVIL MONKEY\", \"smiley-emotion\", \"monkey-face\", \"🙉\"),
        EmojiItem(\"SEE-NO-EVIL MONKEY\", \"smiley-emotion\", \"monkey-face\", \"🙈\"),
    ]

    @staticmethod
    def categories():
        \"\"\"Get a set of categories.

        Returns:

            set:
                Emoji categories.

        Examples:

            ```python
            >>> Emoji.categories()
            {'component', 'animal-nature', 'objects', 'symbols', 'flags',
             'people-body', 'smiley-emotion', 'activities', 'food-drink',
             'travel-places'}
            ```
        \"\"\"
        cat = set()
        for e in Emoji._ITEMS:
            cat.add(e.category)
        return cat

    @staticmethod
    def subcategories(category: str = None):
        \"\"\"Get a set of all subcategories or for a specific category.

        Parameters:

            category (str):
                The name of the category to query.

        Returns:

            set:
                All subcategories or categories for a specific category.

        Examples:

            ```python
            >>> Emoji.subcategories('activities')
            {'award-medal', 'arts & crafts', 'event', 'game', 'sport'}
            ```
        \"\"\"
        subcat = set()
        for e in Emoji._ITEMS:
            if not category:
                subcat.add(e.subcategory)
            else:
                if e.category == category:
                    subcat.add(e.subcategory)
        return subcat

    @staticmethod
    def get(name: str):
        \"\"\"Lookup an emoji by name.

        Parameters:

            name (str):
                The name of the emoji to lookup.

        Returns:

            Union[EmojiItem, None]:
                The selected emoji or None if not found.

        Examples:

            ```python
            >>> Emoji.get('winking face')
            😉

            >>> face = Emoji.get('winking face')
            >>> face.name
            WINKING FACE

            >>> face.category
            smiley-emotion

            >>> face.subcategory
            face.smiling

            >>> face.char
            😉
            ```
        \"\"\"
        for e in Emoji._ITEMS:
            if e.name.lower() == name.lower():
                return e


if __name__ == \"__main__\":
    print(Emoji.get(\"winking face\"))
    print(Emoji.categories())
    print(Emoji.subcategories())
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/scrolled.py": """\"\"\"
    This module contains various custom scrolling widgets, including 
    `ScrolledText` and `ScrolledFrame`.
\"\"\"
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import Pack, Place, Grid


class ScrolledText(ttk.Frame):
    \"\"\"A text widget with optional vertical and horizontal scrollbars.
    Setting `autohide=True` will cause the scrollbars to hide when the
    mouse is not over the widget. The vertical scrollbar is on by
    default, but can be turned off. The horizontal scrollbar can be
    enabled by setting `vbar=True`.

    This widget is identical in configuration to the `Text` widget other
    than the scrolling frame. https://tcl.tk/man/tcl8.6/TkCmd/text.htm

    ![scrolled text](../../../assets/scrolled/scrolledtext.gif)

    Examples:

        ```python
        import ttkbootstrap as ttk
        from ttkbootstrap.constants import *
        from ttkbootstrap.scrolled import ScrolledText

        app = ttk.Window()

        # scrolled text with autohide vertical scrollbar
        st = ScrolledText(app, padding=5, height=10, autohide=True)
        st.pack(fill=BOTH, expand=YES)

        # add text
        st.insert(END, 'Insert your text here.')

        app.mainloop()
        ```
    \"\"\"

    def __init__(
        self,
        master=None,
        padding=2,
        bootstyle=DEFAULT,
        autohide=False,
        vbar=True,
        hbar=False,
        **kwargs,
    ):
        \"\"\"
        Parameters:

            master (Widget):
                The parent widget.

            padding (int):
                The amount of empty space to create on the outside of
                the widget.

            bootstyle (str):
                A style keyword used to set the color and style of the
                vertical scrollbar. Available options include -> primary,
                secondary, success, info, warning, danger, dark, light.

            vbar (bool):
                A vertical scrollbar is shown when **True** (default).

            hbar (bool):
                A horizontal scrollbar is shown when **True**. Turning
                on this scrollbar will also set `wrap=\"none\"`. This
                scrollbar is _off_ by default.

            autohide (bool):
                When **True**, the scrollbars will hide when the mouse
                is not within the frame bbox.

            **kwargs (Dict[str, Any]):
                Other keyword arguments passed to the `Text` widget.
        \"\"\"
        super().__init__(master, padding=padding)

        # setup text widget
        self._text = ttk.Text(self, padx=50, **kwargs)
        self._hbar = None
        self._vbar = None

        # delegate text methods to frame
        for method in vars(ttk.Text).keys():
            if any([\"pack\" in method, \"grid\" in method, \"place\" in method]):
                pass
            else:
                setattr(self, method, getattr(self._text, method))

        # setup scrollbars
        if vbar:
            self._vbar = ttk.Scrollbar(
                master=self,
                bootstyle=bootstyle,
                command=self._text.yview,
                orient=VERTICAL,
            )
            self._vbar.place(relx=1.0, relheight=1.0, anchor=NE)
            self._text.configure(yscrollcommand=self._vbar.set)

        if hbar:
            self._hbar = ttk.Scrollbar(
                master=self,
                bootstyle=bootstyle,
                command=self._text.xview,
                orient=HORIZONTAL,
            )
            self._hbar.place(rely=1.0, relwidth=1.0, anchor=SW)
            self._text.configure(xscrollcommand=self._hbar.set, wrap=\"none\")

        self._text.pack(side=LEFT, fill=BOTH, expand=YES)

        # position scrollbars
        if self._hbar:
            self.update_idletasks()
            self._text_width = self.winfo_reqwidth()
            self._scroll_width = self.winfo_reqwidth()

        self.bind(\"<Configure>\", self._on_configure)

        if autohide:
            self.autohide_scrollbar()
            self.hide_scrollbars()

    def _on_configure(self, *_):
        \"\"\"Callback for when the configure method is used\"\"\"
        if self._hbar:
            self.update_idletasks()
            text_width = self.winfo_width()
            vbar_width = self._vbar.winfo_width()
            relx = (text_width - vbar_width) / text_width
            self._hbar.place(rely=1.0, relwidth=relx)

    @property
    def text(self):
        \"\"\"Returns the internal text object\"\"\"
        return self._text

    @property
    def hbar(self):
        \"\"\"Returns the internal horizontal scrollbar\"\"\"
        return self._hbar

    @property
    def vbar(self):
        \"\"\"Returns the internal vertical scrollbar\"\"\"
        return self._vbar            

    def hide_scrollbars(self, *_):
        \"\"\"Hide the scrollbars.\"\"\"
        try:
            self._vbar.lower(self._text)
        except:
            pass
        try:
            self._hbar.lower(self._text)
        except:
            pass

    def show_scrollbars(self, *_):
        \"\"\"Show the scrollbars.\"\"\"
        try:
            self._vbar.lift(self._text)
        except:
            pass
        try:
            self._hbar.lift(self._text)
        except:
            pass

    def autohide_scrollbar(self, *_):
        \"\"\"Show the scrollbars when the mouse enters the widget frame,
        and hide when it leaves the frame.\"\"\"
        self.bind(\"<Enter>\", self.show_scrollbars)
        self.bind(\"<Leave>\", self.hide_scrollbars)


class ScrolledFrame(ttk.Frame):
    \"\"\"A widget container with a vertical scrollbar.

    The ScrolledFrame fills the width of its container. The height is
    either set explicitly or is determined by the content frame's
    contents.

    This widget behaves mostly like a normal frame other than the
    exceptions stated already. Another exception is when packing it
    into a Notebook or Panedwindow. In this case, you'll need to add
    the container instead of the content frame. For example,
    `mynotebook.add(myscrolledframe.container)`.

    The scrollbar has an autohide feature that can be turned on by
    setting `autohide=True`.

    Examples:

        ```python
        import ttkbootstrap as ttk
        from ttkbootstrap.constants import *
        from ttkbootstrap.scrolled import ScrolledFrame

        app = ttk.Window()

        sf = ScrolledFrame(app, autohide=True)
        sf.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        # add a large number of checkbuttons into the scrolled frame
        for x in range(20):
            ttk.Checkbutton(sf, text=f\"Checkbutton {x}\").pack(anchor=W)

        app.mainloop()
        ```\"\"\"

    def __init__(
        self,
        master=None,
        padding=2,
        bootstyle=DEFAULT,
        autohide=False,
        height=200,
        width=300,
        scrollheight=None,
        **kwargs,
    ):
        \"\"\"
        Parameters:

            master (Widget):
                The parent widget.

            padding (int):
                The amount of empty space to create on the outside of
                the widget.

            bootstyle (str):
                A style keyword used to set the color and style of the
                vertical scrollbar. Available options include -> primary,
                secondary, success, info, warning, danger, dark, light.

            autohide (bool):
                When **True**, the scrollbars will hide when the mouse
                is not within the frame bbox.

            height (int):
                The height of the container frame in screen units.

            width (int):
                The width of the container frame in screen units.

            scrollheight (int):
                The height of the content frame in screen units. If None,
                the height is determined by the frame contents.

            **kwargs (Dict[str, Any]):
                Other keyword arguments passed to the content frame.
        \"\"\"
        # content frame container
        self.container = ttk.Frame(
            master=master,
            relief=FLAT,
            borderwidth=0,
            width=width,
            height=height,
        )
        self.container.bind(\"<Configure>\", lambda _: self.yview())
        self.container.propagate(0)

        # content frame
        super().__init__(
            master=self.container,
            padding=padding,
            bootstyle=bootstyle.replace('round', ''),
            width=width,
            height=height,
            **kwargs,
        )
        self.place(rely=0.0, relwidth=1.0, height=scrollheight)

        # vertical scrollbar
        self.vscroll = ttk.Scrollbar(
            master=self.container,
            command=self.yview,
            orient=VERTICAL,
            bootstyle=bootstyle,
        )
        self.vscroll.pack(side=RIGHT, fill=Y)

        self.winsys = self.tk.call(\"tk\", \"windowingsystem\")

        # setup autohide scrollbar
        self.autohide = autohide
        if self.autohide:
            self.hide_scrollbars()

        # widget event binding
        self.container.bind(\"<Enter>\", self._on_enter, \"+\")
        self.container.bind(\"<Leave>\", self._on_leave, \"+\")
        self.container.bind(\"<Map>\", self._on_map, \"+\")
        self.bind(\"<<MapChild>>\", self._on_map_child, \"+\")

        # delegate content geometry methods to container frame
        _methods = vars(Pack).keys() | vars(Grid).keys() | vars(Place).keys()
        for method in _methods:
            if any([\"pack\" in method, \"grid\" in method, \"place\" in method]):
                # prefix content frame methods with 'content_'
                setattr(self, f\"content_{method}\", getattr(self, method))
                # overwrite content frame methods from container frame
                setattr(self, method, getattr(self.container, method))

    def yview(self, *args):
        \"\"\"Update the vertical position of the content frame within the
        container.

        Parameters:

            *args (List[Any, ...]):
                Optional arguments passed to yview in order to move the
                content frame within the container frame.
        \"\"\"
        if not args:
            first, _ = self.vscroll.get()
            self.yview_moveto(fraction=first)
        elif args[0] == \"moveto\":
            self.yview_moveto(fraction=float(args[1]))
        elif args[0] == \"scroll\":
            self.yview_scroll(number=int(args[1]), what=args[2])
        else:
            return

    def yview_moveto(self, fraction: float):
        \"\"\"Update the vertical position of the content frame within the
        container.

        Parameters:

            fraction (float):
                The relative position of the content frame within the
                container.
        \"\"\"
        base, thumb = self._measures()
        if fraction < 0:
            first = 0.0
        elif (fraction + thumb) > 1:
            first = 1 - thumb
        else:
            first = fraction
        self.vscroll.set(first, first + thumb)
        self.content_place(rely=-first * base)

    def yview_scroll(self, number: int, what: str):
        \"\"\"Update the vertical position of the content frame within the
        container.

        Parameters:

            number (int):
                The amount by which the content frame will be moved
                within the container frame by 'what' units.

            what (str):
                The type of units by which the number is to be interpeted.
                This parameter is currently not used and is assumed to be
                'units'.
        \"\"\"
        first, _ = self.vscroll.get()
        fraction = (number / 100) + first
        self.yview_moveto(fraction)

    def _add_scroll_binding(self, parent):
        \"\"\"Recursive adding of scroll binding to all descendants.\"\"\"
        children = parent.winfo_children()
        for widget in [parent, *children]:
            bindings = widget.bind()
            if self.winsys.lower() == \"x11\":
                if \"<Button-4>\" in bindings or \"<Button-5>\" in bindings:
                    continue
                else:
                    widget.bind(\"<Button-4>\", self._on_mousewheel, \"+\")
                    widget.bind(\"<Button-5>\", self._on_mousewheel, \"+\")
            else:
                if \"<MouseWheel>\" not in bindings:
                    widget.bind(\"<MouseWheel>\", self._on_mousewheel, \"+\")
            if widget.winfo_children() and widget != parent:
                self._add_scroll_binding(widget)


    def _del_scroll_binding(self, parent):
        \"\"\"Recursive removal of scrolling binding for all descendants\"\"\"
        children = parent.winfo_children()
        for widget in [parent, *children]:
            if self.winsys.lower() == \"x11\":
                widget.unbind(\"<Button-4>\")
                widget.unbind(\"<Button-5>\")
            else:
                widget.unbind(\"<MouseWheel>\")
            if widget.winfo_children() and widget != parent:
                self._del_scroll_binding(widget)


    def enable_scrolling(self):
        \"\"\"Enable mousewheel scrolling on the frame and all of its
        children.\"\"\"
        self._add_scroll_binding(self)


    def disable_scrolling(self):
        \"\"\"Disable mousewheel scrolling on the frame and all of its
        children.\"\"\"
        self._del_scroll_binding(self)

    def hide_scrollbars(self):
        \"\"\"Hide the scrollbars.\"\"\"
        self.vscroll.pack_forget()

    def show_scrollbars(self):
        \"\"\"Show the scrollbars.\"\"\"
        self.vscroll.pack(side=RIGHT, fill=Y)

    def autohide_scrollbar(self):
        \"\"\"Toggle the autohide funtionality. Show the scrollbars when
        the mouse enters the widget frame, and hide when it leaves the
        frame.\"\"\"
        self.autohide = not self.autohide

    def _measures(self):
        \"\"\"Measure the base size of the container and the thumb size
        for use in the yview methods\"\"\"
        outer = self.container.winfo_height()
        inner = max([self.winfo_height(), outer])
        base = inner / outer
        if inner == outer:
            thumb = 1.0
        else:
            thumb = outer / inner
        return base, thumb

    def _on_map_child(self, event):
        \"\"\"Callback for when a widget is mapped to the content frame.\"\"\"
        if self.container.winfo_ismapped():
            self.yview()

    def _on_enter(self, event):
        \"\"\"Callback for when the mouse enters the widget.\"\"\"
        self.enable_scrolling()
        if self.autohide:
            self.show_scrollbars()

    def _on_leave(self, event):
        \"\"\"Callback for when the mouse leaves the widget.\"\"\"
        self.disable_scrolling()
        if self.autohide:
            self.hide_scrollbars()

    def _on_configure(self, event):
        \"\"\"Callback for when the widget is configured\"\"\"
        self.yview()

    def _on_map(self, event):
        self.yview()

    def _on_mousewheel(self, event):
        \"\"\"Callback for when the mouse wheel is scrolled.\"\"\"
        if self.winsys.lower() == \"win32\":
            delta = -int(event.delta / 120)
        elif self.winsys.lower() == \"aqua\":
            delta = -event.delta
        elif event.num == 4:
            delta = -10
        elif event.num == 5:
            delta = 10
        self.yview_scroll(delta, UNITS)
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/validation.py": """\"\"\"
    This module contains classes and functions that are used to add
    validation to Entry, Spinbox, and Combobox widgets. Several helper 
    methods are included which start with the \"add\" prefix.

    ## Using predefined methods
    
    When validation is applied to a widget and the input is determined
    to be invalid, a 'danger' colored border is applied to the widget.
    This border disappears when the widget is determined to have valid
    contents.

    Below are a few examples using predefined validation. Browse the 
    full list in the documentation below:
    ```python
    app = ttk.Window()

    entry = ttk.Entry()
    entry.pack(padx=10, pady=10)

    # check if contents is text
    add_text_validation(entry)

    # prevent any entry except text
    add_text_validation(entry, when='key')

    # check for a specific list of options
    add_option_validation(entry, ['red', 'blue', 'green'])

    # validate against a specific regex expression
    add_regex_validation(entry, r'\\d{4}-\\d{2}-\\d{2}')    
    ```

    ## Adding a custom validation

    First, create a custom validation function. This must accept a 
    `ValidationEvent` object and should return a boolean. You should
    also use the @validator decorator to convert this method to a
    validation method. Check the `ValidationEvent` attributes to 
    learn about what is returned in this event.

    ```python
    from ttkbootstrap import validator, add_validation

    @validator
    def validate_long_text(event):
        if len(event.postchangetext) > 20:
            return True
        else:
            return False
    ```

    Apply your custom validation to the widget
    ```python
    add_validation(entry, validate_long_text)
    ```
\"\"\"
import ttkbootstrap as ttk
import re


class ValidationEvent:
    \"\"\"Contains the attributes of a validation event returned by the
    `validatecommand` on a tkinter widget.

    Attributes:

        actioncode (str):
            0 for an attempted deletion, 1 for an attempted insertion,
            or -1 if the callback was for focusin, focusout, or a
            change to the textvariable.

        insertdeletetext (str):
            When the user attempts to insert or delete text, this
            attribute will be the index of the beginning of the
            insertion or deletion. If the callback was due to focusin,
            focusout, or a change to the textvariable, the attribute
            will be -1.

        postchangetext (str):
            The value that the text will have if the change is allowed.

        prechangetext (str):
            The text in the entry before the change.

        insertdeletetext (str):
            The text inserted or deleted if the call was due to an
            insertion or deletion.

        validationtype (str):
            Specifies the widget's validation option which specifies
            _when_ the validation will occur.

        widget (Widget):
            The widget object that is being validated.
    \"\"\"

    def __init__(self, d, i, P, s, S, v, V, W):
        self.actioncode = d
        self.insertdeletetext = i
        self.postchangetext = P
        self.prechangetext = s
        self.insertdeletetext = S
        self.validationtype = v
        self.validationreason = V

        style = ttk.Style.get_instance()
        self.widget = style.master.nametowidget(
            W
        )  # replace with another method


def validator(func):
    \"\"\"Decorates a standard function so that it receives the validation
    events returned by the validate command on the tkinter widgets.

    Parameters:

        func (Callable):
            The validation function to be decorated.
    \"\"\"

    def inner(*args, **kw):
        event = ValidationEvent(*args)
        return func(event, **kw)

    return inner


def add_validation(widget, func, when=\"focusout\", **kwargs):
    \"\"\"Adds validation to the widget of type `Entry`, `Combobox`, or
    `Spinbox`. The func should accept a parameter of type
    `ValidationEvent` and should return a boolean value.

    Parameters:

        widget (Widget):
            The widget on which validation will be applied.

        func (Callable):
            The function that will be called when a validation event
            occurs.

        when (str):
            Indicates when the validation event should occur. Possible
            values include:

            * focus - whenever the widget gets or loses focus
            * focusin - whenever the widget gets focus
            * focusout - whenever the widget loses focus
            * key - whenever a key is pressed
            * all - validate in all of the above situations

        kwargs (Dict):
            Optional arguments passed to the callback.
    \"\"\"
    f = widget.register(lambda *e: func(*e, **kwargs))
    subs = (r\"%d\", r\"%i\", r\"%P\", r\"%s\", r\"%S\", r\"%v\", r\"%V\", r\"%W\")
    widget.configure(validate=when, validatecommand=(f, *subs))


@validator
def _validate_text(event: ValidationEvent):
    \"\"\"Contents is text.\"\"\"
    if len(event.postchangetext) == 0:
        return True
    return str(event.postchangetext).isalpha()


@validator
def _validate_number(event: ValidationEvent):
    \"\"\"Contents is a number.\"\"\"
    if len(event.postchangetext) == 0:
        return True
    return str(event.postchangetext).isnumeric()


@validator
def _validate_options(event: ValidationEvent, options):
    \"\"\"Contents is in a list of options\"\"\"
    return event.postchangetext in options


@validator
def _validate_range(event: ValidationEvent, startrange, endrange):
    \"\"\"Contents is a number between the startrange and endrange
    inclusive
    \"\"\"
    if len(event.postchangetext) == 0:
        return True
    try:
        num = float(event.postchangetext)
        result = num >= startrange and num <= endrange
        return result
    except:
        return False


@validator
def _validate_regex(event: ValidationEvent, pattern):
    \"\"\"Contents matches a regex expression\"\"\"
    match = re.match(pattern, event.postchangetext)
    return match is not None


# helper methods


def add_text_validation(widget, when=\"focusout\"):
    \"\"\"Check if widget contents is alpha. Sets the state to 'Invalid'
    if not text.

    Parameters:

        widget (Widget):
            The widget on which to add validation.

        when (str):
            Specifies when to apply validation. See the `add_validation`
            method docstring for a full list of options.
    \"\"\"
    add_validation(widget, _validate_text, when=when)


def add_numeric_validation(widget, when=\"focusout\"):
    \"\"\"Check if widget contents is numeric. Sets the state to 'Invalid'
    if not a number.

    Parameters:

        widget (Widget):
            The widget on which to add validation.

        when (str):
            Specifies when to apply validation. See the `add_validation`
            method docstring for a full list of options.
    \"\"\"
    add_validation(widget, _validate_number, when=when)


def add_phonenumber_validation(widget, when=\"focusout\"):
    \"\"\"Check if the widget contents matches a phone number pattern.

    Parameters:

        widget (Widget):
            The widget on which to add validation.

        when (str):
            Specifies when to apply validation. See the `add_validation`
            method docstring for a full list of options.
    \"\"\"
    pattern = r\"^[\\+]?[(]?[0-9]{3}[)]?[-\\s\\.]?[0-9]{3}[-\\s\\.]?[0-9]{4,6}$\"
    add_validation(widget, _validate_regex, pattern=pattern, when=when)


def add_regex_validation(widget, pattern, when=\"focusout\"):
    \"\"\"Check if widget contents matches regular expresssion. Sets the
    state to 'Invalid' if no match is found.

    Parameters:

        widget (Widget):
            The widget on which to add validation.

        when (str):
            Specifies when to apply validation. See the `add_validation`
            method docstring for a full list of options.
    \"\"\"
    add_validation(widget, _validate_regex, pattern=pattern, when=when)


def add_range_validation(widget, startrange, endrange, when=\"focusout\"):
    \"\"\"Check if widget contents is within a range of numbers, inclusive.
    Sets the state to 'Invalid' if the number is outside of the range.

    Parameters:

        widget (Widget):
            The widget on which to add validation.

        when (str):
            Specifies when to apply validation. See the `add_validation`
            method docstring for a full list of options.
    \"\"\"
    add_validation(
        widget,
        _validate_range,
        startrange=startrange,
        endrange=endrange,
        when=when,
    )


def add_option_validation(widget, options, when=\"focusout\"):
    \"\"\"Check if the widget contents is in a list of options.


    Parameters:

        widget (Widget):
            The widget on which to add validation.

        when (str):
            Specifies when to apply validation. See the `add_validation`
            method docstring for a full list of options.
    \"\"\"
    add_validation(widget, _validate_options, options=options, when=when)


if __name__ == \"__main__\":

    app = ttk.Window()

    @validator
    def myvalidation(event: ValidationEvent) -> bool:
        print(event.postchangetext)
        return True

    entry = ttk.Entry()
    entry.pack(padx=10, pady=10)
    entry2 = ttk.Entry()
    entry2.pack(padx=10, pady=10)
    # add_validation(entry, validate_range, startrange=5, endrange=10)
    # add_validation(entry, validate_regex, pattern=\"israel\")
    add_text_validation(entry, when=\"key\")  # prevents from using any numbers
    add_text_validation(entry2, when=\"key\")
    # add_option_validation(entry, ['red', 'blue', 'green'], 'focusout')
    # add_regex_validation(entry, r'\\d{4}-\\d{2}-\\d{2}')
    ttk.Button(text=\"Other\").pack(padx=10, pady=10)
    app.mainloop()
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/widgets.py": """import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.ttk import Button, Checkbutton, Combobox
from tkinter.ttk import Entry, Frame, Label
from tkinter.ttk import Labelframe, LabelFrame, Menubutton
from tkinter.ttk import Notebook, OptionMenu, PanedWindow
from tkinter.ttk import Panedwindow, Progressbar, Radiobutton
from tkinter.ttk import Scale, Scrollbar, Separator
from tkinter.ttk import Sizegrip, Treeview

###################################
# Added for Python 3.6 support
try:
    from tkinter.ttk import Spinbox
except:
    from tkinter import Spinbox
###################################

from ttkbootstrap.constants import *

# date entry imports
from ttkbootstrap.dialogs import Querybox
from datetime import datetime

# floodgauge imports
import math

# meter imports
from PIL import Image, ImageTk, ImageDraw
from ttkbootstrap.style import Colors
from ttkbootstrap import utility
from ttkbootstrap.style import Bootstyle

M = 3  # meter image scale, higher number increases resolution

TTK_WIDGETS = (
    ttk.Button,
    ttk.Checkbutton,
    ttk.Combobox,
    ttk.Entry,
    ttk.Frame,
    ttk.Labelframe,
    ttk.Label,
    ttk.Menubutton,
    ttk.Notebook,
    ttk.Panedwindow,
    ttk.Progressbar,
    ttk.Radiobutton,
    ttk.Scale,
    ttk.Scrollbar,
    ttk.Separator,
    ttk.Sizegrip,
    ttk.Treeview,
    ttk.OptionMenu,
)

TK_WIDGETS = (
    tk.Tk,
    tk.Toplevel,
    tk.Button,
    tk.Label,
    tk.Text,
    tk.Frame,
    tk.Checkbutton,
    tk.Radiobutton,
    tk.Entry,
    tk.Scale,
    tk.Listbox,
    tk.Menu,
    tk.Menubutton,
    tk.LabelFrame,
    tk.Canvas,
    tk.OptionMenu,
    tk.Spinbox,
)


class DateEntry(ttk.Frame):
    \"\"\"A date entry widget combines the `Combobox` and a `Button`
    with a callback attached to the `get_date` function.

    When pressed, a date chooser popup is displayed. The returned
    value is inserted into the combobox.

    The date chooser popup will use the date in the combobox as the
    date of focus if it is in the format specified by the
    `dateformat` parameter. By default, this format is \"%Y-%m-%d\".

    The bootstyle api may be used to change the style of the widget.
    The available colors include -> primary, secondary, success,
    info, warning, danger, light, dark.

    The starting weekday on the date chooser popup can be changed
    with the `firstweekday` parameter. By default this value is
    `6`, which represents \"Sunday\".

    The `Entry` and `Button` widgets are accessible from the
    `DateEntry.Entry` and `DateEntry.Button` properties.

    ![](../../assets/widgets/date-entry.png)
    \"\"\"

    def __init__(
        self,
        master=None,
        dateformat=r\"%x\",
        firstweekday=6,
        startdate=None,
        bootstyle=\"\",
        **kwargs,
    ):
        \"\"\"
        Parameters:

            master (Widget, optional):
                The parent widget.

            dateformat (str, optional):
                The format string used to render the text in the entry
                widget. For more information on acceptable formats, see https://strftime.org/

            firstweekday (int, optional):
                Specifies the first day of the week. 0=Monday, 1=Tuesday,
                etc...

            startdate (datetime, optional):
                The date that is in focus when the widget is displayed. Default is
                current date.

            bootstyle (str, optional):
                A style keyword used to set the focus color of the entry
                and the background color of the date button. Available
                options include -> primary, secondary, success, info,
                warning, danger, dark, light.

            **kwargs (Dict[str, Any], optional):
                Other keyword arguments passed to the frame containing the
                entry and date button.
        \"\"\"
        self._dateformat = dateformat
        self._firstweekday = firstweekday

        self._startdate = startdate or datetime.today()
        self._bootstyle = bootstyle
        super().__init__(master, **kwargs)

        # add visual components
        entry_kwargs = {\"bootstyle\": self._bootstyle}
        if \"width\" in kwargs:
            entry_kwargs[\"width\"] = kwargs.pop(\"width\")

        self.entry = ttk.Entry(self, **entry_kwargs)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES)

        self.button = ttk.Button(
            master=self,
            command=self._on_date_ask,
            bootstyle=f\"{self._bootstyle}-date\",
        )
        self.button.pack(side=tk.LEFT)

        # starting value
        self.entry.insert(tk.END, self._startdate.strftime(self._dateformat))

    def __getitem__(self, key: str):
        return self.configure(cnf=key)

    def __setitem__(self, key: str, value):
        self.configure(cnf=None, **{key: value})

    def _configure_set(self, **kwargs):
        \"\"\"Override configure method to allow for setting custom
        DateEntry parameters\"\"\"

        if \"state\" in kwargs:
            state = kwargs.pop(\"state\")
            if state in [\"readonly\", \"invalid\"]:
                self.entry.configure(state=state)
            elif state == \"disabled\":
                self.entry.configure(state=state)
                self.button.configure(state=state)
            else:
                kwargs[state] = state
        if \"dateformat\" in kwargs:
            self._dateformat = kwargs.pop(\"dateformat\")
        if \"firstweekday\" in kwargs:
            self._firstweekday = kwargs.pop(\"firstweekday\")
        if \"startdate\" in kwargs:
            self._startdate = kwargs.pop(\"startdate\")
        if \"bootstyle\" in kwargs:
            self._bootstyle = kwargs.pop(\"bootstyle\")
            self.entry.configure(bootstyle=self._bootstyle)
            self.button.configure(bootstyle=[self._bootstyle, \"date\"])
        if \"width\" in kwargs:
            width = kwargs.pop(\"width\")
            self.entry.configure(width=width)

        super(ttk.Frame, self).configure(**kwargs)

    def _configure_get(self, cnf):
        \"\"\"Override the configure get method\"\"\"
        if cnf == \"state\":
            entrystate = self.entry.cget(\"state\")
            buttonstate = self.button.cget(\"state\")
            return {\"Entry\": entrystate, \"Button\": buttonstate}
        if cnf == \"dateformat\":
            return self._dateformat
        if cnf == \"firstweekday\":
            return self._firstweekday
        if cnf == \"startdate\":
            return self._startdate
        if cnf == \"bootstyle\":
            return self._bootstyle
        else:
            return super(ttk.Frame, self).configure(cnf=cnf)

    def configure(self, cnf=None, **kwargs):
        \"\"\"Configure the options for this widget.

        Parameters:

            cnf (Dict[str, Any], optional):
                A dictionary of configuration options.

            **kwargs:
                Optional keyword arguments.
        \"\"\"
        if cnf is not None:
            return self._configure_get(cnf)
        else:
            return self._configure_set(**kwargs)

    def _on_date_ask(self):
        \"\"\"Callback for pushing the date button\"\"\"
        _val = self.entry.get() or datetime.today().strftime(self._dateformat)
        try:
            self._startdate = datetime.strptime(_val, self._dateformat)
        except Exception as e:
            print(\"Date entry text does not match\", self._dateformat)
            self._startdate = datetime.today()
            self.entry.delete(first=0, last=tk.END)
            self.entry.insert(
                tk.END, self._startdate.strftime(self._dateformat)
            )

        old_date = datetime.strptime(_val, self._dateformat)

        # get the new date and insert into the entry
        new_date = Querybox.get_date(
            parent=self.entry,
            startdate=old_date,
            firstweekday=self._firstweekday,
            bootstyle=self._bootstyle,
        )
        self.entry.delete(first=0, last=tk.END)
        self.entry.insert(tk.END, new_date.strftime(self._dateformat))
        self.entry.focus_force()


class Floodgauge(Progressbar):
    \"\"\"A widget that shows the status of a long-running operation
    with an optional text indicator.

    Similar to the `ttk.Progressbar`, this widget can operate in
    two modes. *determinate* mode shows the amount completed
    relative to the total amount of work to be done, and
    *indeterminate* mode provides an animated display to let the
    user know that something is happening.

    Variable are generated automatically for this widget and can be
    linked to other widgets by referencing them via the
    `textvariable` and `variable` attributes.

    ![](../../assets/widgets/floodgauge.gif)

    Examples:

        ```python
        import ttkbootstrap as ttk
        from ttkbootstrap.constants import *

        app = ttk.Window(size=(500, 500))

        gauge = ttk.Floodgauge(
            bootstyle=INFO,
            font=(None, 24, 'bold'),
            mask='Memory Used {}%',
        )
        gauge.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        # autoincrement the gauge
        gauge.start()

        # stop the autoincrement
        gauge.stop()

        # manually update the gauge value
        gauge.configure(value=25)

        # increment the value by 10 steps
        gauge.step(10)

        app.mainloop()
        ```
    \"\"\"

    def __init__(
        self,
        master=None,
        cursor=None,
        font=None,
        length=None,
        maximum=100,
        mode=DETERMINATE,
        orient=HORIZONTAL,
        bootstyle=PRIMARY,
        takefocus=False,
        text=None,
        value=0,
        mask=None,
        **kwargs,
    ):
        \"\"\"
        Parameters:

            master (Widget, optional):
                Parent widget. Defaults to None.

            cursor (str, optional):
                The cursor that will appear when the mouse is over the
                progress bar. Defaults to None.

            font (Union[Font, str], optional):
                The font to use for the progress bar label.

            length (int, optional):
                Specifies the length of the long axis of the progress bar
                (width if orient = horizontal, height if if vertical);

            maximum (float, optional):
                A floating point number specifying the maximum `value`.
                Defaults to 100.

            mode ('determinate', 'indeterminate'):
                Use `indeterminate` if you cannot accurately measure the
                relative progress of the underlying process. In this mode,
                a rectangle bounces back and forth between the ends of the
                widget once you use the `Floodgauge.start()` method.
                Otherwise, use `determinate` if the relative progress can be
                calculated in advance.

            orient ('horizontal', 'vertical'):
                Specifies the orientation of the widget.

            bootstyle (str, optional):
                The style used to render the widget. Options include
                primary, secondary, success, info, warning, danger, light,
                dark.

            takefocus (bool, optional):
                This widget is not included in focus traversal by default.
                To add the widget to focus traversal, use
                `takefocus=True`.

            text (str, optional):
                A string of text to be displayed in the Floodgauge label.
                This is assigned to the attribute `Floodgauge.textvariable`

            value (float, optional):
                The current value of the progressbar. In `determinate`
                mode, this represents the amount of work completed. In
                `indeterminate` mode, it is interpreted modulo `maximum`;
                that is, the progress bar completes one \"cycle\" when the
                `value` increases by `maximum`.

            mask (str, optional):
                A string format that can be used to update the Floodgauge
                label every time the value is updated. For example, the
                string \"{}% Storage Used\" with a widget value of 45 would
                show \"45% Storage Used\" on the Floodgauge label. If a
                mask is set, then the `text` option is ignored.

            **kwargs:
                Other configuration options from the option database.
        \"\"\"
        # progress bar value variables
        if 'variable' in kwargs:
            self._variable = kwargs.pop('variable')
        else:
            self._variable = tk.IntVar(value=value)
        if 'textvariable' in kwargs:
            self._textvariable = kwargs.pop('textvariable')
        else:
            self._textvariable = tk.StringVar(value=text)
        self._bootstyle = bootstyle
        self._font = font or \"helvetica 10\"
        self._mask = mask
        self._traceid = None

        super().__init__(
            master=master,
            class_=\"Floodgauge\",
            cursor=cursor,
            length=length,
            maximum=maximum,
            mode=mode,
            orient=orient,
            bootstyle=bootstyle,
            takefocus=takefocus,
            variable=self._variable,
            **kwargs,
        )
        self._set_widget_text(self._textvariable.get())
        self.bind(\"<<ThemeChanged>>\", self._on_theme_change)
        self.bind(\"<<Configure>>\", self._on_theme_change)

        if self._mask is not None:
            self._set_mask()

    def _set_widget_text(self, *_):
        ttkstyle = self.cget(\"style\")
        if self._mask is None:
            text = self._textvariable.get()
        else:
            value = self._variable.get()
            text = self._mask.format(value)
        self.tk.call(\"ttk::style\", \"configure\", ttkstyle, \"-text\", text)
        self.tk.call(\"ttk::style\", \"configure\", ttkstyle, \"-font\", self._font)

    def _set_mask(self):
        if self._traceid is None:
            self._traceid = self._variable.trace_add(
                \"write\", self._set_widget_text
            )

    def _unset_mask(self):
        if self._traceid is not None:
            self._variable.trace_remove(\"write\", self._traceid)
        self._traceid = None

    def _on_theme_change(self, *_):
        text = self._textvariable.get()
        self._set_widget_text(text)

    def _configure_get(self, cnf):
        if cnf == \"value\":
            return self._variable.get()
        if cnf == \"text\":
            return self._textvariable.get()
        if cnf == \"bootstyle\":
            return self._bootstyle
        if cnf == \"mask\":
            return self._mask
        if cnf == \"font\":
            return self._font
        else:
            return super(Progressbar, self).configure(cnf=cnf)

    def _configure_set(self, **kwargs):
        if \"value\" in kwargs:
            self._variable.set(kwargs.pop(\"value\"))
        if \"text\" in kwargs:
            self._textvariable.set(kwargs.pop(\"text\"))
        if \"bootstyle\" in kwargs:
            self._bootstyle = kwargs.get(\"bootstyle\")
        if \"mask\" in kwargs:
            self._mask = kwargs.pop(\"mask\")
        if \"font\" in kwargs:
            self._font = kwargs.pop(\"font\")
        if \"variable\" in kwargs:
            self._variable = kwargs.get(\"variable\")
            Progressbar.configure(self, cnf=None, **kwargs)
        if \"textvariable\" in kwargs:
            self.textvariable = kwargs.pop(\"textvariable\")
        else:
            Progressbar.configure(self, cnf=None, **kwargs)

    def __getitem__(self, key: str):
        return self._configure_get(cnf=key)

    def __setitem__(self, key: str, value):
        self._configure_set(**{key: value})

    def configure(self, cnf=None, **kwargs):
        \"\"\"Configure the options for this widget.

        Parameters:

            cnf (Dict[str, Any], optional):
                A dictionary of configuration options.

            **kwargs:
                Optional keyword arguments.
        \"\"\"
        if cnf is not None:
            return self._configure_get(cnf)
        else:
            self._configure_set(**kwargs)

    @property
    def textvariable(self):
        \"\"\"Returns the textvariable object\"\"\"
        return self._textvariable

    @textvariable.setter
    def textvariable(self, value):
        \"\"\"Set the new textvariable property\"\"\"
        self._textvariable = value
        self._set_widget_text(self._textvariable.get())

    @property
    def variable(self):
        \"\"\"Returns the variable object\"\"\"
        return self._variable

    @variable.setter
    def variable(self, value):
        \"\"\"Set the new variable object\"\"\"
        self._variable = value
        if self.cget('variable') != value:
            self.configure(variable=self._variable)


class Meter(ttk.Frame):
    \"\"\"A radial meter that can be used to show progress of long
    running operations or the amount of work completed; can also be
    used as a dial when set to `interactive=True`.

    This widget is very flexible. There are two primary meter types
    which can be set with the `metertype` parameter: 'full' and
    'semi', which shows the arc of the meter in a full or
    semi-circle. You can also customize the arc of the circle with
    the `arcrange` and `arcoffset` parameters.

    The meter indicator can be displayed as a solid color or with
    stripes using the `stripethickness` parameter. By default, the
    `stripethickness` is 0, which results in a solid meter
    indicator. A higher `stripethickness` results in larger wedges
    around the arc of the meter.

    Various text and label options exist. The center text and
    meter indicator is formatted with the `meterstyle` parameter.
    You can set text on the left and right of this center label
    using the `textleft` and `textright` parameters. This is most
    commonly used for '$', '%', or other such symbols.

    If you need access to the variables that update the meter, you
    you can access these via the `amountusedvar`, `amounttotalvar`,
    and the `labelvar`. The value of these properties can also be
    retrieved via the `configure` method.

    ![](../../assets/widgets/meter.gif)

    Examples:

        ```python
        import ttkbootstrap as ttk
        from ttkbootstrap.constants import *

        app = ttk.Window()

        meter = ttk.Meter(
            metersize=180,
            padding=5,
            amountused=25,
            metertype=\"semi\",
            subtext=\"miles per hour\",
            interactive=True,
        )
        meter.pack()

        # update the amount used directly
        meter.configure(amountused = 50)

        # update the amount used with another widget
        entry = ttk.Entry(textvariable=meter.amountusedvar)
        entry.pack(fill=X)

        # increment the amount by 10 steps
        meter.step(10)

        # decrement the amount by 15 steps
        meter.step(-15)

        # update the subtext
        meter.configure(subtext=\"loading...\")

        app.mainloop()
        ```
    \"\"\"

    def __init__(
        self,
        master=None,
        bootstyle=DEFAULT,
        arcrange=None,
        arcoffset=None,
        amounttotal=100,
        amountused=0,
        wedgesize=0,
        metersize=200,
        metertype=FULL,
        meterthickness=10,
        showtext=True,
        interactive=False,
        stripethickness=0,
        textleft=None,
        textright=None,
        textfont=\"-size 20 -weight bold\",
        subtext=None,
        subtextstyle=DEFAULT,
        subtextfont=\"-size 10\",
        stepsize=1,
        **kwargs,
    ):
        \"\"\"
        Parameters:

            master (Widget):
                The parent widget.

            arcrange (int):
                The range of the arc if degrees from start to end.

            arcoffset (int):
                The amount to offset the arc's starting position in degrees.
                0 is at 3 o'clock.

            amounttotal (int):
                The maximum value of the meter.

            amountused (int):
                The current value of the meter; displayed in a center label
                if the `showtext` property is set to True.

            wedgesize (int):
                Sets the length of the indicator wedge around the arc. If
                greater than 0, this wedge is set as an indicator centered
                on the current meter value.

            metersize (int):
                The meter is square. This represents the size of one side
                if the square as measured in screen units.

            bootstyle (str):
                Sets the indicator and center text color. One of primary,
                secondary, success, info, warning, danger, light, dark.

            metertype ('full', 'semi'):
                Displays the meter as a full circle or semi-circle.

            meterthickness (int):
                The thickness of the indicator.

            showtext (bool):
                Indicates whether to show the left, center, and right text
                labels on the meter.

            interactive (bool):
                Indicates that the user may adjust the meter value with
                mouse interaction.

            stripethickness (int):
                The indicator can be displayed as a solid band or as
                striped wedges around the arc. If the value is greater than
                0, the indicator changes from a solid to striped, where the
                value is the thickness of the stripes (or wedges).

            textleft (str):
                A short string inserted to the left of the center text.

            textright (str):
                A short string inserted to the right of the center text.

            textfont (Union[str, Font]):
                The font used to render the center text.

            subtext (str):
                Supplemental text that appears below the center text.

            subtextstyle (str):
                The bootstyle color of the subtext. One of primary,
                secondary, success, info, warning, danger, light, dark.
                The default color is Theme specific and is a lighter
                shade based on whether it is a 'light' or 'dark' theme.

            subtextfont (Union[str, Font]):
                The font used to render the subtext.

            stepsize (int):
                Sets the amount by which to change the meter indicator
                when incremented by mouse interaction.

            **kwargs:
                Other keyword arguments that are passed directly to the
                `Frame` widget that contains the meter components.
        \"\"\"
        super().__init__(master=master, **kwargs)

        # widget variables
        self.amountusedvar = tk.IntVar(value=amountused)
        self.amountusedvar.trace_add(\"write\", self._draw_meter)
        self.amounttotalvar = tk.IntVar(value=amounttotal)
        self.labelvar = tk.StringVar(value=subtext)

        # misc settings
        self._set_arc_offset_range(metertype, arcoffset, arcrange)
        self._towardsmaximum = True
        self._metersize = utility.scale_size(self, metersize)
        self._meterthickness = utility.scale_size(self, meterthickness)
        self._stripethickness = stripethickness
        self._showtext = showtext
        self._wedgesize = wedgesize
        self._stepsize = stepsize
        self._textleft = textleft
        self._textright = textright
        self._textfont = textfont
        self._subtext = subtext
        self._subtextfont = subtextfont
        self._subtextstyle = subtextstyle
        self._bootstyle = bootstyle
        self._interactive = interactive
        self._bindids = {}

        self._setup_widget()

    def _setup_widget(self):
        self.meterframe = ttk.Frame(
            master=self, width=self._metersize, height=self._metersize
        )
        self.indicator = ttk.Label(self.meterframe)
        self.textframe = ttk.Frame(self.meterframe)
        self.textleft = ttk.Label(
            master=self.textframe,
            text=self._textleft,
            font=self._subtextfont,
            bootstyle=(self._subtextstyle, \"metersubtxt\"),
            anchor=tk.S,
            padding=(0, 5),
        )
        self.textcenter = ttk.Label(
            master=self.textframe,
            textvariable=self.amountusedvar,
            bootstyle=(self._bootstyle, \"meter\"),
            font=self._textfont,
        )
        self.textright = ttk.Label(
            master=self.textframe,
            text=self._textright,
            font=self._subtextfont,
            bootstyle=(self._subtextstyle, \"metersubtxt\"),
            anchor=tk.S,
            padding=(0, 5),
        )
        self.subtext = ttk.Label(
            master=self.meterframe,
            text=self._subtext,
            bootstyle=(self._subtextstyle, \"metersubtxt\"),
            font=self._subtextfont,
        )

        self.bind(\"<<ThemeChanged>>\", self._on_theme_change)
        self.bind(\"<<Configure>>\", self._on_theme_change)
        self._set_interactive_bind()
        self._draw_base_image()
        self._draw_meter()

        # set widget geometery
        self.indicator.place(x=0, y=0)
        self.meterframe.pack()
        self._set_show_text()

    def _set_widget_colors(self):
        bootstyle = (self._bootstyle, \"meter\", \"label\")
        ttkstyle = Bootstyle.ttkstyle_name(string=\"-\".join(bootstyle))
        textcolor = self._lookup_style_option(ttkstyle, \"foreground\")
        background = self._lookup_style_option(ttkstyle, \"background\")
        troughcolor = self._lookup_style_option(ttkstyle, \"space\")
        self._meterforeground = textcolor
        self._meterbackground = Colors.update_hsv(background, vd=-0.1)
        self._metertrough = troughcolor

    def _set_meter_text(self):
        \"\"\"Setup and pack the widget labels in the appropriate order\"\"\"
        self._set_show_text()
        self._set_subtext()

    def _set_subtext(self):
        if self._subtextfont:
            if self._showtext:
                self.subtext.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            else:
                self.subtext.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def _set_show_text(self):
        self.textframe.pack_forget()
        self.textcenter.pack_forget()
        self.textleft.pack_forget()
        self.textright.pack_forget()
        self.subtext.pack_forget()

        if self._showtext:
            if self._subtext:
                self.textframe.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
            else:
                self.textframe.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self._set_text_left()
        self._set_text_center()
        self._set_text_right()
        self._set_subtext()

    def _set_text_left(self):
        if self._showtext and self._textleft:
            self.textleft.pack(side=tk.LEFT, fill=tk.Y)

    def _set_text_center(self):
        if self._showtext:
            self.textcenter.pack(side=tk.LEFT, fill=tk.Y)

    def _set_text_right(self):
        self.textright.configure(text=self._textright)
        if self._showtext and self._textright:
            self.textright.pack(side=tk.RIGHT, fill=tk.Y)

    def _set_interactive_bind(self):
        seq1 = \"<B1-Motion>\"
        seq2 = \"<Button-1>\"

        if self._interactive:
            self._bindids[seq1] = self.indicator.bind(
                seq1, self._on_dial_interact
            )
            self._bindids[seq2] = self.indicator.bind(
                seq2, self._on_dial_interact
            )
            return

        if seq1 in self._bindids:
            self.indicator.unbind(seq1, self._bindids.get(seq1))
            self.indicator.unbind(seq2, self._bindids.get(seq2))
            self._bindids.clear()

    def _set_arc_offset_range(self, metertype, arcoffset, arcrange):
        if metertype == SEMI:
            self._arcoffset = 135 if arcoffset is None else arcoffset
            self._arcrange = 270 if arcrange is None else arcrange
        else:
            self._arcoffset = -90 if arcoffset is None else arcoffset
            self._arcrange = 360 if arcrange is None else arcrange
        self._metertype = metertype

    def _draw_meter(self, *_):
        \"\"\"Draw a meter\"\"\"
        img = self._base_image.copy()
        draw = ImageDraw.Draw(img)
        if self._stripethickness > 0:
            self._draw_striped_meter(draw)
        else:
            self._draw_solid_meter(draw)

        self._meterimage = ImageTk.PhotoImage(
            img.resize((self._metersize, self._metersize), Image.CUBIC)
        )
        self.indicator.configure(image=self._meterimage)

    def _draw_base_image(self):
        \"\"\"Draw base image to be used for subsequent updates\"\"\"
        self._set_widget_colors()
        self._base_image = Image.new(
            mode=\"RGBA\", size=(self._metersize * M, self._metersize * M)
        )
        draw = ImageDraw.Draw(self._base_image)

        x1 = y1 = self._metersize * M - 20
        width = self._meterthickness * M
        # striped meter
        if self._stripethickness > 0:
            _from = self._arcoffset
            _to = self._arcrange + self._arcoffset
            _step = 2 if self._stripethickness == 1 else self._stripethickness
            for x in range(_from, _to, _step):
                draw.arc(
                    xy=(0, 0, x1, y1),
                    start=x,
                    end=x + self._stripethickness - 1,
                    fill=self._metertrough,
                    width=width,
                )
        # solid meter
        else:
            draw.arc(
                xy=(0, 0, x1, y1),
                start=self._arcoffset,
                end=self._arcrange + self._arcoffset,
                fill=self._metertrough,
                width=width,
            )

    def _draw_solid_meter(self, draw: ImageDraw.Draw):
        \"\"\"Draw a solid meter\"\"\"
        x1 = y1 = self._metersize * M - 20
        width = self._meterthickness * M

        if self._wedgesize > 0:
            meter_value = self._meter_value()
            draw.arc(
                xy=(0, 0, x1, y1),
                start=meter_value - self._wedgesize,
                end=meter_value + self._wedgesize,
                fill=self._meterforeground,
                width=width,
            )
        else:
            draw.arc(
                xy=(0, 0, x1, y1),
                start=self._arcoffset,
                end=self._meter_value(),
                fill=self._meterforeground,
                width=width,
            )

    def _draw_striped_meter(self, draw: ImageDraw.Draw):
        \"\"\"Draw a striped meter\"\"\"
        meter_value = self._meter_value()
        x1 = y1 = self._metersize * M - 20
        width = self._meterthickness * M

        if self._wedgesize > 0:
            draw.arc(
                xy=(0, 0, x1, y1),
                start=meter_value - self._wedgesize,
                end=meter_value + self._wedgesize,
                fill=self._meterforeground,
                width=width,
            )
        else:
            _from = self._arcoffset
            _to = meter_value - 1
            _step = self._stripethickness
            for x in range(_from, _to, _step):
                draw.arc(
                    xy=(0, 0, x1, y1),
                    start=x,
                    end=x + self._stripethickness - 1,
                    fill=self._meterforeground,
                    width=width,
                )

    def _meter_value(self) -> int:
        \"\"\"Calculate the value to be used to draw the arc length of the
        progress meter.\"\"\"
        value = int(
            (self[\"amountused\"] / self[\"amounttotal\"]) * self._arcrange
            + self._arcoffset
        )
        return value

    def _on_theme_change(self, *_):
        self._draw_base_image()
        self._draw_meter()

    def _on_dial_interact(self, e: tk.Event):
        \"\"\"Callback for mouse drag motion on meter indicator\"\"\"
        dx = e.x - self._metersize // 2
        dy = e.y - self._metersize // 2
        rads = math.atan2(dy, dx)
        degs = math.degrees(rads)

        if degs > self._arcoffset:
            factor = degs - self._arcoffset
        else:
            factor = 360 + degs - self._arcoffset

        # clamp the value between 0 and `amounttotal`
        amounttotal = self.amounttotalvar.get()
        lastused = self.amountusedvar.get()
        amountused = (amounttotal / self._arcrange * factor)

        # calculate amount used given stepsize
        if amountused > self._stepsize//2:
            amountused = amountused // self._stepsize * self._stepsize + self._stepsize
        else:
            amountused = 0
        # if the number is the name, then do not redraw
        if lastused == amountused:
            return
        # set the amount used variable
        if amountused < 0:
            self.amountusedvar.set(0)
        elif amountused > amounttotal:
            self.amountusedvar.set(amounttotal)
        else:
            self.amountusedvar.set(amountused)

    def _lookup_style_option(self, style: str, option: str):
        \"\"\"Wrapper around the tcl style lookup command\"\"\"
        value = self.tk.call(
            \"ttk::style\", \"lookup\", style, \"-%s\" % option, None, None
        )
        return value

    def _configure_get(self, cnf):
        \"\"\"Override the configuration get method\"\"\"
        if cnf == \"arcrange\":
            return self._arcrange
        elif cnf == \"arcoffset\":
            return self._arcoffset
        elif cnf == \"amounttotal\":
            return self.amounttotalvar.get()
        elif cnf == \"amountused\":
            return self.amountusedvar.get()
        elif cnf == \"interactive\":
            return self._interactive
        elif cnf == \"subtextfont\":
            return self._subtextfont
        elif cnf == \"subtextstyle\":
            return self._subtextstyle
        elif cnf == \"subtext\":
            return self._subtext
        elif cnf == \"metersize\":
            return self._metersize
        elif cnf == \"bootstyle\":
            return self._bootstyle
        elif cnf == \"metertype\":
            return self._metertype
        elif cnf == \"meterthickness\":
            return self._meterthickness
        elif cnf == \"showtext\":
            return self._showtext
        elif cnf == \"stripethickness\":
            return self._stripethickness
        elif cnf == \"textleft\":
            return self._textleft
        elif cnf == \"textright\":
            return self._textright
        elif cnf == \"textfont\":
            return self._textfont
        elif cnf == \"wedgesize\":
            return self._wedgesize
        elif cnf == \"stepsize\":
            return self._stepsize
        else:
            return super(ttk.Frame, self).configure(cnf)

    def _configure_set(self, **kwargs):
        \"\"\"Override the configuration set method\"\"\"
        meter_text_changed = False

        if \"arcrange\" in kwargs:
            self._arcrange = kwargs.pop(\"arcrange\")
        if \"arcoffset\" in kwargs:
            self._arcoffset = kwargs.pop(\"arcoffset\")
        if \"amounttotal\" in kwargs:
            amounttotal = kwargs.pop(\"amounttotal\")
            self.amounttotalvar.set(amounttotal)
        if \"amountused\" in kwargs:
            amountused = kwargs.pop(\"amountused\")
            self.amountusedvar.set(amountused)
        if \"interactive\" in kwargs:
            self._interactive = kwargs.pop(\"interactive\")
            self._set_interactive_bind()
        if \"subtextfont\" in kwargs:
            self._subtextfont = kwargs.pop(\"subtextfont\")
            self.subtext.configure(font=self._subtextfont)
            self.textleft.configure(font=self._subtextfont)
            self.textright.configure(font=self._subtextfont)
        if \"subtextstyle\" in kwargs:
            self._subtextstyle = kwargs.pop(\"subtextstyle\")
            self.subtext.configure(bootstyle=[self._subtextstyle, \"meter\"])
        if \"metersize\" in kwargs:
            self._metersize = utility.scale_size(kwargs.pop(\"metersize\"))
            self.meterframe.configure(
                height=self._metersize, width=self._metersize
            )
        if \"bootstyle\" in kwargs:
            self._bootstyle = kwargs.pop(\"bootstyle\")
            self.textcenter.configure(bootstyle=[self._bootstyle, \"meter\"])
        if \"metertype\" in kwargs:
            self._metertype = kwargs.pop(\"metertype\")
        if \"meterthickness\" in kwargs:
            self._meterthickness = self.scale_size(
                kwargs.pop(\"meterthickness\")
            )
        if \"stripethickness\" in kwargs:
            self._stripethickness = kwargs.pop(\"stripethickness\")
        if \"subtext\" in kwargs:
            self._subtext = kwargs.pop(\"subtext\")
            self.subtext.configure(text=self._subtext)
            meter_text_changed = True
        if \"textleft\" in kwargs:
            self._textleft = kwargs.pop(\"textleft\")
            self.textleft.configure(text=self._textleft)
            meter_text_changed = True
        if \"textright\" in kwargs:
            self._textright = kwargs.pop(\"textright\")
            meter_text_changed = True
        if \"showtext\" in kwargs:
            self._showtext = kwargs.pop(\"showtext\")
            meter_text_changed = True
        if \"textfont\" in kwargs:
            self._textfont = kwargs.pop(\"textfont\")
            self.textcenter.configure(font=self._textfont)
        if \"wedgesize\" in kwargs:
            self._wedgesize = kwargs.pop(\"wedgesize\")
        if \"stepsize\" in kwargs:
            self._stepsize = kwargs.pop(\"stepsize\")
        if meter_text_changed:
            self._set_meter_text()

        try:
            if self._metertype:
                self._set_arc_offset_range(
                    metertype=self._metertype,
                    arcoffset=self._arcoffset,
                    arcrange=self._arcrange,
                )
        except AttributeError:
            return

        self._draw_base_image()
        self._draw_meter()

        # pass remaining configurations to `ttk.Frame.configure`
        super(ttk.Frame, self).configure(**kwargs)

    def __getitem__(self, key: str):
        return self._configure_get(key)

    def __setitem__(self, key: str, value) -> None:
        self._configure_set(**{key: value})

    def configure(self, cnf=None, **kwargs):
        \"\"\"Configure the options for this widget.

        Parameters:
            cnf (Dict[str, Any], optional):
                A dictionary of configuration options.

            **kwargs: Optional keyword arguments.
        \"\"\"
        if cnf is not None:
            return self._configure_get(cnf)
        else:
            self._configure_set(**kwargs)

    def step(self, delta=1):
        \"\"\"Increase the indicator value by `delta`

        The indicator will reverse direction and count down once it
        reaches the maximum value.

        Parameters:

            delta (int):
                The amount to change the indicator.
        \"\"\"
        amountused = self.amountusedvar.get()
        amounttotal = self.amounttotalvar.get()
        if amountused >= amounttotal:
            self._towardsmaximum = True
            self.amountusedvar.set(amountused - delta)
        elif amountused <= 0:
            self._towardsmaximum = False
            self.amountusedvar.set(amountused + delta)
        elif self._towardsmaximum:
            self.amountusedvar.set(amountused - delta)
        else:
            self.amountusedvar.set(amountused + delta)
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/utility.py": """def enable_high_dpi_awareness(root=None, scaling=None):
    \"\"\"Enable high dpi awareness.

    **Windows OS**  
    Call the method BEFORE creating the `Tk` object. No parameters
    required.

    **Linux OS**  
    Must provided the `root` and `scaling` parameters. Call the method 
    AFTER creating the `Tk` object. A number between 1.6 and 2.0 is 
    usually suffient to scale for high-dpi screen.

    !!! warning
        If the `root` argument is provided, then `scaling` must also
        be provided. Otherwise, there is no effect.

    Parameters:
    
        root (tk.Tk):
            The root widget

        scaling (float):
            Sets and queries the current scaling factor used by Tk to 
            convert between physical units (for example, points, 
            inches, or millimeters) and pixels. The number argument is 
            a floating point number that specifies the number of pixels 
            per point on window's display. If the window argument is 
            omitted, it defaults to the main window. If the number 
            argument is omitted, the current value of the scaling 
            factor is returned.

            A “point” is a unit of measurement equal to 1/72 inch. A 
            scaling factor of 1.0 corresponds to 1 pixel per point, 
            which is equivalent to a standard 72 dpi monitor. A scaling 
            factor of 1.25 would mean 1.25 pixels per point, which is 
            the setting for a 90 dpi monitor; setting the scaling factor 
            to 1.25 on a 72 dpi monitor would cause everything in the 
            application to be displayed 1.25 times as large as normal. 
            The initial value for the scaling factor is set when the 
            application starts, based on properties of the installed 
            monitor, but it can be changed at any time. Measurements 
            made after the scaling factor is changed will use the new 
            scaling factor, but it is undefined whether existing 
            widgets will resize themselves dynamically to accommodate 
            the new scaling factor.
    \"\"\"
    try:
        from ctypes import windll
        windll.user32.SetProcessDPIAware()
    except:
        pass

    try:
        if root and scaling:
            root.tk.call('tk', 'scaling', scaling)
    except:
        pass

def get_image_name(image):
    \"\"\"Extract and return the tcl/tk image name from a PhotoImage 
    object.
    
    Parameters:

        image (ImageTk.PhotoImage):
            A photoimage object.

    Returns:

        str:
            The tcl/tk name of the photoimage object.
    \"\"\"
    return image._PhotoImage__photo.name

def scale_size(widget, size):
    \"\"\"Scale the size based on the scaling factor of tkinter. 
    This is used most frequently to adjust the assets for 
    image-based widget layouts and font sizes.

    Parameters:

        widget (Widget):
            The widget object.

        size (Union[int, List, Tuple]):
            A single integer or an iterable of integers

    Returns:

        Union[int, List]:
            An integer or list of integers representing the new size.
    \"\"\"
    BASELINE = 1.33398982438864281
    scaling = widget.tk.call('tk', 'scaling')
    factor = scaling / BASELINE

    if isinstance(size, int):
        return int(size * factor)
    elif isinstance(size, tuple) or isinstance(size, list):
        return [int(x * factor) for x in size]""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/__main__.py": """\"\"\"
    ttkbootstrap demo

    ISSUES:
        - the legacy tk widgets do not update after DateDialog is used.
\"\"\"
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.scrolled import ScrolledText


def setup_demo(master):

    ZEN = \"\"\"Beautiful is better than ugly. 
Explicit is better than implicit. 
Simple is better than complex. 
Complex is better than complicated.
Flat is better than nested. 
Sparse is better than dense.  
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!\"\"\"

    root = ttk.Frame(master, padding=10)
    style = ttk.Style()
    theme_names = style.theme_names()

    theme_selection = ttk.Frame(root, padding=(10, 10, 10, 0))
    theme_selection.pack(fill=X, expand=YES)

    theme_selected = ttk.Label(
        master=theme_selection, text=\"litera\", font=\"-size 24 -weight bold\"
    )
    theme_selected.pack(side=LEFT)

    lbl = ttk.Label(theme_selection, text=\"Select a theme:\")
    theme_cbo = ttk.Combobox(
        master=theme_selection,
        text=style.theme.name,
        values=theme_names,
    )
    theme_cbo.pack(padx=10, side=RIGHT)
    theme_cbo.current(theme_names.index(style.theme.name))
    lbl.pack(side=RIGHT)

    ttk.Separator(root).pack(fill=X, pady=10, padx=10)

    def change_theme(e):
        t = cbo.get()
        style.theme_use(t)
        theme_selected.configure(text=t)
        theme_cbo.selection_clear()
        default.focus_set()

    theme_cbo.bind(\"<<ComboboxSelected>>\", change_theme)

    lframe = ttk.Frame(root, padding=5)
    lframe.pack(side=LEFT, fill=BOTH, expand=YES)

    rframe = ttk.Frame(root, padding=5)
    rframe.pack(side=RIGHT, fill=BOTH, expand=YES)

    color_group = ttk.Labelframe(
        master=lframe, text=\"Theme color options\", padding=10
    )
    color_group.pack(fill=X, side=TOP)

    for color in style.colors:
        cb = ttk.Button(color_group, text=color, bootstyle=color)
        cb.pack(side=LEFT, expand=YES, padx=5, fill=X)

    rb_group = ttk.Labelframe(
        lframe, text=\"Checkbuttons & radiobuttons\", padding=10
    )
    rb_group.pack(fill=X, pady=10, side=TOP)

    check1 = ttk.Checkbutton(rb_group, text=\"selected\")
    check1.pack(side=LEFT, expand=YES, padx=5)
    check1.invoke()

    check2 = ttk.Checkbutton(rb_group, text=\"alternate\")
    check2.pack(side=LEFT, expand=YES, padx=5)

    check4 = ttk.Checkbutton(rb_group, text=\"deselected\")
    check4.pack(side=LEFT, expand=YES, padx=5)
    check4.invoke()
    check4.invoke()

    check3 = ttk.Checkbutton(rb_group, text=\"disabled\", state=DISABLED)
    check3.pack(side=LEFT, expand=YES, padx=5)

    radio1 = ttk.Radiobutton(rb_group, text=\"selected\", value=1)
    radio1.pack(side=LEFT, expand=YES, padx=5)
    radio1.invoke()

    radio2 = ttk.Radiobutton(rb_group, text=\"deselected\", value=2)
    radio2.pack(side=LEFT, expand=YES, padx=5)

    radio3 = ttk.Radiobutton(
        master=rb_group, text=\"disabled\", value=3, state=DISABLED
    )
    radio3.pack(side=LEFT, expand=YES, padx=5)

    ttframe = ttk.Frame(lframe)
    ttframe.pack(pady=5, fill=X, side=TOP)

    table_data = [
        (\"South Island, New Zealand\", 1),
        (\"Paris\", 2),
        (\"Bora Bora\", 3),
        (\"Maui\", 4),
        (\"Tahiti\", 5),
    ]

    tv = ttk.Treeview(master=ttframe, columns=[0, 1], show=HEADINGS, height=5)
    for row in table_data:
        tv.insert(\"\", END, values=row)

    tv.selection_set(\"I001\")
    tv.heading(0, text=\"City\")
    tv.heading(1, text=\"Rank\")
    tv.column(0, width=300)
    tv.column(1, width=70, anchor=CENTER)
    tv.pack(side=LEFT, anchor=NE, fill=X)

    # # notebook with table and text tabs
    nb = ttk.Notebook(ttframe)
    nb.pack(side=LEFT, padx=(10, 0), expand=YES, fill=BOTH)
    nb_text = \"This is a notebook tab.\\nYou can put any widget you want here.\"
    nb.add(ttk.Label(nb, text=nb_text), text=\"Tab 1\", sticky=NW)
    nb.add(
        child=ttk.Label(nb, text=\"A notebook tab.\"), text=\"Tab 2\", sticky=NW
    )
    nb.add(ttk.Frame(nb), text=\"Tab 3\")
    nb.add(ttk.Frame(nb), text=\"Tab 4\")
    nb.add(ttk.Frame(nb), text=\"Tab 5\")

    # text widget
    txt = ScrolledText(master=lframe, height=5, width=50, autohide=True)
    txt.insert(END, ZEN)
    txt.pack(side=LEFT, anchor=NW, pady=5, fill=BOTH, expand=YES)
    lframe_inner = ttk.Frame(lframe)
    lframe_inner.pack(fill=BOTH, expand=YES, padx=10)
    s1 = ttk.Scale(
        master=lframe_inner, orient=HORIZONTAL, value=75, from_=100, to=0
    )
    s1.pack(fill=X, pady=5, expand=YES)

    ttk.Progressbar(
        master=lframe_inner,
        orient=HORIZONTAL,
        value=50,
    ).pack(fill=X, pady=5, expand=YES)

    ttk.Progressbar(
        master=lframe_inner,
        orient=HORIZONTAL,
        value=75,
        bootstyle=(SUCCESS, STRIPED),
    ).pack(fill=X, pady=5, expand=YES)

    m = ttk.Meter(
        master=lframe_inner,
        metersize=150,
        amountused=45,
        subtext=\"meter widget\",
        bootstyle=INFO,
        interactive=True,
    )
    m.pack(pady=10)

    sb = ttk.Scrollbar(
        master=lframe_inner,
        orient=HORIZONTAL,
    )
    sb.set(0.1, 0.9)
    sb.pack(fill=X, pady=5, expand=YES)

    sb = ttk.Scrollbar(
        master=lframe_inner, orient=HORIZONTAL, bootstyle=(DANGER, ROUND)
    )
    sb.set(0.1, 0.9)
    sb.pack(fill=X, pady=5, expand=YES)

    btn_group = ttk.Labelframe(master=rframe, text=\"Buttons\", padding=(10, 5))
    btn_group.pack(fill=X)

    menu = ttk.Menu(root)
    for i, t in enumerate(style.theme_names()):
        menu.add_radiobutton(label=t, value=i)

    default = ttk.Button(master=btn_group, text=\"solid button\")
    default.pack(fill=X, pady=5)
    default.focus_set()

    mb = ttk.Menubutton(
        master=btn_group,
        text=\"solid menubutton\",
        bootstyle=SECONDARY,
        menu=menu,
    )
    mb.pack(fill=X, pady=5)

    cb = ttk.Checkbutton(
        master=btn_group,
        text=\"solid toolbutton\",
        bootstyle=(SUCCESS, TOOLBUTTON),
    )
    cb.invoke()
    cb.pack(fill=X, pady=5)

    ob = ttk.Button(
        master=btn_group,
        text=\"outline button\",
        bootstyle=(INFO, OUTLINE),
        command=lambda: Messagebox.ok(\"You pushed an outline button\"),
    )
    ob.pack(fill=X, pady=5)

    mb = ttk.Menubutton(
        master=btn_group,
        text=\"outline menubutton\",
        bootstyle=(WARNING, OUTLINE),
        menu=menu,
    )
    mb.pack(fill=X, pady=5)

    cb = ttk.Checkbutton(
        master=btn_group,
        text=\"outline toolbutton\",
        bootstyle=(SUCCESS, OUTLINE, TOOLBUTTON),
    )
    cb.pack(fill=X, pady=5)

    lb = ttk.Button(master=btn_group, text=\"link button\", bootstyle=LINK)
    lb.pack(fill=X, pady=5)

    cb1 = ttk.Checkbutton(
        master=btn_group,
        text=\"rounded toggle\",
        bootstyle=(SUCCESS, ROUND, TOGGLE),
    )
    cb1.invoke()
    cb1.pack(fill=X, pady=5)

    cb2 = ttk.Checkbutton(
        master=btn_group, text=\"squared toggle\", bootstyle=(SQUARE, TOGGLE)
    )
    cb2.pack(fill=X, pady=5)
    cb2.invoke()

    input_group = ttk.Labelframe(
        master=rframe, text=\"Other input widgets\", padding=10
    )
    input_group.pack(fill=BOTH, pady=(10, 5), expand=YES)
    entry = ttk.Entry(input_group)
    entry.pack(fill=X)
    entry.insert(END, \"entry widget\")

    password = ttk.Entry(master=input_group, show=\"•\")
    password.pack(fill=X, pady=5)
    password.insert(END, \"password\")

    # spinbox = ttk.Spinbox(master=input_group, from_=0, to=100)
    # spinbox.pack(fill=X)
    # spinbox.set(45)

    # spinbox.insert(END, \"spinbox\")

    cbo = ttk.Combobox(
        master=input_group,
        text=style.theme.name,
        values=theme_names,
        exportselection=False,
    )
    cbo.pack(fill=X, pady=5)
    cbo.current(theme_names.index(style.theme.name))

    de = ttk.DateEntry(input_group)
    de.pack(fill=X)

    return root


if __name__ == \"__main__\":

    app = ttk.Window(\"ttkbootstrap widget demo\")

    bagel = setup_demo(app)
    bagel.pack(fill=BOTH, expand=YES)

    app.mainloop()
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/tooltip.py": """import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import utility


class ToolTip:
    \"\"\"A semi-transparent tooltip popup window that shows text when the
    mouse is hovering over the widget and closes when the mouse is no
    longer hovering over the widget. Clicking a mouse button will also
    close the tooltip.

    ![](../assets/tooltip/tooltip.gif)

    Examples:

        ```python
        import ttkbootstrap as ttk
        from ttkbootstrap.constants import *
        from ttkbootstrap.tooltip import ToolTip

        app = ttk.Window()
        b1 = ttk.Button(app, text=\"default tooltip\")
        b1.pack()
        b2 = ttk.Button(app, text=\"styled tooltip\")
        b2.pack()

        # default tooltip
        ToolTip(b1, text=\"This is the default style\")

        # styled tooltip
        ToolTip(b2, text=\"This is dangerous\", bootstyle=(DANGER, INVERSE))

        app.mainloop()
        ```    
    \"\"\"

    def __init__(
        self,
        widget,
        text=\"widget info\",
        bootstyle=None,
        wraplength=None,
        delay=250,    # milliseconds
        **kwargs,
    ):
        \"\"\"
        Parameters:

            widget (Widget):
                The tooltip window will position over this widget when
                hovering.

            text (str):
                The text to display in the tooltip window.

            bootstyle (str):
                The style to apply to the tooltip label. You can use
                any of the standard ttkbootstrap label styles.

            wraplength (int):
                The width of the tooltip window in screenunits before the
                text is wrapped to the next line. By default, this will be
                a scaled factor of 300.

            **kwargs (Dict):
                Other keyword arguments passed to the `Toplevel` window.
        \"\"\"
        self.widget = widget
        self.text = text
        self.bootstyle = bootstyle
        self.wraplength = wraplength or utility.scale_size(self.widget, 300)
        self.toplevel = None
        self.delay = delay
        self.id = None

        # set keyword arguments
        kwargs[\"overrideredirect\"] = True
        kwargs[\"master\"] = self.widget
        if \"alpha\" not in kwargs:
            kwargs[\"alpha\"] = 0.95
        self.toplevel_kwargs = kwargs

        # create default tooltip style
        ttk.Style().configure(
            style=\"tooltip.TLabel\",
            background=\"#fffddd\",
            foreground=\"#333\",
            bordercolor=\"#888\",
            borderwidth=1,
            darkcolor=\"#fffddd\",
            lightcolor=\"#fffddd\",
            relief=RAISED,
        )

        # event binding
        self.widget.bind(\"<Enter>\", self.enter)
        self.widget.bind(\"<Leave>\", self.leave)
        self.widget.bind(\"<Motion>\", self.move_tip)
        self.widget.bind(\"<ButtonPress>\", self.leave)

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hide_tip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.delay, self.show_tip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def show_tip(self, *_):
        \"\"\"Create a show the tooltip window\"\"\"
        if self.toplevel:
            return
        x = self.widget.winfo_pointerx() + 25
        y = self.widget.winfo_pointery() + 10

        self.toplevel = ttk.Toplevel(position=(x, y), **self.toplevel_kwargs)
        lbl = ttk.Label(
            master=self.toplevel,
            text=self.text,
            justify=LEFT,
            wraplength=self.wraplength,
            padding=10,
        )
        lbl.pack(fill=BOTH, expand=YES)
        if self.bootstyle:
            lbl.configure(bootstyle=self.bootstyle)
        else:
            lbl.configure(style=\"tooltip.TLabel\")

    def move_tip(self, *_):
        \"\"\"Move the tooltip window to the current mouse position within the
        widget.
        \"\"\"
        if self.toplevel:
            x = self.widget.winfo_pointerx() + 25
            y = self.widget.winfo_pointery() + 10
            self.toplevel.geometry(f\"+{x}+{y}\")

    def hide_tip(self, *_):
        \"\"\"Destroy the tooltip window.\"\"\"
        if self.toplevel:
            self.toplevel.destroy()
            self.toplevel = None


if __name__ == \"__main__\":

    app = ttk.Window()

    b1 = ttk.Button(app, text=\"default tooltip\")
    b1.pack(side=LEFT, padx=20, pady=20, fill=X, expand=YES)

    l1 = ttk.Label(app, text=\"styled tooltip\")
    l1.pack(side=LEFT, padx=20, pady=20, fill=X, expand=YES)

    ToolTip(
        b1,
        text=\"This is the default tooltip style\",
    )
    ToolTip(
        l1,
        text=\"Do not touch this label unless you are sure you want to do something dangerous.\",
        bootstyle=\"danger-inverse\",
    )

    app.mainloop()
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/constants.py": """from tkinter.constants import *

DEFAULT = 'default'
DEFAULT_THEME = 'litera'
TTK_CLAM = 'clam'
TTK_ALT = 'alt'
TTK_DEFAULT = 'default'

# meter constants
FULL = 'full'
SEMI = 'semi'

# progressbar constant
DETERMINATE = 'determinate'
INDETERMINATE = 'indeterminate'

# bootstyle colors
PRIMARY = 'primary'
SECONDARY = 'secondary'
SUCCESS = 'success'
DANGER = 'danger'
WARNING = 'warning'
INFO = 'info'
LIGHT = 'light'
DARK = 'dark'

# bootstyle types
OUTLINE = 'outline'
LINK = 'link'
TOGGLE = 'toggle'
INVERSE = 'inverse'
STRIPED = 'striped'
TOOLBUTTON = 'toolbutton'
ROUND = 'round'
SQUARE = 'square'

# treeview constants
TREE = 'tree'
HEADINGS = 'headings'
TREEHEADINGS = 'tree headings'

# state constants
READONLY = 'readonly'""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/dialogs/__init__.py": """from ttkbootstrap.dialogs.dialogs import *""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/dialogs/colordropper.py": """\"\"\"
    NOTE: https://stackoverflow.com/questions/25467288/pils-imagegrab-is-capturing-at-the-wrong-resolution

    !! This widget is not currently supported on Mac OS
\"\"\"
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import colorutils, utility
from PIL import ImageGrab, ImageTk, Image
from collections import namedtuple

ColorChoice = namedtuple('ColorChoice', 'rgb hsl hex')


class ColorDropperDialog:
    \"\"\"A widget that displays an indicator and a zoom window for
    selecting a color on the screen.

    Left-click the mouse button to select a color. The result is 
    stored in the `result` property as a `ColorChoice` tuple which
    contains named fields for rgb, hsl, and hex color models.

    Zoom in and out on the zoom window by using the mouse wheel.

    This widget is implemented for **Windows** and **Linux** only.

    ![](../../assets/dialogs/color-dropper.png)       

    !!! warning \"high resolution displays\"
        This widget may not function properly on high resolution
        displays if you are not using the application in high
        resolution mode. This is enabled automatically on Windows.
    \"\"\"

    def __init__(self):
        self.toplevel: ttk.Toplevel = None
        self.result = ttk.Variable()

    def build_screenshot_canvas(self):
        \"\"\"Build the screenshot canvas\"\"\"
        self.screenshot_canvas = ttk.Canvas(
            self.toplevel, cursor='tcross', autostyle=False)
        self.screenshot_data = ImageGrab.grab()
        self.screenshot_image = ImageTk.PhotoImage(self.screenshot_data)
        self.screenshot_canvas.create_image(
            0, 0, image=self.screenshot_image, anchor=NW)
        self.screenshot_canvas.pack(fill=BOTH, expand=YES)

    def build_zoom_toplevel(self, master):
        \"\"\"Build the toplevel widget that shows the zoomed version of
        the pixels underneath the mouse cursor.\"\"\"
        height = utility.scale_size(self.toplevel, 100)
        width = utility.scale_size(self.toplevel, 100)
        text_xoffset = utility.scale_size(self.toplevel, 50)
        text_yoffset = utility.scale_size(self.toplevel, 50)
        toplevel = ttk.Toplevel(master)
        toplevel.transient(master)
        if self.toplevel.winsys == 'x11':
            toplevel.attributes('-type', 'tooltip')
        else:
            toplevel.overrideredirect(True)
        toplevel.geometry(f'{width}x{height}')
        toplevel.lift()
        self.zoom_canvas = ttk.Canvas(
            toplevel, borderwidth=1, height=self.zoom_height, width=self.zoom_width)
        self.zoom_canvas.create_image(0, 0, tags=['image'], anchor=NW)
        self.zoom_canvas.create_text(
            text_xoffset, text_yoffset, text=\"+\", fill=\"white\", tags=['indicator'])
        self.zoom_canvas.pack(fill=BOTH, expand=YES)
        self.zoom_toplevel = toplevel

    def on_mouse_wheel(self, event: tk.Event):
        \"\"\"Zoom in and out on the image underneath the mouse
        TODO Cross platform testing needed
        \"\"\"
        if self.toplevel.winsys.lower() == 'win32':
            delta = -int(event.delta / 120)
        elif self.toplevel.winsys.lower() == 'aqua':
            delta = -event.delta
        elif event.num == 4:
            delta = -1
        elif event.num == 5:
            delta = 1
        self.zoom_level += delta
        self.on_mouse_motion()

    def on_left_click(self, _):
        \"\"\"Capture the color underneath the mouse cursor and destroy
        the toplevel widget\"\"\"
        # add logic here to capture the image color
        hx = self.get_hover_color()
        hsl = colorutils.color_to_hsl(hx)
        rgb = colorutils.color_to_rgb(hx)
        self.result.set(ColorChoice(rgb, hsl, hx))
        self.toplevel.destroy()
        self.zoom_toplevel.destroy()
        self.toplevel.grab_release()
        return self.result.get()

    def on_right_click(self, _):
        \"\"\"Close the color dropper without saving any color information\"\"\"
        self.zoom_toplevel.destroy()
        self.toplevel.grab_release()
        self.toplevel.destroy()

    def on_mouse_motion(self, event=None):
        \"\"\"Callback for mouse motion\"\"\"
        if event is None:
            x, y = self.toplevel.winfo_pointerxy()
        else:
            x = event.x
            y = event.y
        # move snip window
        self.zoom_toplevel.geometry(
            f'+{x+self.zoom_xoffset}+{y+self.zoom_yoffset}')
        # update the snip image
        bbox = (x-self.zoom_level, y-self.zoom_level,
                x+self.zoom_level+1, y+self.zoom_level+1)
        size = (self.zoom_width, self.zoom_height)
        self.zoom_data = self.screenshot_data.crop(
            bbox).resize(size, Image.BOX)
        self.zoom_image = ImageTk.PhotoImage(self.zoom_data)
        self.zoom_canvas.itemconfig('image', image=self.zoom_image)
        hover_color = self.get_hover_color()
        contrast_color = colorutils.contrast_color(hover_color, 'hex')
        self.zoom_canvas.itemconfig('indicator', fill=contrast_color)

    def get_hover_color(self):
        \"\"\"Get the color that is hovered over by the mouse cursor.\"\"\"
        x1, y1, x2, y2 = self.zoom_canvas.bbox('indicator')
        x = x1 + (x2-x1)//2
        y = y1 + (y2-y2)//2
        r, g, b = self.zoom_data.getpixel((x, y))
        hx = colorutils.color_to_hex((r, g, b))
        return hx

    def show(self):
        \"\"\"Show the toplevel window\"\"\"
        self.toplevel = ttk.Toplevel(alpha=1)
        self.toplevel.wm_attributes('-fullscreen', True)
        self.build_screenshot_canvas()

        # event binding
        self.toplevel.bind(\"<Motion>\", self.on_mouse_motion, \"+\")
        self.toplevel.bind(\"<Button-1>\", self.on_left_click, \"+\")
        self.toplevel.bind(\"<Button-3>\", self.on_right_click, \"+\")

        if self.toplevel.winsys.lower() == 'x11':
            self.toplevel.bind(\"<Button-4>\", self.on_mouse_wheel, \"+\")
            self.toplevel.bind(\"<Button-5>\", self.on_mouse_wheel, \"+\")
        else:
            self.toplevel.bind(\"<MouseWheel>\", self.on_mouse_wheel, \"+\")

        # initial snip setup
        self.zoom_level = 2
        self.zoom_toplevel: ttk.Toplevel = None
        self.zoom_data = None
        self.zoom_image = None
        self.zoom_height = utility.scale_size(self.toplevel, 100)
        self.zoom_width = utility.scale_size(self.toplevel, 100)
        self.zoom_xoffset = utility.scale_size(self.toplevel, 10)
        self.zoom_yoffset = utility.scale_size(self.toplevel, 10)

        self.build_zoom_toplevel(self.toplevel)
        self.toplevel.grab_set()
        self.toplevel.lift('.')
        self.zoom_toplevel.lift(self.toplevel)

        self.on_mouse_motion()
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/dialogs/colorchooser.py": """import ttkbootstrap as ttk
from ttkbootstrap.validation import add_range_validation, add_validation, validator
from ttkbootstrap.constants import *
from tkinter import Frame as tkFrame
from tkinter import Label as tkLabel
from ttkbootstrap import utility
from collections import namedtuple
from ttkbootstrap import colorutils
from ttkbootstrap.colorutils import RGB, HSL, HEX, HUE, SAT, LUM
from PIL import ImageColor
from ttkbootstrap.dialogs.colordropper import ColorDropperDialog
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.localization import MessageCatalog

STD_SHADES = [0.9, 0.8, 0.7, 0.4, 0.3]
STD_COLORS = [
    '#FF0000', '#FFC000', '#FFFF00', '#00B050',
    '#0070C0', '#7030A0', '#FFFFFF', '#000000'
]

ColorValues = namedtuple('ColorValues', 'h s l r g b hex')
ColorChoice = namedtuple('ColorChoice', 'rgb hsl hex')

PEN = '✛'


@validator
def validate_color(event):
    try:
        ImageColor.getrgb(event.postchangetext)
        return True
    except:
        return False


class ColorChooser(ttk.Frame):
    \"\"\"A class which creates a color chooser widget
    
    ![](../../assets/dialogs/querybox-get-color.png)    
    \"\"\"

    def __init__(self, master, initialcolor=None, padding=None):
        super().__init__(master, padding=padding)
        self.tframe = ttk.Frame(self, padding=5)
        self.tframe.pack(fill=X)
        self.bframe = ttk.Frame(self, padding=(5, 0, 5, 5))
        self.bframe.pack(fill=X)

        self.notebook = ttk.Notebook(self.tframe)
        self.notebook.pack(fill=BOTH)

        self.style = ttk.Style.get_instance()
        self.colors = self.style.colors
        self.initialcolor = initialcolor or self.colors.bg

        # color variables
        r, g, b = ImageColor.getrgb(self.initialcolor)
        h, s, l = colorutils.color_to_hsl((r, g, b), RGB)
        hx = colorutils.color_to_hex((r, g, b), RGB)
        
        self.hue = ttk.IntVar(value=h)
        self.sat = ttk.IntVar(value=s)
        self.lum = ttk.IntVar(value=l)
        self.red = ttk.IntVar(value=r)
        self.grn = ttk.IntVar(value=g)
        self.blu = ttk.IntVar(value=b)
        self.hex = ttk.StringVar(value=hx)

        # widget sizes (adjusted by widget scaling)
        self.spectrum_height = utility.scale_size(self, 240)
        self.spectrum_width = utility.scale_size(self, 530) # looks better on Mac OS
        #self.spectrum_width = utility.scale_size(self, 480)
        self.spectrum_point = utility.scale_size(self, 12)

        # build widgets
        spectrum_frame = ttk.Frame(self.notebook)
        self.color_spectrum = self.create_spectrum(spectrum_frame)
        self.color_spectrum.pack(fill=X, side=TOP)
        self.luminance_scale = self.create_luminance_scale(self.tframe)
        self.luminance_scale.pack(fill=X)
        self.notebook.add(spectrum_frame, text=MessageCatalog.translate('Advanced'))

        themed_colors = [self.colors.get(c) for c in self.style.colors]
        self.themed_swatches = self.create_swatches(
            self.notebook, themed_colors)
        self.standard_swatches = self.create_swatches(
            self.notebook, STD_COLORS)
        self.notebook.add(self.themed_swatches, text=MessageCatalog.translate('Themed'))
        self.notebook.add(self.standard_swatches, text=MessageCatalog.translate('Standard'))
        preview_frame = self.create_preview(self.bframe)
        preview_frame.pack(side=LEFT, fill=BOTH, expand=YES, padx=(0, 5))
        self.color_entries = self.create_value_inputs(self.bframe)
        self.color_entries.pack(side=RIGHT)

        self.create_spectrum_indicator()
        self.create_luminance_indicator()

    def create_spectrum(self, master):
        \"\"\"Create the color spectrum canvas\"\"\"
        # canvas and point dimensions
        width = self.spectrum_width
        height = self.spectrum_height
        xf = yf = self.spectrum_point

        # create canvas widget and binding
        canvas = ttk.Canvas(master, width=width, height=height, cursor='tcross')
        canvas.bind(\"<B1-Motion>\", self.on_spectrum_interaction, add=\"+\")
        canvas.bind(\"<Button-1>\", self.on_spectrum_interaction, add=\"+\")

        # add color points
        for x, colorx in enumerate(range(0, width, xf)):
            for y, colory in enumerate(range(0, height, yf)):
                values = self.color_from_coords(colorx, colory)
                fill = values.hex
                bbox = [x*xf, y*yf, (x*xf)+xf, (y*yf)+yf]
                canvas.create_rectangle(*bbox, fill=fill, width=0)
        return canvas

    def create_spectrum_indicator(self):
        \"\"\"Create a square indicator that displays in the position of 
        the selected color\"\"\"
        s = utility.scale_size(self, 10)
        width = utility.scale_size(self, 2)
        values = self.get_variables()
        x1, y1 = self.coords_from_color(values.hex)
        colorutils.contrast_color(values.hex, 'hex')
        tag = ['spectrum-indicator']
        self.color_spectrum.create_rectangle(
            x1, y1, x1+s, y1+s, width=width, tags=[tag])
        self.color_spectrum.tag_lower('spectrum-indicator')

    # widget builder methods
    def create_swatches(self, master, colors):
        \"\"\"Create a grid of color swatches\"\"\"
        boxpadx = 2
        boxpady = 0
        padxtotal = (boxpadx*15)
        boxwidth = int((self.spectrum_width-padxtotal)) / len(STD_COLORS)
        boxheight = int((self.spectrum_height-boxpady) / (len(STD_SHADES)+1))
        container = ttk.Frame(master)

        # create color combinations
        color_rows = [colors]
        lastcol = len(colors)-1
        for l in STD_SHADES:
            lum = int(l*LUM)
            row = []
            for color in colors:
                color = colorutils.update_hsl_value(
                    color=color,
                    lum=lum,
                    inmodel='hex',
                    outmodel='hex'
                )
                row.append(color)
            color_rows.append(row)

        # themed colors - regular colors
        for row in color_rows:
            rowframe = ttk.Frame(container)
            for j, color in enumerate(row):
                swatch = tkFrame(
                    master=rowframe,
                    bg=color,
                    width=boxwidth,
                    height=boxheight,
                    autostyle=False
                )
                swatch.bind('<Button-1>', self.on_press_swatch)
                if j == 0:
                    swatch.pack(side=LEFT, padx=(0, boxpadx))
                elif j == lastcol:
                    swatch.pack(side=LEFT, padx=(boxpadx, 0))
                else:
                    swatch.pack(side=LEFT, padx=boxpadx)
            rowframe.pack(fill=X, expand=YES)

        return container

    def create_preview(self, master):
        \"\"\"Create the preview frame for original and new colors\"\"\"
        nbstyle = self.notebook.cget('style')
        # set the border color to match the notebook border color
        bordercolor = self.style.lookup(nbstyle, 'bordercolor')
        container = ttk.Frame(master)

        # the frame and label for the original color (current)
        old = tkFrame(
            master=container,
            relief=FLAT,
            bd=2,
            highlightthickness=1,
            highlightbackground=bordercolor,
            bg=self.initialcolor,
            autostyle=False
        )
        old.pack(side=LEFT, fill=BOTH, expand=YES, padx=(0, 2))
        contrastfg = colorutils.contrast_color(
            color=self.initialcolor,
            model='hex',
        )
        tkLabel(
            master=old,
            text=MessageCatalog.translate('Current'),
            background=self.initialcolor,
            foreground=contrastfg,
            autostyle=False,
            width=7
        ).pack(anchor=NW)
        
        # the frame and label for the new color
        self.preview = tkFrame(
            master=container,
            relief=FLAT,
            bd=2,
            highlightthickness=1,
            highlightbackground=bordercolor,
            bg=self.initialcolor,
            autostyle=False
        )
        self.preview.pack(side=LEFT, fill=BOTH, expand=YES, padx=(2, 0))
        self.preview_lbl = tkLabel(
            master=self.preview,
            text=MessageCatalog.translate('New'),
            background=self.initialcolor,
            foreground=contrastfg,
            autostyle=False,
            width=7
        )
        self.preview_lbl.pack(anchor=NW)

        return container

    def create_value_inputs(self, master):
        \"\"\"Create color value input widgets\"\"\"
        container = ttk.Frame(master)
        for x in range(4):
            container.columnconfigure(x, weight=1)

        # value labels
        lbl_cnf = {'master': container, 'anchor': E}
        ttk.Label(**lbl_cnf, text=f'''{MessageCatalog.translate('Hue')}:''').grid(row=0, column=0, sticky=E)
        ttk.Label(**lbl_cnf, text=f'''{MessageCatalog.translate('Sat')}:''').grid(row=1, column=0, sticky=E)
        ttk.Label(**lbl_cnf, text=f'''{MessageCatalog.translate('Lum')}:''').grid(row=2, column=0, sticky=E)
        ttk.Label(**lbl_cnf, text=f'''{MessageCatalog.translate('Hex')}:''').grid(row=3, column=0, sticky=E)
        ttk.Label(**lbl_cnf, text=f'''{MessageCatalog.translate('Red')}:''').grid(row=0, column=2, sticky=E)
        ttk.Label(**lbl_cnf, text=f'''{MessageCatalog.translate('Green')}:''').grid(row=1, column=2, sticky=E)
        ttk.Label(**lbl_cnf, text=f'''{MessageCatalog.translate('Blue')}:''').grid(row=2, column=2, sticky=E)

        # value spinners and entry widgets
        rgb_cnf = {'master': container, 'from_': 0, 'to': 255, 'width': 3}
        sl_cnf = {'master': container, 'from_': 0, 'to': 100, 'width': 3}
        hue_cnf = {'master': container, 'from_': 0, 'to': 360, 'width': 3}
        sb_hue = ttk.Spinbox(**hue_cnf, textvariable=self.hue)
        sb_hue.grid(row=0, column=1, padx=4, pady=2, sticky=EW)
        sb_sat = ttk.Spinbox(**sl_cnf, textvariable=self.sat)
        sb_sat.grid(row=1, column=1, padx=4, pady=2, sticky=EW)
        sb_lum = ttk.Spinbox(**sl_cnf, textvariable=self.lum)
        sb_lum.grid(row=2, column=1, padx=4, pady=2, sticky=EW)
        sb_red = ttk.Spinbox(**rgb_cnf, textvariable=self.red)
        sb_red.grid(row=0, column=3, padx=4, pady=2, sticky=EW)
        sb_grn = ttk.Spinbox(**rgb_cnf, textvariable=self.grn)
        sb_grn.grid(row=1, column=3, padx=4, pady=2, sticky=EW)
        sb_blu = ttk.Spinbox(**rgb_cnf, textvariable=self.blu)
        sb_blu.grid(row=2, column=3, padx=4, pady=2, sticky=EW)
        ent_hex = ttk.Entry(container, textvariable=self.hex)
        ent_hex.grid(row=3, column=1, padx=4, columnspan=3, pady=2, sticky=EW)

        # add input validation
        add_validation(ent_hex, validate_color)
        add_range_validation(sb_hue, 0, 360)
        for sb in [sb_sat, sb_lum]:
            add_range_validation(sb, 0, 100)
        for sb in [sb_red, sb_grn, sb_blu]:
            add_range_validation(sb, 0, 255)

        # event binding for updating colors on value change
        for sb in [sb_hue, sb_sat, sb_lum]:
            for sequence in ['<<Increment>>', '<<Decrement>>', '<Return>', '<KP_Enter>']:
                sb.bind(
                    sequence=sequence,
                    func=lambda _, w=sb: self.on_entry_value_change(
                        w, HSL),
                    add=\"+\"
                )
        for sb in [sb_red, sb_grn, sb_blu]:
            for sequence in ['<<Increment>>', '<<Decrement>>', '<Return>', '<KP_Enter>']:
                sb.bind(
                    sequence=sequence,
                    func=lambda _, w=sb: self.on_entry_value_change(
                        w, RGB),
                    add=\"+\"
                )
        for sequence in ['<Return>', '<KP_Enter>']:
            ent_hex.bind(
                sequence=sequence,
                func=lambda _, w=ent_hex: self.on_entry_value_change(
                    w, HEX),
                add=\"+\"
            )  

        return container

    def create_luminance_scale(self, master):
        \"\"\"Create the color luminance canvas\"\"\"
        # widget dimensions
        height = xf = self.spectrum_point
        width = self.spectrum_width

        values = self.get_variables()
        canvas = ttk.Canvas(master, height=height, width=width)

        # add color points to scale
        for x, l in enumerate(range(0, width, xf)):
            lum = l/width*LUM
            fill = colorutils.update_hsl_value(
                color=values.hex,
                lum=lum,
                inmodel='hex',
                outmodel='hex'
            )
            bbox = [x*xf, 0, (x*xf)+xf, height]
            tag = f'color{x}'
            canvas.create_rectangle(*bbox, fill=fill, width=0, tags=[tag])
            canvas.bind(\"<B1-Motion>\", self.on_luminance_interaction, add=\"+\")
            canvas.bind(\"<Button-1>\", self.on_luminance_interaction, add=\"+\")
        return canvas

    def create_luminance_indicator(self):
        \"\"\"Create an indicator that displays in the position of the
        luminance value\"\"\"
        lum = 50
        x1 = int(lum / LUM * self.spectrum_width) - \\
            ((self.spectrum_point - 2)//2)
        y1 = 0
        x2 = x1 + self.spectrum_point
        y2 = self.spectrum_point - 3
        tag = 'luminance-indicator'
        bbox = [x1, y1, x2, y2]
        self.luminance_scale.create_rectangle(
            *bbox, fill='white', outline='black', tags=[tag])
        self.luminance_scale.tag_lower(tag)

    def coords_from_color(self, hexcolor):
        \"\"\"Get the coordinates on the color spectrum from the color 
        value\"\"\"
        h, s, _ = colorutils.color_to_hsl(hexcolor)
        x = (h / HUE) * self.spectrum_width
        y = (1-(s / SAT)) * self.spectrum_height
        return x, y

    def color_from_coords(self, x, y):
        \"\"\"Get the color value from the mouse position in the color 
        spectrum\"\"\"
        HEIGHT = self.spectrum_height
        WIDTH = self.spectrum_width
        h = int(min(HUE, max(0, (HUE/WIDTH) * x)))
        s = int(min(SAT, max(0, SAT - ((SAT/HEIGHT) * y))))
        l = 50
        hx = colorutils.color_to_hex([h, s, l], 'hsl')
        r, g, b = colorutils.color_to_rgb(hx)
        return ColorValues(h, s, l, r, g, b, hx)

    def set_variables(self, h, s, l, r, g, b, hx):
        \"\"\"Update the color value variables\"\"\"
        self.hue.set(h)
        self.sat.set(s)
        self.lum.set(l)
        self.red.set(r)
        self.grn.set(g)
        self.blu.set(b)
        self.hex.set(hx)

    def get_variables(self):
        \"\"\"Get the values of all color models and return a 
        tuple of color values\"\"\"
        h = self.hue.get()
        s = self.sat.get()
        l = self.lum.get()
        r = self.red.get()
        g = self.grn.get()
        b = self.blu.get()
        hx = self.hex.get()
        return ColorValues(h, s, l, r, g, b, hx)

    def update_preview(self):
        \"\"\"Update the color in the preview frame\"\"\"
        hx = self.hex.get()
        fg = colorutils.contrast_color(
            color=hx,
            model='hex',
        )
        self.preview.configure(bg=hx)
        self.preview_lbl.configure(bg=hx, fg=fg)

    def update_luminance_scale(self):
        \"\"\"Update the luminance scale with the change in hue and saturation\"\"\"
        values = self.get_variables()
        width = self.spectrum_width
        xf = self.spectrum_point
        for x, l in enumerate(range(0, width, xf)):
            lum = l/width*LUM
            fill = colorutils.update_hsl_value(
                color=values.hex,
                lum=lum,
                inmodel='hex',
                outmodel='hex'
            )
            tag = f'color{x}'
            self.luminance_scale.itemconfig(tag, fill=fill)

    def update_luminance_indicator(self):
        \"\"\"Update the position of the luminance indicator\"\"\"
        lum = self.lum.get()
        x = int(lum / LUM * self.spectrum_width) - \\
            ((self.spectrum_point - 2)//2)
        self.luminance_scale.moveto('luminance-indicator', x, 0)
        self.luminance_scale.tag_raise('luminance-indicator')

    def update_spectrum_indicator(self):
        \"\"\"Move the spectrum indicator to a new location\"\"\"
        values = self.get_variables()
        x, y = self.coords_from_color(values.hex)
        # move to the new color location
        self.color_spectrum.moveto('spectrum-indicator', x, y)
        self.color_spectrum.tag_raise('spectrum-indicator')
        # adjust the outline color based on contrast of background
        color = colorutils.contrast_color(values.hex, 'hex')
        self.color_spectrum.itemconfig('spectrum-indicator', outline=color)

    # color events
    def sync_color_values(self, model):
        \"\"\"Callback for when a color value changes. A change in one
        value will automatically update the other values so that all 
        color models remain in sync.\"\"\"
        values = self.get_variables()
        if model == HEX:
            hx = values.hex
            r, g, b = colorutils.color_to_rgb(hx)
            h, s, l = colorutils.color_to_hsl(hx)
        elif model == RGB:
            r, g, b = values.r, values.g, values.b
            h, s, l = colorutils.color_to_hsl([r, g, b], 'rgb')
            hx = colorutils.color_to_hex([r, g, b])
        elif model == HSL:
            h, s, l = values.h, values.s, values.l
            r, g, b = colorutils.color_to_rgb([h, s, l], 'hsl')
            hx = colorutils.color_to_hex([h, s, l], 'hsl')
        self.set_variables(h, s, l, r, g, b, hx)
        self.update_preview()
        self.update_luminance_indicator()

    def on_entry_value_change(self, widget: ttk.Spinbox, model):
        \"\"\"Update the widget colors when the color value input is 
        changed\"\"\"
        is_valid = widget.validate()
        if is_valid:
            self.sync_color_values(model)
            self.update_luminance_scale()
            self.update_spectrum_indicator()

    def on_press_swatch(self, event):
        \"\"\"Update the widget colors when a color swatch is clicked.\"\"\"
        button: tkFrame = self.nametowidget(event.widget)
        color = button.cget('background')
        self.hex.set(color)
        self.sync_color_values(HEX)
        self.update_luminance_scale()
        self.update_spectrum_indicator()

    def on_spectrum_interaction(self, event):
        \"\"\"Update the widget colors when the color spectrum canvas is
        pressed\"\"\"
        values = self.color_from_coords(event.x, event.y)
        self.hue.set(values.h)
        self.sat.set(values.s)
        self.lum.set(values.l)
        self.sync_color_values(HSL)
        self.update_luminance_scale()
        self.update_spectrum_indicator()

    def on_luminance_interaction(self, event):
        \"\"\"Update the widget colors when the color luminance scale is
        pressed\"\"\"
        l = max(0, min(LUM, int((event.x / self.spectrum_width) * LUM)))
        self.lum.set(l)
        self.sync_color_values(HSL)


from ttkbootstrap.dialogs import Dialog

class ColorChooserDialog(Dialog):
    \"\"\"A class which displays a color chooser dialog. When a color
    option is selected and the \"OK\" button is pressed, the dialog will
    return a namedtuple that contains the color values for rgb, hsl, and
    hex. These values can be accessed by indexing the tuple or by using
    the named fields.

    ![](../../assets/dialogs/querybox-get-color.png)        
    
    Examples:

        ```python
        >>> cd = ColorChooserDialog()
        >>> cd.show()
        >>> colors = cd.result
        >>> colors.hex
        '#5fb04f'
        >>> colors[2]
        '#5fb04f
        >>> colors.rgb
        (95, 176, 79)
        >>> colors[0]
        (95, 176, 79)
        ```
    \"\"\"

    def __init__(self, parent=None, title=\"Color Chooser\", initialcolor=None):
        title = MessageCatalog.translate(title)
        super().__init__(parent=parent, title=title)
        self.initialcolor = initialcolor
        self.dropper = ColorDropperDialog()
        self.dropper.result.trace_add('write', self.trace_dropper_color)

    def create_body(self, master):
        self.colorchooser = ColorChooser(master, self.initialcolor)
        self.colorchooser.pack(fill=BOTH, expand=YES)

    def create_buttonbox(self, master):
        frame = ttk.Frame(master, padding=(5, 5))
        
        # OK button
        ok = ttk.Button(frame, bootstyle=PRIMARY, width=6, text=MessageCatalog.translate('OK'))
        ok.bind(\"<Return>\", lambda _: ok.invoke())
        ok.configure(command=lambda b=ok: self.on_button_press(b))
        ok.pack(padx=2, side=RIGHT)

        # Cancel button
        cancel = ttk.Button(frame, bootstyle=SECONDARY, width=6, text=MessageCatalog.translate('Cancel'))
        cancel.bind(\"<Return>\", lambda _: cancel.invoke())
        cancel.configure(command=lambda b=cancel: self.on_button_press(b))
        cancel.pack(padx=2, side=RIGHT)

        # color dropper (not supported on Mac OS)
        if self._toplevel.winsys != 'aqua':
            dropper = ttk.Label(frame, text=PEN, font=('-size 16'))
            ToolTip(dropper, MessageCatalog.translate('color dropper')) # add tooltip
            dropper.pack(side=RIGHT, padx=2)
            dropper.bind(\"<Button-1>\", self.on_show_colordropper)
                
        frame.pack(side=BOTTOM, fill=X, anchor=S)

    def on_show_colordropper(self, event):
        self.dropper.show()

    def trace_dropper_color(self, *_):
        values = self.dropper.result.get()
        self.colorchooser.hex.set(values[2])
        self.colorchooser.sync_color_values('hex')

    def on_button_press(self, button):
        if button.cget('text') == 'OK':
            values = self.colorchooser.get_variables()
            self._result = ColorChoice(
                rgb=(values.r, values.g, values.b), 
                hsl=(values.h, values.s, values.l), 
                hex=values.hex
            )
            self._toplevel.destroy()            
        self._toplevel.destroy()            
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/dialogs/dialogs.py": """\"\"\"
    This module contains various base dialog base classes that can be 
    used to create custom dialogs for the end user. 

    These classes serve as the basis for the pre-defined static helper
    methods in the `Messagebox`, and `Querybox` container classes.
\"\"\"

import calendar
import textwrap
import locale
from datetime import datetime
from tkinter import font
import ttkbootstrap as ttk
from ttkbootstrap import utility
from ttkbootstrap.icons import Icon
from ttkbootstrap.constants import *
from tkinter import BaseWidget
from ttkbootstrap.localization import MessageCatalog


class Dialog(BaseWidget):
    \"\"\"A simple dialog base class.\"\"\"

    def __init__(self, parent=None, title=\"\", alert=False):
        \"\"\"
        Parameters:

            parent (Widget):
                Makes the window the logical parent of the message box.
                The messagebox is displayed on top of its parent window.

            title (str):
                The string displayed as the title of the message box.
                This option is ignored on Mac OS X, where platform
                guidelines forbid the use of a title on this kind of
                dialog.

            alert (bool):
                Ring the display's bell when the dialog is shown.
        \"\"\"
        BaseWidget._setup(self, parent, {})
        self._winsys = self.master.tk.call(\"tk\", \"windowingsystem\")
        self._parent = parent
        self._toplevel = None
        self._title = title or \" \"
        self._result = None
        self._alert = alert
        self._initial_focus = None

    def _locate(self):
        toplevel = self._toplevel
        if self._parent is None:
            master = toplevel.master
        else:
            master = self._parent
        x = master.winfo_rootx()
        y = master.winfo_rooty()
        toplevel.geometry(f\"+{x}+{y}\")

    def show(self, position=None):
        \"\"\"Show the popup dialog
        Parameters:

            position: Tuple[int, int]
                The x and y coordinates used to position the dialog. By
                default the dialog will anchor at the NW corner of the
                parent window.
        \"\"\"
        self._result = None
        self.build()

        if position is None:
            self._locate()
        else:
            try:
                x, y = position
                self._toplevel.geometry(f'+{x}+{y}')
            except:
                self._locate()

        self._toplevel.deiconify()
        if self._alert:
            self._toplevel.bell()

        if self._initial_focus:
            self._initial_focus.focus_force()

        self._toplevel.grab_set()
        self._toplevel.wait_window()

    def create_body(self, master):
        \"\"\"Create the dialog body.

        This method should be overridden and is called by the `build`
        method. Set the `self._initial_focus` for the widget that
        should receive the initial focus.

        Parameters:

            master (Widget):
                The parent widget.
        \"\"\"
        raise NotImplementedError

    def create_buttonbox(self, master):
        \"\"\"Create the dialog button box.

        This method should be overridden and is called by the `build`
        method. Set the `self._initial_focus` for the button that
        should receive the intial focus.

        Parameters:

            master (Widget):
                The parent widget.
        \"\"\"
        raise NotImplementedError

    def build(self):
        \"\"\"Build the dialog from settings\"\"\"

        # setup toplevel based on widowing system
        if self._winsys == \"win32\":
            self._toplevel = ttk.Toplevel(
                transient=self.master,
                title=self._title,
                resizable=(0, 0),
                minsize=(250, 15),
                iconify=True,
            )
        else:
            self._toplevel = ttk.Toplevel(
                transient=self.master,
                title=self._title,
                resizable=(0, 0),
                windowtype=\"dialog\",
                iconify=True,
            )

        self._toplevel.withdraw()  # reset the iconify state

        # bind <Escape> event to window close
        self._toplevel.bind(\"<Escape>\", lambda _: self._toplevel.destroy())

        # set position of popup from parent window
        # self._locate()

        # create widgets
        self.create_body(self._toplevel)
        self.create_buttonbox(self._toplevel)

        # update the window before showing
        self._toplevel.update_idletasks()

    @property
    def result(self):
        \"\"\"Returns the result of the dialog.\"\"\"
        return self._result


class MessageDialog(Dialog):
    \"\"\"A simple modal dialog class that can be used to build simple
    message dialogs.

    Displays a message and a set of buttons. Each of the buttons in the
    message window is identified by a unique symbolic name. After the
    message window is popped up, the message box awaits for the user to
    select one of the buttons. Then it returns the symbolic name of the
    selected button. Use a `Toplevel` widget for more advanced modal
    dialog designs.
    \"\"\"

    def __init__(
        self,
        message,
        title=\" \",
        buttons=None,
        command=None,
        width=50,
        parent=None,
        alert=False,
        default=None,
        padding=(20, 20),
        icon=None,
        **kwargs,
    ):
        \"\"\"
        Parameters:

            message (str):
                A message to display in the message box.

            title (str):
                The string displayed as the title of the message box.
                This option is ignored on Mac OS X, where platform
                guidelines forbid the use of a title on this kind of
                dialog.

            buttons (List[str]):
                A list of buttons to appear at the bottom of the popup
                messagebox. The buttons can be a list of strings which
                will define the symbolic name and the button text.
                `['OK', 'Cancel']`. Alternatively, you can assign a
                bootstyle to each button by using the colon to separate the
                button text and the bootstyle. If no colon is found, then
                the style is set to 'primary' by default.
                `['OK:success','Cancel:danger']`.

            command (Tuple[Callable, str]):
                The function to invoke when the user closes the dialog.
                The actual command is a tuple that consists of the
                function to call and the symbolic name of the button that
                closes the dialog.

            width (int):
                The maximum number of characters per line in the message.
                If the text stretches beyond the limit, the line will break
                at the word.

            parent (Widget):
                Makes the window the logical parent of the message box.
                The messagebox is displayed on top of its parent window.

            alert (bool):
                Ring the display's bell when the dialog is shown.

            default (str):
                The symbolic name of the default button. The default
                button is invoked when the the <Return> key is pressed.
                If no default is provided, the right-most button in the
                button list will be set as the default.,

            padding  (Union[int, Tuple[int]]):
                The amount of space between the border and the widget
                contents.

            icon (str):
                An image path, path-like object or image data to be
                displayed to the left of the text.

            **kwargs (Dict):
                Other optional keyword arguments.

        Example:

            ```python
            root = tk.Tk()

            md = MessageDialog(\"Displays a message with buttons.\")
            md.show()
            ```
        \"\"\"
        super().__init__(parent, title, alert)
        self._message = message
        self._command = command
        self._width = width
        self._alert = alert
        self._default = (default,)
        self._padding = padding
        self._icon = icon
        self._localize = kwargs.get(\"localize\")

        if buttons is None:
            self._buttons = [
                f\"{MessageCatalog.translate('Cancel')}:secondary\",
                f\"{MessageCatalog.translate('OK')}:primary\",
            ]
        else:
            self._buttons = buttons

    def create_body(self, master):
        \"\"\"Overrides the parent method; adds the message section.\"\"\"
        container = ttk.Frame(master, padding=self._padding)
        if self._icon:
            try:
                # assume this is image data
                self._img = ttk.PhotoImage(data=self._icon)
                icon_lbl = ttk.Label(container, image=self._img)
                icon_lbl.pack(side=LEFT, padx=5)
            except:
                try:
                    # assume this is a file path
                    self._img = ttk.PhotoImage(file=self._icon)
                    icon_lbl = ttk.Label(container, image=self._img)
                    icon_lbl.pack(side=LEFT, padx=5)
                except:
                    # icon is neither data nor a valid file path
                    print(\"MessageDialog icon is invalid\")

        if self._message:
            for msg in self._message.split(\"\\n\"):
                message = \"\\n\".join(textwrap.wrap(msg, width=self._width))
                message_label = ttk.Label(container, text=message)
                message_label.pack(pady=(0, 3), fill=X, anchor=N)
        container.pack(fill=X, expand=True)

    def create_buttonbox(self, master):
        \"\"\"Overrides the parent method; adds the message buttonbox\"\"\"
        frame = ttk.Frame(master, padding=(5, 5))

        button_list = []

        for i, button in enumerate(self._buttons[::-1]):
            cnf = button.split(\":\")
            if len(cnf) == 2:
                text, bootstyle = cnf
            else:
                text = cnf[0]
                bootstyle = \"secondary\"

            if self._localize == True:
                text = MessageCatalog.translate(text)

            btn = ttk.Button(frame, bootstyle=bootstyle, text=text)
            btn.configure(command=lambda b=btn: self.on_button_press(b))
            btn.pack(padx=2, side=RIGHT)
            btn.lower()  # set focus traversal left-to-right
            button_list.append(btn)

            if self._default is not None and text == self._default:
                self._initial_focus = btn
            elif self._default is None and i == 0:
                self._initial_focus = btn

        # bind default button to return key press and set focus
        self._toplevel.bind(\"<Return>\", lambda _, b=btn: b.invoke())
        self._toplevel.bind(\"<KP_Enter>\", lambda _, b=btn: b.invoke())

        ttk.Separator(self._toplevel).pack(fill=X)
        frame.pack(side=BOTTOM, fill=X, anchor=S)

        if not self._initial_focus:
            self._initial_focus = button_list[0]

    def on_button_press(self, button):
        \"\"\"Save result, destroy the toplevel, and execute command.\"\"\"
        self._result = button[\"text\"]
        command = self._command
        if command is not None:
            command()
        self._toplevel.destroy()

    def show(self, position=None):
        \"\"\"Create and display the popup messagebox.\"\"\"
        super().show(position)


class QueryDialog(Dialog):
    \"\"\"A simple modal dialog class that can be used to build simple
    data input dialogs. Displays a prompt, and input box, and a set of
    buttons. Additional data manipulation can be performed on the
    user input post-hoc by overriding the `apply` method.

    Use a `Toplevel` widget for more advanced modal dialog designs.
    \"\"\"

    def __init__(
        self,
        prompt,
        title=\" \",
        initialvalue=\"\",
        minvalue=None,
        maxvalue=None,
        width=65,
        datatype=str,
        padding=(20, 20),
        parent=None,
    ):
        \"\"\"
        Parameters:

            prompt (str):
                A message to display in the message box above the entry
                widget.

            title (str):
                The string displayed as the title of the message box.
                This option is ignored on Mac OS X, where platform
                guidelines forbid the use of a title on this kind of
                dialog.

            initialvalue (Any):
                The initial value in the entry widget.

            minvalue (Any):
                The minimum allowed value. Only valid for int and float
                data types.

            maxvalue (Any):
                The maximum allowed value. Only valid for int and float
                data types.

            width (int):
                The maximum number of characters per line in the
                message. If the text stretches beyond the limit, the
                line will break at the word.

            parent (Widget):
                Makes the window the logical parent of the message box.
                The messagebox is displayed on top of its parent
                window.

            padding (Union[int, Tuple[int]]):
                The amount of space between the border and the widget
                contents.

            datatype (Union[int, str, float]):
                The data type used to validate the entry value.
        \"\"\"
        super().__init__(parent, title)
        self._prompt = prompt
        self._initialvalue = initialvalue
        self._minvalue = minvalue
        self._maxvalue = maxvalue
        self._width = width
        self._datatype = datatype
        self._padding = padding
        self._result = None

    def create_body(self, master):
        \"\"\"Overrides the parent method; adds the message and input
        section.\"\"\"
        frame = ttk.Frame(master, padding=self._padding)
        if self._prompt:
            for p in self._prompt.split(\"\\n\"):
                prompt = \"\\n\".join(textwrap.wrap(p, width=self._width))
                prompt_label = ttk.Label(frame, text=prompt)
                prompt_label.pack(pady=(0, 5), fill=X, anchor=N)

        entry = ttk.Entry(master=frame)
        entry.insert(END, self._initialvalue)
        entry.pack(pady=(0, 5), fill=X)
        entry.bind(\"<Return>\", self.on_submit)
        entry.bind(\"<KP_Enter>\", self.on_submit)
        entry.bind(\"<Escape>\", self.on_cancel)
        frame.pack(fill=X, expand=True)
        self._initial_focus = entry

    def create_buttonbox(self, master):
        \"\"\"Overrides the parent method; adds the message buttonbox\"\"\"
        frame = ttk.Frame(master, padding=(5, 10))

        submit = ttk.Button(
            master=frame,
            bootstyle=\"primary\",
            text=MessageCatalog.translate(\"Submit\"),
            command=self.on_submit,
        )
        submit.pack(padx=5, side=RIGHT)
        submit.lower()  # set focus traversal left-to-right

        cancel = ttk.Button(
            master=frame,
            bootstyle=\"secondary\",
            text=MessageCatalog.translate(\"Cancel\"),
            command=self.on_cancel,
        )
        cancel.pack(padx=5, side=RIGHT)
        cancel.lower()  # set focus traversal left-to-right

        ttk.Separator(self._toplevel).pack(fill=X)
        frame.pack(side=BOTTOM, fill=X, anchor=S)

    def on_submit(self, *_):
        \"\"\"Save result, destroy the toplevel, and apply any post-hoc
        data manipulations.\"\"\"
        self._result = self._initial_focus.get()
        valid_result = self.validate()
        if not valid_result:
            return  # keep toplevel open for valid response
        self._toplevel.destroy()
        self.apply()

    def on_cancel(self, *_):
        \"\"\"Close the toplevel and return empty.\"\"\"
        self._toplevel.destroy()
        return

    def validate(self):
        \"\"\"Validate the data

        This method is called automatically to validate the data before
        the dialog is destroyed. Can be subclassed and overridden.
        \"\"\"
        # no default checks required for string data types
        if self._datatype not in [float, int, complex]:
            return True

        # convert result to appropriate data type
        try:
            self._result = self._datatype(self._result)
        except ValueError:
            msg = MessageCatalog.translate(\"Should be of data type\")
            Messagebox.ok(
                message=f\"{msg} `{self._datatype}`\",
                title=MessageCatalog.translate(\"Invalid data type\"),
                parent=self._toplevel
            )
            return False

        # max value range
        if self._maxvalue is not None:
            if self._result > self._maxvalue:
                msg = MessageCatalog.translate(\"Number cannot be greater than\")
                Messagebox.ok(
                    message=f\"{msg} {self._maxvalue}\",
                    title=MessageCatalog.translate(\"Out of range\"),
                    parent=self._toplevel
                )
                return False

        # min value range
        if self._minvalue is not None:
            if self._result < self._minvalue:
                msg = MessageCatalog.translate(\"Number cannot be less than\")
                Messagebox.ok(
                    message=f\"{msg} {self._minvalue}\",
                    title=MessageCatalog.translate(\"Out of range\"),
                    parent=self._toplevel
                )
                return False

        # valid result
        return True

    def apply(self):
        \"\"\"Process the data.

        This method is called automatically to process the data after
        the dialog is destroyed. By default, it does nothing.
        \"\"\"
        pass  # override


class DatePickerDialog:
    \"\"\"A dialog that displays a calendar popup and returns the
    selected date as a datetime object.

    The current date is displayed by default unless the `startdate`
    parameter is provided.

    The month can be changed by clicking the chevrons to the left
    and right of the month-year title.

    Left-click the arrow to move the calendar by one month.
    Right-click the arrow to move the calendar by one year.
    Right-click the title to reset the calendar to the start date.

    The starting weekday can be changed with the `firstweekday`
    parameter for geographies that do not start the calendar on
    Sunday, which is the default.

    The widget grabs focus and all screen events until released.
    If you want to cancel a date selection, click the 'X' button
    at the top-right corner of the widget.

    The bootstyle api may be used to change the style of the widget.
    The available colors include -> primary, secondary, success,
    info, warning, danger, light, dark.

    ![](../../assets/dialogs/date-picker-dialog.png)

    \"\"\"

    locale.setlocale(locale.LC_ALL, locale.setlocale(locale.LC_TIME, \"\"))

    def __init__(
        self,
        parent=None,
        title=\" \",
        firstweekday=6,
        startdate=None,
        bootstyle=PRIMARY,
    ):
        \"\"\"
        Parameters:

            parent (Widget):
                The parent widget; the popup will appear to the
                bottom-right of the parent widget. If no parent is
                provided, the widget is centered on the screen.

            title (str):
                The text that appears on the titlebar.

            firstweekday (int):
                Specifies the first day of the week. 0=Monday,
                1=Tuesday, etc...

            startdate (datetime):
                The date to be in focus when the widget is
                displayed.

            bootstyle (str):
                The following colors can be used to change the color of
                the title and hover / pressed color -> primary,
                secondary, info, warning, success, danger, light, dark.
        \"\"\"
        self.parent = parent
        self.root = ttk.Toplevel(
            title=title,
            transient=self.parent,
            resizable=(False, False),
            topmost=True,
            minsize=(226, 1),
            iconify=True,
        )
        self.firstweekday = firstweekday
        self.startdate = startdate or datetime.today().date()
        self.bootstyle = bootstyle or PRIMARY

        self.date_selected = self.startdate
        self.date = startdate or self.date_selected
        self.calendar = calendar.Calendar(firstweekday=firstweekday)

        self.titlevar = ttk.StringVar()
        self.datevar = ttk.IntVar()

        self._setup_calendar()
        self.root.grab_set()
        self.root.wait_window()

    def _setup_calendar(self):
        \"\"\"Setup the calendar widget\"\"\"
        # create the widget containers
        self.frm_calendar = ttk.Frame(
            master=self.root, padding=0, borderwidth=0, relief=FLAT
        )
        self.frm_calendar.pack(fill=BOTH, expand=YES)
        self.frm_title = ttk.Frame(self.frm_calendar, padding=(3, 3))
        self.frm_title.pack(fill=X)
        self.frm_header = ttk.Frame(self.frm_calendar, bootstyle=SECONDARY)
        self.frm_header.pack(fill=X)

        # setup the toplevel widget
        self.root.withdraw()  # reset the iconify state
        self.frm_calendar.update_idletasks()  # actualize geometry

        # create visual components
        self._draw_titlebar()
        self._draw_calendar()

        # make toplevel visible
        self._set_window_position()
        self.root.deiconify()

    def _update_widget_bootstyle(self):
        self.frm_title.configure(bootstyle=self.bootstyle)
        self.title.configure(bootstyle=f\"{self.bootstyle}-inverse\")
        self.prev_period.configure(style=f\"Chevron.{self.bootstyle}.TButton\")
        self.next_period.configure(style=f\"Chevron.{self.bootstyle}.TButton\")

    def _draw_calendar(self):
        self._update_widget_bootstyle()
        self._set_title()
        self._current_month_days()
        self.frm_dates = ttk.Frame(self.frm_calendar)
        self.frm_dates.pack(fill=BOTH, expand=YES)

        for row, weekday_list in enumerate(self.monthdays):
            for col, day in enumerate(weekday_list):
                self.frm_dates.columnconfigure(col, weight=1)
                if day == 0:
                    ttk.Label(
                        master=self.frm_dates,
                        text=self.monthdates[row][col].day,
                        anchor=CENTER,
                        padding=5,
                        bootstyle=SECONDARY,
                    ).grid(row=row, column=col, sticky=NSEW)
                else:
                    if all(
                        [
                            day == self.date_selected.day,
                            self.date.month == self.date_selected.month,
                            self.date.year == self.date_selected.year,
                        ]
                    ):
                        day_style = \"secondary-toolbutton\"
                    else:
                        day_style = f\"{self.bootstyle}-calendar\"

                    def selected(x=row, y=col):
                        self._on_date_selected(x, y)

                    btn = ttk.Radiobutton(
                        master=self.frm_dates,
                        variable=self.datevar,
                        value=day,
                        text=day,
                        bootstyle=day_style,
                        padding=5,
                        command=selected,
                    )
                    btn.grid(row=row, column=col, sticky=NSEW)

    def _draw_titlebar(self):
        \"\"\"Draw the calendar title bar which includes the month title
        and the buttons that increment and decrement the selected
        month.

        In addition to the previous and next MONTH commands that are
        assigned to the button press, a \"right-click\" event is assigned
        to each button that causes the calendar to move to the previous
        and next YEAR.
        \"\"\"
        # create and pack the title and action buttons
        self.prev_period = ttk.Button(
            master=self.frm_title, text=\"«\", command=self.on_prev_month
        )
        self.prev_period.pack(side=LEFT)

        self.title = ttk.Label(
            master=self.frm_title,
            textvariable=self.titlevar,
            anchor=CENTER,
            font=\"-weight bold\",
        )
        self.title.pack(side=LEFT, fill=X, expand=YES)

        self.next_period = ttk.Button(
            master=self.frm_title,
            text=\"»\",
            command=self.on_next_month,
        )
        self.next_period.pack(side=LEFT)

        # bind \"year\" callbacks to action buttons
        self.prev_period.bind(\"<Button-3>\", self.on_prev_year, \"+\")
        self.next_period.bind(\"<Button-3>\", self.on_next_year, \"+\")
        self.title.bind(\"<Button-1>\", self.on_reset_date)

        # create and pack days of the week header
        for col in self._header_columns():
            ttk.Label(
                master=self.frm_header,
                text=col,
                anchor=CENTER,
                padding=5,
                bootstyle=(SECONDARY, INVERSE),
            ).pack(side=LEFT, fill=X, expand=YES)

    def _set_title(self):
        _titledate = f'{self.date.strftime(\"%B %Y\")}'
        self.titlevar.set(value=_titledate.capitalize())

    def _current_month_days(self):
        \"\"\"Fetch the day numbers and dates for all days in the current
        month. `monthdays` is a list of days as integers, and
        `monthdates` is a list of `datetime` objects.
        \"\"\"
        self.monthdays = self.calendar.monthdayscalendar(
            year=self.date.year, month=self.date.month
        )
        self.monthdates = self.calendar.monthdatescalendar(
            year=self.date.year, month=self.date.month
        )

    def _header_columns(self):
        \"\"\"Create and return a list of weekdays to be used as a header
        in the calendar. The order of the weekdays is based on the
        `firstweekday` property.

        Returns:

            List[str]:
                A list of weekday column names for the calendar header.
        \"\"\"
        weekdays = [
            MessageCatalog.translate(\"Mo\"),
            MessageCatalog.translate(\"Tu\"),
            MessageCatalog.translate(\"We\"),
            MessageCatalog.translate(\"Th\"),
            MessageCatalog.translate(\"Fr\"),
            MessageCatalog.translate(\"Sa\"),
            MessageCatalog.translate(\"Su\"),
        ]
        header = weekdays[self.firstweekday :] + weekdays[: self.firstweekday]
        return header

    def _on_date_selected(self, row, col):
        \"\"\"Callback for selecting a date.

        An index is assigned to each date button that corresponds to
        the dates in the `monthdates` matrix. When the user clicks a
        button to select a date, the index from this button is used
        to lookup the date value of the button based on the row and
        column index reference. This value is saved in the
        `date_selected` property and the `Toplevel` is destroyed.

        Parameters:

            index (Tuple[int, int]):
                A row and column index of the date selected; to be
                found in the `monthdates` matrix.

        Returns:

            datetime:
                The date selected
        \"\"\"
        self.date_selected = self.monthdates[row][col]
        self.root.destroy()

    def _selection_callback(func):
        \"\"\"Calls the decorated `func` and redraws the calendar.\"\"\"

        def inner(self, *args):
            func(self, *args)
            self.frm_dates.destroy()
            self._draw_calendar()

        return inner

    @_selection_callback
    def on_next_month(self):
        \"\"\"Increment the calendar data to the next month\"\"\"
        year, month = self._nextmonth(self.date.year, self.date.month)
        self.date = datetime(year=year, month=month, day=1).date()

    @_selection_callback
    def on_next_year(self, *_):
        \"\"\"Increment the calendar data to the next year\"\"\"
        year = self.date.year + 1
        month = self.date.month
        self.date = datetime(year=year, month=month, day=1).date()

    @_selection_callback
    def on_prev_month(self):
        \"\"\"Decrement the calendar to the previous year\"\"\"
        year, month = self._prevmonth(self.date.year, self.date.month)
        self.date = datetime(year=year, month=month, day=1).date()

    @_selection_callback
    def on_prev_year(self, *_):
        year = self.date.year - 1
        month = self.date.month
        self.date = datetime(year=year, month=month, day=1).date()

    @_selection_callback
    def on_reset_date(self, *_):
        \"\"\"Set the calendar to the start date\"\"\"
        self.date = self.startdate

    def _set_window_position(self):
        \"\"\"Move the window the to bottom-right of the parent widget, or
        the top-left corner of the master window if no parent is 
        provided.
        \"\"\"
        if self.parent:
            xpos = self.parent.winfo_rootx() + self.parent.winfo_width()
            ypos = self.parent.winfo_rooty() + self.parent.winfo_height()
            self.root.geometry(f\"+{xpos}+{ypos}\")
        else:
            xpos = self.root.master.winfo_rootx()
            ypos = self.root.master.winfo_rooty()
            self.root.geometry(f\"+{xpos}+{ypos}\")

    @staticmethod
    def _nextmonth(year, month):
        if month == 12:
            return year + 1, 1
        else:
            return year, month + 1

    @staticmethod
    def _prevmonth(year, month):
        if month == 1:
            return year - 1, 12
        else:
            return year, month - 1


class FontDialog(Dialog):

    \"\"\"A dialog that displays a variety of options for choosing a font.

    This dialog constructs and returns a `Font` object based on the
    options selected by the user. The initial font is based on OS
    settings and will vary.

    The font object is returned when the **Ok** button is pressed and
    can be passed to any widget that accepts a _font_ configuration
    option.

    ![](../../assets/dialogs/querybox-get-font.png)
    \"\"\"

    def __init__(self, title=\"Font Selector\", parent=None):
        title = MessageCatalog.translate(title)
        super().__init__(parent=parent, title=title)
        self._style = ttk.Style()
        self._default = font.nametofont(\"TkDefaultFont\")
        self._actual = self._default.actual()
        self._size = ttk.Variable(value=self._actual[\"size\"])
        self._family = ttk.Variable(value=self._actual[\"family\"])
        self._slant = ttk.Variable(value=self._actual[\"slant\"])
        self._weight = ttk.Variable(value=self._actual[\"weight\"])
        self._overstrike = ttk.Variable(value=self._actual[\"overstrike\"])
        self._underline = ttk.Variable(value=self._actual[\"underline\"])
        self._preview_font = font.Font()
        self._slant.trace_add(\"write\", self._update_font_preview)
        self._weight.trace_add(\"write\", self._update_font_preview)
        self._overstrike.trace_add(\"write\", self._update_font_preview)
        self._underline.trace_add(\"write\", self._update_font_preview)

        _headingfont = font.nametofont(\"TkHeadingFont\")
        _headingfont.configure(weight=\"bold\")

        self._update_font_preview()
        self._families = set([self._family.get()])
        for f in font.families():
            if all([f, not f.startswith(\"@\"), \"emoji\" not in f.lower()]):
                self._families.add(f)

    def create_body(self, master):
        width = utility.scale_size(master, 600)
        height = utility.scale_size(master, 500)
        self._toplevel.geometry(f\"{width}x{height}\")

        family_size_frame = ttk.Frame(master, padding=10)
        family_size_frame.pack(fill=X, anchor=N)
        self._initial_focus = self._font_families_selector(family_size_frame)
        self._font_size_selector(family_size_frame)
        self._font_options_selectors(master, padding=10)
        self._font_preview(master, padding=10)

    def create_buttonbox(self, master):
        container = ttk.Frame(master, padding=(5, 10))
        container.pack(fill=X)

        ok_btn = ttk.Button(
            master=container,
            bootstyle=\"primary\",
            text=MessageCatalog.translate(\"OK\"),
            command=self._on_submit,
        )
        ok_btn.pack(side=RIGHT, padx=5)
        ok_btn.bind(\"<Return>\", lambda _: ok_btn.invoke())

        cancel_btn = ttk.Button(
            master=container,
            bootstyle=\"secondary\",
            text=MessageCatalog.translate(\"Cancel\"),
            command=self._on_cancel,
        )
        cancel_btn.pack(side=RIGHT, padx=5)
        cancel_btn.bind(\"<Return>\", lambda _: cancel_btn.invoke())

    def _font_families_selector(self, master):
        container = ttk.Frame(master)
        container.pack(fill=BOTH, expand=YES, side=LEFT)

        header = ttk.Label(
            container,
            text=MessageCatalog.translate(\"Family\"),
            font=\"TkHeadingFont\",
        )
        header.pack(fill=X, pady=(0, 2), anchor=N)

        listbox = ttk.Treeview(
            master=container,
            height=5,
            show=\"\",
            columns=[0],
        )
        listbox.column(0, width=utility.scale_size(listbox, 250))
        listbox.pack(side=LEFT, fill=BOTH, expand=YES)

        listbox_vbar = ttk.Scrollbar(
            container,
            command=listbox.yview,
            orient=VERTICAL,
            bootstyle=\"rounded\",
        )
        listbox_vbar.pack(side=RIGHT, fill=Y)
        listbox.configure(yscrollcommand=listbox_vbar.set)

        for f in self._families:
            listbox.insert(\"\", iid=f, index=END, tags=[f], values=[f])
            listbox.tag_configure(f, font=(f, self._size.get()))

        iid = self._family.get()
        listbox.selection_set(iid)  # select default value
        listbox.see(iid)  # ensure default is visible
        listbox.bind(
            \"<<TreeviewSelect>>\", lambda e: self._on_select_font_family(e)
        )
        return listbox

    def _font_size_selector(self, master):
        container = ttk.Frame(master)
        container.pack(side=LEFT, fill=Y, padx=(10, 0))

        header = ttk.Label(
            container,
            text=MessageCatalog.translate(\"Size\"),
            font=\"TkHeadingFont\",
        )
        header.pack(fill=X, pady=(0, 2), anchor=N)

        sizes_listbox = ttk.Treeview(container, height=7, columns=[0], show=\"\")
        sizes_listbox.column(0, width=utility.scale_size(sizes_listbox, 24))

        sizes = [*range(8, 13), *range(13, 30, 2), 36, 48, 72]
        for s in sizes:
            sizes_listbox.insert(\"\", iid=s, index=END, values=[s])

        iid = self._size.get()
        sizes_listbox.selection_set(iid)
        sizes_listbox.see(iid)
        sizes_listbox.bind(
            \"<<TreeviewSelect>>\", lambda e: self._on_select_font_size(e)
        )

        sizes_listbox_vbar = ttk.Scrollbar(
            master=container,
            orient=VERTICAL,
            command=sizes_listbox.yview,
            bootstyle=\"round\",
        )
        sizes_listbox.configure(yscrollcommand=sizes_listbox_vbar.set)
        sizes_listbox.pack(side=LEFT, fill=Y, expand=YES, anchor=N)
        sizes_listbox_vbar.pack(side=LEFT, fill=Y, expand=YES)

    def _font_options_selectors(self, master, padding: int):
        container = ttk.Frame(master, padding=padding)
        container.pack(fill=X, padx=2, pady=2, anchor=N)

        weight_lframe = ttk.Labelframe(
            container, text=MessageCatalog.translate(\"Weight\"), padding=5
        )
        weight_lframe.pack(side=LEFT, fill=X, expand=YES)
        opt_normal = ttk.Radiobutton(
            master=weight_lframe,
            text=MessageCatalog.translate(\"normal\"),
            value=\"normal\",
            variable=self._weight,
        )
        opt_normal.invoke()
        opt_normal.pack(side=LEFT, padx=5, pady=5)
        opt_bold = ttk.Radiobutton(
            master=weight_lframe,
            text=MessageCatalog.translate(\"bold\"),
            value=\"bold\",
            variable=self._weight,
        )
        opt_bold.pack(side=LEFT, padx=5, pady=5)

        slant_lframe = ttk.Labelframe(
            container, text=MessageCatalog.translate(\"Slant\"), padding=5
        )
        slant_lframe.pack(side=LEFT, fill=X, padx=10, expand=YES)
        opt_roman = ttk.Radiobutton(
            master=slant_lframe,
            text=MessageCatalog.translate(\"roman\"),
            value=\"roman\",
            variable=self._slant,
        )
        opt_roman.invoke()
        opt_roman.pack(side=LEFT, padx=5, pady=5)
        opt_italic = ttk.Radiobutton(
            master=slant_lframe,
            text=MessageCatalog.translate(\"italic\"),
            value=\"italic\",
            variable=self._slant,
        )
        opt_italic.pack(side=LEFT, padx=5, pady=5)

        effects_lframe = ttk.Labelframe(
            container, text=MessageCatalog.translate(\"Effects\"), padding=5
        )
        effects_lframe.pack(side=LEFT, padx=(2, 0), fill=X, expand=YES)
        opt_underline = ttk.Checkbutton(
            master=effects_lframe,
            text=MessageCatalog.translate(\"underline\"),
            variable=self._underline,
        )
        opt_underline.pack(side=LEFT, padx=5, pady=5)
        opt_overstrike = ttk.Checkbutton(
            master=effects_lframe,
            text=MessageCatalog.translate(\"overstrike\"),
            variable=self._overstrike,
        )
        opt_overstrike.pack(side=LEFT, padx=5, pady=5)

    def _font_preview(self, master, padding: int):
        container = ttk.Frame(master, padding=padding)
        container.pack(fill=BOTH, expand=YES, anchor=N)

        header = ttk.Label(
            container,
            text=MessageCatalog.translate(\"Preview\"),
            font=\"TkHeadingFont\",
        )
        header.pack(fill=X, pady=2, anchor=N)

        content = MessageCatalog.translate(
            \"The quick brown fox jumps over the lazy dog.\"
        )
        self._preview_text = ttk.Text(
            master=container,
            height=3,
            font=self._preview_font,
            highlightbackground=self._style.colors.primary,
        )
        self._preview_text.insert(END, content)
        self._preview_text.pack(fill=BOTH, expand=YES)
        container.pack_propagate(False)

    def _on_select_font_family(self, e):
        tree: ttk.Treeview = self._toplevel.nametowidget(e.widget)
        fontfamily = tree.selection()[0]
        self._family.set(value=fontfamily)
        self._update_font_preview()

    def _on_select_font_size(self, e):
        tree: ttk.Treeview = self._toplevel.nametowidget(e.widget)
        fontsize = tree.selection()[0]
        self._size.set(value=fontsize)
        self._update_font_preview()

    def _on_submit(self) -> font.Font:
        self._toplevel.destroy()
        return self.result

    def _on_cancel(self):
        self._toplevel.destroy()

    def _update_font_preview(self, *_):
        family = self._family.get()
        size = self._size.get()
        slant = self._slant.get()
        overstrike = self._overstrike.get()
        underline = self._underline.get()

        self._preview_font.config(
            family=family,
            size=size,
            slant=slant,
            overstrike=overstrike,
            underline=underline,
        )
        try:
            self._preview_text.configure(font=self._preview_font)
        except:
            pass
        self._result = self._preview_font


class Messagebox:
    \"\"\"This class contains various static methods that show popups with
    a message to the end user with various arrangments of buttons
    and alert options.\"\"\"

    @staticmethod
    def show_info(message, title=\" \", parent=None, alert=False, **kwargs):
        \"\"\"Display a modal dialog box with an OK button and an INFO
        icon.

        ![](../../assets/dialogs/messagebox-show-info.png)

        Parameters:

            message (str):
                A message to display in the message box.

            title (str):
                The string displayed as the title of the messagebox. This
                option is ignored on Mac OS X, where platform guidelines
                forbid the use of a title on this kind of dialog.

            parent (Union[Window, Toplevel]):
                Makes the window the logical parent of the message box. The
                message box is displayed on top of its parent window.

            alert (bool):
                Specified whether to ring the display bell.

            **kwargs (Dict):
                Other optional keyword arguments.
        \"\"\"
        dialog = MessageDialog(
            message=message,
            title=title,
            alert=alert,
            parent=parent,
            buttons=[\"OK:primary\"],
            icon=Icon.info,
            localize=True,
        )
        if \"position\" in kwargs:
            position = kwargs.pop(\"position\")
        else:
            position = None
        dialog.show(position)

    @staticmethod
    def show_warning(message, title=\" \", parent=None, alert=True, **kwargs):
        \"\"\"Display a modal dialog box with an OK button and a
        warning icon. Also will ring the display bell.

        ![](../../assets/dialogs/messagebox-show-warning.png)

        Parameters:

            message (str):
                A message to display in the message box.

            title (str):
                The string displayed as the title of the messagebox. This
                option is ignored on Mac OS X, where platform guidelines
                forbid the use of a title on this kind of dialog.

            parent (Union[Window, Toplevel]):
                Makes the window the logical parent of the message box. The
                message box is displayed on top of its parent window.

            alert (bool):
                Specified whether to ring the display bell.

            **kwargs (Dict):
                Other optional keyword arguments.
        \"\"\"
        dialog = MessageDialog(
            message=message,
            title=title,
            parent=parent,
            buttons=[\"OK:primary\"],
            icon=Icon.warning,
            alert=alert,
            localize=True,
            **kwargs,
        )
        if \"position\" in kwargs:
            position = kwargs.pop(\"position\")
        else:
            position = None
        dialog.show(position)

    @staticmethod
    def show_error(message, title=\" \", parent=None, alert=True, **kwargs):
        \"\"\"Display a modal dialog box with an OK button and an
        error icon. Also will ring the display bell.

        ![](../../assets/dialogs/messagebox-show-error.png)

        Parameters:

            message (str):
                A message to display in the message box.

            title (str):
                The string displayed as the title of the messagebox. This
                option is ignored on Mac OS X, where platform guidelines
                forbid the use of a title on this kind of dialog.

            parent (Union[Window, Toplevel]):
                Makes the window the logical parent of the message box. The
                message box is displayed on top of its parent window.

            alert (bool):
                Specified whether to ring the display bell.

            **kwargs (Dict):
                Other optional keyword arguments.
        \"\"\"
        dialog = MessageDialog(
            message=message,
            title=title,
            parent=parent,
            buttons=[\"OK:primary\"],
            icon=Icon.error,
            alert=alert,
            localize=True,
            **kwargs,
        )
        if \"position\" in kwargs:
            position = kwargs.pop(\"position\")
        else:
            position = None
        dialog.show(position)

    @staticmethod
    def show_question(
        message,
        title=\" \",
        parent=None,
        buttons=[\"No:secondary\", \"Yes:primary\"],
        alert=True,
        **kwargs,
    ):
        \"\"\"Display a modal dialog box with yes, no buttons and a
        question icon. Also will ring the display bell. You may also
        change the button scheme using the `buttons` parameter.

        ![](../../assets/dialogs/messagebox-show-question.png)

        Parameters:

            message (str):
                A message to display in the message box.

            title (str):
                The string displayed as the title of the messagebox. This
                option is ignored on Mac OS X, where platform guidelines
                forbid the use of a title on this kind of dialog.

            parent (Union[Window, Toplevel]):
                Makes the window the logical parent of the message box. The
                message box is displayed on top of its parent window.

            buttons (List[str]):
                A list of buttons to appear at the bottom of the popup
                messagebox. The buttons can be a list of strings which
                will define the symbolic name and the button text.
                `['OK', 'Cancel']`. Alternatively, you can assign a
                bootstyle to each button by using the colon to separate the
                button text and the bootstyle. If no colon is found, then
                the style is set to 'primary' by default.
                `['Yes:success','No:danger']`.

            alert (bool):
                Specified whether to ring the display bell.

            **kwargs (Dict):
                Other optional keyword arguments.

        Returns:

            Union[str, None]:
                The symbolic name of the button pressed, or None if the
                window is closed without pressing a button.
        \"\"\"
        dialog = MessageDialog(
            message=message,
            title=title,
            parent=parent,
            buttons=buttons,
            icon=Icon.question,
            alert=alert,
            localize=True,
            **kwargs,
        )
        if \"position\" in kwargs:
            position = kwargs.pop(\"position\")
        else:
            position = None
        dialog.show(position)
        return dialog.result

    @staticmethod
    def ok(message, title=\" \", alert=False, parent=None, **kwargs):
        \"\"\"Display a modal dialog box with an OK button and and optional
        bell alert.

        ![](../../assets/dialogs/messagebox-ok.png)

        Parameters:

            message (str):
                A message to display in the message box.

            title (str):
                The string displayed as the title of the messagebox. This
                option is ignored on Mac OS X, where platform guidelines
                forbid the use of a title on this kind of dialog.

            alert (bool):
                Specified whether to ring the display bell.

            parent (Union[Window, Toplevel]):
                Makes the window the logical parent of the message box. The
                message box is displayed on top of its parent window.

            **kwargs (Dict):
                Other optional keyword arguments.
        \"\"\"
        dialog = MessageDialog(
            title=title,
            message=message,
            parent=parent,
            alert=alert,
            buttons=[\"OK:primary\"],
            localize=True,
            **kwargs,
        )
        if \"position\" in kwargs:
            position = kwargs.pop(\"position\")
        else:
            position = None
        dialog.show(position)

    @staticmethod
    def okcancel(message, title=\" \", alert=False, parent=None, **kwargs):
        \"\"\"Displays a modal dialog box with OK and Cancel buttons and
        return the symbolic name of the button pressed.

        ![](../../assets/dialogs/messagebox-ok-cancel.png)

        Parameters:

            message (str):
                A message to display in the message box.

            title (str):
                The string displayed as the title of the messagebox. This
                option is ignored on Mac OS X, where platform guidelines
                forbid the use of a title on this kind of dialog.

            alert (bool):
                Specified whether to ring the display bell.

            parent (Union[Window, Toplevel]):
                Makes the window the logical parent of the message box. The
                message box is displayed on top of its parent window.

            **kwargs (Dict):
                Other optional keyword arguments.

        Returns:

            Union[str, None]:
                The symbolic name of the button pressed, or None if the
                window is closed without pressing a button.
        \"\"\"
        dialog = MessageDialog(
            title=title,
            message=message,
            parent=parent,
            alert=alert,
            localize=True,
            **kwargs,
        )
        if \"position\" in kwargs:
            position = kwargs.pop(\"position\")
        else:
            position = None
        dialog.show(position)
        return dialog.result

    @staticmethod
    def yesno(message, title=\" \", alert=False, parent=None, **kwargs):
        \"\"\"Display a modal dialog box with YES and NO buttons and return
        the symbolic name of the button pressed.

        ![](../../assets/dialogs/messagebox-yes-no.png)

        Parameters:

            message (str):
                A message to display in the message box.

            title (str):
                The string displayed as the title of the messagebox. This
                option is ignored on Mac OS X, where platform guidelines
                forbid the use of a title on this kind of dialog.

            alert (bool):
                Specified whether to ring the display bell.

            parent (Union[Window, Toplevel]):
                Makes the window the logical parent of the message box. The
                message box is displayed on top of its parent window.

            **kwargs (Dict):
                Other optional keyword arguments.

        Returns:

            Union[str, None]:
                The symbolic name of the button pressed, or None if the
                window is closed without pressing a button.
        \"\"\"
        dialog = MessageDialog(
            title=title,
            message=message,
            parent=parent,
            buttons=[\"No\", \"Yes:primary\"],
            alert=alert,
            localize=True,
            **kwargs,
        )
        if \"position\" in kwargs:
            position = kwargs.pop(\"position\")
        else:
            position = None
        dialog.show(position)
        return dialog.result

    @staticmethod
    def yesnocancel(message, title=\" \", alert=False, parent=None, **kwargs):
        \"\"\"Display a modal dialog box with YES, NO, and Cancel buttons,
        and return the symbolic name of the button pressed.

        ![](../../assets/dialogs/messagebox-yes-no-cancel.png)

        Parameters:

            message (str):
                A message to display in the message box.

            title (str):
                The string displayed as the title of the messagebox. This
                option is ignored on Mac OS X, where platform guidelines
                forbid the use of a title on this kind of dialog.

            alert (bool):
                Specified whether to ring the display bell.

            parent (Union[Window, Toplevel]):
                Makes the window the logical parent of the message box. The
                message box is displayed on top of its parent window.

            **kwargs (Dict):
                Optional keyword arguments.

        Returns:

            Union[str, None]:
                The symbolic name of the button pressed, or None if the
                window is closed without pressing a button.
        \"\"\"
        dialog = MessageDialog(
            title=title,
            message=message,
            parent=parent,
            alert=alert,
            buttons=[\"Cancel\", \"No\", \"Yes:primary\"],
            localize=True,
            **kwargs,
        )
        if \"position\" in kwargs:
            position = kwargs.pop(\"position\")
        else:
            position = None
        dialog.show(position)
        return dialog.result

    @staticmethod
    def retrycancel(message, title=\" \", alert=False, parent=None, **kwargs):
        \"\"\"Display a modal dialog box with RETRY and Cancel buttons;
        returns the symbolic name of the button pressed.

        ![](../../assets/dialogs/messagebox-retry-cancel.png)

        Parameters:

            message (str):
                A message to display in the message box.

            title (str):
                The string displayed as the title of the messagebox. This
                option is ignored on Mac OS X, where platform guidelines
                forbid the use of a title on this kind of dialog.

            alert (bool):
                Specified whether to ring the display bell.

            parent (Union[Window, Toplevel]):
                Makes the window the logical parent of the message box. The
                message box is displayed on top of its parent window.

            **kwargs (Dict):
                Other optional keyword arguments.

        Returns:

            Union[str, None]:
                The symbolic name of the button pressed, or None if the
                window is closed without pressing a button.
        \"\"\"
        dialog = MessageDialog(
            title=title,
            message=message,
            parent=parent,
            alert=alert,
            buttons=[\"Cancel\", \"Retry:primary\"],
            localize=True,
            **kwargs,
        )
        if \"position\" in kwargs:
            position = kwargs.pop(\"position\")
        else:
            position = None
        dialog.show(position)
        return dialog.result


class Querybox:
    \"\"\"This class contains various static methods that request data
    from the end user.\"\"\"

    @staticmethod
    def get_color(
        parent=None, title=\"Color Chooser\", initialcolor=None, **kwargs
    ):
        \"\"\"Show a color picker and return the select color when the
        user pressed OK.

        ![](../../assets/dialogs/querybox-get-color.png)

        Parameters:

            parent (Widget):
                The parent widget.

            title (str):
                Optional text that appears on the titlebar.

            initialcolor (str):
                The initial color to display in the 'Current' color
                frame.

        Returns:

            Tuple[rgb, hsl, hex]:
                The selected color in various colors models.
        \"\"\"
        from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog

        dialog = ColorChooserDialog(parent, title, initialcolor)
        if \"position\" in kwargs:
            position = kwargs.pop(\"position\")
        else:
            position = None
        dialog.show(position)
        return dialog.result

    @staticmethod
    def get_date(
        parent=None,
        title=\" \",
        firstweekday=6,
        startdate=None,
        bootstyle=\"primary\",
    ):
        \"\"\"Shows a calendar popup and returns the selection.

        ![](../../assets/dialogs/querybox-get-date.png)

        Parameters:

            parent (Widget):
                The parent widget; the popup will appear to the
                bottom-right of the parent widget. If no parent is
                provided, the widget is centered on the screen.

            title (str):
                The text that appears on the popup titlebar.

            firstweekday (int):
                Specifies the first day of the week. `0` is Monday, `6` is
                Sunday (the default).

            startdate (datetime):
                The date to be in focus when the widget is displayed;

            bootstyle (str):
                The following colors can be used to change the color of the
                title and hover / pressed color -> primary, secondary, info,
                warning, success, danger, light, dark.

        Returns:

            datetime:
                The date selected; the current date if no date is selected.
        \"\"\"
        chooser = DatePickerDialog(
            parent=parent,
            title=title,
            firstweekday=firstweekday,
            startdate=startdate,
            bootstyle=bootstyle,
        )
        return chooser.date_selected

    @staticmethod
    def get_string(
        prompt=\"\", title=\" \", initialvalue=None, parent=None, **kwargs
    ):
        \"\"\"Request a string type input from the user.

        ![](../../assets/dialogs/querybox-get-string.png)

        Parameters:

            prompt (str):
                A message to display in the message box above the entry
                widget.

            title (str):
                The string displayed as the title of the message box. This
                option is ignored on Mac OS X, where platform guidelines
                forbid the use of a title on this kind of dialog.

            initialvalue (Any):
                The initial value in the entry widget.

            parent (Widget):
                Makes the window the logical parent of the message box. The
                messagebox is displayed on top of its parent window.

            **kwargs (Dict):
                Other optional keyword arguments.

        Returns:

            str:
                The string value of the entry widget.
        \"\"\"
        initialvalue = initialvalue or \"\"
        if \"position\" in kwargs:
            position = kwargs.pop(\"position\")
        else:
            position = None
        dialog = QueryDialog(
            prompt, title, initialvalue, parent=parent, **kwargs
        )
        dialog.show(position)
        return dialog._result

    @staticmethod
    def get_integer(
        prompt=\"\",
        title=\" \",
        initialvalue=None,
        minvalue=None,
        maxvalue=None,
        parent=None,
        **kwargs,
    ):
        \"\"\"Request an integer type input from the user.

        ![](../../assets/dialogs/querybox-get-integer.png)

        Parameters:

            prompt (str):
                A message to display in the message box above the entry
                widget.

            title (str):
                The string displayed as the title of the message box. This
                option is ignored on Mac OS X, where platform guidelines
                forbid the use of a title on this kind of dialog.

            initialvalue (int):
                The initial value in the entry widget.

            minvalue (int):
                The minimum allowed value.

            maxvalue (int):
                The maximum allowed value.

            parent (Widget):
                Makes the window the logical parent of the message box. The
                messagebox is displayed on top of its parent window.

            **kwargs (Dict):
                Other optional keyword arguments.

        Returns:

            int:
                The integer value of the entry widget.
        \"\"\"
        initialvalue = initialvalue or \"\"
        if \"position\" in kwargs:
            position = kwargs.pop(\"position\")
        else:
            position = None
        dialog = QueryDialog(
            prompt,
            title,
            initialvalue,
            minvalue,
            maxvalue,
            datatype=int,
            parent=parent,
            **kwargs,
        )
        dialog.show(position)
        return dialog._result

    @staticmethod
    def get_float(
        prompt=\"\",
        title=\" \",
        initialvalue=None,
        minvalue=None,
        maxvalue=None,
        parent=None,
        **kwargs,
    ):
        \"\"\"Request a float type input from the user.

        ![](../../assets/dialogs/querybox-get-float.png)

        Parameters:

            prompt (str):
                A message to display in the message box above the entry
                widget.

            title (str):
                The string displayed as the title of the message box. This
                option is ignored on Mac OS X, where platform guidelines
                forbid the use of a title on this kind of dialog.

            initialvalue (float):
                The initial value in the entry widget.

            minvalue (float):
                The minimum allowed value.

            maxvalue (float):
                The maximum allowed value.

            parent (Widget):
                Makes the window the logical parent of the message box. The
                messagebox is displayed on top of its parent window.

            **kwargs (Dict):
                Other optional keyword arguments.

        Returns:

            float:
                The float value of the entry widget.
        \"\"\"
        initialvalue = initialvalue or \"\"
        if \"position\" in kwargs:
            position = kwargs.pop(\"position\")
        else:
            position = None
        dialog = QueryDialog(
            prompt,
            title,
            initialvalue,
            minvalue,
            maxvalue,
            datatype=float,
            parent=parent,
            **kwargs,
        )
        dialog.show(position)
        return dialog._result

    @staticmethod
    def get_font(parent=None, **kwargs):
        \"\"\"Request a customized font

        ![](../../assets/dialogs/querybox-get-font.png)

        Parameters:

            parent (Widget):
                Makes the window the logical parent of the dialog box. The
                dialog is displayed on top of its parent window.

            **kwargs (Dict):
                Other keyword arguments.

        Returns:

            Font:
                A font object.
        \"\"\"
        if \"position\" in kwargs:
            position = kwargs.pop(\"position\")
        else:
            position = None
        dialog = FontDialog(parent=parent, **kwargs)
        dialog.show(position)
        return dialog.result
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/localization/__init__.py": """\"\"\"
    A partial wrapper on the tcl/tk msgcat (Tcl message catalog)

    The MessageCatalog provides a set of functions that can be used to 
    manage multi-lingual user interfaces. Text strings are defined in a 
    “message catalog” which is independent from the application, and 
    which can be edited or localized without modifying the application 
    source code. New languages or locales may be provided by adding a 
    new file to the message catalog.

    https://www.tcl.tk/man/tcl/TclCmd/msgcat.html    
\"\"\"
from ttkbootstrap.localization.msgs import initialize_localities
from ttkbootstrap.localization.msgcat import MessageCatalog




""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/localization/README.md": """# Message Catalog

Instructions for adding to the ttkbootstrap message catalog

1. Open the file **src/ttkbootstrap/localization/msgs.py**
2. If adding to an existing catalog, locate the language and add the message as a tuple `(\"original\", \"translated\")`
3. If adding a new language to the catalog, append a new instance of `LocaleMsgs` to the `MESSAGES` list using the same pattern demonstrated in the file for other languages:
```python
MESSAGES.append(
    LocaleMsgs(
        \"language_code\",
        (\"original\", \"translated\"),
        (\"original\", \"translated\")
    )
)
```
4. Use the language code as presented in the **LCID string** [on this site](https://wiki.freepascal.org/Language_Codes), except replace the dash with an undercore. For example: **zh-cn** should be **zh_cn**.

5. The following words / phrases should be translated for a new language in ttkbootstrap at a minimum:

    - \"OK\"
    - \"Ok\"
    - \"Retry\"
    - \"Delete\"
    - \"Next\"
    - \"Prev\"
    - \"Yes\"
    - \"No\"
    - \"Open\"
    - \"Close\"
    - \"Add\"
    - \"Remove\"
    - \"Submit\"
    - \"Family\"
    - \"Weight\"
    - \"Slant\"
    - \"Effects\"
    - \"Preview\"
    - \"Size\"
    - \"Should be of data type\"
    - \"Invalid data type\"
    - \"Number cannot be greater than\"
    - \"Out of range\"
    - \"Previous\"
    - \"The quick brown fox jumps over the lazy dog.\"
    - \"Font Selector\"
    - \"normal\"
    - \"bold\"  \"negrito\"
    - \"roman\"
    - \"italic\"
    - \"underline\"
    - \"overstrike\"
    - \"Color Chooser\"
    - \"Advanced\"
    - \"Themed\"
    - \"Standard\"
    - \"Current\"
    - \"New\"
    - \"Hue\"
    - \"Sat\"
    - \"Lum\"
    - \"Hex\"
    - \"Red\"
    - \"Green\"
    - \"Blue\"
    - \"color dropper\"
    - \"Cancel\"
    - \"Search\"
    - \"Page\"
    - \"of\"
    - \"⎌\"
    - \"Reset table\"
    - \"Columns\"
    - \"Move\"
    - \"Align\"
    - \"Hide column\"
    - \"Delete column\"
    - \"Show All\"
    - \"Move to left\"
    - \"Move to right\"
    - \"Move to first\"
    - \"Move to last\"
    - \"Align left\"
    - \"Align center\"
    - \"Align right\"
    - \"Sort\"
    - \"Filter\"
    - \"Export\"
    - \"Delete selected rows\"
    - \"Sort Ascending\"
    - \"Sort Descending\"
    - \"Clear filters\"
    - \"Filter by cell's value\"
    - \"Hide select rows\"
    - \"Show only select rows\"
    - \"Export all records\"
    - \"Export current page\"
    - \"Export current selection\"
    - \"Export records in filter\"
    - \"Move up\"
    - \"Move down\"
    - \"Move to top\"
    - \"Move to bottom\"
    - \"Mo\"
    - \"Tu\"
    - \"We\"
    - \"Th\"
    - \"Fr\"
    - \"Sa\"
    - \"Su\"
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/localization/msgcat.py": """from ttkbootstrap.window import get_default_root


class MessageCatalog:
    @staticmethod
    def translate(src):
        \"\"\"Returns a translation of src according to the user's current
        locale.

        This is the main function used to localize an application.
        Instead of using an English string directly, an applicaton can
        pass the English string through `translate` and use the result.
        If an application is written for a single language in this
        fashion, then it is easy to add support for additional languages
        later simply by defining new message catalog entries.

        Parameters:

            src (str):
                The string to be translated.

        Returns:

            str:
                The translated string.
        \"\"\"
        root = get_default_root()
        command = \"::msgcat::mc\"
        return root.tk.eval(f'{command} \"{src}\"')

    @staticmethod
    def locale(newlocale=None):
        \"\"\" \"This function sets the locale to newlocale. If newlocale is
        omitted, the current locale is returned, otherwise the current
        locale is set to newlocale. The initial locale defaults to the
        locale specified in the user's environment.

        Parameters:

            newlocale (str):
                The new locale code used to define the language for the
                application.

        Returns:

            str:
                The current locale name if newlocale is None or an empty
                string.
        \"\"\"
        root = get_default_root()
        command = \"::msgcat::mclocale\"
        return root.tk.eval(f'{command} {newlocale or \"\"}')

    @staticmethod
    def preferences():
        \"\"\"Returns an ordered list of the locales preferred by the user,
        based on the user's language specification. The list is ordered
        from most specific to least preference. If the user has specified
        LANG=en_US_funky, this method would return {en_US_funky en_US en}.

        Returns:

            List[str, ...]:
                Locales preferred by the user.
        \"\"\"
        root = get_default_root()
        command = \"::msgcat::mcpreferences\"
        items = root.tk.eval(command).split(\" \")
        if len(items) > 0:
            return items[0:-1]
        else:
            return []

    @staticmethod
    def load(dirname):
        \"\"\"Searches the specified directory for files that match the
        language specifications returned by `preferences`. Each file
        located is sourced.

        Parameters:

            dirname (str or Pathlike object):
                The directory path of the msg files.

        Returns:

            int:
                Then number of message files which matched the
                specification and were loaded.
        \"\"\"
        from pathlib import Path
        msgs = Path(dirname).as_posix() # format path for tcl/tk
        
        root = get_default_root()
        command = \"::msgcat::mcload\"
        return int(root.tk.eval(f\"{command} [list {msgs}]\"))

    @staticmethod
    def set(locale, src, translated=None):
        \"\"\"Sets the translation for 'src' to 'translated' in the
        specified locale. If translated is not specified, src is used
        for both.

        Parameters:

            locale (str):
                The local code used when translating the src.

            src (str):
                The original language string.

            translated (str):
                The translated string.
        \"\"\"
        root = get_default_root()
        command = \"::msgcat::mcset\"
        root.tk.eval(f'{command} {locale} {src} {translated or \"\"}')

    @staticmethod
    def set_many(locale, *args):
        \"\"\"Sets the translation for multiple source strings in *args in
        the specified locale and the current namespace. Must be an even
        number of args.

        Parameters:

            locale (str):
                The local code used when translating the src.

            *args (str):
                A series of src, translated pairs.

        Returns:

            int:
                The number of translation sets.
        \"\"\"
        root = get_default_root()
        command = \"::msgcat::mcmset\"
        messages = \" \".join([f'\"{x}\"' for x in args])
        out = f\"{command} {locale} {{{messages}}}\"
        return int(root.tk.eval(out))

    @staticmethod
    def max(*src):
        \"\"\"Given several source strings, max returns the length of the
        longest translated string. This is useful when designing localized
        GUIs, which may require that all buttons, for example, be a fixed
        width (which will be the width of the widest button).

        Parameters:

            *src (str):
                A series of strings to compare

        Returns:

            int:
                The length of the longest str.
        \"\"\"
        root = get_default_root()
        command = \"::msgcat::mcmax\"
        return int(root.tk.eval(f'{command} {\" \".join(src)}'))


if __name__ == \"__main__\":

    # testing
    from ttkbootstrap import localization

    localization.initialize_localities()
    MessageCatalog.locale(\"zh_cn\")
    result = MessageCatalog.translate(\"Skip Messages\")
    print(result)
    result = MessageCatalog.translate(\"yes\")
    print(result)
    from ttkbootstrap.dialogs import Messagebox

    Messagebox.okcancel(\"this is my message\")
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/localization/msgs.py": """from ttkbootstrap.localization.msgcat import MessageCatalog

MESSAGES = []


def initialize_localities():
    \"\"\"Load all custom msg files.\"\"\"
    for m in MESSAGES:
        m.initialize()


class LocaleMsgs:
    \"\"\"A helper class to allow loading the library message catalog
    without having to package library resources which can cause
    problems with creating distributable applications with some
    packagers.\"\"\"

    def __init__(self, locale, *msgs):
        self.locale = locale
        self.messages = msgs

    def initialize(self):
        \"\"\"Initialize this locale in the MessageCatalog\"\"\"
        from itertools import chain

        messages = list(chain(*self.messages))
        MessageCatalog.set_many(self.locale, *messages)


MESSAGES.append(
    # CZECH translation
    LocaleMsgs(
        \"cs\",
        (\"Continue\", \"Pokračovat\"),
        (\"Retry\", \"Znovu\"),
        (\"Delete\", \"Vymazat\"),
        (\"Next\", \"Další\"),
        (\"Prev\", \"Předchozí\"),
        (\"Yes\", \"Ano\"),
        (\"No\", \"Ne\"),
        (\"Open\", \"Otevřený\"),
        (\"Close\", \"Zavřít\"),
        (\"Add\", \"Přidat\"),
        (\"Remove\", \"Odstranit\"),
        (\"Submit\", \"Podat\"),
        (\"Family\", \"Rodina\"),
        (\"Weight\", \"Hmotnost\"),
        (\"Slant\", \"Sklonit\"),
        (\"Effects\", \"Účinky\"),
        (\"Preview\", \"Náhled\"),
        (\"Size\", \"Velikost\"),
    )
)
MESSAGES.append(
    # DANISH translation
    LocaleMsgs(
        \"da\",
        (\"Continue\", \"Fortsætte\"),
        (\"Retry\", \"Prøv\"),
        (\"Delete\", \"Slette\"),
        (\"Next\", \"Næste\"),
        (\"Prev\", \"Forrige\"),
        (\"Yes\", \"Ja\"),
        (\"No\", \"Nej\"),
        (\"Open\", \"Åben\"),
        (\"Close\", \"Lukke\"),
        (\"Add\", \"Tilføje\"),
        (\"Remove\", \"Fjerne\"),
        (\"Submit\", \"Indsende\"),
        (\"Family\", \"Familie\"),
        (\"Weight\", \"Vægt\"),
        (\"Slant\", \"Drejning\"),
        (\"Effects\", \"Effekter\"),
        (\"Size\", \"Størrelse\"),
    )
)
MESSAGES.append(
    # SPANISH translation
    LocaleMsgs(
        \"es\",
        (\"Cancel\", \"Cancelar\"),
        (\"Retry\", \"Reintentar\"),
        (\"Delete\", \"Borrar\"),
        (\"Next\", \"Próximo\"),
        (\"Prev\", \"Anterior\"),
        (\"Yes\", \"Sí\"),
        (\"Open\", \"Abrir\"),
        (\"Close\", \"Cerrar\"),
        (\"Add\", \"Agregar\"),
        (\"Remove\", \"Eliminar\"),
        (\"Submit\", \"Enviar\"),
        (\"Family\", \"Familia\"),
        (\"Weight\", \"Peso\"),
        (\"Slant\", \"Inclinación\"),
        (\"Effects\", \"Efectos\"),
        (\"Preview\", \"Vista previa\"),
        (\"Size\", \"Tamaño\"),
    )
)
MESSAGES.append(
    # PORTUGUESE - BRAZIL translation   
    LocaleMsgs(
        \"pt_br\",
        (\"Retry\", \"Repetir\"),
        (\"Delete\", \"Excluir\"),
        (\"Next\", \"Próximo\"),
        (\"Prev\", \"Anterior\"),
        (\"Yes\", \"Sim\"),
        (\"No\", \"Não\"),
        (\"Open\", \"Abrir\"),
        (\"Close\", \"Fechar\"),
        (\"Add\", \"Adicionar\"),
        (\"Remove\", \"Remover\"),
        (\"Submit\", \"Enviar\"),
        (\"Family\", \"Família\"),
        (\"Weight\", \"Espessura\"),
        (\"Slant\", \"Estilo\"),
        (\"Effects\", \"Efeitos\"),
        (\"Preview\", \"Visualizar\"),
        (\"Size\", \"Tamanho\"),
        (\"Should be of data type\", \"Deve ser do tipo de dados\"),
        (\"Invalid data type\", \"Tipo de dados inválido\"),
        (\"Number cannot be greater than\", \"O número não deve ser maior que\"),
        (\"Out of range\", \"Fora do limite\"),
        (\"Previous\", \"Anterior\"),
        (
            \"The quick brown fox jumps over the lazy dog.\",
            \"A rápida raposa marrom pula sobre o cachorro preguiçoso.\",
        ),
        (\"Font Selector\", \"Seletor de Fontes\"),
        (\"normal\", \"normal\"),
        (\"bold\", \"negrito\"),
        (\"roman\", \"romano\"),
        (\"italic\", \"itálico\"),
        (\"underline\", \"sublinhado\"),
        (\"overstrike\", \"taxado\"),
        (\"Color Chooser\", \"Seletor de Cores\"),
        (\"Advanced\", \"Avançado\"),
        (\"Themed\", \"Tema\"),
        (\"Standard\", \"Básicas\"),
        (\"Current\", \"Atual\"),
        (\"New\", \"Nova\"),
        (\"Hue\", \"Matiz\"),
        (\"Sat\", \"Sat\"),
        (\"Lum\", \"Lum\"),
        (\"Hex\", \"Hex\"),
        (\"Red\", \"Vermelho\"),
        (\"Green\", \"Verde\"),
        (\"Blue\", \"Azul\"),
        (\"color dropper\", \"Selecionador de cores (conta-gotas)\"),
        (\"Cancel\", \"Cancelar\"),
        (\"Search\", \"Buscar\"),
        (\"Page\", \"Página\"),
        (\"of\", \"de\"),
        (\"⎌\", \"↺\"),
        (\"Reset table\", \"Resetar Tabela\"),
        (\"Columns\", \"Colunas\"),
        (\"Move\", \"Mover\"),
        (\"Align\", \"Alinhar\"),
        (\"Hide column\", \"Ocultar coluna\"),
        (\"Delete column\", \"Excluir coluna\"),
        (\"Show All\", \"Exibir todas\"),
        (\"Move to left\", \"Mover para esquerda\"),
        (\"Move to right\", \"Mover para direira\"),
        (\"Move to first\", \"Mover para o início\"),
        (\"Move to last\", \"Mover para o fim\"),
        (\"Align left\", \"Alinhar à esquerda\"),
        (\"Align center\", \"Alinhar ao centro\"),
        (\"Align right\", \"Alinhar à direita\"),
        (\"Sort\", \"Classificar\"),
        (\"Filter\", \"Filtrar\"),
        (\"Export\", \"Exportar\"),
        (\"Delete selected rows\", \"Excluir linhas selecionadas\"),
        (\"Sort Ascending\", \"Ordem crescente\"),
        (\"Sort Descending\", \"Ordem decrescente\"),
        (\"Clear filters\", \"Limpar filtros\"),
        (\"Filter by cell's value\", \"Filtrar pelo valor da célula\"),
        (\"Hide select rows\", \"Ocultar linha selecionada\"),
        (\"Show only select rows\", \"Exibir somente as linhas selecionadas\"),
        (\"Export all records\", \"Exportar todos os dados\"),
        (\"Export current page\", \"Exportar página atual\"),
        (\"Export current selection\", \"Exportar seleção atual\"),
        (\"Export records in filter\", \"Exportar dados do filtro\"),
        (\"Move up\", \"Mover para cima\"),
        (\"Move down\", \"Mover para baixo\"),
        (\"Move to top\", \"Mover para o início\"),
        (\"Move to bottom\", \"Mover para o fim\"),
        (\"Mo\", \"S\"),
        (\"Tu\", \"T\"),
        (\"We\", \"Q\"),
        (\"Th\", \"Q\"),
        (\"Fr\", \"S\"),
        (\"Sa\", \"S\"),
        (\"Su\", \"D\"),
    )
)
MESSAGES.append(
    # CHINESE - CHINA translation
    LocaleMsgs(
        \"zh_cn\",
        (\"&Abort\", \"&中止\"),
        (\"&About...\", \"&关于……\"),
        (\"All Files\", \"所有文件\"),
        (\"Application Error\", \"应用程序错误\"),
        (\"&Apply\", \"&添加\"),
        (\"Bold\", \"粗体\"),
        (\"Bold Italic\", \"加粗斜体\"),
        (\"&Blue\", \"&蓝色\"),
        (\"Cancel\", \"取消\"),
        (\"&Cancel\", \"&取消\"),
        (
            'Cannot change to the directory %1\\$s.\\nPermission denied.',
            '无法更改目录 %1\\$s。\\n访问被拒绝。',
        ),
        (\"Choose Directory\", \"选择文件夹\"),
        (\"Cl&ear\", \"清&除\"),
        (\"&Clear Console\", \"&清除终端\"),
        (\"Color\", \"颜色\"),
        (\"Console\", \"终端\"),
        (\"&Copy\", \"&复制\"),
        (\"Cu&t\", \"剪&切\"),
        (\"&Delete\", \"&删除\"),
        (\"Details >>\", \"详细信息 >>\"),
        ('Directory %1\\$s does not exist.', '目录 %1\\$s 不存在。'),
        (\"&Directory:\", \"&目录：\"),
        (\"&Edit\", \"&编辑\"),
        (\"Effects\", \"效果\"),
        (\"Error: %1\\$s\", \"错误： %1\\$s\"),
        (\"E&xit\", \"退&出\"),
        (\"&File\", \"&文件\"),
        (
            'File %1\\$s already exists.\\nDo you want to overwrite it?',
            '文件 %1\\$s 已经存在。\\n您想要覆盖它吗？',
        ),
        ('File %1\\$s already exists.\\n\\n', '文件 %1\\$s 已经存在。\\n\\n'),
        ('File %1\\$s does not exist.', '文件 %1\\$s 不存在。'),
        (\"File &name:\", \"文件&名：\"),
        (\"File &names:\", \"文件&名：\"),
        (\"Files of &type:\", \"文件&类型：\"),
        (\"Fi&les:\", \"文&件：\"),
        (\"&Filter\", \"&过滤\"),
        (\"Fil&ter:\", \"过&滤：\"),
        (\"Font\", \"字体\"),
        (\"&Font:\", \"&字体：\"),
        (\"Font st&yle:\", \"字体&样式：\"),
        (\"&Green\", \"&绿色\"),
        (\"&Help\", \"&帮助\"),
        (\"Hi\", \"你好\"),
        (\"&Hide Console\", \"&隐藏终端\"),
        (\"&Ignore\", \"&忽略\"),
        ('Invalid file name %1\\$s.', '无效的文件名 %1\\$s。'),
        (\"Italic\", \"斜体\"),
        (\"Log Files\", \"日志文件\"),
        (\"&No\", \"&取消\"),
        (\"No\", \"取消\"),
        (\"&OK\", \"&确定\"),
        (\"OK\", \"确定\"),
        (\"Ok\", \"确定\"),
        (\"Open\", \"打开\"),
        (\"&Open\", \"&打开\"),
        (\"Open Multiple Files\", \"打开多个文件\"),
        (\"P&aste\", \"粘&贴\"),
        (\"&Quit\", \"&退出\"),
        (\"&Red\", \"红色\"),
        (\"Regular\", \"规则\"),
        (\"Replace existing file?\", \"替换已有文件？\"),
        (\"&Retry\", \"&重试\"),
        (\"Sample\", \"样式\"),
        (\"&Save\", \"&保存\"),
        (\"Save As\", \"另存为\"),
        (\"Save To Log\", \"保存到日志\"),
        (\"Select Log File\", \"选择日志文件\"),
        (\"Select a file to source\", \"选择一个源文件\"),
        (\"&Selection:\", \"&选择：\"),
        (\"&Size:\", \"&大小：\"),
        (\"Show &Hidden Directories\", \"显示&隐藏目录\"),
        (\"Show &Hidden Files and Directories\", \"显示&隐藏文件和目录\"),
        (\"Skip Messages\", \"跳过信息\"),
        (\"&Source...\", \"&来源……\"),
        (\"Stri&keout\", \"删&除线\"),
        (\"Tcl Scripts\", \"Tcl脚本\"),
        (\"Tcl for Windows\", \"适用于Windows的Tcl\"),
        (\"Text Files\", \"文本文档\"),
        (\"&Underline\", \"&下划线\"),
        (\"&Yes\", \"&确定\"),
        (\"abort\", \"中止\"),
        (\"blue\", \"蓝色\"),
        (\"cancel\", \"取消\"),
        (\"extension\", \"拓展\"),
        (\"extensions\", \"拓展\"),
        (\"green\", \"绿色\"),
        (\"ignore\", \"忽略\"),
        (\"ok\", \"确定\"),
        (\"red\", \"红色\"),
        (\"retry\", \"重试\"),
        (\"Retry\", \"重试\"),
        (\"yes\", \"确认\"),
        (\"Yes\", \"确认\"),
        (\"Should be of data type\", \"应为数据类型\"),
        (\"Invalid data type\", \"无效数据类型\"),
        (\"Number cannot be greater than\", \"数字不能大于\"),
        (\"Out of range\", \"超出范围\"),
        (\"Submit\", \"提交\"),
        (\"Delete\", \"删除\"),
        (\"Next\", \"下一步\"),
        (\"Previous\", \"以前的\"),
        (\"Open\", \"打开\"),
        (\"Close\", \"关闭\"),
        (\"Add\", \"添加\"),
        (\"Remove\", \"移除\"),
        (\"Family\", \"组\"),
        (\"Weight\", \"重量\"),
        (\"Slant\", \"倾斜\"),
        (\"Effects\", \"效果\"),
        (\"Preview\", \"预览\"),
        (\"Size\", \"大小\"),
        (\"The quick brown fox jumps over the lazy dog.\", \"敏捷的棕色狐狸跳过懒惰的狗。\"),
        (\"Print\", \"输出\"),
        (\"Printer\", \"打印机\"),
        (\"Letter \", \"信 \"),
        (\"Legal \", \"合法的 \"),
        (\"A4\", \"A4\"),
        (\"Grayscale\", \"灰度\"),
        (\"RGB\", \"RGB\"),
        (\"Options\", \"设置\"),
        (\"Copies\", \"复制\"),
        (\"Paper\", \"纸\"),
        (\"Scale\", \"规模\"),
        (\"Orientation\", \"方向\"),
        (\"Portrait\", \"竖向\"),
        (\"Landscape\", \"横向\"),
        (\"Output\", \"输出\"),
    )
)

MESSAGES.append(
    LocaleMsgs(
        # French
        \"fr\",
        (\"OK\", \"OK\"),
        (\"Ok\", \"Ok\"),
        (\"Retry\", \"Recommencer\"),
        (\"Delete\", \"Supprimer\"),
        (\"Next\", \"Suivant\"),
        (\"Prev\", \"Préc.\"),
        (\"Yes\", \"Oui\"),
        (\"No\", \"Non\"),
        (\"Open\", \"Ouvrir\"),
        (\"Close\", \"Fermer\"),
        (\"Add\", \"Ajouter\"),
        (\"Remove\", \"Supprimer\"),
        (\"Submit\", \"Envoyer\"),
        (\"Family\", \"Famille\"),
        (\"Weight\", \"Poids\"),
        (\"Slant\", \"Italique\"),
        (\"Effects\", \"Effets\"),
        (\"Preview\", \"Prévisualiser\"),
        (\"Size\", \"Taille\"),
        (\"Should be a of data type\", \"Doit être du type de données\"),
        (\"Invalid data type\", \"Type de données invalide\"),
        (\"Number cannot be greater than\", \"Le nombre ne peut pas être plus grand que\"),
        (\"Out of range\", \"Hors limites\"),
        (\"Previous\", \"Précédent\"),
        (\"The quick brown fox jumps over the lazy dog.\", \"The quick brown fox jumps over the lazy dog.\"),
        (\"Font Selector\", \"Sélecteur de Polices\"),
        (\"normal\", \"normal\"),
        (\"bold\", \"gras\"),
        (\"roman\", \"roman\"),
        (\"italic\", \"italique\"),
        (\"underline\", \"souligné\"),
        (\"overstrike\", \"barré\"),
        (\"Color Chooser\", \"Sélecteur de couleur\"),
        (\"Advanced\", \"Avancé\"),
        (\"Themed\", \"Thème\"),
        (\"Standard\", \"Standard\"),
        (\"Current\", \"Courant\"),
        (\"New\", \"Nouveau\"),
        (\"Hue\", \"Teinte\"),
        (\"Sat\", \"Sat\"),
        (\"Lum\", \"Lum\"),
        (\"Hex\", \"Hex\"),
        (\"Red\", \"Rouge\"),
        (\"Green\", \"Vert\"),
        (\"Blue\", \"Bleu\"),
        (\"color dropper\", \"Sélecteur de couleurs\"),
        (\"Cancel\", \"Annuler\"),
        (\"Search\", \"Chercher\"),
        (\"Page\", \"Page\"),
        (\"of\", \"de\"),
        (\"⎌\", \"↺\"),
        (\"Reset table\", \"Réinit. table\"),
        (\"Columns\", \"Colonnes\"),
        (\"Move\", \"Déplacer\"),
        (\"Align\", \"Aligner\"),
        (\"Hide column\", \"Cacher la colonne\"),
        (\"Delete column\", \"Supprimer la colonne\"),
        (\"Show All\", \"Afficher tout\"),
        (\"Move to left\", \"Déplacer vers la gauche\"),
        (\"Move to right\", \"Déplacer vers la droite\"),
        (\"Move to first\", \"Déplacer en premier\"),
        (\"Move to last\", \"Déplacer en dernier\"),
        (\"Align left\", \"Aligner à gauche\"),
        (\"Align center\", \"Aligner au centre\"),
        (\"Align right\", \"Aligner à droite\"),
        (\"Sort\", \"Trier\"),
        (\"Filter\", \"Filtrer\"),
        (\"Export\", \"Exporter\"),
        (\"Delete selected rows\", \"Supprimer les lignes sélectionnées\"),
        (\"Sort Ascending\", \"Tri ascendant\"),
        (\"Sort Descending\", \"Tri descendant\"),
        (\"Clear filters\", \"Effacer les filtres\"),
        (\"Filter by cell's value\", \"Filtrer par valeur de cellules\"),
        (\"Hide select rows\", \"Cacher les lignes sélectionnées\"),
        (\"Show only select rows\", \"N’afficher que les lignes sélectionnées\"),
        (\"Export all records\", \"Exporter tous les enregistrements\"),
        (\"Export current page\", \"Exporter la page active\"),
        (\"Export current selection\", \"Exporter la sélection\"),
        (\"Export records in filter\", \"Exporter les enregistrements filtrés\"),
        (\"Move up\", \"Déplacer vers le haut\"),
        (\"Move down\", \"Déplacer vers le bas\"),
        (\"Move to top\", \"Déplacer en premier\"),
        (\"Move to bottom\", \"Déplacer en dernier\"),
        (\"Mo\", \"Lu\"),
        (\"Tu\", \"Ma\"),
        (\"We\", \"Me\"),
        (\"Th\", \"Je\"),
        (\"Fr\", \"Ve\"),
        (\"Sa\", \"Sa\"),
        (\"Su\", \"Di\"),
    )
)
""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/themes/__init__.py": """""",
    
    "ttkbootstrap-python3.6/ttkbootstrap/themes/standard.py": """STANDARD_THEMES = {
    \"cosmo\": {
        \"type\": \"light\",
        \"colors\": {
            \"primary\": \"#2780e3\",
            \"secondary\": \"#7E8081\",
            \"success\": \"#3fb618\",
            \"info\": \"#9954bb\",
            \"warning\": \"#ff7518\",
            \"danger\": \"#ff0039\",
            \"light\": \"#F8F9FA\",
            \"dark\": \"#373A3C\",
            \"bg\": \"#ffffff\",
            \"fg\": \"#373a3c\",
            \"selectbg\": \"#7e8081\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#ced4da\",
            \"inputfg\": \"#373a3c\",
            \"inputbg\": \"#fdfdfe\",
            \"active\": \"#efefef\",
        },
    },
    \"flatly\": {
        \"type\": \"light\",
        \"colors\": {
            \"primary\": \"#2c3e50\",
            \"secondary\": \"#95a5a6\",
            \"success\": \"#18bc9c\",
            \"info\": \"#3498db\",
            \"warning\": \"#f39c12\",
            \"danger\": \"#e74c3c\",
            \"light\": \"#ECF0F1\",
            \"dark\": \"#7B8A8B\",
            \"bg\": \"#ffffff\",
            \"fg\": \"#212529\",
            \"selectbg\": \"#95a5a6\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#ced4da\",
            \"inputfg\": \"#212529\",
            \"inputbg\": \"#ffffff\",
            \"active\": \"#e2e2e2\",
        },
    },
    \"litera\": {
        \"type\": \"light\",
        \"colors\": {
            \"primary\": \"#4582ec\",
            \"secondary\": \"#adb5bd\",
            \"success\": \"#02b875\",
            \"info\": \"#17a2b8\",
            \"warning\": \"#f0ad4e\",
            \"danger\": \"#d9534f\",
            \"light\": \"#F8F9FA\",
            \"dark\": \"#343A40\",
            \"bg\": \"#ffffff\",
            \"fg\": \"#343a40\",
            \"selectbg\": \"#adb5bd\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#bfbfbf\",
            \"inputfg\": \"#343a40\",
            \"inputbg\": \"#fff\",
            \"active\": \"#e5e5e5\",
        },
    },
    \"minty\": {
        \"type\": \"light\",
        \"colors\": {
            \"primary\": \"#78c2ad\",
            \"secondary\": \"#f3969a\",
            \"success\": \"#56cc9d\",
            \"info\": \"#6cc3d5\",
            \"warning\": \"#ffce67\",
            \"danger\": \"#ff7851\",
            \"light\": \"#F8F9FA\",
            \"dark\": \"#343A40\",
            \"bg\": \"#ffffff\",
            \"fg\": \"#5a5a5a\",
            \"selectbg\": \"#f3969a\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#ced4da\",
            \"inputfg\": \"#696969\",
            \"inputbg\": \"#fff\",
            \"active\": \"#e5e5e5\",
        },
    },
    \"lumen\": {
        \"type\": \"light\",
        \"colors\": {
            \"primary\": \"#158cba\",
            \"secondary\": \"#919191\",
            \"success\": \"#28b62c\",
            \"info\": \"#75caeb\",
            \"warning\": \"#ff851b\",
            \"danger\": \"#ff4136\",
            \"light\": \"#F6F6F6\",
            \"dark\": \"#555555\",
            \"bg\": \"#ffffff\",
            \"fg\": \"#555555\",
            \"selectbg\": \"#919191\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#ced4da\",
            \"inputfg\": \"#555555\",
            \"inputbg\": \"#fff\",
            \"active\": \"#e5e5e5\",
        },
    },
    \"sandstone\": {
        \"type\": \"light\",
        \"colors\": {
            \"primary\": \"#325D88\",
            \"secondary\": \"#8e8c84\",
            \"success\": \"#93c54b\",
            \"info\": \"#29abe0\",
            \"warning\": \"#f47c3c\",
            \"danger\": \"#d9534f\",
            \"light\": \"#F8F5F0\",
            \"dark\": \"#3E3F3A\",
            \"bg\": \"#ffffff\",
            \"fg\": \"#3e3f3a\",
            \"selectbg\": \"#8e8c84\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#ced4da\",
            \"inputfg\": \"#6E6D69\",
            \"inputbg\": \"#fff\",
            \"active\": \"#e5e5e5\",
        },
    },
    \"yeti\": {
        \"type\": \"light\",
        \"colors\": {
            \"primary\": \"#008cba\",
            \"secondary\": \"#707070\",
            \"success\": \"#43ac6a\",
            \"info\": \"#5bc0de\",
            \"warning\": \"#e99002\",
            \"danger\": \"#f04124\",
            \"light\": \"#EEEEEE\",
            \"dark\": \"#222222\",
            \"bg\": \"#ffffff\",
            \"fg\": \"#222222\",
            \"selectbg\": \"#707070\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#cccccc\",
            \"inputfg\": \"#222222\",
            \"inputbg\": \"#fff\",
            \"active\": \"#e5e5e5\",
        },
    },
    \"pulse\": {
        \"type\": \"light\",
        \"colors\": {
            \"primary\": \"#593196\",
            \"secondary\": \"#69676E\",
            \"success\": \"#13b955\",
            \"info\": \"#009cdc\",
            \"warning\": \"#efa31d\",
            \"danger\": \"#fc3939\",
            \"light\": \"#F9F8FC\",
            \"dark\": \"#17141F\",
            \"bg\": \"#ffffff\",
            \"fg\": \"#444444\",
            \"selectbg\": \"#69676e\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#cbc8d0\",
            \"inputfg\": \"#444444\",
            \"inputbg\": \"#fdfdfe\",
            \"active\": \"#e5e5e5\",
        },
    },
    \"united\": {
        \"type\": \"light\",
        \"colors\": {
            \"primary\": \"#e95420\",
            \"secondary\": \"#aea79f\",
            \"success\": \"#38b44a\",
            \"info\": \"#17a2b8\",
            \"warning\": \"#efb73e\",
            \"danger\": \"#df382c\",
            \"light\": \"#E9ECEF\",
            \"dark\": \"#772953\",
            \"bg\": \"#ffffff\",
            \"fg\": \"#333333\",
            \"selectbg\": \"#aea79f\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#ced4da\",
            \"inputfg\": \"#333333\",
            \"inputbg\": \"#fff\",
            \"active\": \"#e5e5e5\",
        },
    },
    \"morph\": {
        \"type\": \"light\",
        \"colors\": {
            \"primary\": \"#378DFC\",
            \"secondary\": \"#aaaaaa\",
            \"success\": \"#43cc29\",
            \"info\": \"#5B62F4\",
            \"warning\": \"#FFC107\",
            \"danger\": \"#E52527\",
            \"light\": \"#F0F5FA\",
            \"dark\": \"#212529\",
            \"bg\": \"#D9E3F1\",
            \"fg\": \"#7B8AB8\",
            \"selectbg\": \"#aaaaaa\",
            \"selectfg\": \"#FBFDFF\",
            \"border\": \"#B9C7DA\",
            \"inputfg\": \"#7F8EBA\",
            \"inputbg\": \"#F0F5FA\",
            \"active\": \"#C3CCD8\",
        },
    },
    \"journal\": {
        \"type\": \"light\",
        \"colors\": {
            \"primary\": \"#eb6864\",
            \"secondary\": \"#aaaaaa\",
            \"success\": \"#22b24c\",
            \"info\": \"#336699\",
            \"warning\": \"#f5e625\",
            \"danger\": \"#f57a00\",
            \"light\": \"#F8F9FA\",
            \"dark\": \"#222222\",
            \"bg\": \"#ffffff\",
            \"fg\": \"#222222\",
            \"selectbg\": \"#aaaaaa\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#ced4da\",
            \"inputfg\": \"#565656\",
            \"inputbg\": \"#fff\",
            \"active\": \"#e5e5e5\",
        },
    },
    \"darkly\": {
        \"type\": \"dark\",
        \"colors\": {
            \"primary\": \"#375a7f\",
            \"secondary\": \"#444444\",
            \"success\": \"#00bc8c\",
            \"info\": \"#3498db\",
            \"warning\": \"#f39c12\",
            \"danger\": \"#e74c3c\",
            \"light\": \"#ADB5BD\",
            \"dark\": \"#303030\",
            \"bg\": \"#222222\",
            \"fg\": \"#ffffff\",
            \"selectbg\": \"#555555\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#222222\",
            \"inputfg\": \"#ffffff\",
            \"inputbg\": \"#2f2f2f\",
            \"active\": \"#1F1F1F\",
        },
    },
    \"superhero\": {
        \"type\": \"dark\",
        \"colors\": {
            \"primary\": \"#4c9be8\",
            \"secondary\": \"#4e5d6c\",
            \"success\": \"#5cb85c\",
            \"info\": \"#5bc0de\",
            \"warning\": \"#f0ad4e\",
            \"danger\": \"#d9534f\",
            \"light\": \"#ABB6C2\",
            \"dark\": \"#20374C\",
            \"bg\": \"#2b3e50\",
            \"fg\": \"#ffffff\",
            \"selectbg\": \"#526170\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#222222\",
            \"inputfg\": \"#ebebeb\",
            \"inputbg\": \"#32465a\",
            \"active\": \"#2B4155\",
        },
    },
    \"solar\": {
        \"type\": \"dark\",
        \"colors\": {
            \"primary\": \"#bc951a\",
            \"secondary\": \"#94a2a4\",
            \"success\": \"#44aca4\",
            \"info\": \"#3f98d7\",
            \"warning\": \"#d05e2f\",
            \"danger\": \"#d95092\",
            \"light\": \"#A9BDBD\",
            \"dark\": \"#073642\",
            \"bg\": \"#002B36\",
            \"fg\": \"#ffffff\",
            \"selectbg\": \"#0b5162\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#00252e\",
            \"inputfg\": \"#A9BDBD\",
            \"inputbg\": \"#073642\",
            \"active\": \"#002730\",
        },
    },
    \"cyborg\": {
        \"type\": \"dark\",
        \"colors\": {
            \"primary\": \"#2a9fd6\",
            \"secondary\": \"#555555\",
            \"success\": \"#77b300\",
            \"info\": \"#9933cc\",
            \"warning\": \"#ff8800\",
            \"danger\": \"#cc0000\",
            \"light\": \"#ADAFAE\",
            \"dark\": \"#222222\",
            \"bg\": \"#060606\",
            \"fg\": \"#ffffff\",
            \"selectbg\": \"#454545\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#060606\",
            \"inputfg\": \"#ffffff\",
            \"inputbg\": \"#191919\",
            \"active\": \"#282828\",
        },
    },
    \"vapor\": {
        \"type\": \"dark\",
        \"colors\": {
            \"primary\": \"#6e40c0\",
            \"secondary\": \"#ea38b8\",
            \"success\": \"#3af180\",
            \"info\": \"#1da2f2\",
            \"warning\": \"#ffbd05\",
            \"danger\": \"#e34b54\",
            \"light\": \"#44d7e8\",
            \"dark\": \"#170229\",
            \"bg\": \"#190831\",
            \"fg\": \"#32fbe2\",
            \"selectbg\": \"#461a8a\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#060606\",
            \"inputfg\": \"#bfb6cd\",
            \"inputbg\": \"#30115e\",
            \"active\": \"#17082E\",
        },
    },
    \"simplex\": {
        \"type\": \"light\",
        \"colors\": {
            \"primary\": \"#d8220e\",
            \"secondary\": \"#858e96\",
            \"success\": \"#469307\",
            \"info\": \"#0099ce\",
            \"warning\": \"#d88220\",
            \"danger\": \"#9a479e\",
            \"light\": \"#f2f2f2\",
            \"dark\": \"#3b3d3f\",
            \"bg\": \"#fcfcfc\",
            \"fg\": \"#3b3d3f\",
            \"selectbg\": \"#a9afb6\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#858e96\",
            \"inputfg\": \"#3b3d3f\",
            \"inputbg\": \"#fcfcfc\",
            \"active\": \"#e2e2e2\",
        },
    },
    \"cerculean\": {
        \"type\": \"light\",
        \"colors\": {
            \"primary\": \"#4bb1ea\",
            \"secondary\": \"#a9b4be\",
            \"success\": \"#84b251\",
            \"info\": \"#225384\",
            \"warning\": \"#e16e25\",
            \"danger\": \"#cf3c40\",
            \"light\": \"#eceef1\",
            \"dark\": \"#33383e\",
            \"bg\": \"#ffffff\",
            \"fg\": \"#2ea4e7\",
            \"selectbg\": \"#adb5bd\",
            \"selectfg\": \"#ffffff\",
            \"border\": \"#a9b4be\",
            \"inputfg\": \"#495057\",
            \"inputbg\": \"#ffffff\",
            \"active\": \"#e5e5e5\",
        },
    },
}
""",
     
}

for d in dirs:
    d = (output_root/d).resolve()
    print("Created Directory:", d)
    d.mkdir(exist_ok=True, parents=True)

for f, t in files.items():
    f = (output_root/f).resolve()
    print("Created File:", f)
    f.write_text(t)
