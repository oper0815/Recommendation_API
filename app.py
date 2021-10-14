from flask import Flask, jsonify, request, render_template

import pickle
import numpy as np
import random

from gensim.models.word2vec import Word2Vec
import matplotlib.pyplot as plt
from gensim.models import Word2Vec

app = Flask(__name__, static_url_path='/static')

@app.route('/check')
def hello_html():
    # html file은 templates 폴더에 위치해야 함
    # n1 = [1,2,3,4,5,6,7,8,9,10]
    # out = random.sample(n1, 3)
    title = []
    for i in out:
        title.append(products_dict[i][0])
    return render_template('list2.html', out = out, title = title)

@app.route('/predict1')
def predict1():
    #parser = reqparse.RequestParser() 
    #parser.add_argument('number')
    #args = parser.parse_args()
    #nb = np.fromiter(args.values(), dtype=float)

    nb = int(out[0])
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

@app.route('/predict2')
def predict2():
    #parser = reqparse.RequestParser() 
    #parser.add_argument('number')
    #args = parser.parse_args()
    #nb = np.fromiter(args.values(), dtype=float)

    nb = int(out[1])
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

@app.route('/predict3')
def predict3():
    #parser = reqparse.RequestParser() 
    #parser.add_argument('number')
    #args = parser.parse_args()
    #nb = np.fromiter(args.values(), dtype=float)

    nb = int(out[2])
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

if __name__ == '__main__':
    with open('data_dict.pkl', 'rb') as f:     # 경로 수정
        products_dict = pickle.load(f)
    n1 = list(range(100))
    out = random.sample(n1, 3)
    # out = [4, 14, 53] # 이미지를 위해 미리 지정
    model = Word2Vec.load('movie_w2v.model')   # 경로 수정
    app.run(host="0.0.0.0", port=9090)