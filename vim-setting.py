#!/usr/bin/env python

import os
from os.path import expanduser

home = expanduser("~")

if not os.path.isdir(home + '/.vim'):
    os.system('mkdir ~/.vim')

if not os.path.isdir(home + '/.vim/colors'):
    os.system('mkdir ~/.vim/colors')

if not os.path.isdir(home + '/.vim/syntax'):
    os.system('mkdir ~/.vim/syntax')

os.system('cp ./c.vim ~/.vim/syntax/c.vim')
os.system('cp ./python.vim ~/.vim/syntax/python.vim')
os.system('cp ./Sublime-Like-Vim.vim ~/.vim/colors/Sublime-Like-Vim.vim')

opt = []
opt.append('set mouse=a')
opt.append('set nu')
opt.append('set ai')
opt.append('syntax enable')
opt.append('colorscheme Sublime-Like-Vim')
opt.append('set backspace=indent,eol,start')

if not os.path.isfile(home + '/.vimrc'):
    os.system('>~/.vimrc')

with open(home + '/.vimrc','r') as f:
    vimrc = f.read()

for option in opt:
    if (vimrc.find(option) == -1):
        os.system('echo "' + option + '" >> ~/.vimrc')

print 'Completed Sublime-Like-Vim install with no error.'
