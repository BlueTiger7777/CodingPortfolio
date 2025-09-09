# Cosmic CPU Tester

This document outlines the use of the Cosmic CPU Testing programss

## Contents
- [Cosmic1](#cosmic1)

## Cosmic1
This part of the document out lines the Cosmic1 testing process
Testers:
- [Tester1](#tester-1)

### Tester 1
Tests:
- [Initial Test](#initial-test)

#### Initial Test
This test checks if it can output to at least registers 1 and 2\
Lines 1-5 in [`Cos1 - T1.coa`](Cos1 - T1.coa)
```
LDI R1 1
LDI R2 1
CMP R1 R2
BRH Z .pass
HLT
```
