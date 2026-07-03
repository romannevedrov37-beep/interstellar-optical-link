# Literature Notes

## 1. Photon-Starved Optical Channel
A photon-deficient optical channel is a communication channel in which the receiver detects only a very small number of photons per time interval.
In interstellar optical communication, even a highly collimated laser beam propagates over extremely long distances due to diffraction and other physical losses. As a result, a ground-based telescope can intercept only a tiny fraction of the total transmitted photon flux. It must contend with rare photon detections, background photons, detector error, and temporal noise.
For this project, the photon-deficient channel is modeled using the following parameters:
number of signal photons per time interval;
number of background photons per time interval;
detector efficiency;
synchronization jitter;
symbol or packet drops;
packet loss events;
probabilistic behavior of photon counting.

The main question is whether it is possible to reconstruct structured messages when the received signal is weak, noisy, and partially missing.

## 1.1 Laser Transmitter and PPM Encoding
In this project, the transmitter is modeled as a system that converts digital data into timed optical pulses using pulse-position modulation (PPM).

In PPM, information is represented by the position of a short pulse inside a predefined time frame. For example, a group of bits such as `0010` can be mapped to a specific PPM slot. The encoder determines which slot should contain the pulse, and the modulator generates the corresponding electrical control signal for the laser source.

The laser source converts this electrical input into coherent optical radiation. In simplified terms, electrical pumping excites the active medium of the laser. Through stimulated emission, photons are amplified in a selected optical mode, producing radiation with narrow spectral bandwidth, high directionality, and phase coherence within the limits of the laser system.

When the modulator sends a control pulse, the laser emits a short optical pulse at the required time. In a PPM system, the information is carried mainly by the timing position of this pulse rather than by continuous changes in optical intensity.

The laser transmitter is treated as a simplified source of timed coherent optical pulses that can be sent through the photon-starved optical channel.

## 1.2 Beam Propagation and Diffraction
After generation, the laser beam passes through transmitting optics such as a beam expander or a telescope-like optical system. The purpose of this stage is to increase the beam diameter, improve collimation, reduce divergence, and point the beam toward the target receiver.

Even with strong collimation, the beam cannot remain perfectly parallel over interstellar distances. Because of diffraction, the beam gradually expands during propagation. As the beam footprint grows, the transmitted photons are distributed over an increasingly large area, which reduces the photon flux available to the receiver.

Over distances on the order of `10^16` meters, this spreading becomes a central limitation of interstellar optical communication.

## 1.3 Photon-Starved Receiver
In a situation where a ground-based or space-based telescope captures only a very small fraction of the transmitted photon flux, the receiver operates using rare photon detections within discrete PPM time slots. Some slots may contain signal photons, some may contain only background photons, and some may contain no detected photons at all.

The receiver’s task is to estimate which time slot most likely contained the transmitted PPM pulse. This is challenging because the observed photon counts are influenced by several factors:

- low signal photon rate;
- background photons;
- detector efficiency;
- dark counts;
- timing jitter;
- synchronization uncertainty;
- photon-counting randomness;
- possible symbol or packet erasures.

Since photon arrivals are random, the receiver cannot assume that the correct slot will always contain a large number of detected photons. Instead, the receiver must make a probabilistic decision based on the photon counts observed in each slot.

For example, in a PPM frame, the receiver can compare photon counts across all slots and select the slot that provides the strongest evidence for the transmitted pulse. If the evidence is too weak or ambiguous, the receiver may mark the symbol as an erasure instead of forcing a potentially incorrect decision.

This is important because erasures are often easier for error-correcting codes such as Reed–Solomon to handle than unknown symbol errors.

## 2. Detector Model
The detector model describes how the receiver converts incoming photons into measured photon-count events.

In this project, the detector is modeled as an SNSPD-like photon-counting detector. SNSPD stands for Superconducting Nanowire Single-Photon Detector. A real SNSPD is a highly sensitive detector capable of registering individual photons, but this project does not model the full hardware physics of the device. Instead, it uses a simplified detector abstraction with the parameters most relevant for communication reliability.

The detector model answers the question:

> If photons arrive at the detector input, how many of them are actually detected, and how reliable are those detections?

The main parameters of the detector model are:

- **detector efficiency** — the probability that an incoming photon is actually registered;
- **dark counts** — false detection events that occur even when no signal photon arrives;
- **background counts** — detected events caused by background photons from external sources such as stars, sky background, or other optical noise;
- **timing jitter** — uncertainty in the measured arrival time of a photon;
- **maximum count rate** — the approximate limit on how many photon events the detector can register in a given time interval;
- **dead time or recovery time** — a short period after a detection during which the detector may be unable to register another photon.

In the simulation, the detector receives incoming photons from the optical receiver path and produces observed photon-count events for each PPM time slot. These observed counts are not always equal to the true transmitted signal because photons may be missed, false counts may be added, and photon arrival times may be shifted by timing jitter.

The detector output is then passed to the PPM demodulation stage. The demodulator uses the observed photon counts to estimate which PPM slot most likely contained the transmitted pulse. If the evidence is weak or ambiguous, the symbol may be marked as an erasure instead of forcing a potentially incorrect decision.

## 3. Forward Error Correction

Forward Error Correction (FEC) is a method of adding redundancy to transmitted data before it passes through the communication channel. The goal is to allow the receiver to recover the original message even if some symbols are corrupted, lost, or marked as unreliable.

In this project, Reed–Solomon coding is used as the main FEC method. Reed–Solomon is a symbol-level error-correcting code, which makes it suitable for packetized or byte-oriented data. It is especially useful when the receiver can identify unreliable symbols as erasures.

A Reed–Solomon code is commonly written as `RS(n, k)`, where:

