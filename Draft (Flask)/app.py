from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/upload', methods=['POST'])
def upload():
    if 'photo' in request.files:
        photo = request.files['photo']
        photo.save('static/photo.jpeg')  # Sauvegarde dans le dossier 'static'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
