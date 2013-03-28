.. _mhv-quadcopter-workshop:

MHV Quadcopter Workshop
=======================

Developer: Stephen. With help from Tridge, Jack, Alastair, Andreas and Chris (Wolfe)

The purpose of this workshop was to guide a group of 12 attendees through the process of building, calibrating and flying APM-based quadcopters.

It should be:

* (Relatively) Cheap
* Commonly available spare parts
* Open source or hackable hardware/software where available
* Easy for beginners to build
* Strong/tough enough to withstand beginner pilots
* Able to carry a 200g payload (such as a small camera)

The workshop itself is designed to be:

* Accessible to beginners
* Full documentation of the build process
* Able to be completed in 3 to 4 evenings (not including flight time)
* Educational as to how quadcopters work and how to safely use them

Resources
----------------

.. toctree::
   :glob:

   quadcopter-workshop/*


Build Manual

 * :download:`Build Manual (word 2010) <quadcopter-workshop/BuildManual.docx>`, :download:`Build Manual (PDF) <quadcopter-workshop/BuildManual.pdf>`

Parameters File

* :download:`MHV.parm <quadcopter-workshop/MHV.param>`

Photos and Videos

http://www.flickr.com/photos/dburkey/sets/72157632928544691/with/8581032739/

http://youtu.be/C87mYyyV9qQ


Lessons Learned
---------------

* Always double check the correct parameters file is loaded.
* Check the quadcopter is calibrated correctly before flight testing.
* Encourage the workshop attendees to use simulator software (such as CRRCSim) to learn the basics of flying.
* Run a beta workshop beforehand with a few friends (particularly if using a custom hardware setup) to ensure all the bits and pieces fit together and are compatible with each other.
* Don't skimp out on the frame. Use a decent, strong frame.
* A ratio of 1 expert to every 3 to 5 attendees will cover most technical issues encountered by the attendees.
* It is very easy for attendees to get left behind in the build process. Schedule 1 or 2 small catchup sessions between the workshop evenings.
* Make sure you have enought screwdrivers, soldering irons and other tools.
* When ordering parts in bulk (such as motors and propellers) make sure the supplier has enough stock to cover your whole order.
* Always check RTL mode works correctly (by holding the quadcopter above your head and enabling RTL) before relying on it during an emergency.
* Fly well away from populated areas in case a quadcopter goes crazy and flys away.
* Check vibration level in Mission Planner.
* Always use telemetry radio logging.

Ideas For Future Workshops
--------------------------

* Anti-vibration foam for APM
* Use Gym for initial flying lessons - It's safer. Maybe Dickson College.
* Prop shrouds for safety.
* Use AR Drone frame and PX4 electronics.
* Use more solid frames from jDrones.
* Use the Turnigy 9xR Transmitter - it already has the firmware and backlight modifications done.
