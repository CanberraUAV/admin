Subprojects
==========================

A record of the status and progress of our subprojects

The stages of a subproject are based on the Technology Readiness Levels (TRL) - http://en.wikipedia.org/wiki/Technology_readiness_level

The levels we use are:

#. Initial Research - what stage is the technology at? Commecially available? Practical to build?

#. Detailed Research - does it seem feasible given CanberraUAV's financial and member resources

#. Ground Prototype - A simple prototype showing that the project's major concepts are sound

#. Small Scale Testing - field testing at a small scale

#. Full Size Testing - scaling up the pruject to the size we intend to use it at

#. Integration - ensure the project works with the other components (such as radios/ APM) reliably

#. Deployment - It is now able to be used reliably in CanberraUAV's operations


Current and Past Projects
-------------------------

Catapult System for the X8 UAV 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Stage: 5

Description: A rail launcher with internal bungee cords that can launch a fully loaded X8 UAV. It should be car-portable and simple to use.

Developers: Jack and Tridge

Status - Is able to launch small airframes (<2 kg). A major redesign will be required to scale it up to launching 5kg UAVs.


First person View (FPV) Technologies 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Stage: 1

Description: A custom FPV system and can be hooked into the onboard computer systems

Developers: Tridge

Status - On hold due to other projects taking priority


COFDM-based system for digital video transmission 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Stage: 1

Description: A long range radio transmission system for high-bandwidth video. Must be ACMA-legal

Developers: Dave

Status - On hold due to other projects taking priority


D-GPS for increased positioning accuracy 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Stage: 3

Description: A cheap Differential GPS (D-GPS) system for increased positioning accuracy

Developers: Tridge, Chris

Status - Intial research says it should be possible. Currently looking a GPS datastreams and building prototype.


ADS-B receiver for sense-and-avoid of other aircraft 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Stage: 3

Description: Using an ADS-B reciever to sense and avoid other aircraft in the area 

Developers: Tridge

Status - Hardware reciever works fine. Need to develop software to interpret messages and develop collision avoiding waypoints to send to the APM


(Automatic) tracking antenna for ground station 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Stage: 3

Description: A ground station antenna that will automatically point the (very directional) antenna at the UAV

Developers: Matt, Jack

Status - We have the pan/tilt servo. Needs a driver. Other infrastructure still needed too


Pan/Tilt/Rectract camera mount 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Stage: 1

Description: A roll/pitch stabilised platform for cameras on the UAV. Should have a cover to protect the camera during takeoff and landing

Developers: Chris, Matt

Status - On hold due to other projects


Radar system for terrain tracking and object avoidance 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Stage: 2

Description: Using a proper RADAR system for height above ground (AGL) detection and avoidance of ground-based obstacles

Developers: Steve

Status - Cost of a commercial system is too high at this point. Weight/Size is too high. We will bide our time until the technology becomes smaller/cheaper.


Ardurover-based truck for launching the X8 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Stage: 4

Description: Using a high-speed RC truck to launch the X8 UAV

Developers: Steve

Status - Works for small (<2kg) UAV's. The truck will need major upgrades to carry the X8 up to speed. On hold for now.


Weather Station for CMAC  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Stage: 7

Description: A remote weather station and camera located at CMAC with a web-based GUI

Developers: Jack, Tridge

Status - Is now up and running at http://weather.cmac.org.au/


General Non-technical Projects
------------------------------
Assisting local schools with their UAV programs 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: Assisting local colleges in integrating UAV technologies into their curriculums

Developers: Jack, Tridge

Github wiki and documentation system 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: Developing a way for CanberraUAV to store it's documentation online

Developers: Chris, Michael

MHV Quadcopter project 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Description: Run a workshop for the MakeHackVoid (MHV) community, showing them how to build and fly APM-based quadcopters.

Developers: Steve
