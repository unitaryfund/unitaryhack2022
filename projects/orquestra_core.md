---
title: Orquestra Core
emoji: 🎶
project_url: "https://github.com/zapatacomputing/orquestra-core"
metaDescription: Set of libraries for quantum computing developed at Zapata Computing.
date: 2022-05-31
summary: Set of libraries for quantum computing developed at Zapata Computing.
tags:
  - python
  - VQA
  - quantum-computing
bounties:
  - name: Update VQE integration test to converge on the correct value
    issue_num: 9
    value: 120
  - name: Add inverse() function to Circuit
    issue_num: 10
    value: 35
  - name: `test_variance_of_added_perturbations_is_correct` in orquestra-vqa is non-deterministic
    issue_num: 11
    value: 30
  - name: Speed up export of qiskit circuits 
    issue_num: 12
    value: 110
  - name: Create `subdistribution()` function for `MeasurementOutcomeDistribution`
    issue_num: 13
    value: 30
  - name: Implement `power` wrapper for Gates
    issue_num: 14
    value: 35
  - name: Create `exponential` wrapper class
    issue_num: 15
    value: 35
---

[Orquestra Core] is a collection of open-source libraries developed at [Zapata Computing](https://www.zapatacomputing.com/). It currently consists of the following packages:

- [orquestra-core](https://github.com/zapatacomputing/orquestra-core) – a "meta-package" which contains code examples and provides an easy installation option.
- [orquestra-quantum](https://github.com/zapatacomputing/orquestra-quantum) – all the general quantum computing capabilities: data structures, circuits, interfaces for quantum backends, etc.
- [orquestra-opt](https://github.com/zapatacomputing/orquestra-opt) – data structures and interfaces for optimizers, cost functions, etc.
- [orquestra-vqa](https://github.com/zapatacomputing/orquestra-vqa) – algorithms and tools for running variational quantum algorithms such as VQE or QAOA.
- [orquestra-qiskit](https://github.com/zapatacomputing/orquestra-qiskit) – integration with Qiskit and IBM backends.
- [orquestra-cirq](https://github.com/zapatacomputing/orquestra-cirq) – integration with CirQ.
- [orquestra-forest](https://github.com/zapatacomputing/orquestra-forest) – integration with Forest platform: PyQuil and QVM simulator.
- [orquestra-qulacs](https://github.com/zapatacomputing/orquestra-qulacs) – integration with Qulacs simulator.

For the ease of browsing, we added all the issues to the [orquestra-core](https://github.com/zapatacomputing/orquestra-core) repository, even if the changes should be actually made in other repositories – please see the description of the issues for more details.

For the good introduction to the libraries, please refer to [the documentation](https://zapatacomputing.github.io/orquestra-core).