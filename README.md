Photo Album Management System:

Django app for creating photo albums and uploading images to Cloudinary.

Features
- User signup/login/logout
- Create, edit, delete albums (owner only)
- Upload, edit, delete photos (owner only)
- Images stored on Cloudinary
- PostgreSQL on Render

Local Setup:

```bash
python -m venv venv
source venv/bin/activate or venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Environment Variables:

Required (set on Render or in `.env` for local development):
- `SECRET_KEY`
- `DEBUG` (set to `False` on Render)
- `DATABASE_URL` (provided by Render PostgreSQL)
- `CLOUDINARY_CLOUD_NAME`
- `CLOUDINARY_API_KEY`
- `CLOUDINARY_API_SECRET`

Deployment: 

Live on Render: https://it383-assignment6-9r2h.onrender.com

Requirements: 

See requirements.txt