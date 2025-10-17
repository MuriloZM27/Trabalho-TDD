# TDD Timeline — Red → Green → Refactor

Este pacote contém **10 ciclos TDD** (TEST-01 a TEST-10), cada um com três snapshots:
- `red/` — teste escrito causando falha
- `green/` — implementação mínima para fazer **apenas este teste** passar
- `refactor/` — melhoria do código sem alterar comportamento

## Como rodar um snapshot
Entre numa pasta de snapshot (ex.: `TEST-03/green`) e execute:
```bash
python -m unittest -v
```
Cada snapshot traz apenas **um** teste focado naquele passo. 
