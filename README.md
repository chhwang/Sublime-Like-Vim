Sublime-Like-Vim
================

This repository makes sublime-text-like Vim environment for Ubuntu based on refined monokai colorscheme.

Current version only supports C/C++.

Please help to develop this repository.


Install
================
1. Download this repository and execute vim-setting.py, then it's all done.

  CAUTION : vim-setting.py code includes 'rm -r -f ./Sublime-Like-Vim'. If you already have a directory named   "Sublime-Like-Vim", don't execute vim-setting.py on that path.

  If you have any problem executing vim-setting.py, you can just follow step 4 and 5 to install.


2. I recommand you to use YouCompleteMe.
  
  Link to YouCompleteMe repository : https://github.com/Valloric/YouCompleteMe

  This link clearly explains how to install : http://christopherpoole.github.io/setting-up-vim-with-YouCompleteMe/


3. I recommand you to use Ctags. To install Ctags:

  sudo apt-get install ctags
  
  
4. On the terminal:
  
  mkdir ~/SLV
  
  cd ~/SLV/
  
  git init
  
  git clone https://github.com/ysokcs/Sublime-Like-Vim
  
  cd Sublime-Like-Vim

  mkdir ~/.vim/syntax
  
  mkdir ~/.vim/colors

  cp c.vim ~/.vim/syntax/c.vim
  
  cp Sublime-Like-Vim.vim ~/.vim/colors/Sublime-Like-Vim.vim
  

5. Write this at the bottom of your ~/.vimrc file:

  set nu
  
  set ai
  
  syntax enable
  
  colorscheme Sublime-Like-Vim
  
  set backspace=indent,eol,start
  
  
