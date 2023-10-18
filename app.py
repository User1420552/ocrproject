from flask import Flask, render_template, request
import pytesseract
from PIL import Image

app = Flask(__name__)


def extract_text_from_image(image):
    try:
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img)
        return extracted_text
    except Exception as e:
        return str(e)


@app.route('/', methods=['GET', 'POST'])
def assistant():
    chatgpt_response = ""
    if request.method == 'POST':
        run = request.form.get('run')
        if run == 'submit':
            uploaded_file = request.files['filename']
            if uploaded_file:
                chatgpt_response = extract_text_from_image(uploaded_file)
                return render_template('assistant_page.html', chatgpt_response=chatgpt_response)
    return render_template('assistant_page.html', chatgpt_response=chatgpt_response)


if __name__ == '__main__':
    app.run(debug=True)
