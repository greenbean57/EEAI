from flask import Flask, render_template
import json

from script import getAnswerFromOpenAI

app = Flask(__name__)

config = json.load(open('./resource/config.json'))


@app.route('/', methods=("GET", "POST"))
def survey():
    #prompt = 'I want to generate questions for employee engagement survey. ' \
    #         'Generate %d questions with scale of 1 to 10 on employee ' \
    #         '%s' % (config['questions'], ', '.join([str(elem) for elem in config['category']]))
    prompt = 'Generate %d questions with scale of 1 to 10 on employee ' \
             '%s' % (config['questions'], ', '.join([str(elem) for elem in config['category']]))

    print(prompt)
    questions = getAnswerFromOpenAI(prompt)
    questions = questions.choices[0].text
    print(questions)
    questionsArray = questions.splitlines()
    while( "" in questionsArray):
        questionsArray.remove("")
    return render_template('survey.html', questions=questionsArray)
