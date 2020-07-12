from app import app
from flask import render_template

@app.route('/admin/dashboard')
def admin_dahboard():
    return render_template("/admin/dashboard.html")

@app.route('/admin/profile')
def admin_profile():
    return "<h1>This is Admin Profile</h1>"