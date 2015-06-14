#!/usr/bin/env python3

import sys
import cherrypy

# Create a basic app
class App:
    def __init__(self):
        pass
    
    @cherrypy.expose
    def index(self):
        yield "It works!"
appinst = App()

# Set up cherrypy config
appdir = "/home/python/app"
appconf = {
    '/': {
        'tools.sessions.on':True,
        'tools.sessions.storage_type':'file',
        'tools.sessions.storage_path':appdir+'/sessions/',
        'tools.sessions.timeout':525600,
        'request.show_tracebacks': True
    },
    '/media': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': appdir+"/static/"
    }
}

cherrypy.config.update({
    'server.socket_port':3000,
    'server.thread_pool':1,
    'server.socket_host': '0.0.0.0',
    'sessionFilter.on':True,
    'server.show.tracebacks': True
})

cherrypy.server.socket_timeout = 5

sys.stderr = sys.stdout
cherrypy.config.update({'environment': 'embedded'})
application = cherrypy.tree.mount(appinst, "/", appconf)
