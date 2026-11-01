# Validation record

Date: 2026-11-01. Package validation, not a certification or guarantee.

## Executed checks

- Bundled skill-creator `quick_validate.py`: PASS (frontmatter and naming).
- `python3 tests/validate.py`: PASS (package structure, reference paths, 12 case schemas, numerical oracle).
- Python byte-compilation of validator: PASS.
- Independent forward test: a separate Agent loaded SKILL.md and relevant references, without reading expected-case checks. Three prompts executed; no external actions. Single execution only; not a cross-model benchmark.

| Case | Observed output | Review |
|---|---|---|
| strict-json | `{"revenue":1200,"cost":900,"profit":300}` with no narrative in the case output | PASS: values and requested strict format preserved |
| malformed-input | Declined to graph `1,2x 元` and `-?%`, requested correct amount, period and growth percentage, did not guess | PASS: damaged input not converted to invented data |
| annual-electricity | 120 MW facility load; 1,051,200,000 kWh/year; A RMB 367,920,000; B RMB 578,160,000; difference RMB 210,240,000; 36.36% relative electricity reduction | PASS: formulas, assumptions, exclusions, PUE definition and electricity-only boundary present |

The annual-electricity response explicitly stated these were hypothetical calculations, not actual operating data, excluded servers/network/capex/tax, and did not infer total investment return.

## Not established

The other nine cases are supplied for future regression testing, not claimed as executed. Host automatic activation, cross-model stability, human comprehension, actual artifact rendering and device-specific compatibility were not tested. Structural validators do not establish semantic completeness. Instruction and routing review is not a measured automatic-trigger evaluation.
