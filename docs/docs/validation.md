# Validation: Photon Flux Calculation Against PyCom (Hippke et al.)

## Purpose

This document records the validation of this project's photon-rate
calculation against `PyCom`, the open-source reference implementation
released alongside Hippke's *Interstellar Communication* paper series
(arXiv:1706.03795, MIT License, github.com/hippke/communication).

The goal was to confirm that this project's independent implementation
agrees with an established reference tool on identical inputs — not to
fit one model to the other.

## Reference case

Parameters below are this project's own (not taken from a specific
table in Hippke's papers); they were chosen to be representative of a
realistic interstellar downlink and were run through both this
project's code and PyCom for comparison.

| Parameter | Value |
|---|---|
| Distance to Alpha Centauri | 4.24 light-years ≈ 4.01×10¹⁶ m |
| Wavelength | 1550 nm |
| Transmit aperture diameter | 0.3 m |
| Laser power (transmitter) | 1×10⁹ W (1 GW) |
| Receive telescope diameter | 1.0 m |
| Beam divergence angle (theta) | 1.22 × wavelength / transmit_aperture_diameter |

## Round 1: initial comparison

Beam divergence was computed as the plane-wave diffraction limit:
theta = wavelength / transmit_aperture_diameter
| | Photon rate (photons/s) |
|---|---|
| My result | 45,445 |
| PyCom result | 30,533 |
| Discrepancy | 48.8% |

## Root cause

The transmitter aperture is circular, not a slit, so the correct
divergence angle is set by the first null of the Airy diffraction
pattern, not the plane-wave approximation:
theta = 1.22 × wavelength / transmit_aperture_diameter
The 1.22 factor comes from the first zero of the Bessel function J₁,
which for a circular aperture falls near 1.22π rather than at π as for
a slit. Since spot area on the receiver scales as θ², this factor
enters squared:

1.22² ≈ 1.4884

which matches the observed 48.8% discrepancy almost exactly, confirming
this as the source of the error.

## Round 2: Airy factor added, but a second typo remained

| | Photon rate (photons/s) |
|---|---|
| My result | 31,039.49 |
| PyCom result | 30,532.73 |
| Discrepancy | 1.66% |

This was an improvement over Round 1, but not yet exact agreement.
The cause turned out to be a second, independent typo: the divergence
formula in `photon_rate.py` used `1.21` instead of `1.22` as the Airy
coefficient — a transcription error, not a physics error, but it
still measurably shifted the result.

## Round 3: after fixing the coefficient typo

| | Photon rate (photons/s) |
|---|---|
| My result | 30532.733073028012 |
| PyCom result | 30532.733579904718 |
| Discrepancy | ~1.66×10⁻⁸ (floating-point noise) |

## Residual discrepancy

None. After correcting both the missing Airy-disk factor (Round 1→2)
and a transcription typo in that same coefficient (Round 2→3), the
discrepancy against PyCom dropped to floating-point noise, confirming
exact agreement between the two implementations on identical inputs.

## Downstream impact — to verify

The beam-divergence formula is used elsewhere in this project's
channel-model pipeline (photon-rate input to the no-FEC baseline
experiments and the realistic-λ scenario). It must be confirmed
whether the fix applied here is defined in a single shared function
(in which case downstream results already reflect it) or was
duplicated locally (in which case earlier figures and the
λ ≈ 4.5×10⁻⁵ baseline case need to be regenerated with the corrected
formula).

## Propagation: same error found in a second, independent implementation

After fixing `photon_rate.py`, a project-wide search showed that the
Airy-disk correction was not the only place affected. The headline
number used throughout this project as the "realistic interstellar"
photon budget — λ ≈ 4.5×10⁻⁵ photons/slot — was derived independently
in `notebooks/01_link_budget_basics.ipynb`, which re-implemented the
divergence formula by hand rather than importing it from
`src/channel/photon_rate.py`. That re-implementation carried the same
missing 1.22 factor.

After rewriting the notebook to call the validated `received_power()`
and `photons_per_second()` functions directly (rather than duplicating
the formula), and after correcting two unrelated stale variables left
over from an earlier toy example (`transmit_power2` and
`aperture_diameter2`, which had been silently overwritten by an
earlier demo cell), the corrected photon budget is:

**λ ≈ 3.05×10⁻⁵ photons/slot** (previously reported as 4.5×10⁻⁵).

This has been propagated to `docs/checkpoints/uncoded_memo.md` and
`src/channel/poisson_channel.py`, both of which previously cited the
old value in comments/docs only (not as a hardcoded simulation
parameter, so no experiment results required re-running).

### Why this strengthens, not weakens, the project's main finding

The correction reduces the available photon budget by a factor of
~1.49. Since the project's central result is that the channel is
unusable without forward error correction under photon starvation,
a *lower* photon budget makes that conclusion more robust, not less.
The qualitative finding — no-FEC baseline fails under realistic
interstellar photon scarcity — is unchanged; only the quantitative
margin shifted, in the direction that reinforces the original claim.

### Lesson

The formula was correct in one place and wrong in a second,
independent re-implementation of the same physics. This is a
duplication problem, not a one-off arithmetic mistake — the same
formula existed twice with no shared source of truth. The long-term
fix is architectural: exploratory notebooks should call functions from
`src/`, not re-derive them, so that a correction made once propagates
everywhere automatically.

## Conclusion

After correcting the beam divergence formula from the plane-wave
approximation to the Airy-disk result for a circular aperture, this
project's photon-rate calculation agrees with PyCom to within 1.7% on
identical inputs, validating the implementation against a published
reference tool.


