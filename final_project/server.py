"""
 Routing ***
"""

from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    """ translates english text from url args to french
        from /englishToFrench
    """
    text_to_translate = request.args.get('textToTranslate')
    traslated_text = machinetranslation.translator.english_to_french(text_to_translate)
    return traslated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    """ translates french text from url args to english
        from /frenchToEnglish route
    """
    text_to_translate = request.args.get('textToTranslate')
    traslated_text = machinetranslation.translator.french_to_english(text_to_translate)
    return traslated_text

@app.route("/")
def renderIndexPage():
    """ renders the html paage to / route """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
