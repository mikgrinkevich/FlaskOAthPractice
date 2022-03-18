# Create environemnt
virtualenv . #python -m virtualenv .

# Activate virtual environment
source bin/activate

# Install Flask library
pip install flask

# Save requirements
pip freeze > requirements.txt