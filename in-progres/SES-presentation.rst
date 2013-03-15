.. _20130314_Belconnen_SES_presentation:

SES Presentation
================

On 2013/03/14, representatives of CanberraUAV visited the Belconnen Branch of the ACT State Emergency Service. Tridge gave a presentation (available in :download:`PDF<SES-presentation/20130314_Belconnen_CanberraUAV.pdf>` or :download:`ODP<SES-presentation/20130314_Belconnen_CanberraUAV.odp>` format), we showed them some planes, and we had some interesting hypothetical conversations about how the SES might deploy small UAVs to contribute to search and rescues.



Summary of applications discussed
---------------------------------

The following scenarios are a synthesis of questions asked during the presentation and general discussion afterwards.

Aerial Search
^^^^^^^^^^^^^

Contrary to what we had imagined, the OBC search area is not unrealistically small. In fact, SES are routinely deployed to search areas under 1 square km.

Searching for an unobscured, high visibility target that strongly contrasts a monotonous background is however unrealistic. It's clear we need to push our vision system harder with some more difficult scenes. Various scenarios were discussed, and the focus was on effectively detecting people in different terrain. It was suggested we continue those discussions with personnel involved in spotting from full scale aircraft (this is not something the SES do themselves).

There was some specific interest in searching over waterways and swampy terrain, where foot traffic is especially slow and we could reasonably expect a UAV to have good visual access to the ground (surface). There was also specific interest in thermal imaging, especially at night, and especially rapid deployment of thermal imaging at crime scenes where the search target might have a fading heat signature.


Aerial contribution to ground-based search of roads
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One common mode of operation for SES in a wide area search is to travel along roads/tracks (as opposed to grid-searching). This is a high impact activity typically performed early in a search process. A UAV could act as a "force multiplier" that accelerate this process, so that a combination ground/UAV effort completes the task sooner.

Scenario (without UAVs): A search team has been tasked with scanning the roads between point A and point B. The primary route may be up to 30km. They whole party travels along the primary route for a few Km, where they meet a junction. At the junction, the team splits and a rapid response team are sent to investigate a the side road while the main party travels more slowly along the primary route. The rapid response team travels up the side road, then backtracks to the main road and catches up with the main party. Meanwhile, the main party travels to the next junction and dispatches another rapid response team. The search continues in this fashion until the team arrives at point B, having searched the main route and side tracks.

Scenario with a UAV: A medium sized UAV is deployed from an improvised runway (section of road) somewhere in the vicinity of point A. The UAV is deployed at the same time as the search party, and completes a preliminary search of the primary route within 15 minutes. By 20 minutes, the coordinators have identified numerous junctions/side roads along the primary route and issue updated information to the search team.

During the next 40 minutes, the UAV travels another 80km on it's return journey. Perhaps 40km of this is spent effectively scanning identified side routes. Many of the side route investigations reveal tracks that are obscured by foliage, and will still require investigation by a ground team. However, some of the side routes are clear and searched effectively by the UAV. Each time a side route is effectively searched by the UAV, the coordinators issue a report to the to the search team informing them that it will not be necessary for them to visit that route during this phase of the search.

Approximately 60 minutes after the UAV/search party have been deployed, the UAV lands. At the 70 minute mark it has been refueled and relaunched, and goes on to effectively scan another 60km of side route in the next hour (traveling over 120km in the process). This is repeated as many times as necessary.


Aerial Reconnaissance
^^^^^^^^^^^^^^^^^^^^^
Route-finding and route-planning is a significant aspect of ground based search operations. To access a search area, teams sometimes have to travel significant distances through dense or challenging terrain. This can impose a high time-cost on the SAR effort. As well as being difficult and time consuming, the access routes can exposed teams to unexpected hazards (e.g. wild dog packs). Aerial reconnaissance with a UAV could assist the SES team reach the search area faster and more safely.

Scenario: A search team has been tasked with searching an area 8km from the nearest road. Examination of the topographic maps suggest a number of possible routes, but on the information available there is no clear best route. If they chose a good route team might arrive at the search area in as little as 90 minutes, but if they are hampered by terrain or forced to backtrack they might take 3 hours to reach the search area.

It would be of benefit in this situation to have a small UAV reconnoiter candidate routes, and (through image post-processing) augment their existing maps with high resolution orthophotos. For example, if a small fixed wing UAV was deployed at the same time the search party, within 30 minutes it could have traveled 50 km and photographically surveyed all candidate route. A coordinator at the UAV ground-station (or headquarters if the ground-station has 3G reception) could relay intelligence to the ground team over radio, describing vegetation along various routes and comparing it with vegetation that the team has already passed through, alerting them to hazards or issues, etc.


Patrolling previously searched areas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Roads are rapidly searched during the early phase of a search. During later stages of the search (for example when the ground based teams are occupied with grid searches) it's possible that the target will self-rescue and arrive on a road. During these later stages, there would be value in repeatedly re-searching (patrolling) the roads from the air.


Interoperability Research
-------------------------
As well as understanding the scenarios where UAVs might be a useful tool, we were also very interested to discover what we would have to do to inter-operate with the SES. We need to know how we might communicate with the SES during a SAR operation (real or simulated), as well as how we might integrate with training, planning and other logistical aspects.

It turn's out that there is a well organised and clearly structured way to solve this problem, called Australasian Inter-Service Incident Management System.

http://en.wikipedia.org/wiki/Australasian_Inter-Service_Incident_Management_System

SMEAC
^^^^^

One significant artifact from AIIMS is  a 'SMEAC' document (Situation, Mission, Execution, Administration, Command). Essentially, this document is the message passed to an emergency services team that tasks them with performing an operation (such as a search and rescue operation).

