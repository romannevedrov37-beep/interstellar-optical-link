# Week 1 Report (28.06 – 12.07)

## Completed
- Project setup: repo structure, venv, requirements.txt, git workflow
- docs: project_scope.md, model_assumptions.md, architecture.md
- Link budget notebook: free-space spreading, aperture gain, diffraction-limited spot
- Alpha Centauri benchmark: distance calculation, realistic photon rate estimate
- src/common: physical constants, unit conversion utils
- src/channel: photon_rate.py, channel_config.py (PPM slot model), poisson_channel.py
- src/detector: snspd_model.py (efficiency + dark counts)
- Statistical validation: sample mean/variance vs theoretical Poisson (notebooks/02_poisson_validation.ipynb)

## Known issues / bugs fixed along the way
- Floating point comparison in test_constants.py (fixed with tolerance-based assert)
- Variable scope confusion in Jupyter notebooks (fixed by Restart + Run All discipline)
- Physically impossible link budget result (93 MW > transmitted power) — fixed with if/else cap logic

## Open questions for next week
- What realistic transmit aperture / laser power values should the benchmark actually use?
- How should timing jitter (jitter_ps) be modeled once implemented (16.07)?
- Need to decide dead-time modeling approach for max_count_rate (reserved, not yet used)

## Status
On track, minor delays recovered. Moving into Phase 2 (PPM encoder/decoder) next.

# Week 4 Report (20.07 – 26.07)

## Completed
- frame format - SYNC, LENGTH, PAYLOAD, CHECKSUM with build/parse round-trip
- iid Bernoulli erasure mask generator
- contiguous burst-loss mask generator
- reliability-based erasure classification via margin threshold
- no-FEC baseline under direct iid erasures
- no-FEC baseline under burst loss vs iid comparison
## Key findings
- On the no-FEC baseline, SER for iid and burst erasures is nearly identical at matched loss_rate. The SER metric counts how many symbols were lost, not where — so equal loss counts produce equal SER regardless of pattern. Small differences observed between curves (typically 1–2 symbols out of 64) are single-trial noise from a fixed seed, not a real effect.
- Without FEC, SER tracks loss_rate almost 1:1 — every lost symbol stays lost, so the output error rate mirrors the input loss rate directly.
- Full-frame recovery probability without FEC follows P(success) = (1−p)^N. At N=64 and p=0.15, this is ≈3×10⁻⁵ — roughly 1 in 33,000 frames arrives intact. This is the quantitative case for why FEC is not optional at realistic loss rates.
- Toy analysis (64 symbols split into 8 packets of 8, all-or-nothing survival): burst loss concentrates damage into 1–2 packets and leaves the rest untouched, while iid loss spreads the same number of losses across most packets, destroying more of them. This reverses once error correction has a tolerance above zero (RS decoding with n−k redundancy survives up to n−k erasures per block) — concentrated bursts can exceed that tolerance in one block while the same losses spread thin across many blocks may not exceed it anywhere. Burst becomes more dangerous than iid exactly where a recovery margin exists.
## Open issues
- Single trial per data point (fixed seed=42), no averaging — sweep results should not be read as smooth curves yet; point-to-point noise is 1–2 symbols out of 64.
- Small symbol count (N=64) makes discretization coarse: SER can only take values in increments of 1/64.
- No RS/interleaving yet — current baseline has zero error tolerance, so any single loss corrupts its symbol with no recovery path.
## Questions for the FEC week
- What redundancy (n−k) gives an acceptable overhead vs recovery trade-off at realistic loss rates (15–20%)?
- How does interleaving depth affect burst tolerance once burst lengths exceed a single RS block?
- At what point does burst loss become worse than iid loss under RS — is there a clean threshold in terms of burst length vs block size?
- Should erasure-aware decoding (known positions) be validated separately from unknown-error correction before combining them?
## Status
Two weeks behind original schedule after travel (Munich–Copenhagen, 27.07–04.08). Recovery plan: compress remaining Phase 3B/4 sweeps, split final deadline into code (31.08) and writeup (15.09).
