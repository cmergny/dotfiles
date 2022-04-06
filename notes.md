# Xorg
Installer un driver proprietaire nvidia cause des pbms. Cela réécrit les fichiers confs et peut causer des crashs.
Mouse and keyboard not detected after startx : pas besoin de changer xorg.conf il fallait installer xf86-input-evdev

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


## C++
# CMake, Make 
Manages the build process of softwares using compiler independant method.
To compile: in the CMakeList.txt folder run "cmake ." it should create the build.
To buid: in the same dir run "make"
To install on system: "sudo make install"
# Compiling in C++
To compile a C code called "test.c" run in the same folder "make test" or "gcc test"
Then run the generated file with "./test"
With snowpack when a .cc file is change I run "make" in the parent dir and then "sudo make install" in same dir.
# C++ pointers
The operator * is used to deference a pointer.
Deferencing means getting the value stroed in the  memory location pointed by the pointer.
example:
int a = 10;
int* ptr = &a;
The unary prefix operator &, when applied to an object, yields the address of the object.
Modern C++ provides smart pointers for allocating objects, iterators for traversing data structures
# C++ size t
Used to define a variable (most often int) of unknown size
std::size_t is commonly used for array indexing and loop counting. 
# C++ try/throw
Do code unless exeception given at then end of try{} with "catch".

## Vim
ultisnips snippets engine
vim-snippets library of many languages snippets
use ctrl-j ctrl-k to navigate inside snippet
coc-vimtex, coc-snippets required
# Wrapping
set wrap
set breakindent
set formatoptions=l
set lbr # linebreak ?

# Run sh output to a file
./script.sh > file

