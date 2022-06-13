"""
Setup script to create all the symlink necessary for the config files.
Author: C. Mergny
Date: June 2022
"""

### IMPORTS

import os
import subprocess

### FUNCTIONS

class Linker:
    
    def __init__(self, home, folders):
        self.home = home
        self.folders = folders
        self.oldpath = f"{self.home}/.oldotfiles"
        self.dotpath = f"{self.home}/dotfiles"
        self.confpath = f"{self.home}/.config"
        self.already = []
        self.count = 0
        self.symbol = "  >"

    def make_links(self):
        """Create symlinks for all configs"""
        print("Symlinking dotfiles...")
        # Make a backup dir if do not exist
        self.create_dir(self.oldpath)
        # Loop through all configs
        for folder in self.folders:
            self.folder = folder
            src = f"{self.dotpath}/config/{folder}"
            dst = f"{self.confpath}/{folder}"
            self.create_symlink(src, dst)
        # Vim
        self.folder = "vim"
        src = f"{self.dotpath}/{self.folder}"
        dst = f"{self.home}/.{self.folder}"
        self.create_symlink(src, dst)
        # Bashrc
        self.folder = "bashrc"
        src = f"{self.dotpath}/{self.folder}"
        dst = f"{self.home}/.{self.folder}"
        self.create_symlink(src, dst)
        # Print msg
        self.print_msg()

    def print_msg(self):
        """Just for log msgs in the end of the script."""
        msg = ""
        for word in self.already:
            msg += word + " "
        msg = msg[:-1]
        print(f"{self.symbol} The following symlinks already existed :")
        print(f"\t {msg}")
        if self.count == 0:
            print("\033[32mNothing needed to be changed.\033[0m")
        print("Done \033[32m✓\033[0m")
        
    def create_dir(self, path):
        """Make a backup dir if it doesnt already exist."""
        try:
            os.mkdir(path)
            print(f"{self.symbol} Created backup folder at {path}") 
        except OSError:
            print(f"{self.symbol} Backup folder is at {path}") 

    def run_cmd(self, cmd):
        """Convert cmd string to list of words and call subprocess."""
        cmd = cmd.split(" ")
        out = subprocess.run(cmd)
        return(out)

    def mv_oldconf(self, dst):
        """Backup previous conf by moving it elsewhere."""
        exist = os.path.isdir(dst)
        if exist:
            cmd = f"rsync -a {dst} {self.oldpath}"
            subprocess.run(cmd, shell=True)
            cmd = f"rm -rf {dst}"
            subprocess.run(cmd, shell=True)
            print(f"{self.symbol} Moved prev {self.folder} conf to backup folder.")

    def create_symlink(self, src, dst):
        """Make a symlink if there is not one already."""
        # Check if link exists
        exist = os.path.islink(dst)
        if exist: # count the nbr of already existing links
            self.already.append(self.folder)
        # Make symlink
        else:
            self.count += 1
            self.mv_oldconf(dst)
            destination = self.confpath
            if self.folder in ["vim", "bashrc"]:
                destination = dst
            out = os.system(f"ln -s {src} {destination}")
            if out == 0:
                print(f"\033[33m{self.symbol} Created symlink {destination} -> {src}\033[0m")

### MAIN

if __name__ == "__main__":

    home = "/home/cmergny"
    folders = ["alacritty", "compton", "dunst", "i3",
        "polybar", "zathura", "fish"]

    linker = Linker(home, folders)
    linker.make_links()

