#!/usr/bin/env python3
"""Offline package sanity checks. Does not evaluate an LLM or certify behavior."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
assert skill.startswith('---\n'), 'Missing YAML frontmatter'
frontmatter = skill.split('---', 2)[1]
assert re.search(r'^name: clear-output$', frontmatter, re.M)
assert re.search(r'^description: .+', frontmatter, re.M)
assert len(skill.splitlines()) < 150, 'Keep entrypoint concise'
for target in re.findall(r'\]\((references/[^)]+)\)', skill):
    assert (ROOT / target).is_file(), f'Broken reference: {target}'
cases = json.loads((ROOT / 'tests/cases.json').read_text(encoding='utf-8'))
assert len(cases) >= 10
assert len({c['id'] for c in cases}) == len(cases)
for case in cases:
    assert set(case) == {'id', 'prompt', 'checks'}
    assert isinstance(case['prompt'], str) and case['prompt']
    assert isinstance(case['checks'], list) and all(case['checks'])
energy = 100 * 1000 * 1.2 * 8760
assert energy == 1051200000
assert round(energy * .35) == 367920000
assert round(energy * .55) == 578160000
assert round(energy * (.55 - .35)) == 210240000
print(f'PASS: package structure, reference paths, {len(cases)} case schemas, numerical oracle.')
print('NOT TESTED by this script: skill selection, generated answers, human comprehension, device compatibility.')
