import json

import openai

config = json.load(open('./resource/config.json'))

openai.organization = config['openAI']['orgKey']
openai.api_key = config['openAI']['apiKey']

def getAnswerFromOpenAI(prompt):
    return openai.Completion.create(
        model=config['openAI']['model'],
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0,
        best_of=1,
        stop=[" Human:", " AI:"]
    )