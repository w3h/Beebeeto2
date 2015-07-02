#!/usr/bin/env python
# coding=utf-8

# Author: W_HHH
# Create: 2014-10-25
# Team: W_HHH

import sys,os
from util.get_file_list import get_file_list,findfiles
from util.factory import moduleFactory

class BeePlugins:
    def __init__(self, debug = False):
        self._debug = debug
        self._plugins = []

    def load_exp(self):
        file_list = []
        findfiles("./Beebeeto-framework/demo/", file_list)
        #file_list = [f for f in os.listdir(os.path.join(os.getcwd(), "./Beebeeto/demo/"))]
        self._all_plugins = [os.path.splitext(f)[0] for f in file_list if os.path.splitext(f)[1] == '.py']
        try: self._all_plugins.remove('__init__') 
        except: pass
        try: self._all_plugins.remove('baseframe') 
        except: pass
        if self._debug: print self._all_plugins


    def get_plugin_list(self):
        """
        :return: A string list of the names of all available plugins by type.
        """
        return self._plugins


    def get_plugin_inst(self, exp_name):
        """
        :return: An instance of a plugin.
        """
        exp_name = exp_name.replace("//", "/")
        exp_name = exp_name.replace("./", "")
        exp_name = exp_name.replace("/", ".")
        #print exp_name
        module_inst = moduleFactory(exp_name)
        class_name = "MyPoc"
        plugin_inst = getattr(module_inst, class_name)

        return plugin_inst

    def create_instances_appname(self, plugin_instance, app_name=None):
        info = plugin_instance.__dict__.get('poc_info')
        info = info['vul']['app_name'].lower()
        if app_name:
            if app_name.lower() in info:
                self._plugins.append(plugin_instance)
        else:
            self._plugins.append(plugin_instance)

    def create_instances(self, exp_name=None, app_name=None):
        if exp_name:
            z = [i for i in self._all_plugins if (i[i.rfind("/")+1:] == exp_name)]
            if z: 
                plugin_instance = self.get_plugin_inst(z[0])
                self.create_instances_appname(plugin_instance, app_name)
        else:
            for plugin_name in self._all_plugins:
                plugin_instance = self.get_plugin_inst(plugin_name)
                self.create_instances_appname(plugin_instance, app_name)
       
        if self._debug: print self._plugins
        return

    def add_plugin(self, exp_name=None, app_name=None):
        self.load_exp()
        self.create_instances(exp_name, app_name)


if __name__ == '__main__':
    bf = BeePlugins(debug=True)
    bf.load_exp()
    bf.create_instances()

