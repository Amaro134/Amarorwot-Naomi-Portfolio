# Amarorwot Naomi — Django Portfolio

## Files to place in your existing project

Your project already has the right structure. Just copy the files below into the correct locations.

```
portifolio.ANG/
├── case/
│   └── urls.py          ← REPLACE with the provided file
├── name/
│   ├── views.py         ← REPLACE with the provided file
│   ├── urls.py          ← CREATE this new file
│   ├── templates/
│   │   └── name/
│   │       └── index.html   ← CREATE this folder path + file
│   └── static/
│       └── name/
│           ├── css/
│           │   └── style.css    ← CREATE this folder path + file
│           └── js/
│               └── main.js      ← CREATE this folder path + file
```

## Key differences from Flask

| Flask                          | Django                              |
|-------------------------------|-------------------------------------|
| `{{ url_for('static', ...) }}` | `{% load static %}` + `{% static '...' %}` |
| `skills.items()`              | `skills.items` (no brackets!)        |
| No CSRF on forms              | `{% csrf_token %}` inside every form |
| `render_template()`           | `render(request, template, context)` |

## Run the server

```bash
# Make sure venv is active
source venv/Scripts/activate

# Run migrations (first time only)
python manage.py migrate

# Start the server
python manage.py runserver
```

Open: **http://127.0.0.1:8000**

## Customise your content

All your projects and skills data lives in `name/views.py` in the `index()` function.
Edit the `projects` list and `skills` dict to update the page content.

## settings.py checklist

Make sure these are already in your settings.py (they should be):

```python
INSTALLED_APPS = [
    ...
    'name',       # ✓ already there
]

# Static files - add this if missing:
STATIC_URL = '/static/'
```