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
# Test code execution script.
#


import datetime;

import context;
import ibodypart;
import components;



components.start();




int_value = -20;


while int_value != 3:


    print( "" );
    print( "" );
    print( "What Do You Want To Do? " )
    print( "" );
    print( "1. Set A Time To The Current Date" );
    print( "2. Determine Best Options" );
    print( "3. Quit" );
    print( "" );

    text = input( "Please Enter Something : " );

    int_value = int( text );

    print("You entered " + str( int_value ) );
    
    
    if int_value == 1:
        print( "" );
        print( "" );
        lst = [];
        cnt = int( 0 );
        for x in context.get():
            if not isinstance(x, ibodypart.IBodyPart ): raise Exception('Bad interface');
            lst.append( x );
            print( str( cnt ) + ' -- ' + x.name() );
            cnt = cnt + 1;
        print( "" );
        text = input( "Enter Which One : " );
        sel = int( text );
        lst[ sel ].setDate( datetime.date.today() );
        print( "Date Set" );


    if int_value == 2:
        print( "" );
        print( "" );
        for x in context.get():
            if not isinstance(x, ibodypart.IBodyPart ): raise Exception('Bad interface');
            print( x.name() )
            ddel = ( datetime.date.today() - x.getDate() ).days;
            print( str( 100.0 * ddel / x.numDays() ) + "%" )
            if not isinstance(x.getDate(), datetime.date ): raise Exception('Bad interface');
            print( x.getDate() )



print( "" );
print( "" );
components.stop();



