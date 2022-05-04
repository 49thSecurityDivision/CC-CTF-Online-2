#!/usr/bin/python3
import falcon, bjoern, json, uuid, random, math, io
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

app = falcon.API()

guh = []

for x in range(100):
        guh.append(str(uuid.uuid4()).replace('o', '0'))

print(guh[len(guh)-1])#las

class linker():
    def on_get(self, req, resp, innit):
        if str(innit) in guh:
            if innit == guh[len(guh)-1]:
                resp.content_type = falcon.MEDIA_HTML
                resp.body = '<p>congrats flag{RXAQWH9itYAT5TVC2WyJv10_q-tOpN46}</p>'
                resp.status = falcon.HTTP_200
            else:
                img = Image.new('RGB', (500, 100))
                d = ImageDraw.Draw(img)
                d.text((20, 20), guh[guh.index(str(innit))+1], fill=(255, 0, 255), font=ImageFont.truetype("RobotoMono-Regular.ttf", 20))

                s = io.BytesIO()
                img.save(s, 'png')

                resp.body = s.getvalue()
                resp.status = falcon.HTTP_200
                resp.content_type = falcon.MEDIA_PNG
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
