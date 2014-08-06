Sublime-Like-Vim
================

This repository makes sublime-text-like Vim environment for Ubuntu based on refined monokai colorscheme.

Please help to develop this repository.


Install
================

1. I recommand you to use YouCompleteMe.
  
  Link to YouCompleteMe repository : https://github.com/Valloric/YouCompleteMe

  This link clearly explains how to install : http://christopherpoole.github.io/setting-up-vim-with-YouCompleteMe/
  
  If you are going to install YouCompleteMe, you may have to change your Vim install path to compile Vim
  with Python2.x support, so move to next step after checking successful installation of YouCompleteMe.
  
2. I recommand you to use Ctags. To install Ctags:
  sudo apt-get install ctags
  
3. Execute Vim on your terminal and check your Vim install path by typing :echo $VIMRUNTIME.
  Then on the terminal:
  
  mkdir ~/Sublime-Like-Vim
  cd ~/Sublime-Like-Vim/
  git init
  git clone https://github.com/ysokcs/Sublime-Like-Vim
  cp ~/Sublime-Like-Vim/c.vim your/vim/path/c.vim
  cp ~/Sublime-Like-Vim/Sublime-Like-Vim.vim ~/.vim/colors

4. Write this at the bottom of your ~/.vimrc file:
  set nu
  set ai
  syntax enable
  colorscheme Sublime-Like-Vim
  set backspace=indent,eol,start
  
