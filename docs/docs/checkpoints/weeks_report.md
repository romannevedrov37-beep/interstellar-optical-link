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