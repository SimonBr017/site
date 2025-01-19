import os
from flask import url_for, current_app

def versioned_file(filename):
    "Generates a path with a timestamp to prevent caching."
    file_path = os.path.join(current_app.static_folder, filename)
    if os.path.exists(file_path):
        timestamp = int(os.path.getmtime(file_path))
        return url_for('static', filename=filename, v=timestamp)
    return url_for('static', filename=filename)