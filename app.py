from flask import Flask, render_template
import json

from script import getAnswerFromOpenAI

app = Flask(__name__)

config = json.load(open('./resource/config.json'))


@app.route('/', methods=("GET", "POST"))
def survey():

    _prompt_numeric_response = 'Generate %d questions with scale of 1 to 10 on employee ' \
             '%s' % (config['questions'], ', '.join([str(elem) for elem in config['category']]))

    _prompt_text_response = 'Generate %d question on employee ' \
             '%s' % (config['text_questions'], ', '.join([str(elem) for elem in config['category']]))

    print(_prompt_numeric_response)
    _response = getAnswerFromOpenAI(_prompt_numeric_response)
    _response = _response.choices[0].text
    print(_response)
    _response_array = _response.splitlines()

    # remove empty splits
    while "" in _response_array:
        _response_array.remove("")

    print(_prompt_text_response)
    _text_response = getAnswerFromOpenAI(_prompt_text_response)
    _text_response = _text_response.choices[0].text
    _response_text_array = _text_response.splitlines()
    print(_text_response)
    # remove empty splits
    while "" in _response_text_array:
        _response_text_array.remove("")

    return render_template('survey.html', questions=_response_array, text_questions=_response_text_array)
