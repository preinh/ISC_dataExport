# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
from datetime import datetime, timedelta

time_before = timedelta(weeks=4)

connection_string = "-d postgresql://sysop:sysop@10.110.0.130/sc_master"

t0 = datetime.now() - time_before
tf = datetime.now()

filename = "picks_%s_%s.xml"%(t0.strftime("%Y%m%dT%H%M"), tf.strftime("%Y%m%dT%H%M"))

_t0 = t0.strftime("%Y-%m-%d %H:%M:%S")
_tf = tf.strftime("%Y-%m-%d %H:%M:%S")

#dump Picks
cmd = "python dumpManualPicks.py %s --begin '%s' --end '%s' > %s" % (connection_string, t0, tf, filename)
print cmd
os.system(cmd)

# compress file
tar_filename = "%s.tar.gz" % filename
cmd = "tar czf %s %s" % (tar_filename, filename)
print cmd
os.system(cmd)

import sendMail as mail
mail.sendMail(tar_filename)

#remove old file
cmd = "rm -f %s %s" % (tar_filename, filename)
print cmd
os.system(cmd)
