Administrivia
=============

todo:
 * organisation/committee details
 * ...

.. toctree::
   :maxdepth: 1

   TRL
   Finances
   livery/index
   Incorporation


.. _mumble-session:

Weekly Meeting
--------------

We meet at 8pm each Monday, on the 3DRobotics mumble server (cuav channel).

 * host: mumble.3DRobotics.com
 * user-name: pick something that looks a lot like your real name
 * password: contact a committee member off-list for the password

There is a standardised agenda, basically
 * :ref:`wip`
 * :ref:`new-ideas`
 * other business
 * plans for the next week

Minutes:

.. toctree::
   :maxdepth: 1 
   :glob:
   :reversed:

   minutes/*


Notes for meeting chair/minute takers
-------------------------------------

One idea behind the current documentation system was to have an "automatically current meeting agenda" for any given meeting. e.g. every project in the in-progress directory was current, so it should be on the default meeting agenda (along with whatever other standing items we want, such as "other business").

We now have a tireless robot assistant to help us with administration. It can't yet tidy my workshop, but can update "administrivia/minutes/template.rst.copyme" with today's date and whenever the in-progress items change. So for any given day, if we are having a meeting, this file is the agenda. If you want to put something else on the agenda, consider moving it to "in-progress" before the meeting (hint/nudge, update project documentation before meetings ;)

.. spelling::

   copyme
   hudson
   py

The process if taking minutes is now quite streamlined:
 1. ``cd administrivia/minutes``
 2. ``MINUTES="`date +'%Y%m%d'`.rst"``
 3. ``cp template.rst.copyme $MINUTES``
 4. ``#yack yack yack, edit the $MINUTES``
 5. [ ``cd ../../; make spellcheck; # fix typos/update OK_wordlist.txt; cd administrivia/minutes`` ]
 6. ``git add $MINUTES   #and /OK_wordlist.txt, if you changed it``
 7. ``git commit -m "minuted today's mumble session, ad-hock elevator conversation or whatever"``
 8. ``git push``

If you don't like what the admin-robot is doing, either raise a ticket or change administrivia/generate_agenda.py and/or administrivia/hudson_admin_task.sh.

