"""
Usage:
  http2sms [-i IP ] [-p PORT ]     

Options:
   -i IP --ip IP Hostname or ip address of the web server to listen 
   [default: 0.0.0.0]     
   -p PORT --port PORT Port where the web server is listen 
   [default: 8080] 
"""

import tempfile
import json
from docopt import docopt
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def post_sms():
   phonenumber, msg = parsesms(request.get_json())
   for phonenumber in phonenumbers:
       textmsg = sms_toolformatfile(phonenumber, msg)
       sms_writetodisk(textmsg)

def parse_sms(sms):
   return sms['to'] , sms['msg']

def sms_toolformatfile(to, msg):
    return "To:{0}\n\n{1}\n".format(to, msg)

def sms_writetodisk(textmessage, dir_='/var/spool/sms/outgoing'):
    with tempfile.NamedTemporaryFile( mode="at", dir=dir_, delete=False) as file_:
        file_.write(textmessage)

if __name__ == '__main__' :
   arguments = docopt(__doc__, version="1.0.0")
   ipaddress = arguments["--ip"]
   port = int( arguments["--port"] )
   app.run(host=ipaddress, port=port)