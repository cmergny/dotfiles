# Xorg
Installer un driver proprietaire nvidia cause des pbms. Cela réécrit les fichiers confs et peut causer des crashs.

# Zathura
Looking for annotations ?

# SSH
ssh-agent: program to hold private/public keys authentification.
Need to start the program in the background with command 
	eval "ssh-agent"

# Fonts
I liked the X11 misc font 6x13 but was a bitmap font.
So I found a repo on git: https://github.com/dse/xorg-monospace-fonts-ttf/tree/master/ttf/misc-fixed
where the guy created the ttf (truetype) equivalent. Useful to use in polhybar for exemple.

# Rofi
Should add rofi to dotfiles

# Git
git checkout branchname: permet de changer de branch
git resert HEAD~1 --hard : permet de revenir un commit en arriere
Pbm de demande de login lors de git push: il fallait changer le .git/config 
l'adresse https doit etre changé en ssh (voir net).

# Anaconda
AUR package install with yay on arch
use source /opt/anaconda/bin/activate root to activate 

# Tex
Installer texlive pour avoir compiler latex

# Matlab
bin/activate_matlab pour lancer l'activation de licences
libgconf necessaire pour que ca marche

# CMake, Make 
Manages the build process of softwares using compiler independant method.
To compile: in the CMakeList.txt folder run "cmake ." it should create the build.
To buid: in the same dir run "make"
To install on system: "sudo make install"

# Compiling in C++
To compile a C code called "test.c" run in the same folder "make test" or "gcc test"
Then run the generated file with "./test"
With snowpack when a .cc file is change I run "make" in the parent dir and then "sudo make install" in same dir.

# Vim
ultisnips snippets engine
vim-snippets library of many languages snippets
use ctrl-j ctrl-k to navigate inside snippet
coc-vimtex, coc-snippets required
