import web

urls = (
    '/add', 'add'
)
app = web.application(urls, globals())

class add:        
    def GET(self):
        a = int(web.input()['A'])
        b = int(web.input()['B'])
        return "{0} + {1} = {2}".format(a, b, (a+b))

if __name__ == "__main__":
    app.run()