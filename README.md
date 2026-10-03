# Capability Composition Using Vector Embeddings

## Overview

This project implements a simple capability composition system for an online
shopping application.

The main idea is to represent application states, goals, and capabilities
using numerical vectors. These representations are then used to compare
capabilities, check whether capabilities can be connected, and compose several
capabilities into a larger workflow.

The implementation is written in Python.

## Project Objectives

The project demonstrates:

- Representation of application states and goals
- Vector representation of capabilities
- Cosine similarity between capability vectors
- Compatibility checking between capabilities
- Comparison of alternative implementations
- Composition of multiple compatible capabilities
- Calculation of cost, reliability, and availability
- Verification that a composed capability achieves the required goal

## Application Example

The example application represents a simple online shopping workflow.

The main capabilities are:

- `CreateOrder`
- `MakePayment`
- `SendNotification`
- `CancelCart`
- `SendEmailConfirmation`

A successful purchase workflow is represented as:

```text
CreateOrder
     |
     v
MakePayment
     |
     v
SendNotification
