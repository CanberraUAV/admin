OBC 2014 Review
======================

This document is a review of the things that CanberraUAV did and did not do well at the 2014 OBC. It will serve as a starting point for how to improve our safety and reliability.

Things that went well
------------------------
 * Transport to/from Kingaroy worked well for everyone
 * Accommodation was suitable, despite the 2.4km separation. The 3-bedroom house had plenty of room for workshops to be set up
 * Spares and tools were appropriate. No spares or tools left behind that we required
 * RFD900 modems worked extremely well with a decent SNR margin (around 40dB) during all sections of the flight
 * Camera and Imaging worked as expected
 * Bottle drop accuracy was extremely good with the wind calculations taken into account.
 * Failover between the 5.8 GHz and 900MHz links worked as expected
 * Waypoint tracking during the mission was very accurate, despite the strong winds
 * The “butterfly” overflight for Joe location refinement, wind estimation and bottle drop confirmation was very valuable and resulted in a much closer drop distance to Joe
 * Packup after the flight went smoothly


Things that did not go well
---------------------------
 * RC failsafe did not work during scrutineering. Some cables were loose too
 * Team interview – equalise the speaking parts a bit more
 * The trailer worked very badly when carrying the Porter. Due to the rough ground it was bouncing around significantly. Could have led to damage.
 * Could have reduced the convoy to 3 cars (GCS van, car with airframe, car with people and spares)
 * Ethernet switch was killed when it was accidentally connect to 12V power rather than a 7.5V UBEC
 * Checklist had multiple issues
 
  * Not enough practice with the checklist
  * Confusion over who was supposed to do which check item
  * Lack of communication between GCS and Pilot as to status of checks
  * Confusion of the lack of separation from checklist items and procedural items
  
 * No contingency plans for an aborted takeoff or landing
 * No contingency plans for dealing with technical failures (such as the compass)
 * Hard ground at the GCS made setting up the GCS tent (with pegs) difficult
 * No method to level the antenna tracker on un-level ground
 * Tent prevented visibility of the runway from the GCS operator stations
 * Antenna tracker required a some yaw but mainly pitch offsets to correctly track the UAV
 * Takeoff had many issues
 
  * Incorrect compass offsets
  * Not accounting for the strong crosswind
  * Lack of experience in launching in strong crosswinds
  * Abort procedures was too binary (STICK_MIXING was disabled)
  * Lack of communication between Pilot and GCS in relation to wind conditions
  
 * Matt’s GCS station had the incorrect (older) version of MAVProxy (due to last minute update of cuav repo for NMEA support)
 * 5.8GHz antenna had too small a beamwidth, made tracking difficult
 * Servo cables in the wings came out during roadtrip
 * Due to dropped radio packets, the “joe move” command to move the butterfly pattern to a new position did not move all the appropriate waypoints the first time
 * Confused communications between GCS, OBC Liaison and OBC Judges in regards to permission to return to airport
 * Landing issues:
 
  * UAV came in too fast due to too short approach
  * Flare point was too far down the runway
  * Lack of experience in landing in windy conditions
  * Too much focus on gaining extra points in the OBC, rather than on safety
  
 * No data on airframe safe limits (ie. max windspeed before operations are aborted)


Items to focus on
------------------------

 * Checklists and procedures
 
  * Make them clearer (who does what)
  * Separate the checklist and procedure items
  * Practice them regularly
  
 * Abort modes and Contingencies
 
  * Write up clearer procedures for aborted takeoff, landing, etc
  * Practice them regularly
  
 * Automated takeoff and landing
 
  * APM code needs to be changed to be compass-independent
  * Need to test in a variety of conditions
  * Determine the maximum envelope for a "good" takeoff to guide saftey pilot decisions.
  
 * Tracking antenna
 
  * Perhaps replace with a couple of sector antennas
  * Need a method to level the antenna mast independent of ground/van level
  * Hard mounting of PixHawk may improve pitch accuracy
  
 * Create a safety management system for CanberraUAV
 
  * Checklists
  * Procedures
  * Tracking airframe and engine hours
  * Abort modes and contingencies
  
 * Ground Control Van
 
  * Potentially move the GCS into the van itself to reduce setup complexity
  * Integrate UBEC’s (don’t leave them separate) into any equipment connection to the 12V power system.
  
 * Better develop communications between Pilot and GCS
 * Practice more “full” setup (van, full GCS, etc) regularly with all team members on a regular basis.
 * Have a set of speaking points (regularly updated) that team members can use when talking about CanberraUAV, to ensure all team members have a similar level of knowledge about our operations.
 * Source Code Management
 
  * Continous build and integration of MAVProxy, cuav etc. with email notifications of each successful/failed build. i.e. when Tridge or someone else makes a change, we all know about it and can update our own setups.
  * Use the canberrauav git repo for deployment


