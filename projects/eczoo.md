---
title: Error Correction Zoo
emoji: 🐒
project_url: "https://github.com/errorcorrectionzoo/eczoo_generator"
metaDescription: Collecting and organizing classical and quantum error-correcting codes
date: 2019-01-01T00:00:00.000Z
summary: Collecting and organizing classical and quantum error-correcting codes
tags:
  - error-correction
  - website
  - javascript
bounties:
  - name: A true, better code graph
    issue_num: 5
    value: 200
---

# The Error Correction Zoo collects and organizes error-correcting codes.

Error correction is what ensures that the audio in your phone calls remains sharp, your hard drives
do not deteriorate too quickly, and signals can be reliably transmitted to remote satellites.

We created the Error Correction Zoo to categorize and to organize known classical and quantum
error-correction schemes. It is inspired by other similar zoos, including the complexity zoo
and the quantum algorithm zoo.

We strongly believe that the data should be stored in structured form, with specific meta-information
that make it possible to systematically explore the collection of error-correcting codes and generate
lists of codes that have a given property, a code graph that displays relations between codes, etc.
All the information about the error-correction codes that are in the zoo are stored as YaML data files
on [github.com](https://github.com/errorcorrectionzoo/eczoo_data/), and we have some simple code to
[build the site](https://github.com/errorcorrectionzoo/eczoo_generator/).
