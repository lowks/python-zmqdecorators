import sys,os
from baseclass import *


def main(launcherclass, **kwargs):
    """Boilerplate main program check, .launcher will be added to the interface by the baseclass and path generated from the interface"""
    import dbus,gobject
    # Enable threading
    gobject.threads_init()
    dbus.mainloop.glib.threads_init()
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    
    # Get the bus and mainloop
    bus = dbus.SessionBus()
    loop = gobject.MainLoop()

    # If no launcher specified use the baseclass one    
    if not launcherclass:
        launcherclass = baseclass
    instance = launcherclass(loop, bus, **kwargs)
    # And start the eventloop (catch KeyboardInterrupt here for [hopefully] clean mainloop quit)
    try:
        loop.run()
    except KeyboardInterrupt:
        loop.quit()

# This does not work in a module, some copy-pasting is invariably going to be needed
#def use_launcher(name=None):
#    """Boilerplate main program check: Prints a message to use the launcher and exits"""
#    if not name:
#        name = __file__.replace('.py', '_launcher.py')
#    print "Use %s" % name
#    sys.exit(1)
#
