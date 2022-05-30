---
title: Orquestra Core
emoji: 🎶
project_url: "https://github.com/zapatacomputing/orquestra-core"
metaDescription: Set of libraries for quantum computing developed at Zapata Computing.
date: 2022-04-27
summary: Set of libraries for quantum computing developed at Zapata Computing.
tags:
  - python
  - VQA
  - quantum-computing
  - algorithms
---

[Orquestra Core] is a collection of open-source libraries developed at [Zapata Computing](https://www.zapatacomputing.com/). It currently consists of the following packages:

- [orquestra-core](https://github.com/zapatacomputing/orquestra-core) – a "meta-package" which contains code examples and provides an easy installation option.
- [orquestra-quantum](https://github.com/zapatacomputing/orquestra-quantum) – all the general quantum computing capabilities: data structures, circuits, interfaces for quantum backends, etc.
- [orquestra-opt](https://github.com/zapatacomputing/orquestra-opt) – data structures and interfaces for optimizers, cost functions, etc.
- [orquestra-vqa](https://github.com/zapatacomputing/orquestra-vqa) – algorithms and tools for running variational quantum algorithms such as VQE or QAOA.
- [orquestra-qiskit](https://github.com/zapatacomputing/orquestra-qiskit) – integration with Qiskit and IBM backends.
- [orquestra-cirq](https://github.com/zapatacomputing/orquestra-cirq) – integration with CirQ.
- [orquestra-forest](https://github.com/zapatacomputing/orquestra-forest) – integration with Forest platform: PyQuil and QVM simulator.


For the ease of browsing, we added all the issues to the [orquestra-core](https://github.com/zapatacomputing/orquestra-core) repository, even if the changes should be actually made in other repositories – please see the description of the issues for more details.

Unfortunately, we're still working on the documentation. For now you can either refer to the [integration tests](https://github.com/zapatacomputing/orquestra-core/tree/main/tests) or the source code of the particular package.