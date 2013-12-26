# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import SocketServer

class MyTCPRequestHandler(SocketServer.StreamRequestHandler):

 def handle(self):
    
     data = self.rfile.readline().strip()
     print data
     
     self.wfile.write(data)
     
     
if __name__ == "__main__":
    HOST, PORT = "localhost", 8888
    
    server = SocketServer.TCPServer((HOST, PORT), MyTCPRequestHandler)
    
    ip, port = server.server_address
    print "IP: %s" % ip
    print "Port: %s" % port
    
    print "IP: %s" % ip
    print "Port: %s" %port
    
    server.serve_forever()



