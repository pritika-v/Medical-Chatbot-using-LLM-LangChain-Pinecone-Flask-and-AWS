#creating directories
mkdir -p src #p means parameter
mkdir -p research

#creating files
touch src/__init__.py #this is a constructor file
touch src/helper.py
touch src/prompt.py
touch .env #base environmet will already have a lot of files in it
touch setup.py
touch app.py
touch research/trials.ipynb #notebook file
touch requirements.txt

echo "Directories and files created successfully"