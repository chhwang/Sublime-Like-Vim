Sublime-Like-Vim
================

This repository makes sublime-text-like Vim environment for Ubuntu based on refined monokai colorscheme.

Current version only supports C/C++.

Please help to develop this repository.


Install
================

1. I recommand you to use YouCompleteMe.
  
  Link to YouCompleteMe repository : https://github.com/Valloric/YouCompleteMe

  This link clearly explains how to install : http://christopherpoole.github.io/setting-up-vim-with-YouCompleteMe/



2. I recommand you to use Ctags. To install Ctags:

  sudo apt-get install ctags
  
  
3. On the terminal:
  
  mkdir ~/Sublime-Like-Vim
  
  cd ~/Sublime-Like-Vim/
  
  git init
  
  git clone https://github.com/ysokcs/Sublime-Like-Vim
  
  cp c.vim ~/.vim/syntax/c.vim
  
  cp Sublime-Like-Vim.vim ~/.vim/colors
  

4. Write this at the bottom of your ~/.vimrc file:

  set nu
  
  set ai
  
  syntax enable
  
  colorscheme Sublime-Like-Vim
  
  set backspace=indent,eol,start
  
  
