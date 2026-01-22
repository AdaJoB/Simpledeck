import os
from markdown_it import MarkdownIt

md = MarkdownIt()

# directory list
BASE_DIR = '.'
DIR_LIST = os.listdir(BASE_DIR)
SUBDIR_LIST = [name for name in DIR_LIST if os.path.isdir(os.path.join(BASE_DIR, name)) and name[0]!='.'] # list of directories that are not hidden

# gets user directory/file input
def select(prompt_type, base, dir_list): # type=input phrase, base=path containing choice, list=list of choices for user
    print(*dir_list, sep='\n')
    choice = input(f'Select a {prompt_type}: ')
    print()
    path = os.path.join(base, choice)
    return path

# finds markdown files from input directory
def find_md(path):
    path_files = os.listdir(path)
    md_list = [name for name in path_files if name.endswith('.md')]
    return md_list

# open markdown file
def open_md(md_in):
    print(md_in)
    tokens = md.parse(open(md_in).read())


dir_in = select('directory', BASE_DIR, SUBDIR_LIST)
md_list = find_md(dir_in)
md_in = select('markdown file', dir_in, md_list)
open_md(md_in)