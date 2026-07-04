# Project Scope

This document defines the scope of the project and separates the simulation work from topics that are outside the current project boundaries.

## Project Objective

The goal of the project is to build a reproducible simulation environment for studying message recovery in a photon-starved interstellar optical communication channel.

The project focuses on the reliability of the communication pipeline, not on building real optical hardware.

## What Is Included in the Project

The project includes:

- modeling a structured message as bytes and frames;
- applying Reed–Solomon forward error correction;
- applying interleaving to reduce the effect of burst loss;
- converting encoded data into PPM symbols;
- simulating a photon-starved optical channel;
- modeling random photon-counting behavior;
- modeling detector imperfections such as efficiency, dark counts, timing jitter, and dead time;
- simulating symbol erasures, packet erasures, and burst-loss events;
- performing PPM demodulation;
- applying deinterleaving and Reed–Solomon decoding;
- measuring recovery performance using reliability metrics.

## Reliability Metrics

The main reliability metrics are:

- recovery success rate;
- bit error rate;
- symbol error rate;
- packet error rate;
- erasure rate;
- uncorrectable failure rate;
- coding overhead;
- performance difference between no FEC, Reed–Solomon only, and Reed–Solomon with interleaving.

## What Is Not Included

The project does not include:

- building a real laser transmitter;
- building a real telescope receiver;
- designing real SNSPD hardware;
- modeling the full superconducting physics of SNSPD detectors;
- designing cryogenic cooling systems;
- implementing real adaptive optics hardware;
- modeling a full astrophysical background radiation environment;
- simulating every possible atmospheric effect in detail;
- creating a complete mission-grade DSOC system;
- proving new coding theory results.

These topics may be mentioned as background, but they are not part of the implementation goal.

## Why This Is a Simulation-Only Project

This project is limited to software simulation because building a real interstellar optical communication system would require specialized hardware, laboratory equipment, optical components, cryogenic detector systems, and mission-level engineering.

The project does not attempt to build:

- a real laser transmitter;
- a real telescope receiver;
- a real SNSPD detector;
- cryogenic electronics;
- adaptive optics hardware;
- spacecraft pointing hardware.

Instead, the project uses simplified mathematical and computational models to study the reliability of message recovery under photon-starved conditions.

## What Hardware Rabbit Holes Are Prohibited

The following topics are considered hardware rabbit holes for the current phase of the project:

- laser cavity design;
- semiconductor laser fabrication;
- optical amplifier hardware;
- telescope mirror engineering;
- adaptive optics hardware design;
- SNSPD material physics;
- cryogenic electronics;
- real-time spacecraft pointing hardware;
- physical construction of a transmitter or receiver.

These topics are important in real optical communication systems, but they are outside the scope of this simulation project.

The project may use simplified parameters inspired by real systems, but it does not attempt to reproduce the full hardware design.

## What Assumptions Are Used

The project uses simplified assumptions to make the simulation controllable and reproducible.

The main assumptions are:

- the transmitter can produce timed optical pulses according to PPM encoding;
- the channel can be modeled using photon-counting behavior;
- photon arrivals can be approximated probabilistically;
- detector behavior can be simplified using efficiency, dark counts, timing jitter, and dead time;
- missing or unreliable symbols can be represented as erasures;
- Reed–Solomon coding is used as the main symbol-level FEC method;
- interleaving is used to spread burst losses across multiple codewords.

These assumptions are simplified and may be refined later.

## What Constitutes a Successful Outcome

The project is successful if it produces:

- a working Python simulation pipeline;
- clear assumptions and limitations;
- reproducible experiments;
- comparison between at least three strategies:
  - no FEC;
  - Reed–Solomon only;
  - Reed–Solomon with interleaving;
- metrics showing when recovery succeeds or fails;
- graphs or tables summarizing the results;
- a written analysis explaining the findings.
