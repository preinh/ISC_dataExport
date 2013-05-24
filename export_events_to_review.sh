#!/bin/bash

#FROM_DB="-d sqlite3:////home/suporte/.seiscomp3/sc3.db"
FROM_DB="-d sqlite3:////home/lucio/.seiscomp3/sc3.db"
TO_DB="-d mysql://sysop:sysop@10.110.0.46/seiscomp3"

START="2010-01-01 00:00:00"
END="2014-01-01 00:00:00"

for evt in $(scevtls $FROM_DB --begin "${START}" --end "${END}"); do
	echo exporting $evt
	scxmldump  $FROM_DB  -fPAMF -E $evt | \
	scdb --plugins dbmysql -i -  $TO_DB
done



