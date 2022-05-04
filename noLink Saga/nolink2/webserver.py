#!/usr/bin/python3
import falcon, bjoern, json, uuid, random, math

app = falcon.API()

guh = []

for x in range(1000):
        guh.append(str(uuid.uuid4()))

print(guh[len(guh)-1])

class linker():
    def on_get(self, req, resp, innit):
        if str(innit) in guh:
            if innit == guh[len(guh)-1]:
                resp.content_type = falcon.MEDIA_HTML
                resp.body = '<p>congrats flag{YsIkNDXBpMtbikmt6IM8I_1bCQp4al8e}</p>'
                resp.status = falcon.HTTP_200
            else:
                resp.content_type = falcon.MEDIA_HTML
                un = [ '<p>Hello, please go <a href="' + guh[guh.index(str(innit))+1] +'">here</a></p>',
                    '<p>Hello, please go <a href="' + guh[math.ceil((guh.index(str(innit))+1) / 2)] +'">here</a></p>'
                    '<p>Hello, please go <a href="' + str(uuid.uuid4()) +'">here</a></p>'
                ]
                random.shuffle(un)
                resp.body = "".join(un)
                resp.status = falcon.HTTP_200
        else:
            resp.content_type = falcon.MEDIA_HTML
            resp.body = '<p>rip</p>'
            resp.status = falcon.HTTP_404

class start():
    def on_get(self, req, resp):
        resp.content_type = falcon.MEDIA_HTML
        resp.body = '<p>Hello, please go <a href="/article/' + guh[0] + '">here</a></p>'
        resp.status = falcon.HTTP_200

app.add_route('/article/{innit}', linker())
app.add_route('/article', start())
app.add_route('/', start())

if __name__ == '__main__':
    bjoern.listen(app, '0.0.0.0', 8080)
    bjoern.run()
