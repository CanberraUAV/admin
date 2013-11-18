.. _obc2014:

2014 UAV Outback Challenge - Hints for Other Teams
==================================================

These hints have been taken from CanberraUAV's efforts for the 2012 OBC, in addition to comments from the other teams that made it to Kingaroy.

 * Information (and rules) are available from http://www.uavoutbackchallenge.com.au/index.cfm?contentID=5
 * Note that the rules are usually updated several time throughout the competition, mostly to clarify any questions raised by entrants. Make sure to check that you are using the latest version.


Organisational:
 
 * A good number of team members is 4-7. Any fewer and you'll have too much work per person (unless you're doing this full-time). Any more and it'll be too difficult to manage and organise everyone.
 * Have a well structured and easily accessible central repository of data and documents. The data will accumulate faster than you think.
 * Have 1 person act as Team Manager to make sure things are going according to schedule.
 * Have a realistic schedule! Be prepared to change it in the face of airframe, technology, etc changes. As a general rule you should be settled on the hardware platform 6 months out and you should be able to fly a scaled-down OBC mission at 2 months out from the Challenge.
 * There should be a backup pilot and ground station operator.
 * Make sure each team member know what their role and responsibilities are during the challenge.

 
Testing:

 * Test as much as possible!!! This cannot be emphasised enough. This was one of the major reasons for teams not making it through the Challenge.
 * Test in a variety of weather conditions (wind, sunlight, temperature).
 * Run small scale tests and use software simulations to verify individual components work, before integrating them all together.
 * Use small RC aircraft as test platforms - they are far easier to repair or replace.
 * Build up your own RC flying skills.
 * Test the ground station operations and procedures to ensure they fit into the 1 hour time slot for the Challenge.
 * Make check-lists and operations manuals to reduce the risk of something being forgotten.
 * Log all the flights!! Telemetry data is essential for debugging a crashed flight after-the-fact.
 * Take photos and videos of the flight where possible!
 * Do a few practice OBC's to ensure the everything works together.
 * Verify the failsafe systems work by simulating the failure modes on the ground. Always test that the failsafes cannot be accidentally triggered by unrelated events during flight.
 
 
Airframe:
 
 * Have a number of small airframes for testing individual parts of the UAV system.
 * Look carefully at the range/weight requirements when selecting the airframe. Validate them on a real flight.
 * How much does wind affect the airframe? Can this wind be expected at Kingaroy?
 * Vibration (particularly in nitro/petrol airframes) can degrade sensor accuracy (particularly accelerometers and gyros) and cause plugs and ports to come apart in mid-flight. Make sure all plugs are securely fastened with tape or similar. Use lock-tight on the screws.
 
 
Autopilot:
 
 * If using off-the-shelf autopilot:
 
   * Spend time working out exactly how to program/edit the settings
   * Understand it's limitations.
   * Fly with it as much as possible to get experienced with it.
   * Make sure it has a manual override so the pilot can "rescue" the UAV if needed.
   * Work out early on what soft of changes need to be made (or bought/built) to make it OBC compliant.
   
 * If developing your own:
 
   * Start early, they are very complex to build (unless you have an degree in aerospace engineering and a lot of free time).
   * Build a software simulator for the code. Bugs can be very deadly on real flights.
   
   
Radios

 * Be aware of the Australian limitations on the maximum EIRP of radio transmitters:
 
   * For the 900MHz band 1W EIRP (minimum 20 hopping channels - a frequency hopping transmitter).
   * 4W  EIRP for the 5.8 GHz band and 2.4 GHz band (a digital modulation radiotransmitter).
   * See http://www.comlaw.gov.au/Details/F2011C00543 for full info.
   
 * Check the radio link will still work (and have enough bandwidth) over the maximum range into the search area.
 * Using two links over different frequencies (and technologies) can provide redundancy.
 * Using 3G radios over the mobile phone network can have some latency and drop outs.
   
   
Camera and Image Detection

 * Check that the camera can easily see a person (want a minimum of 20cm/pixel) from the UAV.
 * The camera's field of view and the UAV's altitude will determine how large an area can be captured per frame.
 * Vibration from the UAV's power plant (see Airframe section) can lead to blurred images. A camera with a global shutter will vastly reduce this problem.
 * If doing automatic image detection on the UAV, prepare to spend plenty of time fine-tuning the algorithm.
 * Collect sets from test flights over a variety of terrain types (and colours). Build and use a Joe dummy.
 * If doing manual image detection, ensure the radio link has enough bandwidth to dump the images to the ground station in a timely manner.
 * A full description of the imaging software that CanberraUAV used can be found at http://diydrones.com/profiles/blogs/demonstration-of-canberrauav-image-search-algorithm
 
 
Ground Station
 
 * Have a setup that is quick and easy to build and and take down (you have 20 min in the Challenge).
 * Have some sort of sunshade for the screens - it is very sunny in Kingaroy.
 * Multiple laptops and ground station roles are a plus (i.e. someone to monitor UAV status, someone to monitor the imagery).
 * Bring chairs!
 
 
Getting to Kingaroy
 
 * Kingaroy is about 200km West of Brisbane. For international visitors, it would be easiest to fly into Brisbane and hire and car and drive up to Kingaroy.
 * Arrive several days in advance to repair any equipment broken or lost in transit.
 * Kingaroy is a small town. They will not necessarily have spare airframe or electronics parts available. Bring spares (and tools).
 
 
The Deliverables

 * Understand what each deliverable is asking for well in advance
 * D1 and D2 are relatively easy
 * D3 (the 5 hours worth of flight logs) is where most teams fall down. Get the flight hours up as soon as possible. Don't wait until a few weeks beforehand. It is very easy for a bug or crash to delay flying for a week or more.

 
Misc Hints

 * Be careful of any RC failsafes. In most autopilots, the UAV will activate a failsafe if it loses the RC signal during  flight. It does not have to do this during the OBC - indeed it must not, due to the UAV going outside of normal RC control range and thus losing RC link during the main flight.
 * Don't fly close to the mission boundary. The GPS can be off by up to 15m in Australia (due to a lack of WAAS). If the UAV brushes the boundary, it will activate the failsafe.
 * Test the bottle drop mechanism many, many times. If your airframe configuration is a pusher, be aware that a bottle drop parachute may get caught in the propeller.
 
 
 