- `k` is the number of original information symbols;
- `n` is the total number of symbols after encoding;
- `n - k` is the number of added parity symbols.

For example, an `RS(7, 3)` code takes 3 information symbols and adds 4 parity symbols, producing a 7-symbol codeword:

```text
D1 D2 D3 → D1 D2 D3 P1 P2 P3 P4
```

If some symbols are lost during transmission, the decoder may still recover the original data:

```text
D1 ? D3 P1 ? P3 P4
```

The `?` symbols represent erasures, meaning that the receiver knows which symbol positions are missing or unreliable.

For unknown symbol errors, where the decoder does not know the error positions, an `RS(n, k)` code can correct up to:

```text
t = floor((n - k) / 2)
```

unknown symbol errors.

For erasures, where the unreliable positions are known, Reed–Solomon can handle up to `n - k` erased symbols. More generally, for a mixture of unknown errors and erasures, successful decoding requires:

```text
2e + s ≤ n - k
```

where `e` is the number of unknown symbol errors and `s` is the number of erasures.

In many practical examples, one Reed–Solomon symbol is treated as one byte, or 8 bits. More generally, an RS symbol is an element of a finite field, so its size depends on the chosen code parameters.

Reed–Solomon coding and PPM modulation operate at different layers of the communication chain. Reed–Solomon protects the data by adding parity symbols, while PPM converts the protected bitstream into timed optical pulses.

The transmission order is:

```text
structured message
bytes
Reed–Solomon encoding
protected symbols
bitstream
PPM modulation
optical pulses
photon-starved channel
```

At the receiver, the process is reversed:

```text
photon detections
PPM demodulation
recovered bitstream
RS symbols
Reed–Solomon decoding
recovered message
```

This distinction is important because an RS symbol is not the same as a PPM symbol. An RS symbol is a data symbol used for error correction, while a PPM symbol is a time-slot pattern used for optical modulation.

In this project, Reed–Solomon coding is used to test whether structured messages can still be recovered when the photon-starved channel produces random errors, erasures, or burst-loss events.

## 4. Erasures and Burst Loss
An erasure is a symbol or packet that the receiver identifies as missing or unreliable.

This is different from an unknown error. In an unknown error, the receiver gets a value, but the value may be wrong and the receiver does not know where the error is. In an erasure, the receiver knows the position of the missing or unreliable data.

Example:

```text
original:  D1 D2 D3 D4
received:  D1 ?  D3 D4
```

The `?` symbol represents an erasure.

Erasures are important because error-correcting codes such as Reed–Solomon can usually handle known missing positions more effectively than unknown symbol errors.

Burst loss is a group of consecutive losses or erasures.

Example:

```text
original:  D1 D2 D3 D4 D5 D6 D7 D8
received:  D1 D2 ?  ?  ?  D6 D7 D8
```

This type of loss is more damaging than isolated random erasures because it can destroy a continuous part of the encoded data.

In this project, erasures and burst-loss events are used to model unreliable photon-starved reception. They may be caused by weak signal intervals, detector uncertainty, synchronization problems, pointing errors, or temporary increases in background noise.

The main purpose of this section is to define the loss patterns that will later be tested with Reed–Solomon coding and interleaving.
## 5. Interleaving
An erasure is a symbol or packet that the receiver identifies as missing or unreliable.

This is main difference: in an unknown error, the receiver gets a value, but the value may be wrong and the receiver does not know where the error is. In an erasure, the receiver knows the position of the missing or unreliable data.

Example:

```text
original:  D1 D2 D3 D4
received:  D1 ?  D3 D4
```

The `?` symbol represents an erasure.

Erasures are important because error-correcting codes such as Reed–Solomon can usually handle known missing positions more effectively than unknown symbol errors.

Burst loss is a group of consecutive losses or erasures.

Example:

```text
original:  D1 D2 D3 D4 D5 D6 D7 D8
received:  D1 D2 ?  ?  ?  D6 D7 D8
```

This type of loss is more damaging than isolated random erasures because it can destroy a continuous part of the encoded data.

In this project, erasures and burst-loss events are used to model unreliable photon-starved reception. They may be caused by weak signal intervals, detector uncertainty, synchronization problems, pointing errors, or temporary increases in background noise.

The main purpose of this section is to define the loss patterns that will later be tested with Reed–Solomon coding and interleaving.
## Note

These concept notes are currently draft explanations generated with the assistance of AI.  
They will be verified and expanded using scientific papers, technical reports, and official documentation.

## Source Notes
## 1.3 Photon-Starved Receiver
**Title:** A superconducting nanowire photon number resolving four-quadrant detector-based Gigabit deep-space laser communication receiver prototype  
**Authors:** Hao Hao et al.  
**Year:** 2022  
**Type:** arXiv preprint  
**Category:** SNSPD / PPM / FEC / Photon-sensitive receiver  
**Link:** https://arxiv.org/abs/2212.04927

## 2. Detector Model
### SNSPD-like detector
**Title:** Superconducting Nanowire Single Photon Detectors for DSOC  
**Author / Organization:** NASA Jet Propulsion Laboratory, Microdevices Laboratory  
**Year:** 2022  
**Type:** Official technical webpage  
**Category:** SNSPD / Detector Model / DSOC / Photon-counting receiver  
**Link:** https://microdevices.jpl.nasa.gov/news/superconducting-nanowire-single-photon-detectors-for-dsoc/

## 3. Forward Error Correction
**Title:** Reed-Solomon and Concatenated Codes with Applications in Space Communication  
**Authors:** Polykarpos Thomadakis and Antonios Argyriou  
**Year:** 2016  
**Type:** arXiv preprint  
**Category:** Forward Error Correction / Reed–Solomon / Space communication  
**Link:** https://arxiv.org/abs/1608.03961


