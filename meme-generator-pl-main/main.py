# Import
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Formularz z rezultatami
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
# odczytywanie wybranego obrazka
        selected_image = request.form.get('image-selector')
        TextTop = request.form.get('textTop')
        textBottom = request.form.get('textBottom')
        colorSelector = request.form.get('color-selector')
        textTopY = request.form.get('textTop_y')
        textBottomy = request.form.get('textBottom_y')

        return render_template('index.html', 
                               selected_image=selected_image,
                                textTop = TextTop,
                                textBottom=textBottom,
                                colorSelector=colorSelector,
                                textTopY=textTopY,
                                textBottomy=textBottomy
        )
    else:
        # Wyświetlanie pierwszego obrazka, jako grafika domyślna
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
