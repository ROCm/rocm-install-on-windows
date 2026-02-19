.. meta::
  :description: Windows GPU and OS support
  :keywords: Windows support, ROCm distributions, ROCm, AMD, HIP SDK, HIP

.. _releasenotes-win:

******************************************************************************
AMD HIP SDK for Windows 7.1.1 — Release Notes
******************************************************************************

This page documents the release history, new features, improvements, limitations, and known issues for the AMD HIP SDK on Windows. It is organized for developers, QA, and partner teams who need a reliable, reference-style view of what changed across releases.

What’s new
==========
1. Support for ROCm 7.1.1 

2. Introduction of the AMD ROCm Debugger on Windows

HIP SDK changes
===============

As of ROCm version 7.1.1, the HIP SDK for Windows includes updated versions of
the runtime components ``amdhip64`` and ``amd_comgr``. To use the latest
capabilities of the HIP SDK, reference the new versions of these DLL binaries:

* ``amdhip64_7.dll`` (formerly ``amdhip64.dll``)

* ``amd_comgr_3.dll`` (formerly ``amd_comgr.dll``)

The latest version of HIP Ray Tracing (RT) (version 3.0.21d4f81) is named hiprt0300064.dll as of ROCm version 7.1.1.

.. important::

   The HIP SDK on Windows for ROCm 7.x is not backwards compatible with previous versions.

Fixed issues
============

* Intermittent compilation errors while running cooperative_groups examples due to ds_gws_barrier on AMD Radeon™ RX 9060 and RX 9070 series products.
* Manual build failures for various math libraries are fixed.

Limitations
===========

The following items reflect the current state of HIP SDK for Windows and the ROCm Debugger (ROCgdb) as documented in internal notes and public guidance. Where applicable, workarounds are provided.

**Limitations of ROCm Debugger (ROCgdb) on Windows**

* **Architecture support**: Windows is currently supported on the AMD Radeon™ RX 9000 series graphics products. Other architectures are not supported with AMD ROCm Debugger for Windows.
* **Multi-GPU**: Configurations with more than one AMD GPU are not supported with AMD ROCm Debugger for Windows.
* **Core dumps**: Generating or loading AMD GPU core dumps is not supported on Windows.
* **Python scripting**: Not supported.
* **Signals**: Due to a HIP runtime limitation, intercepted signals (SIGFPE, SIGSEGV, etc.) cannot currently be passed through to the inferior on Windows; signals are always suppressed by the runtime.
* **Host debug info**: HIPCC on Windows defaults to PDB/CodeView for host debug info, which ROCgdb does not support. Workaround: compile with -gdwarf -Wl,-debug:dwarf to emit DWARF host debug info supported by ROCgdb.
* **ABI compatibility**: HIPCC emits host code targeting Microsoft x64 ABI and MSVC C++ ABI. ROCgdb does not fully support these, which may cause incorrect symbol names or misprinted C++ objects during host debugging. Device-side GPU debugging is not affected..

Known issues
============

* Intermittent application crash may be observed while running long-duration rocFFT workloads on AMD Ryzen AI Max series processors and AMD Radeon RX 7600 series graphics products.
* Intermittent system or application crash may be observed while running long-duration rocFFT or rocSPARSE workloads on AMD Ryzen™ AI Max 380, 390, and AMD Radeon™ RX 7000 series products.
* Intermittent script failure may be observed while using hipify-clang with the VS2019 MSVC toolchain.
* Intermittent failure may be observed while executing HIP memory API calls on AMD Radeon™ RX 9070 series products.
* TDR (Timeout Detection and Recovery) may be observed while running Orochi tests on AMD Radeon™ RX 7000 series products with multi-GPU configurations.
* Intermittent TDR (Timeout Detection and Recovery) may be observed while debugging with AMD ROCm Debugger for Windows, which may result in a system crash with error code 0x116.
