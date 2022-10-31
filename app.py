from flask import Flask, request, jsonify
import numpy as np
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers import pipeline

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def makecalc():
    if request.method=="POST":
        data = request.get_json()
        print("data ---- > ", data)
        results = (classifier(data, candidate_labels, multi_label=True))        
        return jsonify(results)
    return jsonify({'result' : 'not a proper method!'})

@app.route('/classes', methods=['GET', 'POST'])
def nameClasses():
    if request.method=="POST":
        data = request.get_json()
        print("data ---- > ", data)
        if len(data) > 0:
            candidate_labels.clear()
            for i in range(1, len(data)+1):
                candidate_labels.append(data["class"+str(i)])
            print("New classes: ", candidate_labels)
            return jsonify({'result' : 'success!'})
        else:
            return jsonify({'result' : 'fail!'})
            
    elif request.method=="GET":
            return jsonify({'classes' : candidate_labels})
        
  

if __name__ == '__main__':
    # models path
    path = "./models/transformers"

    # load model
    nli_model = AutoModelForSequenceClassification.from_pretrained(path)
    print("Transformer model loaded...")

    # load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(path, local_files_only=True)
    print("Tokenizer loaded...")

    classifier = pipeline('zero-shot-classification', model=nli_model, tokenizer=tokenizer)

    # classes
    candidate_labels = ['urgent', 'illness', 'danger', 'abuse', 'homeless', 'suicide', 'death', 'panic attacks', 'depression', 'addiction']

    app.run(debug=True, host='0.0.0.0')

