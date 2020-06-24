# django-fullstack-boilerplate
__Stop Starting__
A boilerplate example for starting a Django/React app more quickly.

The technology stack:
- Django
- React
- Bootstrap/Reactstrap
- Axios
- GraphQL with Relay
- JWT Auth.
- Any SQL dialect
- AWS and Heroku for deployment

Many of the necessary add-ons are already configured, including:
- Custom user model
- Django-storages
- Graphene-django
- Django-graphql-jwt
- Django-graphql-auth
- Django-heroku with `Procfile`, `runtime.txt` files
- Django-cors-headers
- Python-dotenv

Both Django and React apps are served from the same endpoint during production to keep the advantages of Django's CSRF protection, admin pages while still taking advantage of the benefits offered by a single-page application using react-router/react-router-dom. During development, the hot-reloading React dev server is still available. As an added bonus, settings have already been configured to proxy requests to Django's port, and whitelist the dev port to prevent CORS blockages.

# Set up (for Bash/Linux)
Fork the repository, then

    git clone <forked-repo-url>         # clone the repo
    npm install                         # configure node environment
    python3.8 -m virtualenv venv        # configure python environment
    source venv/bin/activate            # activate python environment
    pip install -r requirements.txt     # install python dependencies
    python manage.py migrate            # set up Django
    python manage.py runserver          # run django dev server in 1st terminal
                                        # set any required environment variables in .env file
    npm start                           # run react dev server in 2nd terminal

## Required Environment Variables
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_STORAGE_BUCKET_NAME`
- `SECRET_KEY`

To generate a secret key
```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

## Optional Environment Variables
- `DEBUG` (will default to False in `settings.py` if not set, for security reasons)

# Example Development Workflow
- Create app (e.g. polls, blog, etc.) with django-admin startapp
- Create models in Django, makemigrations, migrate
- `touch <app-name>/{types,queries,mutations}.py`
- Create nodes in GraphQL schema for queries and mutations (creating, reading objects)
- Load queries and mutation into `backend/schema.py`
- Create React components for displaying data using Axios to query to API at `/graphql/` and reactstrap for rendering.
- Create views in React as a compilation of components
- Create routes to display views
- Add routes to switch statement in `App.js`
- View immediate changes on each of the development servers
- Create tests with Django and React (at any time, really)

An example blog app is already created that mostly follows this workflow.

# Deployment to Heroku
## Steps

Install the heroku-cli

    heroku create <website-name>
    heroku buildpacks:add --index 1 heroku/nodejs
    heroku buildpacks:add --index 2 heroku/python
    heroku config:set \
        DEBUG='False' \
        SECRET_KEY='<your-secret-key>' \
        AWS_ACCESS_KEY_ID='<your-aws-access-key-id>' \
        AWS_SECRET_ACCESS_KEY='<your-aws-secret-access-key>' \
        AWS_STORAGE_BUCKET_NAME='<your-aws-storage-bucket-name>'
    git add .
    git commit -m "Initial commit."
    git push heroku master