## Initial Parameter Set v0

The first version of the simulation uses a simplified parameter set.

### PPM-parameter
- `M = 4`
- `T_slot = 1 arbitrary unit`
- `bits_per_ppm_symbol = log2(M)`

- ### Photon-Counting Channel

- - `lambda_signal = 0.5`
- `lambda_background = 0.05`

Photon arrivals are modeled probabilistically.

### Detector parameter
eta_detector = 0.8
dark_count_rate = 0.001 per slot
timing_jitter = 0 for v0
dead_time = ignored for v0
timing_jitter and dead_time are not modeled in v0, but are reserved for later versions.

### Reed–Solomon Coding

- `rs_parity_symbols = 16`

Reed–Solomon coding is used as the main FEC method.

### Loss Model

- `p_symbol_erasure = 0.20`
- `p_burst = 0.10`
- `burst_length = 3`

The simulation includes both random symbol erasures and burst-loss events.

### Interleaving

- `interleaving_depth = 4`

Interleaving is used to spread burst losses across multiple Reed–Solomon codewords.

### Metrics

The simulation will measure:

- message recovery success rate;
- bit error rate;
- symbol erasure rate;
- packet loss rate;
- uncorrectable failure rate;
- coding overhead.
