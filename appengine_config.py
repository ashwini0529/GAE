from gaesessions import SessionMiddleware
def webapp_add_wsgi_middleware(app):
    app = SessionMiddleware(app, cookie_key="sfakdsafj2$!@#Eqeqeqeioj4n123jfasfn31$!@@#")
    return app