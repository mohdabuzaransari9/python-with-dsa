# python-with-dsa
learning python with dsa
## upgrading pip
**Note:** run this command in cmd<br>
python.exe -m pip install --upgrade pip

## reset global python
**Note:** run this command in Windows (PowerShell):<br>
pip freeze | % { $_.split('==')[0] } | % { pip uninstall $_ -y }

# anaconda
## create new venv
conda create -p venv "python==3.10.12" -y

## Activate your environment
conda activate full_path_without_commas
like this
conda activate path\venv

## delete environment

conda env list

conda remove --prefix D:\python\venv --all -y

**Note:**--prefix (-p) specifies the environment path.

**Note:**--all removes all packages and the environment itself.

**Note:**-y skips confirmation.


## to get localhost link

### if jupyter is not installed
pip install notebook

### then write this to open jupyter notebook and get local hostlink in cmd
jupyter notebook

# pip list command to get alist of all installed packages
pip list

# pip freeze command
pip freeze > requirements.txt

jupyter notebook
# pytorch versions

## latest

## gpu version
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

## cpu only
pip3 install torch torchvision torchaudio

## pytorch 2.1

## gpu version
conda install pytorch==2.1.1 torchvision==0.16.1 torchaudio==2.1.1 pytorch-cuda=12.1 -c pytorch -c nvidia

## cpu only
conda install pytorch==2.1.0 torchvision==0.16.0 torchaudio==2.1.0 cpuonly -c pytorch

# colab essential

## folder download in colab via zipping folder
!zip -r booknlp_output.zip /content/booknlp_output

from google.colab import files
files.download('booknlp_output.zip')


# github lfs file upload way of *.csv

**Note:** https link of your repository<br>

git clone https://github.com/username/your-repository-name.git<br>

**Note:** install git on your pc<br>

**Note:** Navigate to repository folder<br>
cd your-repository-name<br>

**Note:** Install Git LFS<br>
git lfs install<br>

**Note:** Track CSV files<br>

git lfs track "*.csv"<br>

**Note:** Copy your CSV file into the repository folder<br>
**Note:** Then in terminal:<br>

git add .gitattributes<br>
git add yourfile.csv<br>
git commit -m "Add large CSV file"<br>
git push origin main<br>
