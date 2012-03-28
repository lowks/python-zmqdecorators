from __future__ import with_statement
import sys,os,signal
import yaml
import dbus,dbus.service,gobject

class baseclass(dbus.service.Object):
    def __init__(self, mainloop, bus, **kwargs):
        # These we will need (and will pass on)
        self.mainloop = mainloop
        self.bus = bus
        
        # Some sanity-checking and automation
        if not kwargs.has_key('dbus_launcher_interface_name'):
            kwargs['dbus_launcher_interface_name'] = kwargs['dbus_default_interface_name'] + '.launcher'
        if not kwargs.has_key('dbus_launcher_object_path'):
            kwargs['dbus_launcher_object_path'] = "/%s" % kwargs['dbus_launcher_interface_name'].replace('.', '/')
        self.dbus_object_path = kwargs['dbus_object_path']
        self.dbus_interface_name = kwargs['dbus_interface_name']
        # Start the DBUS stuff
        dbus.service.Object.__init__(self, dbus.service.BusName(self.dbus_interface_name, bus=self.bus), self.dbus_object_path)
        
        # Load config
        self.load_config()

        # If the class was defined import that too
        if launcher_config.has_key('main_class_name')
            exec("from %s import %s as main_class" % (launcher_config['main_class_name'],launcher_config['main_class_name']))
            self.main_instance = main_class(self.mainloop, self.bus, self.config, **kwargs)


    def quit(self):
        """Quits the mainloop"""
        self.mainloop.quit()

    def reload(self):
        """Used to reload the config"""
        self.load_config()

    def load_config(self):
        """Loads (or reloads) the configuration file"""
        with open(self.config_file_path) as f:
            self.config = yaml.load(f)
