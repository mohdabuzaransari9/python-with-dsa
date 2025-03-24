# python-with-dsa
learning python with dsa


# anaconda
conda env list

(do this when you have selected the directory)
conda env remove --name my_env_name_only


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
