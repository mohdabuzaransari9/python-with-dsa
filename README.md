# python-with-dsa
learning python with dsa

conda env list

conda env remove --name my_env_name_only

# do this when you have selected the directory

# Activate your environment
conda activate full_path_without_commas

# pip freeze command
pip freeze > requirements.txt

jupyter notebook

# folder download in colab via zipping folder
!zip -r booknlp_output.zip /content/booknlp_output

from google.colab import files
files.download('booknlp_output.zip')
