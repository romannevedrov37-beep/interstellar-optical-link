# Архитектура проекта

Поток данных: message → framing → fec → modem → channel → detector → modem (demod) → fec (decode) → framing → message

| Папка | Назначение |
|---|---|
| src/framing/ | сообщение → bytes, заголовок, checksum |
| src/fec/ | Reed-Solomon + interleaving |
| src/modem/ | PPM encode/decode |
| src/channel/ | Poisson photon loss, erasures, burst-loss |
| src/detector/ | SNSPD: efficiency, dark counts, jitter |
| src/metrics/ | BER, SER, PER, recovery success |
| src/experiments/ | Monte Carlo, parameter sweeps |