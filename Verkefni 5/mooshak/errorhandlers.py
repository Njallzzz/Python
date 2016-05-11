from flask import Flask

def new_errorhandlers(app):
    @app.errorhandler(402)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(403)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(404)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(405)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(406)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(408)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(409)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(410)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(411)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(412)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(413)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(414)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(415)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(416)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(417)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(418)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(422)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(500)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(502)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(503)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code
    
    @app.errorhandler(506)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(507)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(508)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(509)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(599)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code
