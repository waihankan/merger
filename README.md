## Installation Guide

```bash
pip install pypdf 
```
If the above command doesn't work, try:
```bash
pip3 install pypdf
```

### Clone the Repo into bin folder
```bash
mkdir ~/bin
cd ~/bin
git clone https://github.com/waihankan/merger.git
```

### Edit Environment variable and make alias
if you have bash shell go edit `~/.bashrc`.
if you have zsh shell, go edit `~/.zshrc`

```bash
export PATH="$PATH:$HOME/bin"
alias merger="python3 ~/bin/merger.py"
```

After editing, source the file using `source ~/.zshrc` or `source ~/.bashrc`

## Usage [MOST IMPORTANT]
```bash
merger -o OUTPUT.pdf input_file1.pdf input_file2.pdf [input_file3.pdf] [etc.]
```

