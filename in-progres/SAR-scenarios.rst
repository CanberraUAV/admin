.. _sar-scenarios:

SAR Scenario Project
====================

This CanberraUAV project was spawned on :ref:`20130525-meeting`. It has an associated `SAR Scenario repository`_, initialised with content from :ref:`20130314_Belconnen_SES_presentation`.

.. _`SAR Scenario repository`: http://github.com/CanberraUAV/SAR-Scenarios

Work in Progress
----------------

 * documentation in the SAR-Scenario repository requires review, feedback and elaboration
 * Chris/Alex todo a desktop review session before next meeting 


Ideas
-----

Currently we have 4 "stories", which are more generic/abstract than a scenario. I think of them as use-cases, (classes of requirement) rather than scenarios (instances), which could be tested, evaluated, simulated, etc.

 * PROPOSAL: under each 'story', create a collection of realistic example scenarios. These would include a map, timeline and notes.
 * PROPOSAL: add an 'airframe hardware' section describing a few different classes of airframe. For example, 2.5kg multicopter, 4.5kg electric fixed wing, 20kg petrol fixed wing.
 * PROPOSAL: add a 'payload hardware' section describing a few different classes of sensor packages. For example, $1K CV rig (chameleon etc), $6K CV rig (upgraded chameleon-type rig), FPV (because it will come up), economy night vision rig, expensive night vision rig and multi-spectral agronomy rig (pair of CHDK point and shoot cameras, one with then NIR hack, coordinating RPi, etc).
 * PROPOSAL: Then, match up payloads, airframes and scenarios, and run simulated missions. Add a summary and the details of the relevant simulation to each scenario.
  
