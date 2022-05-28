---
title: PyQIR
emoji: 🐲
project_url: https://github.com/qir-alliance/pyqir
metaDescription: Python and Rust QIR APIs
date: 2022-05-27
summary: PyQIR is a set of APIs for generating, parsing, and evaluating Quantum Intermediate Representation (QIR)
tags:
  - QIR
  - rust
  - python
bounties:
  - name: Upgrade samples to ANTLR 4.10
    issue_num: 102
    value: TBD
  - name: pyqir-evaluator should gracefully fail when bitcode contains unknown external functions
    issue_num: 122
    value: TBD
  - name: Migrate to Rust 2021 Edition
    issue_num: 123
    value: TBD
---

PyQIR is a set of APIs for generating, parsing, and evaluating [Quantum
Intermediate Representation (QIR)](https://github.com/qir-alliance/qir-spec). It
consists of the following components:

- [**pyqir-generator**](https://github.com/qir-alliance/pyqir/tree/main/pyqir-generator)
  [[examples](https://github.com/qir-alliance/pyqir/tree/main/examples/generator)]:
  <br/>
  Provides a Python API for generating QIR
  ([bitcode](https://www.llvm.org/docs/BitCodeFormat.html) and
  [IR](https://llvm.org/docs/LangRef.html)). It is intended to easily integrate
  the QIR toolchain into existing Python-based frontends.

- [**pyqir-evaluator**](https://github.com/qir-alliance/pyqir/tree/main/pyqir-evaluator)
  [[examples](https://github.com/qir-alliance/pyqir/tree/main/examples/evaluator)]:
  <br/>
  Provides an easy way to execute generated QIR. It contains the
  necessary [just-in-time
  compilation](https://en.wikipedia.org/wiki/Just-in-time_compilation)
  infrastructure as well an extensibility mechanism to define what actions to
  perform when a gate is applied in Python.

- [**pyqir-parser**](https://github.com/qir-alliance/pyqir/tree/main/pyqir-parser):
  <br/>
  Provides a Python API for loading QIR for basic analysis and
  transformation.

- [qirlib](https://github.com/qir-alliance/pyqir/tree/main/qirlib) - a Rust library
wrapping [LLVM](https://llvm.org/) libraries for working with QIR that is used
by the above Python packages.

> Open PyQIR GitHub issues are [here](https://github.com/qir-alliance/pyqir/issues).
