# Model Assumptions — Alpha Centauri Benchmark

## Benchmark Scenario

Calculation based on a simplified free-space link budget model with
diffraction-limited spot size (see notebooks/01_link_budget_basics.ipynb).

| Parameter | Value |
|---|---|
| Distance to Alpha Centauri | 4.24 light-years ≈ 4.01×10¹⁶ m |
| Wavelength | 1550 nm |
| Transmit aperture diameter | 0.3 m |
| Laser power (transmitter) | 1×10⁹ W (1 GW) |
| Receive telescope diameter | 1.0 m |
| Beam divergence angle (theta) | wavelength / transmit_aperture_diameter |
| Received power | ≈5.82×10⁻¹⁵ W |
| Photons per second | ≈45,414 |
| Slot duration | 1 ns (1×10⁻⁹ s) |
| Photons per slot | ≈4.54×10⁻⁵ |

## Key Finding

Under a realistic, favorable scenario (1 GW laser, meter-scale apertures on
both ends), the receiver captures on average **less than one ten-thousandth
of a photon per time slot**. This confirms the project's core premise: the
channel is genuinely photon-starved, requiring specialized recovery methods
(erasure-aware FEC, interleaving) rather than relying on a steady photon
stream.

## Uncertain Assumptions

- **Transmit aperture diameter (0.3 m)** — arbitrary placeholder value.
  Real proposals such as Breakthrough Starshot discuss laser arrays on the
  scale of hundreds of meters to kilometers, which would drastically change
  the result (aperture affects beam divergence, and thus spot area,
  quadratically).
- **Laser power (1 GW)** — optimistic estimate in line with figures
  discussed in the literature; real engineering and energy constraints are
  not modeled.
- **Atmospheric losses not modeled** — the model assumes free-space
  propagation with no atmosphere (physically correct for deep space, but
  ignores losses if the transmitter or receiver is ground-based).
- **Pointing errors not modeled** — the model assumes perfect beam
  alignment with the receiver.
- **Background photons not included in this calculation** — only the
  signal component is estimated here; a full noise model will be added in
  Phase 1 (Poisson noise model, 09.07).

## Why This Matters

Changing even a single parameter (e.g., increasing the transmit aperture
diameter by 10x) can drastically change the resulting photons-per-slot
count, because beam divergence — and therefore the spot size at the
receiver — depends on aperture size nonlinearly. This highlights why the
project explicitly documents and revisits its assumptions rather than
treating any single benchmark as final.