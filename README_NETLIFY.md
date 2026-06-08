Preparing a static export for Netlify

1) Install your project's virtualenv and dependencies (Django present).

2) Run the export script to render templates and copy static files:

```bash
python export_static.py
```

3) This will create an `export/` directory with:
- `index.html` (home)
- `about/index.html` (about page)
- `contact/index.html` (contact page)
- `static/` (CSS and images)

4) Deploy the contents of the `export/` directory to Netlify. You can drag-and-drop
   the folder in Netlify's site dashboard, or connect a Git repo and configure the
   publish directory to `export`.

Notes:
- This is a static export of templates — dynamic Django features (forms, DB-driven
  product listings, admin) will not function in the static build. For a full Django
  deployment consider using a platform like Render, Railway, or a VPS.
