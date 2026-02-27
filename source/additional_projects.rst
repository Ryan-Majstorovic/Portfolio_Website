Additional Projects
===================

Project 1: ESP32 Smart Thermostat (Home Assistant Integrated)
--------------------------------------------------------------

**Timeframe:** Summer 2025

Description
~~~~~~~~~~~

Built a custom smart thermostat that interfaces with a standard 24 VAC HVAC
control system while providing monitoring and control through Home Assistant.
The objective was to replace an off-the-shelf thermostat with a fully
customizable system for logging, control, and automation integration.

Your Role
~~~~~~~~~

- Owned the project end-to-end
- Designed and debugged 24 VAC to 3.3 V power and interface circuitry
- Implemented firmware and Home Assistant integration workflow
- Performed integration testing and documentation

Tech Stack
~~~~~~~~~~

- MCU: ESP32
- Firmware: C/C++ (ESP-IDF/Arduino workflow by stage)
- Interfaces: GPIO HVAC control, sensor I2C/analog, Wi-Fi integration
- Tools: Home Assistant, DMM, oscilloscope

Skills or Knowledge Gained
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Mixed-voltage system design
- Embedded debugging and validation with instrumentation
- End-to-end integration of an embedded node into a broader automation system

Resources Used
~~~~~~~~~~~~~~

- Home Assistant documentation/community references
- ESP32 framework documentation
- Component datasheets
- DMM and oscilloscope for bring-up

Measurable Outcome
~~~~~~~~~~~~~~~~~~

Demonstrated stable HVAC control from a 3.3 V platform with repeatable
sensor-driven behavior and Home Assistant telemetry/setpoint control.

Proof and Links
~~~~~~~~~~~~~~~

.. image:: _static/img/HA_thermostat.png
   :alt: Senior design deliverables overview diagram
   :align: center
   :width: 40%

:ref:`Home Assistant integration Code <Thermostat.yaml.txt>`_

Project 2: 10 GHz BPSK Modulator Board (Balun + RF Switch)
-----------------------------------------------------------

**Timeframe:** Fall 2026

Description
~~~~~~~~~~~

Designed a BPSK modulation approach for a 10 GHz carrier using a passive phase
split and an RF switch. Two carrier paths 180 degrees apart are generated, and
an SPDT RF switch selects the output path using an NRZ data stream to produce
0 degree and 180 degree BPSK phase states.

Your Role
~~~~~~~~~

- Defined system architecture for phase-path generation and selection
- Selected RF components based on frequency range and insertion loss goals
- Planned GHz PCB layout strategy (impedance control, grounding, isolation)
- Planned validation measurements for phase state and spectral behavior

Tech Stack
~~~~~~~~~~

- RF blocks: balun/phase split path, SPDT RF switch, RF connectors
- Control: NRZ logic signal for switch drive
- CAD: PCB layout workflow
- Test equipment: RF source, spectrum analyzer, VNA, oscilloscope

Skills or Knowledge Gained
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Translating modulation theory into implementable RF architecture
- Evaluating GHz RF components (loss, isolation, return loss, bandwidth)
- RF layout fundamentals and digital-to-RF coupling control
- RF measurement workflows for modulation verification

Resources Used
~~~~~~~~~~~~~~

- Vendor RF component datasheets/application notes
- Course notes on modulation and measurement
- RF lab instrumentation references

Measurable Outcome
~~~~~~~~~~~~~~~~~~

Achieved a working BPSK modulator with clear phase states and expected spectral characteristics at 10 GHz, validated through measurements.


Project 3: CPRE 288 CyBot Autonomous Robot
------------------------------------------

**Timeframe:** Spring 2025

Description
~~~~~~~~~~~

Developed software for a CyBot-style robotics platform focused on sensing,
motion control, and autonomy. The work emphasized real embedded workflow:
drivers, timing, calibration, and structured hardware testing.

Your Role
~~~~~~~~~

- Implemented embedded drivers and integration logic for sensing and motion
- Performed calibration to map sensor data into control decisions
- Built and tuned control loop behavior using measured results

Tech Stack
~~~~~~~~~~

- MCU: TI Tiva TM4C123G
- Language: C
- Peripherals: GPIO, timers, PWM, UART, ADC
- Tools: course toolchain, serial terminal, lab instrumentation

Skills or Knowledge Gained
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Embedded peripheral configuration and timing-aware driver development
- Sensor calibration and validation workflows
- UART-based debugging and structured test execution

Resources Used
~~~~~~~~~~~~~~

- TivaWare library and TM4C123G datasheet
- Course libraries, lab handouts, reference code
- Oscilloscope, DMM, and serial tools

Measurable Outcome
~~~~~~~~~~~~~~~~~~

Achieved repeatable autonomous behavior with sensor-informed decisions validated
through test runs and logged measurements.



