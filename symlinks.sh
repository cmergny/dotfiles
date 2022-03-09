#!/bin/bash
mkdir -p  ~/.dotfiles_old
mkdir -p  ~/.config

folders="alacritty compton dunst i3 polybar zathura"

# Save previous files in a backup dir
mv -f ~/.vim ~/.dotfiles_old/vim
mv -f ~/.bashrc ~/.dotfiles_old/
# Create symlinks
ln -s ~/dotfiles/bashrc ~/.bashrc
ln -s ~/dotfiles/vim/ ~/.vim

for folder in $folders; do
	mv -f ~/.config/$folder ~/.dotfiles_old/
	# rm -rfv  ~/dotfiles/config/$folder/$folder
	echo "Symlinking $folder"
	ln -s ~/dotfiles/config/$folder ~/.config/$folder
done
