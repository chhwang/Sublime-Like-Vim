#!/usr/bin/env python

import os
from os.path import expanduser

if not os.path.isdir('./Sublime-Like-Vim'):
    os.system('mkdir ./Sublime-Like-Vim')

if not os.path.isdir('~/.vim'):
    os.system('mkdir ~/.vim')

if not os.path.isdir('~/.vim/colors'):
    os.system('mkdir ~/.vim/colors')

if not os.path.isdir('~/.vim/syntax'):
    os.system('mkdir ~/.vim/syntax')

os.system('wget -P ./Sublime-Like-Vim https://github.com/ysocks/Sublime-Like-Vim/archive/master.zip')
os.system('unzip ./Sublime-Like-Vim/master.zip -d ./Sublime-Like-Vim')
os.system('cp ./Sublime-Like-Vim/Sublime-Like-Vim-master/c.vim ~/.vim/syntax/c.vim')
os.system('cp ./Sublime-Like-Vim/Sublime-Like-Vim-master/Sublime-Like-Vim.vim ~/.vim/colors/Sublime-Like-Vim.vim')
os.system('rm -r -f ./Sublime-Like-Vim')

opt = []
opt.append('set mouse=a')
opt.append('set nu')
opt.append('set ai')
opt.append('syntax enable')
opt.append('colorscheme Sublime-Like-Vim')
opt.append('set backspace=indent,eol,start')

if not os.path.isfile('~/.vimrc'):
    os.system('>~/.vimrc')

home = expanduser("~")

with open(home+'/.vimrc','r') as f:
    vimrc = f.read()

for option in opt:
    if (vimrc.find(option) == -1):
        os.system('echo "'+option+'" >> ~/.vimrc')

