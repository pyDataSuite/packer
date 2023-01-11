#!/usr/bin/env python
from pathlib import Path
from argparse import ArgumentParser
from typing import Any, List, Dict
import sys
import os
import jinja2

unpacker_template = """# MIT License
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
        prog="{{ filename }}",
        description=\"""
            This file is a plain-text unpacking tool. Execute it
            to generate a folder structure of plain text files identical
            to the structure of the directory that was used to make this.
        \"""
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
    {% for dir in dirs %}"{{ dir }}",
    {% endfor %}]

files = { 
    {% for file in files %}
    "{{ file.name }}": \"""{{ file.text }}\""",
    {% endfor %} 
}

for d in dirs:
    d = (output_root/d).resolve()
    print("Created Directory:", d)
    d.mkdir(exist_ok=True, parents=True)

for f, t in files.items():
    f = (output_root/f).resolve()
    print("Created File:", f)
    f.write_text(t)

"""

def parse_arguments(args: List[str]) -> Dict[str, Any]:
    """Parses the command-line arguments given to the packer tool"""

    parser = ArgumentParser(
        prog="packer.py",
        description="""
            This tool recursively turns a directory of plain text
            files into a single executable python file which generates
            the given directory. It can be used for transferring large
            sets of files for cases where binary packing methods, like
            .zip files, are not permitted.
        """
    )

    parser.add_argument(
        "directory", 
        type=Path, 
        default=None,
        nargs='?',
        help="""The directory to recursively pack. 
                Defaults to the current working directory."""
    )

    parser.add_argument(
        "-o", "--output", type=Path,
        default=None, help="Path to the output file"
    )

    parser.add_argument(
        "-i", "--ignore", default=[], nargs='+', help="Path components that should be ignored. For example, '__pycache__'"
    )

    return parser.parse_args(args).__dict__

def generate_packed_file(inp: Path, out: Path, ignore_list: List[str], root_dir: Path, print_output=True) -> bool:
    """
    Packs an entire directory of plain text files into one single
    python file
    """

    # out.write_text()

    files = []
    dirs = [inp.name]

    # inp.mkdir(parents=True)
    for item in inp.rglob("*"):
        # Skip any values found in the ignore list
        skip = False
        for ignored in ignore_list:
            if ignored in str(item):
                skip = True
                break
        if skip:
            continue

        # Add dirs
        if item.is_dir():
            dirs.append(item.relative_to(root_dir))
        else:
            files.append({
                'name': str(item.relative_to(root_dir)),
                'text': item.read_text().replace('\\','\\\\').replace('"', '\\"')
            })

        # Print the value
        print( item.relative_to(root_dir) )

    template = jinja2.Template( unpacker_template )
    out.write_text(
        template.render({
            "filename": out.name,
            "files": files,
            "dirs": dirs,
        })
    )

if __name__ == "__main__":
    args = parse_arguments(sys.argv[1:])
    
    # Pre-process the directories
    input_dir: Path = args["directory"]
    output_file: Path = args["output"]
    root_dir = Path()

    if input_dir is None:
        root_dir = Path('..')
        input_dir = Path('..')/Path.cwd().name
    if output_file is None:
        output_file = input_dir.parent/f"{input_dir.name}_packed.py"

    print(f"Packing {input_dir} into {output_file}")
    
    # Actually perform the packing
    generate_packed_file(input_dir, output_file, args["ignore"], root_dir)
