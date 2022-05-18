---
title: Qrack
emoji: ⚡
project_url: https://github.com/vm6502q/qrack
metaDescription: High-performance quantum gate simulator framework
date: 2022-04-05
summary: High-performance quantum gate simulator framework
tags:
  - c++
  - opencl
  - python
  - simulation
bounties:
  - name: (Qrack) Coverage update
    issue_num: 612
    value: 100
  - name: (PyQrack) Unit tests: mirror circuits
    issue_num: 13
    value: 100
  - name: (PyQrack) Official PyQrack Documentation
    issue_num: 16
    value: 100
---


[Qrack](https://github.com/vm6502q/qrack) is an ideal simulator of noiseless quantum computers, designed for maximum practical performance on all consumer computer platforms, including multi-device acceleration with OpenCL. The library is open source software, under the LGPL, with 0 required linker dependencies outside of standard C and C++ libraries. Featured optimizations include Schmidt decomposition and a novel, transparent extension of stabilizer tableau simulation.

[PyQrack](https://github.com/vm6502q/pyqrack) is the official pure Python ctypes wrapper on C++ Qrack, also with 0 package dependencies. It provides a back end for Qiskit, with [qiskit-qrack-provider](https://github.com/vm6502q/qiskit-qrack-provider). Qrack also supports Q#, Cirq, XACC, and other quantum computing front ends, though we'd love if unitaryhack could help us update the plugins!

> Open Qrack GitHub issues are [here](https://github.com/vm6502q/qrack/issues).
