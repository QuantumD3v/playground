from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import psutil

app = Flask(__name__)

# Base folder to store uploaded files
BASE_UPLOAD_FOLDER = 'files'
app.config['UPLOAD_FOLDER'] = BASE_UPLOAD_FOLDER

# Ensure the base folder exists
if not os.path.exists(BASE_UPLOAD_FOLDER):
    os.makedirs(BASE_UPLOAD_FOLDER)

# Counters for tracking uploads and downloads
upload_count = 0
download_count = 0

@app.route('/', methods=['GET', 'POST'])
@app.route('/<path:subfolder>/', methods=['GET', 'POST'])
def index(subfolder=""):
    global upload_count
    current_folder = os.path.join(app.config['UPLOAD_FOLDER'], subfolder)

    # Ensure the current folder exists
    if not os.path.exists(current_folder):
        os.makedirs(current_folder)

    if request.method == 'POST':
        files = request.files.getlist('files')
        for file in files:
            if file and file.filename:
                filepath = os.path.join(current_folder, file.filename)
                file.save(filepath)
                upload_count += 1  # Increment upload count
        return redirect(url_for('index', subfolder=subfolder))
    
    files = os.listdir(current_folder)
    return render_template('index.html', files=files, subfolder=subfolder)

@app.route('/list/')
@app.route('/list/<path:subfolder>/')
def list_files(subfolder=""):
    current_folder = os.path.join(app.config['UPLOAD_FOLDER'], subfolder)
    if not os.path.exists(current_folder):
        os.makedirs(current_folder)
    
    files = os.listdir(current_folder)
    return render_template('list.html', files=files, subfolder=subfolder)

@app.route('/download/<path:filename>/')
@app.route('/download/<path:subfolder>/<filename>/')
def download_file(subfolder="", filename=""):
    global download_count
    file_folder = os.path.join(app.config['UPLOAD_FOLDER'], subfolder)
    download_count += 1  # Increment download count
    return send_from_directory(file_folder, filename)

# Endpoint for fetching the upload/download counts and system info
@app.route('/info')
def get_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    return {
        "uploads": upload_count,
        "downloads": download_count,
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage
    }

if __name__ == "__main__":
    app.run(debug=True, port=8080)
