from optparse import OptionParser
import logging.config

from app.application import Application


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--logconfig", dest="logconfig", help="log config file", type="string")
    parser.add_option("--port", dest="port", help="run on the given port", type="int", default=5000)
    parser.add_option("--env", dest="env", help="enviroment", type="string")
    parser.add_option("--host", dest="host", help="host ip", type="string", default="0.0.0.0")
    parser.add_option("--debug", dest="debug", default=False, help="run on debug", action="store_true")

    options, args = parser.parse_args()

    if options.logconfig:
        logging.config.fileConfig(options.logconfig)
    if options.env == 'prod':
        config_obj = 'ProductionConfig'
    if options.env == 'staging':
        config_obj = 'StagingConfig'
    elif options.env == 'test':
        config_obj = 'TestingConfig'
    else:
        config_obj = 'DevelopmentConfig'

    app = Application(config_obj).get_app()

    app.run(debug=options.debug, port=options.port, host=options.host)

