#from rbml_extract_new import *
from rbml_embed_new import *
import os
from flask import Flask, send_from_directory, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
import socket
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)
#from en_de import *

ipv4 = ''

def ipv4_finder():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    global ipv4
    ipv4 = s.getsockname()[0]
    s.close()

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))

@app.route('/cdn/<path:path>')
@cross_origin()
def send_image(path):
    return send_from_directory('output', path)

@app.route('/')
@cross_origin()
def send_welcome_msg():
    return '<h1>Backend API</h1>'

@app.route('/encrypt', methods=['POST'])
@cross_origin()
def encrypt():
        content = request.json
    # if the user gaives the option to encrypt
        #m=encryption(msg,key)
        #l=[m,key]
        #s=' '.join(l) #jhbkh keyr
        img=rbml_em(content['msg'])
        #print(img)
        # with open('encode.bin', "wb") as file:
        #     file.write(img)
        # with open('image.txt', 'w') as f:
        #     f.write(img)
        new_data = { "data" : "http://{}:5000/cdn/{}.png".format(ipv4,img) }
        return new_data

        #pass to front end
        # if user gives option to decrypt
        # get the image in image
            #s=rbml_extract(image)
            #l= s.split(" ")
            #m=l[0]
            # key=l[1]
            # hidden_msg=decrypt(m,key)
            #pass to frontend

if __name__=='__main__':
    ipv4_finder()
    app.run(host="0.0.0.0")