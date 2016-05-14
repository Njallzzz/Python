from flask import Flask
import logging

def new_errorhandlers(app):
    @app.errorhandler(402)
    def payment_required(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(403)
    def forbidden(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(404)
    def page_not_found(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(405)
    def method_not_allowed(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(406)
    def not_acceptable(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(408)
    def request_timeout(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(409)
    def conflict(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(410)
    def gone(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(411)
    def length_required(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(412)
    def precondition_failed(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(413)
    def request_entity_too_large(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(414)
    def request_uri_too_long(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(415)
    def unsupported_media_type(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(416)
    def requested_range_not_satisfiable(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(417)
    def expectation_failed(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(418)
    def im_a_teapot(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(422)
    def unprocessable_entity(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code
    
    @app.errorhandler(423)
    def locked(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(424)
    def failed_dependency(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(425)
    def unordered_collection(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(426)
    def upgrade_required(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(429)
    def too_many_requests(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(431)
    def request_header_fields_too_large(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(444)
    def no_response(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(450)
    def windows_parental_controls(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(451)
    def unavailable_legal_reasons(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(500)
    def internal_server_error(e):
        try:
            return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code
        except:
            logging.error(e)
            app.logger.error(e)
            return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(500, 500), 500

    @app.errorhandler(502)
    def bad_gateway(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(503)
    def service_unavailable(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code
    
    @app.errorhandler(506)
    def variant_also_negotiates(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(507)
    def insufficient_storage(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(508)
    def loop_detected(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(509)
    def bandwidth_limit_exceeded(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code

    @app.errorhandler(599)
    def network_connect_timeout(e):
        return '<center><img src="https://http.cat/{}"><br>{}</center>'.format(e.code, e.code), e.code
