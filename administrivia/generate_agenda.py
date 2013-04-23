#!/usr/bin/env python
""" generate meeting agenda
    =======================

    The purpose of this script is to minimise the effort required
    propperly document meetings. The way it does that is to
    automatically maintain an agenda/minutes document, populated
    with current agenda items.

    The process of having a meeting is to copy the agenda/minute
    document, which is populated with current agenda items, modify
    it as required during the meeting, and commit the changes.

    TODO
    ----

     * finish the Project class
     * Use a jinja template, not all these silly print statements.

"""
from os import listdir
from os.path import isfile, join
from datetime import datetime

class Project:
    def __init__(self, fname):
        self.fname = fname
        ref_header = self.ref_header()
        if ref_header:
            # if first non-blank line of the file is a :ref:,
            # use it for the page header
            self.heading = ref_header
        elif self.second_non_blank_line_is_all_equals() \
             and self.line_before_second_non_blank_line_is_non_blank():
            self.heading = self.first_non_blank_line()
        else:
            # otherwise, use the file name, sans extension
            self.heading = self.fname[:-4]

    def ref_header(self):
        # return None unless the first line of the file is a :ref:
	# TODO
        return None

    def second_non_blank_line_is_all_equals(self):
        #TODO
        return None

    def line_before_second_non_blank_line_is_non_blank(self):
        # TODO
        return None

    def first_non_blank_line(self):
        # TODO
        return None

today = datetime.now().strftime("%Y %B %d")

# list activities
in_prog_dir = '../in-progres';
activities = [
    Project(f) for f in listdir(in_prog_dir)
    if isfile(
        join(in_prog_dir,f))
    and f != 'index.rst'
    and f[-4:] == '.rst' ]


print today
print '=' * len(today)
print ''
print 'present:'
print ''
print ' * TBD'
print ''
print ''
print '[this line intentionally non-blank] '
print ''
print 'Report on in-progress items'
print '---------------------------'
print ''
if len(activities) == 0:
    print 'No activities currently in-progress.'
    print ''
else:
    for item in activities:
        print ''
        print item.heading
        print '^'*len(item.heading)
        print ''
        print ' * no action noted'
        print ''
print ''
print 'Other business'
print '--------------'
print ''
print ' * no items discussed'
print ''
print ''
