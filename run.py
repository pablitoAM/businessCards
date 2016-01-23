import logging
from app import app

__version__ = '1.0.0'

port = 5000
host = '0.0.0.0'
dev = True

log = logging.getLogger(__name__)

if __name__ == '__main__':
	if dev == True:
		import formic
		import livereload

                app.config['DEBUG'] = True
                app.config['PROPAGATE_EXCEPTIONS'] = True

                # LiveReload HTTP+TCP server (watches files for changes)
                lr_server = livereload.Server(app.wsgi_app)
                for path in formic.FileSet(directory='.', include=['**.py', '**.conf']):
        	       lr_server.watch(path)

        	log.info('LiveReload listening on port %d' % port)
        	lr_server.serve(host=host,
        		port=port,
        		liveport=port)
        else:
                app.run(port=port, host=host)
