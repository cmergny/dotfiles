call plug#begin('~/.vim/plugged')
	":FloatermNew fzf For file
	"Plug 'preservim/nerdtree'
	"Plug 'Xuyuanp/nerdtree-git-plugin'
	"Plug 'ryanoasis/vim-devicons'
	Plug 'itchyny/lightline.vim'
	" Theme
	Plug 'morhetz/gruvbox'
	" For autocompletion
	Plug 'neoclide/coc.nvim', {'branch': 'release'}
	Plug 'neoclide/coc-tsserver', {'do': 'yarn install --frozen-lockfile'}
	"Snippets
	Plug 'SirVer/ultisnips'
	Plug 'honza/vim-snippets'
	"For using cocvim and snippets
	Plug 'ervandew/supertab' 
	"Fuzzy Files Finder
	Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
	Plug 'junegunn/fzf.vim'
	"FloatingTerminal
	Plug 'voldikss/vim-floaterm'
	"Auto close brackets
	Plug 'Raimondi/delimitMate'
	"To comment blocks
	Plug 'tpope/vim-commentary'
call plug#end()

colorscheme gruvbox
let mapleader = " "
nnoremap <SPACE> <Nop>
set encoding=utf-8
set hidden	
set updatetime=300 
set number	
set belloff=all	
set tabstop=4
set shiftwidth=4
set autoindent	
set incsearch
set hlsearch
set nocompatible 
set background=dark
set nowrap
set noswapfile
set nobackup
set nowritebackup
set undofile
set undodir=~/.vim/undodir
set laststatus=2

" MAPPING
" Change windows easely
nnoremap <c-j> <c-w>j
nnoremap <c-k> <c-w>k
nnoremap <c-h> <c-w>h
nnoremap <c-l> <c-w>l
" Indent in visual keeps the selection
vnoremap < <gv
vnoremap > >gv
" FZF config
nmap <leader>ff :Files <CR>
nmap <leader>fb :Buffers <CR>
nmap <leader>tt :FloatermNew <CR>
nmap <leader>tk :FloatermKill <CR>
" Open vimrc quickly
nmap <leader>vv :e ~/.vim/vimrc <CR>  
"Resize windows
nmap <M-Right> :vertical resize +1<CR>
nmap <M-Left> :vertical resize -1<CR>
nmap <M-Down> :resize +1<CR>
nmap <M-Up> :resize -1<CR>

"Hide tildes on blanck lines
highlight EndOfBuffer ctermfg=bg

" Make vertical separator pretty
highlight VertSplit cterm=NONE
set fillchars+=vert:\▏

"Netrw file browser
let g:netrw_banner = 0
let g:netrw_winsize = 20

" GoTo code navigation.
nmap <silent> gd <Plug>(coc-definition)

" Coc vim config
let g:coc_global_extensions = ['coc-snippets', 'coc-json', 'coc-browser', 'coc-css', 'coc-eslint', 'coc-html', 'coc-sh', 'coc-pyright', 'coc-highlight']
