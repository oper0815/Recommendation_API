from flask import Flask, jsonify, request, render_template
from gensim.models.word2vec import Word2Vec
import matplotlib.pyplot as plt
from gensim.models import Word2Vec

import pickle
import numpy as np

app = Flask(__name__)

#@app.route('/predict', methods=['POST'])
@app.route('/predict')
def predict():
    #parser = reqparse.RequestParser() 
    #parser.add_argument('number')
    #args = parser.parse_args()
    #nb = np.fromiter(args.values(), dtype=float)

    nb = request.args.get('number')
    nb = int(nb)
    recom = []
    per = []
    n = []
    rec = model.wv.most_similar(nb)
    for i, a in enumerate(rec):
        # 콘텐츠명
        recom.append(products_dict[a[0]])
        # 확률
        #res = list(map(float, str(a[1])))
        per.append(a[1])
        # 개수
        n.append(i)
        # recom.append(recommendation)
    print(per)
    # for i in rec:
    #    print(products_dict[i[0]])
    return render_template('output.html', recom = recom, per = per, n = n) 


@app.route('/check')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    return render_template('list.html')

if __name__ == '__main__':
    with open('./project_ms/data_dict.pkl', 'rb') as f:     # 경로 수정
        products_dict = pickle.load(f)
    model = Word2Vec.load('./project_ms/movie_w2v.model')   # 경로 수정
    app.run(host="0.0.0.0", port=9090)