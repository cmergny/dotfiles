if status is-interactive
    # Commands to run in interactive sessions can go here
end

if [ (prompt_hostname) = "archgeops" ]
	set conda_path /opt/miniconda3/bin/conda
	# >>> conda initialize >>>
	# !! Contents within this block are managed by 'conda init' !!
	eval $conda_path "shell.fish" "hook" $argv | source
	# <<< conda initialize <<<
else
	set conda_path /opt/anaconda/bin/conda
end

# Start X at login
if status --is-login
  if test -z "$DISPLAY" -a $XDG_VTNR = 1
      exec startx -- -keeptty
	    end
		end

# Aliases
alias vpnsaclay 'sudo openconnect --protocol=gp -u cyril.mergny vpn.universite-paris-saclay.fr'
alias startssh 'eval (ssh-agent -c) and ssh-add ~/.ssh/gitlab_rsa'
