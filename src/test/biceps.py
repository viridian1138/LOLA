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


import datetime;


import context;
import ibodypart;


#
# Test component registering an instance of IBodyPart upon activation.
#


#
# IBodyPart class to be registered by component activation.
#
class MyClass(ibodypart.IBodyPart):
    
    #
    # Name of the associated text file for persistence.
    #
    __fname = 'biceps.txt';
    
    #
    # Constructor
    #
    def __init__(self):
        self.__myDate = datetime.date( 1970 , 1 , 1 );
        with open( self.__fname , 'r' ) as file:
            line = file.readline();
            self.__myDate = datetime.datetime.strptime( line.rstrip() , "%Y-%m-%d" ).date();
            file.close();


    #
    # Gets the name of the body part.
    #
    def name(self):
        return 'Biceps'

    def numDays(self):
        return 3
    
    #
    # Gets the date when exercise last happened,
    #
    def getDate(self):
        return self.__myDate
    
    #
    # Sets the date when exercise last happened,
    #
    def setDate(self,date):
        if not isinstance(date, datetime.date ): raise Exception('Bad interface');
        self.__myDate = date;
        with open( self.__fname , 'w' ) as file:
            file.write( "%s\n" % str( self.__myDate ) );
            file.close();



#
# IBodyPart instance to be registered by component activation.
#
__myEnt = MyClass();


#
# Activates the component.  This is similar to the activate() method in the
# OSGi activation class for a component.
#
def activate():
    print( 'activate called -- biceps' )
    context.add( __myEnt );


#
# Deactivates the component.  This is similar to the deactivate() method in the
# OSGi activation class for a component.
#
def deactivate():
    print( 'deactivate called -- biceps' )
    context.remove( __myEnt );




