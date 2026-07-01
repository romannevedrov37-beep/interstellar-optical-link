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
The modulator drives an electric current as follows: the computer outputs data, for example the combination `0010`, using the logic of the pulse-position modulation (PPM) method. 
The electric current excites the active medium inside the laser, and when the particles in this medium transition to a lower energy state, they can emit photons. 
The laser’s design causes these photons to be formed in the same optical mode, meaning that they have nearly identical frequency, phase coherence, and direction within the parameters of the laser beam.
The technology is designed to select and amplify the desired order of photons through a process known as stimulated emission.
According to quantum mechanics, when a photon passes near an excited particle in the active medium, it can cause that particle to transition to a lower energy state and emit another photon.
As a result, the photons have nearly identical frequency, phase coherence, and direction within the parameters of the laser beam.
The key process is avalanche-like amplification due to stimulated emission — a process in which one photon can lead to the generation of additional photons in the same optical mode within a very short time. 
The time it takes for this photon amplification to build up is extremely small. For us, it appears almost instantaneous, in some regimes on the scale of picoseconds — trillionths of a second. 
Therefore, as soon as the modulator sends a current pulse, the laser pulse has already formed and left the transmitter as a compact coherent packet.

At the transmitter output, to prevent the extremely narrow photon beam from diverging too quickly, it must be made wider and more collimated. 
After generation, the laser beam passes through a beam expander or a telescopic optical system. 
The entire laser design is arranged so that photons emitted spontaneously and not coupled into the main optical mode are mostly lost, scattered, or do not contribute to the useful directed beam. 
Furthermore, the mirrors and optical elements are specifically designed for this process, so they have minimal losses at the desired wavelength. 
When the photons exit the transmitting optics, they can be described both as a stream of photons and as a coherent electromagnetic field. 
At this stage, we have a powerful directed laser pulse, in which the photons propagate almost parallel to one another and remain phase-coherent within the parameters of the beam. 
This pulse carries information through its timing structure.

Let’s move on to the stage of flight through distances on the order of `10^16` meters. Due to diffraction, the beam does not remain perfectly parallel. 
As it travels, the beam slowly expands into a cone, causing the photons to spread over an increasingly large area, thereby reducing the flux density.

As it approaches Earth, instead of a compact beam, we have a gigantic invisible beam spot covering a large region of space. 
When an Earth-based telescope intercepts only a microscopic fraction of this beam, rare, isolated, individual photons strike the telescope’s mirror.

## 1.2 Beam Propagation and Diffraction
The propagation of a laser beam over interstellar distances is inevitably subject to the laws of diffraction, which leads to significant beam broadening and a dramatic drop in the signal’s power density. Even when using a coherent laser source and a high-quality optical system, it is impossible to obtain a perfectly parallel beam, since the finite size of the aperture causes the formation of a diffraction pattern. For a circular aperture, the divergence of the central maximum is typically estimated using the Rayleigh diffraction limit, which relates the divergence angle to the wavelength of the radiation and the diameter of the transmitting optics. Consequently, increasing the aperture and decreasing the wavelength allow for a reduction in divergence and an increase in power density at the receiver. However, at interstellar distances, even small divergence angles result in the formation of an astronomically large light spot, whose radius in the far field is determined by the geometric ratio between the divergence angle and the distance to the receiver. As a result, the energy is distributed over a large area, and the received power is determined by the ratio of the receiving aperture area to the area of the illuminated spot. This requires the use of large telescopes, precise pointing, sensitive photodetectors, narrowband filtering, and error correction methods. 
Additional factors include the motion of stars and spacecraft, signal propagation delay, background radiation, as well as absorption and scattering by interstellar dust and gas. When a communication node is located on the surface of a planet, atmospheric turbulence, cloud cover, and wavefront distortions play a significant role.
Diffraction is a fundamental limitation of interstellar optical communication, determining the minimum beam divergence, the size of the light spot, and the energy balance of the channel.

## 1.3 Photon-Starved Receiver
In a situation where a ground-based telescope captures only a very small fraction of the transmitted photon flux, the receiver operates based on rare photon detections within discrete time intervals. Some intervals may contain signal photons, others may contain only background photons, and in still others, no photons may be detected at all.
The receiver’s task is to estimate in which time interval the transmitted PPM pulse was most likely present. This is challenging because several factors influence the number of detected photons:
the low frequency of signal photons;
background photons;
detector efficiency;
dark counts;
synchronization fluctuations;
randomness in photon counting;
possible missing symbols or packets.
Since the arrival of photons is random, the receiver cannot assume that the correct interval will always contain a large number of photons. Instead, the receiver must make a probabilistic decision based on the number of photons detected in each interval.
For example, in a PPM frame, the receiver can compare the number of photons in all slots and select the slot that provides the strongest evidence of the presence of the transmitted pulse. If the evidence is too weak or ambiguous, the receiver may mark the symbol as deleted rather than make a potentially erroneous decision.
This is important because missing symbols are often easier for error-correcting codes, such as Reed–Solomon, to handle than errors involving unknown symbols.

## 2. Detector Model
The detector model describes how the receiver converts incoming photons into measured photon-count events.
In this project, the detector is modeled as an SNSPD-like photon-counting receiver. SNSPD stands for Superconducting Nanowire Single-Photon Detector. A real SNSPD is a highly sensitive detector capable of registering individual photons, but this project does not model the full hardware physics of the device. Instead, it uses a simplified detector abstraction with the parameters most relevant for communication reliability.
The detector model answers the question:
If photons arrive at the receiving telescope, how many of them are actually detected, and how reliable are those detections?
The main parameters of the detector model are:
detector efficiency — the probability that an incoming photon is actually registered;
dark counts — false detection events that occur even when no signal photon arrives;
background counts — photons from external sources such as stars, sky background, or other optical noise;
timing jitter — uncertainty in the measured arrival time of a photon;
maximum count rate — the approximate limit on how many photon events the detector can register in a given time interval.
In the simulation, the detector receives photon-count events from the photon-starved channel and produces observed counts for each PPM time slot. These observed counts are not always equal to the true transmitted signal because photons may be missed, false counts may be added, and photon arrival times may be shifted by timing jitter


The detector output can be used by the receiver to decide which PPM slot most likely contained the transmitted pulse. If one slot has clearly stronger photon evidence than the others, the receiver can choose that slot as the decoded symbol. If the evidence is weak or ambiguous, the receiver may mark the symbol as an erasure instead of forcing a possibly incorrect decision.

## 3. Forward Error Correction

## 4. Erasures and Burst Loss

## 5. Interleaving

## Note

These concept notes are currently draft explanations generated with the assistance of AI.  
They will be verified and expanded using scientific papers, technical reports, and official documentation.

## Source Notes

