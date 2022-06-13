if status is-interactive
    # Commands to run in interactive sessions can go here
end

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
eval /opt/miniconda3/bin/conda "shell.fish" "hook" $argv | source
conda activate ice
# <<< conda initialize <<<

# Start X at login
if status --is-login
  if test -z "$DISPLAY" -a $XDG_VTNR = 1
      exec startx -- -keeptty
	    end
		end

# Aliases
alias vpnsaclay 'sudo openconnect --protocol=gp -u cyril.mergny vpn.universite-paris-saclay.fr'
alias startssh 'eval (ssh-agent -c) and ssh-add ~/.ssh/gitlab_rsa'
