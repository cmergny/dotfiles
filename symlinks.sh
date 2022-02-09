#!/bin/bash
mkdir -p  ~/.dotfiles_old
mkdir -p  ~/.config

folders="alacritty compton dunst i3 polybar zathura"

# ln -sfv ~/dotfiles/bashrc ~/.bashrc
# ln -sfv ~/dotfiles/vim/ ~/.vim

for folder in $folders; do
	mv -vf ~/.config/$folder ~/.dotfiles_old/
	# rm -rfv  ~/dotfiles/config/$folder/$folder
	ln -sv ~/dotfiles/config/$folder ~/.config/$folder
done
