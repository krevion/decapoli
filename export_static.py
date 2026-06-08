"""
Simple static site exporter for this project.

Usage:
    python export_static.py

This script requires the project's virtualenv with Django available. It will render
the main templates to HTML files under the `export/` directory and copy static files
so you can deploy the `export/` folder to Netlify as a static site.
"""
import os
import shutil

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wadi.settings')

import django
from django.template.loader import render_to_string

django.setup()

HERE = os.path.dirname(__file__)
OUT = os.path.join(HERE, 'export')

PAGES = {
    'index.html': 'home.html',
    os.path.join('about', 'index.html'): 'about.html',
    os.path.join('contact', 'index.html'): 'contactus.html',
}


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def write_pages():
    for outpath, template in PAGES.items():
        full = os.path.join(OUT, outpath)
        ensure_dir(os.path.dirname(full))
        html = render_to_string(template, {})
        with open(full, 'w', encoding='utf-8') as f:
            f.write(html)
        print('Wrote', full)


def copy_static():
    src = os.path.join(HERE, 'wadiapp', 'static')
    dst = os.path.join(OUT, 'static')
    if os.path.exists(dst):
        shutil.rmtree(dst)
    if os.path.exists(src):
        shutil.copytree(src, dst)
        print('Copied static to', dst)
    else:
        print('No static/ folder found to copy')


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    ensure_dir(OUT)
    write_pages()
    copy_static()
    print('Static export complete. Deploy the `export/` directory to Netlify.')


if __name__ == '__main__':
    main()
