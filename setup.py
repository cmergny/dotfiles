import os
import subprocess

### FUNCTIONS

class Linker:
    
    def __init__(self, home, folders):
        self.home = home
        self.folders = folders
        self.oldpath = f"{self.home}/.oldotfiles"
        self.dotpath = f"{self.home}/.dotfiles"
        self.confpath = f"{self.home}/.config"
        self.already = []
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
        self.print_msg()

    def print_msg(self):
        msg = ""
        for word in self.already:
            msg += word + ","
        msg = msg[:-1]
        print(f"{self.symbol} The following symlinks already existed :")
        print(f"\t {msg}")
        
    def create_dir(self, path):
        try:
            os.mkdir(path)
        except OSError:
            print(f"{self.symbol} Backup folder is at {path}") 

    def run_cmd(self, cmd):
        cmd = cmd.split(" ")
        out = subprocess.run(cmd)
        return(out)

    def mv_oldconf(self, confpath):
        """backup previous conf by moving it elsewhere."""
        exist = os.path.isdir(confpath)
        if exist:
            print(confpath)
            cmd = f"mv -f {confpath} {self.oldpath}"
            subprocess.run(cmd, shell=True)
            print(f"{self.symbol} Moved {self.folder} to {self.oldpath}.")

    def create_symlink(self, src, dst):
        """Make a symlink if there is not one already."""
        # Check if link exists
        exist = os.path.islink(dst)
        if exist: # count the nbr of already existing links
            self.already.append(self.folder)
        # Make symlink
        else:
            self.mv_oldconf(dst)
            self.run_cmd(f"ln -s {dst} {src}")
            print(f"{self.symbol} Created symlink {src} -> {dst}")

### MAIN

if __name__ == "__main__":

    home = "/home/cmergny"
    folders = ["alacritty", "compton", "dunst", "i3",
        "polybar", "zathura", "fish"]

    linker = Linker(home, folders)
    linker.make_links()

