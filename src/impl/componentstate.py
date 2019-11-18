# -*- coding: utf-8 -*-

#$$strtCprt
#
# Lightweight OSGi-Like Activation for Python (LOLA)
# 
# Copyright (C) 2019 Thornton Green
# 
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty 
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program; if not, 
# see <http://www.gnu.org/licenses>.
# Additional permission under GNU GPL version 3 section 7
#
#
#$$endCprt



#
# Module encapsulating the loading and activation of a component.
#



import enum;
import importlib;




#
# The various states in which the component can reside.
#
class RunState( enum.Enum ):
    INIT = 0
    LOAD = 1
    UNLOAD = 2
    START = 3
    STOP = 4



#
# Class encapsulating the loading and activation of a component.
#
class ComponentState:
    
    #
    # Constructs the ComponentState.
    #
    def __init__(self, moduleName, packageName=None):
        self.moduleName = moduleName
        self.packageName = packageName
        self.moduleState = RunState.INIT

    #
    # Loads a compnent.  If the request is to load a component
    # that was unloaded, Python apparently can't unload a
    # module but it can reload the module upon this load
    # request.
    #
    def load(self):
        if self.moduleState == RunState.INIT:
            self.module = importlib.import_module( self.moduleName , self.packageName )
            self.moduleState = RunState.LOAD
        elif self.moduleState == RunState.UNLOAD:
            self.module = importlib.reload( self.module )
            self.moduleState = RunState.LOAD
        elif self.moduleState == RunState.LOAD:
            print( "Already Loaded" )
        else:
            print( "Illegal State" );
            
    #
    # Unloads a loaded component.
    # Python apparently can't un-import a module
    # like OSGi can unload a component, so the code
    # advances the state without performing any other
    # action.
    #
    def unload(self):
        if self.moduleState == RunState.STOP:
            self.moduleState = RunState.UNLOAD
        elif self.moduleState == RunState.LOAD:
            self.moduleState = RunState.UNLOAD
        elif self.moduleState == RunState.UNLOAD:
            print( "Already Unloaded" )
        else:
            print( "Illegal State" )

    #
    # Starts a loaded component.
    #
    def start(self):
        if self.moduleState == RunState.LOAD:
            activate = getattr(self.module, 'activate')
            activate()
            self.moduleState = RunState.START
        elif self.moduleState == RunState.STOP:
            activate = getattr(self.module, 'activate')
            activate()
            self.moduleState = RunState.START
        elif self.moduleState == RunState.START:
            print( "Already Started" )
        else:
            print( "Illegal State" )

    #
    # Stops a started component.
    #
    def stop(self):
        if self.moduleState == RunState.START:
            deactivate = getattr(self.module, 'deactivate')
            deactivate()
            self.moduleState = RunState.STOP
        elif self.moduleState == RunState.STOP:
            print( "Already Stopped" )
        else:
            print( "Illegal State" )




