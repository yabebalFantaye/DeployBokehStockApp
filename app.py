from configure import configure_flask, TornadoApplication
from bokeh.server.app import app
from bokeh.server.configure import register_blueprint
from bokeh.server.settings import settings as server_settings
from bokeh.server.utils.plugins import object_page
from flask import render_template


configure_flask(config_file='config.py')
register_blueprint()

app.secret_key = server_settings.secret_key

@object_page("stocks")
def make_stock_applet(self):
    app = StockApp.create()
    return app

@app.route("/")
def applet(self):
    applet = make_stock_applet()
    return render_template(
        "stocks.html",
        app_url = bokeh_url + "/bokeh/jsgenerate/VBox/StockApp/StockApp",
        app_tag = applet._tag
    )


tornado_app = TornadoApplication(app, debug=server_settings.debug)
tornado_app.start_threads()
