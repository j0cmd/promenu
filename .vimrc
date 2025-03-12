"Ativar a sintax colorida"
syntax on

"Ativar a indentação automática"
set autoindent

"Ativar a indentação inteligente, o vim tentará advinhar
"qual e a melhor indentação para o codigo quando voce
"efetuar a quebra de linha, funciona bem para a linguagem c
set smartindent

" mapeia a identação para desativar ou ativar
let g:indentLine_enabled = 1
map <c-k>i :IndentLinesToggle<cr>

"por padrão o vim armazena os ultimos 50 comandos que vc digitou
"para mudar basta modificar.
set history=51

"Ativar numeração de linha
set number

"Destacar a linha que o cursor esta posicionado
set cursorline

"Ativar o cursor do mouse para navegar pelos documentos
set mouse=a

"Ativar o compartilhamento de area de transferenciaentre o vim e a interface
"grafica
set clipboard=unnamedplus

"Converte o tab em espaço em branco ao teclar tab o vim irá substituir por
"dois espaços
set tabstop=2 softtabstop=2 expandtab shiftwidth=2

"Ao teclar a barra de espaço no modo normal o vim irá colapsar ou expandir o
"bloco de codigo do cursor foldlevel é apartir de que nivel de identação o
"codigo iniciará o colapsado
set foldmethod=syntax
set foldlevel=99
nnoremap <space> za

let g:indentline_enabled = 1

" loading the plugin
let g:webdevicons_enable = 1
" adding the flags to NERDTree
let g:webdevicons_enable_nerdtree = 1
" adding the custom source to unite
let g:webdevicons_enable_unite = 1
let g:WebDevIconsOS = 'Lubuntu'

let g:airline_powerline_fonts = 1
map <C-n> :NERDTreeToggle<cr>
set encoding=utf8
" set guifont=HasKlug\ Nerd\ Font\ Propo:21
set guifont=DroidSansM\ Nerd\ Font\ Propo\ 12

set laststatus=2
let g:airline#extensios#tabline#enabled = 1
let g:airline_powerline_fonts = 1
let g:airline_statusline_ontop=0
let g:airline_theme='base16_twilight'

let g:airline#extensions#tabline#formatter = 'default'
" navegação entre os buffers
nnoremap <M-Right> :bn<cr>
nnoremap <M-Left> :bp<cr>
nnoremap <c-x> :bp \|bd #<cr>

" Fechamento automatico de pares"
imap { {}<left>
imap ( ()<left>
imap [ []<left>

inoremap < <><left>
inoremap ' ''<left>
inoremap " ""<left>

" salvamento automatico de arquivo
" 1000 milisegundos = 1 segundo
set updatetime=1000

" * significa todos os arquivos, você pode filtrar por 
" *.txt,*.py e assim vai
autocmd CursorHold,CursorHoldI * update

" dar cor ao tema e destaca a linha com uma faixa clara
colo materialbox

" Fechamento automatico de tags html
imap ><Tab> ><Esc>mt?<\w<Cr>:let @/=""<Cr>lyiw`ta</><Esc>P`tli


let g:ctrlp_custom_ignore = ' v[ /] .(swp|zip)$'
let g:ctrlp_user_command = ['.git', 'cd %s && git ls-files -co --exclude-standard']
let g:ctrlp_show_hidden = 1

" inserindo comentarios
filetype plugin on
let g:NERDSpaceDelims = 1
let g:NERDDefaultAlign = 'left'
map cc <Plug>NERDCommenterInvert

let g:ale_linters = {'python': ['flake8', 'pylint'], 'javascript': ['eslint']}
let g:ale_completion_enabled = 0

Plug 'jackMort/ChatGPT.nvim'

require('chatgpt').setup({
  api_key_cmd = 'echo "sua-chave-openai"'
})
source ~/.vim/coc.nvimrc