We obtained a recent SMEAC. It's not appropriate to publish it here because it contains specific names and contact details of various parties, however in reviewed it has the following sections:

 * Situation: ~1/2 page of text describing the assignment
 * Mission: one sentence describing the scope and outcome of the assignment
 * Execution: ~3 1/2 pages of text, broken down into the following (highly domain specific) sections:

   * Ambulance support: FRB Ambulance Support, Patient Transport, First-aid supplies and Kits, SES PPE/Uniform.
   * Flood Rescue Boats and AFP Support: Operations Position Holders, SES PPE/Uniform
   * Event Management Support: SES PPE/Uniform

 * Administration: ~1/2 page covering vehicles and parking, catering, access to maps, etc.
 * Command/control/communication (somewhat domain specific): 

   * ~1/2 page describing time and place of briefings, use of TRN network, etc.
   * ~ 1 1/2 page (tabulated) member attendance roster, contact details etc.
   * 1 page map

If we were participating as part of the SES, our assignment would be described within the SES SMEAC. If we were operating in conjunction with other emergency service then we would have a specific SMEAC covering our assignment.

The example SMEAC we reviewed was issued by the the ACT Emergency Service Agency.

http://en.wikipedia.org/wiki/Australian_Capital_Territory_Emergency_Services_Agency

It was suggested that we make contact with someone from the Planning and Logistics section of the above agency to further discuss hypothetical inter-operate as part of a larger emergency service response.


SES Training
^^^^^^^^^^^^

If we are to work with the SES, we need to understand there capabilities as well as they understand ours. A consultant from Trimevac_ (A training service provider to the SES) was present at the meeting, and we briefly reviewed three training packages delivered to the SES. This is defined under the AQTF_ (Australian Quality Training Framework) as:

 * PUASAROO8A_: Search as a Member of a Land Search Team
 * PUAOPE003A: Navigate in Urban and Rural Environments
 * The SES General Rescue Learners Guide, covering:

   * PUASAR001A: Participate in a rescue operation
   * PUAEQU001A: Prepare, maintain and test response equipment
   * PUAOH001A: follow defined occupational health and safety policies and procedures (part of the Public Safety training package)

The context of these competencies is the PUA00_ Public Safety Training Package.

.. _Trimevac: http://www.trimevac.com.au
.. _AQTF: http://www.comlaw.gov.au/Details/C2011A00012
.. _PUASAROO8A: http://www.communitysafety.qld.gov.au/CRTI/PDF/ODO_20_0_Search_Urban_and_Rural_v1_0.pdf
.. _PUA00: http://training.gov.au/TrainingComponentFiles/PUA00/PUA00_R8.1.pdf

.. ,_PUAOPE003A:
.. ._PUASAR001A:
.. ._PUAEQU001A:
.. ._PUAOH001A:

This seems relevant for a few reasons:
 * if we provide training to SES members, this defines the skills/knowledge we can assume they bring to the training
 * this identifies the knowledge/certification we may need to obtain before we are able to participate in joint exercise with the SES
 * any training we provide should be framed in a similar way
 * most likely opportunities for joint exercises would be a variation on existing training packages

The trainer responded positively to the prospect of contributing to desktop and live field search and rescue simulations incorporating UAVs.


Preparation for the SES presentation
------------------------------------

The following information was prepared prior to our meeting with the SES.

related page: :ref:`obc2012`

Current Capability
^^^^^^^^^^^^^^^^^^

> what you're capable of doing at the moment?

We essentially have two capabilities; operational capability to compete in (and win) the OBC competition, and development capability to push the boundaries of what's currently possible with open-source UAV technology. We use the OBC search and rescue competition to focus our development efforts.

We have several small scale technology demonstrators showing the major features of our search and rescue capability:

 * Cameras
 * Automatic person recognition
 * Automatic waypoint generation, given a search area
 * Ground station

Currently we can search a 2x4km area in less than 1 hour (assuming a nearby sealed road/runway to use) using our main UAV.

Current Activity
^^^^^^^^^^^^^^^^

> what you're working on/think might be possible?

We are currently working on:

 * Ability to takeoff from unprepared tracks or surfaces (using a catapult or similar)
 * More automation of flight phases
 * Longer range and larger search areas
 * Incremental upgrades to the camera and image processing system will allow us to cover a given search area in less time
 * Better terrain avoidance
 * Sense and avoid of manned aircraft
 * More user-friendly ground station software
 * Better positioning accuracy for the UAV
 * Reducing and simplifying setup time
 * Increasing overall reliability of systems (especially the autopilot and fail-safe devices)

> What's possible?

One day, a future version of the technology we are making now will save a life in the ACT. It's not a matter of *if*, it's a matter of **when**.

There is much work to do before that can happen though. In 18 months we will be fielding at least one team in the next OBC SAR competition. Our main development goal is to demonstrate capability much closer real world SAR requirements.

SAR Ignorance
^^^^^^^^^^^^^

> what you guys want to know from us?

We don't know what we don't know. How far are we from being able to work with the SES?

 * table-top exercises?
 * field exercises?
 * ... possibility of contributing to an actual search?

Characteristics of a typical SAR operation:

 * What is the average search area size?
 * How fast can it be searched on foot?

System requirements:

 * What level of ease-of-use of the software is needed?
 * Would you be comfortable operating the UAV in manual mode if the autopilot fails?
 * Do you require the ability for the UAV to drop a small payload to the stranded person (water, radio?)
 * What sort of setup time is required (is currently 4 or so hours, using 4 people)
 * Does the entire UAV/Ground station need to be self-contained. Like a plug and play system?

Resource availability:

 * What infrastructure (if any) could you furnish us with at the “base command” of a SAR or training exercise? (power, radios, Internet, fuel, takeoff/landing space)
 * If the UAV does crash, could you assist with recovery?
