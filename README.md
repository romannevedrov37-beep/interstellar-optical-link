## Simulation and Reliability Analysis of a Photon-Starved Interstellar Optical Communication Channel

## Brief Description

This project creates a reproducible Python simulation platform to investigate how structured information can be transmitted, degraded, and recovered across an interstellar-scale optical communication channel.

The project focuses on laser-based communication under photon-starved conditions, where the receiver may detect only a very small number of photons per time slot. The goal is to compare different error-control strategies and determine which combinations of modulation, erasure detection, forward error correction, and interleaving provide reliable message recovery under symbol loss, packet loss, and burst-loss conditions.

## Problem

Interstellar optical communication is extremely difficult because even a highly collimated laser beam spreads over interstellar distances due to diffraction, pointing limitations, and other physical losses. By the time the signal reaches the receiver, only a small fraction of the transmitted photons may be detected.

In this photon-starved regime, communication reliability depends not only on average signal power, but also on:

* randomness in photon arrival;
* background photons;
* detector efficiency;
* timing jitter;
* symbol and packet erasures;
* burst loss, meaning grouped losses of consecutive data;
* forward error correction and interleaving.

A communication system designed for this environment must be able to recover useful information even when part of the transmitted data is missing, unreliable, or incorrectly detected.

## Research Question

Which combination of PPM modulation, erasure detection, forward error correction, and interleaving provides the most reliable recovery of structured messages in a simulated photon-starved interstellar optical communication channel under 15–20% symbol or packet loss?

The project will compare several recovery strategies:

1. transmission without forward error correction;
2. simple bit-level correction methods, such as Hamming-style codes;
3. Reed–Solomon coding at the symbol level;
4. Reed–Solomon coding combined with interleaving for burst-loss resilience.

Additional stress tests may evaluate performance under higher loss rates, such as 25–30%, to identify the failure boundary of the system.

## Hypothesis

Reliable message recovery in a photon-starved interstellar optical communication channel depends not on a single error-correction code alone, but on the combined design of modulation, erasure detection, forward error correction, and interleaving.

The main hypothesis is that Reed–Solomon coding combined with interleaving and erasure-aware decoding will recover structured messages under 15–20% symbol or packet loss more reliably than transmission without FEC or simple bit-level correction methods, such as Hamming-style codes.

Reed–Solomon is used as the primary symbol-level error-correction method because it is well suited for recovering known erasures. Hamming-style codes and uncoded transmission are used as baseline methods for comparison.

## Approach

The project models a communication channel as a sequence of layers:

- message
- bytes 
- frame format
- Reed–Solomon coding
- interleaving
- PPM modulation
- photon-deficient optical channel
- SNSPD-type detector model
- PPM demodulation
- deinterleaving
- Reed–Solomon decoding 
- reconstructed message 
- The current goal of the project is to create a reproducible simulation environment in which different communication strategies can be compared under controlled assumptions.

## Metrics

The project will measure:

- recovery success rate;
- bit error rate;
- symbol error rate;
- packet error rate;
- erasure rate;
- uncorrectable failure rate;
- coding overhead;
- latency expansion;
- the difference in performance between no FEC, Reed–Solomon only, and Reed–Solomon with interleaving.

## Planned Repository Structure

 Root Files
README.md — main project overview and documentation.
requirements.txt — Python dependencies required to run the project.
run_demo.py — a simple end-to-end demonstration of the simulation pipeline.
run_experiments.py — script for running larger experiment sweeps and Monte Carlo trials.

 Configuration
configs/default.yaml — default simulation parameters.
configs/experiment_plan.yaml — planned experiment matrix for comparing different recovery strategies.

 Data
data/sample_payload.bin — sample structured message or binary payload used for testing.

 Documentation
docs/research_question.md — research question and hypothesis.
docs/project_scope.md — project boundaries, goals, and exclusions.
docs/model_assumptions.md — physical and computational assumptions used in the simulation.
docs/literature_notes.md — notes from scientific and technical sources.
docs/main_findings.md — final conclusions and key results.
docs/checkpoints/ — weekly progress reports and development notes.

 Source Code
src/channel/ — optical channel model, photon-rate calculations, erasure models, and burst-loss simulation.
src/detector/ — SNSPD-like detector model, including efficiency, dark counts, and timing jitter.
src/modem/ — PPM encoding and decoding.
src/framing/ — message framing, packet structure, headers, and checksums.
src/fec/ — error-control coding, including Hamming-style baseline, Reed–Solomon coding, and interleaving.
src/metrics/ — recovery success rate, BER, SER, PER, overhead, and failure metrics.
src/experiments/ — Monte Carlo trials and parameter sweep logic.

 Outputs
results/ — raw experiment results in CSV or similar formats.
figures/ — generated plots and final visualizations.
notebooks/ — exploratory notebooks for link budget, Poisson validation, and recovery demos.

 Tests
tests/ — unit tests for the main components of the simulation pipeline.

## Current Status

Initial phase of research and project setup.

Currently in progress:

- formulating the research question;
- setting up the repository;
- creating the first project documents;
- setting up the Python environment;
- building the first link budget and photon-rate models.

## Roadmap

Phase 1: Research Setup
Define the research question, assumptions, metrics, repository structure, and literature notes.

Phase 2: Physical Channel Model
Implement link budget calculations, photon rate estimation, and simulation of a Poisson photon-counting channel.

Phase 3: Modulation Layer
Implement and test PPM encoding and PPM decoding.

Phase 4: Loss and Reliability Models
Incorporate random erasures, burst loss, detector uncertainty, and confidence-based erasure marking.

Phase 5: Error Correction
Implement Reed–Solomon encoding, erasure-aware decoding, and interleaving.

Phase 6: Experiments
Conduct Monte Carlo comparisons between no FEC, Reed–Solomon only, and Reed–Solomon with interleaving.

Phase 7: Final Report
Prepare graphs, results, a reproducible demonstration, a technical report, and a final presentation.

## Limitations

The model is simplified and does not yet fully account for:

atmospheric turbulence;
real-world optical beam steering errors;
a complete astrophysical model of background radiation;
the detector’s hardware electronics;
real-world mission constraints in real-time mode.

## Current Final Goal

By the end of this project, the repository should contain a working simulation pipeline, experimental results, graphs, and a written analysis showing when structured messages can or cannot be recovered under 15–20% erasure and burst-loss conditions.

git add README.md
git commit -m "Write initial project README"
