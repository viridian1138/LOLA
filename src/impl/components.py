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
# Module performing load/unload and start/stop on a predefined list of components in lieu of an OSGi prompt.
# The component list is defined in the components.conf file.
#


import componentstate;




#
# The set of component states for the components.
#
__componentStates = set()



#
# Loads and starts the set of components.
#
def start():
    with open( 'components.conf' ) as f:
        for line in f:
            print( line.rstrip() );
            c = componentstate.ComponentState( line.rstrip() );
            c.load();
            c.start();
            __componentStates.add( c );
    
    
    

#
# Unloads and stops the set of components.
#
def stop():
    for x in __componentStates:
        if not isinstance(x, componentstate.ComponentState ): raise Exception('Bad interface')
        x.stop()
        x.unload()


