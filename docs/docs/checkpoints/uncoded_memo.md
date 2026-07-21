# Uncoded Pipeline Memo (15.07–18.07)

## What Works

- Full end-to-end round-trip pipeline is implemented and verified:
  payload → bits → PPM encoding → Poisson photon channel → SNSPD detector
  (efficiency, dark counts, timing jitter) → PPM decoding → bits → payload.
  Confirmed exact match on `b"Hi"` at high signal strength (lambda_signal=50).

- Metrics module (`src/metrics/metrics.py`) implements and validates:
  bit_error_rate (BER), symbol_error_rate (SER), recovery_success.
  All three tested against hand-calculated examples before use.

- First systematic experiment completed: `run_sweep.py` sweeps lambda_signal
  from 0.05 to 50.0, results saved to `results/uncoded_baseline.csv`,
  visualized in `figures/uncoded_baseline_ber_ser.png` and
  `figures/uncoded_baseline_success.png`.

## Key Finding

Clear threshold behavior between lambda_signal=5 and lambda_signal=10:
below the threshold, error rates rise sharply (SER=95% at lambda_signal=0.05,
close to realistic interstellar photon counts); above it, recovery is
essentially perfect (BER=SER=0, success=True).

At the realistic Alpha Centauri benchmark scale (lambda ~ 4.5e-5, from the
05.07 link budget), the uncoded pipeline would fail almost completely.
This confirms the core premise of the project: FEC is not optional for a
photon-starved channel, it is required for any usable link.

## Bottlenecks / Known Limitations

- No forward error correction exists yet — every symbol error is currently
  unrecoverable. This is expected at this stage but means current results
  are a pure baseline, not a usable communication scheme.
- Timing jitter (`apply_jitter`) uses a simplified probability proxy rather
  than being derived from the actual `jitter_ps` parameter — acceptable per
  project scope, but worth noting as a simplification.
- `max_count_rate` (detector dead-time) is still an unused, reserved
  parameter — not yet modeled.
- No framing/packet structure exists yet (no header, no checksum) — the
  pipeline currently operates on raw bit streams without packet boundaries.

## Decisions for Next Phase

- Proceed to Phase 3A (Framing, starting 20.07) to establish packet
  structure before introducing erasure and burst-loss models.
- Reed-Solomon coding (end of July, Phase 3B) is the priority fix for the
  uncoded pipeline's failure at realistic photon counts — this baseline
  sweep will serve as the direct comparison point for RS-only and
  RS+interleaving results later in the project.