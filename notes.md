# Xorg
# Which config file uses startx
There are two paths but the one startx actually uses is ~/.xinitrc
# Nvidia driver install
Works well for new drivers (dell xps 17 uses version NV167).
just install the drivers: sudo pacman -S nvidia nvidia-utils nvidia-settings
reboot
then install optimus manager poru hybrid GPU intel/nvidia
yay -S optimus-manager
reboot
Change ~/.xinitrc as shown in https://dev.to/snikhill/optimus-manager-on-arch-linux-1589
specify startup mode in /etc/optimus-manager/optimus-manager.conf
# Driver pour archgeops
Installer un driver proprietaire nvidia cause des pbms. Cela réécrit les fichiers confs et peut causer des crashs.
Mouse and keyboard not detected after startx : pas besoin de changer xorg.conf il fallait installer xf86-input-evdev
## Automatic startx
put this in fish shell: 
if status --is-login
  if test -z "$DISPLAY" -a $XDG_VTNR = 1
        exec startx -- -keeptty
			    end
						end

# Zathura
Looking for annotations ? -> Zathura is not made for that

# Arch Linux Install
## AUDIO not working for dell xps
The ONLY solution that work was found at: https://bbs.archlinux.org/viewtopic.php?id=186597
you need to create a new file with sudo vim /etc/modprobe.d/50-alsa.conf 
and exactly this name! Inside the file write these two lines bw the quotes:
"
options snd_hda_intel enable=1 index=0
options snd_hda_intel index=1
"
Note that all other solutions found on the net were tested and did not work.

# SSH
ssh-agent: program to hold private/public keys authentification.
Need to start the program in the background with command 
	eval "ssh-agent"
## Xforwarding (graphical interface)
Need to change some options in /etc/ssh/sshd_config, see:
https://wiki.archlinux.org/title/OpenSSH#Step_2_(Variant_B):_set_up_a_local_TUN_interface

# Fonts
I liked the X11 misc font 6x13 but was a bitmap font.
So I found a repo on git: https://github.com/dse/xorg-monospace-fonts-ttf/tree/master/ttf/misc-fixed
where the guy created the ttf (truetype) equivalent. Useful to use in polhybar for exemple.

# Dotfiles
# Managing slightly diff dots
In case you need dotfiles for diff hosts you'll probably want to slightly change some settings.
For exemple, the font size on Alacritty.
It's a problem bc with git it means you'd have to create a diff branch each team.
To solve this there exist smth called templating that enables to have a single config file but with blocks proper to each hosts.
For more, see arch wiki on dotfiles and  https://github.com/deadc0de6/dotdrop
# Rofi
Should add rofi to dotfiles

# Git
## Change branch
git checkout branchname: permet de changer de branch
git resert HEAD~1 --hard : permet de revenir un commit en arriere
## Login to push
Pbm de demande de login lors de git push: il fallait changer le .git/config 
l'adresse https doit etre changé en ssh (voir net).
## Go to previous commit
see : https://stackoverflow.com/questions/4114095/how-do-i-revert-a-git-repository-to-a-previous-commit
git checkout 0d1d7fc32
if you want to create new branch
git checkout -b old-state 0d1d7fc32
## Git stable version tag
git tag: list all tags
to create a tag do git tag -a v1.0 -m "my version1.0"
You can also tag a version as stable, like "v1.0" or something, exactly like he said 
Here's the git command to do that: 
https://git-scm.com/book/en/v2/Git-Basics-Tagging
It gives you the ability to revert directly to the stable version by checking it out

# Anaconda
AUR package install with yay on arch
use /opt/miniconda3/bin/conda init to put conda in path.
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

# Unix Shell
Bash(default), Fish or Zsh
# Greyed autosuggestion
Terminal showing greyed text suggestion after writting the start of a command (ex: "ssh" adds in grey "host@truc").
This is a fish shell feature, not really available in bash.
https://apple.stackexchange.com/questions/140758/terminal-iterm-autocomplete-greyed-functionality
# fish config
Make sure defaut browser is set when running the command. 
Make sure python env is fully deactivated or activated because the command uses python packages.
# Prompt 
I use Terlar.
# Fish vi keybindings
You can have normal and insert mode in the shell with  fish_vi_key_bindings
go back to default with fish_default_key_bindings
To have my current vim mode displayed in prompt. Either modify file in  /usr/share/fish/functions/fish_default_mode_prompt.fish
Or run fish_config got to functions and find fish_default_mode_prompt
# Conda autoenv
added conda activate (envname) to my bashrc

# Alacritty
Alacritty is a GPU-accelerated terminal emulator.

# Tmux
 tmux is  a so-called terminal multiplexer. Simply speaking, tmux acts as a window manager within your terminal1 and allows you to create multiple windows and panes within a single terminal window.
 
# ETHERNET 
Cable connected but not internet : to solve go to gnome control center. Onglet Network.
The cable oscilated bw plugged and unplugged. J'ai fait 'oublier cette connection reseau' dans les settings du wired.
Puis restart network manager "sudo systemctl restart NetworkManager.service" ou juste un reboot et c'est bon.
# DNS
The Domain Name System is the hierarchical and decentralized naming system used to identify computers reachable through the Internet or other Internet Protocol networks

### Python
# iPython
It is a shell, modified to be used with python.
# Python pdb debugging
paste "import pdb; pdb.set_trace()" in line to mark a breakpoint. 
Then run normally with "python file.py". In pdb use c to continue, p to print etc.
I am using pdb++ which has syntax highlighting and more, see githup repo.
# Decorators
It's a way to modify existing function. It's like if you do the function of a function.
modified_fct = decorator(old_fct)

# Pacman repo
sudo nano /etc/pacman.conf
to include other repos uncomment the line AND the header.

# Steam
install from multilib repo pacman
if font is not displayed:
Try installing lib32-fontconfig, ttf-liberation
## Proton
Proton is by default in steam just need to activate it in settings, steam play.
Rivals:
PROTON_USE_WINED3D11=1 %command%

# Network
use nmcli for connecting to wifi.
if in the tty use iwctl

# Xrandr
Use autorandr for automatic screen detection. Should work out of the box.

# Print paper on arch linux
You need to install cups then enable
sudo systemctl enable cups.service 
and start it
sudo systemctl start cups.service 
then you need to install the driver for your printer: see for exemple https://aur.archlinux.org/packages/brother-dcp1510
and go to the webUI of cups at  http://localhost:631/admin and add the printer here.
Then it should be good.

# DUNST
Just copy pasting the content of a file at :
https://github.com/Godkayaki/dotfiles/blob/main/.config/dunst/dunstrc-mech
into my dunstrc

# ROFI
used a custom theme from git
