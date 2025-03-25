# python-with-dsa
learning python with dsa


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

<--!--prefix (-p) specifies the environment path.-->

<--!--all removes all packages and the environment itself.-->

<--!-y skips confirmation.-->


## Activate your environment
conda activate full_path_without_commas
## to get localhost link
### if jupyter is not installed
pip install notebook
### then write this
jupyter notebook

# pip freeze command
pip freeze > requirements.txt

# pip freeze command
pip freeze > requirements.txt

jupyter notebook
# colab essential

## folder download in colab via zipping folder
!zip -r booknlp_output.zip /content/booknlp_output

from google.colab import files
files.download('booknlp_output.zip')


# github lfs file upload way of *.csv

<!-- https link of your repository -->

clone https://github.com/username/your-repository-name.git

<!-- install git on your pc -->

<!--Navigate to repository folder-->
cd your-repository-name

<!--Install Git LFS-->
git lfs install

<!--Track CSV files-->

git lfs track "*.csv"

<!--Copy your CSV file into the repository folder-->
<!--Then in terminal:-->

git add .gitattributes
git add yourfile.csv
git commit -m "Add large CSV file"
git push origin main
