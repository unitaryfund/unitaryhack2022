---
title: Mitiq
emoji: 🌴
project_url: "https://github.com/unitaryfund/mitiq"
metaDescription: Making NISQ hardware less noisy with a Python-based error mitigating package.
date: 2019-01-01T00:00:00.000Z
summary: Python package for quantum error mitigation techniques
tags:
  - error-mitigation
  - noise
  - run-on-hardware
  - python
bounties:
  - name: Avoid ignoring silently bad inputs in fold_gates_at_random
    issue_num: 1179
    value: 25
  - name: Add support to the GH pages documentation pipeline for selecting different mitiq versions
    issue_num: 1168
    value: 25
  - name: Qrack extended stabilizer for CDR and other near-Clifford applications
    issue_num: 1165
    value: 50
  - name: Improve H2 example
    issue_num: 1094
    value: 100
  - name: Using a CZPowGate produces an error with CDR
    issue_num: 1062
    value: 100
---

Mitiq is a Python toolkit for implementing error mitigation techniques on quantum computers.

Current quantum computers are noisy due to interactions with the environment, imperfect gate applications, state preparation and measurement errors, etc.
Error mitigation seeks to reduce these effects at the software level by compiling quantum programs in clever ways.
You can watch some videos about Mitiq on the [Unitary Fund YouTube channel](https://www.youtube.com/watch?v=5KDQtWzJcfw&list=PL-VMs2BCTI_lklMMfY4iMdETT19rgZe5o).

> General issues we are looking for help with during [unitaryHACK](https://github.com/unitaryfund/mitiq/contribute)
