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
# Test context into which IBodyPart instances are registered.
#


import ibodypart;



__storeSet = set();


def add( myEnt ):
    if not isinstance(myEnt, ibodypart.IBodyPart ): raise Exception('Bad interface')
    print( 'add called -- context' )
    __storeSet.add( myEnt )


def remove( myEnt ):
    if not isinstance(myEnt, ibodypart.IBodyPart ): raise Exception('Bad interface')
    print( 'remove called -- context' )
    __storeSet.remove( myEnt )


def get():
    print( 'get called -- context' )
    return __storeSet










