# Cosmic CPU Tester

This document outlines the use of the Cosmic CPU Testing programss

## Contents
- [Cosmic1](#cosmic1)

## Cosmic1
This part of the document out lines the Cosmic1 testing process
Testers:
- [Tester1](#test-program-1)

### Test Program 1
Tests:
- [Initial Test](#test-0)

#### Test 0
Lines 1-5 in [`Cos1 - T1.coa`](Cos1-T1.coa)
```
LDI R1 1
LDI R2 1
CMP R1 R2
BRH Z .passT0
HLT
```
This test is intended to checks if registers 1 and 2 can be used to output for later tests.

Potential reasons for a failed test
| Debug Step                | Reason  |
| ---                       | ---     |
| Update with error and fix | Temp :) |

#### Test 1
Lines 6-11 in [`Cos1 - T1.coa`](Cos1-T1.coa)
```
.passT0 LDI R2 0
STR R0 R1 0
LOD R0 R2 0
CMP R1 R2
BRH Z .passT1
LDI R1 0
```
This test is intended to check if address 0 is read and writable

Potential reasons for a failed test
| Debug Step                               | Reason                                                          |
| ---                                      | ---                                                             |
| `LOD` Operand dose not write to reg file | Check if bits 4-7 (Reg B on datasheet) set the reg file `cAddr` |
