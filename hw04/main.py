import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self,i,j):
        html= '''
        <html>
        <body>
        <table>
        '''
        for i in range(1,10):
            for j in range(1,i+1):
                print('{}x{}={}\t'.format(j, i, i*j), end='')
            print()
            html+= '''
            </table>
            </bady>
            </html>
            '''
        self.write(html)
        
application = tornado.web.Application([
    (r"/([0-9]+)(?:/([0-9]+))?", MainHandler),
],debug=True)

if __name__ == "__main__":
    application.listen(8888)
    server = tornado.ioloop.IOLoop.instance()
    tornado.ioloop.IOLoop.instance().start() 
    tornado.ioloop.PeriodicCallback(lambda: None, 500, server).start()
    server.start() 
