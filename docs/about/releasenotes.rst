.. meta::
  :description: Windows GPU and OS support
  :keywords: Windows support, ROCm distributions, ROCm, AMD, HIP SDK, HIP

.. _releasenotes-win:

******************************************************************************
AMD HIP SDK for Windows 7.2 — Release Notes
******************************************************************************

This page documents the release history, new features, improvements, limitations, and known issues for the AMD HIP SDK on Windows. It is organized for developers, QA, and partner teams who need a reliable, reference-style view of what changed across releases.

What’s new
==========
1. Support for ROCm 7.2 

2. Support for AMD Ryzen™ AI 300 Series, AMD Ryzen™ AI 400 Series, and AMD Ryzen™ AI Max 400 Series and AMD Ryzen™ AI Max+ 400 Series.

Fixed issues
============

* Various performance improvements to ROCm Debugger (ROCgdb) on Windows

* Improved stability with various math libraries.

Limitations
===========

The following items reflect the current state of HIP SDK for Windows and the ROCm Debugger (ROCgdb) as documented in internal notes and public guidance. Where applicable, workarounds are provided.

**ROCm Debugger (ROCgdb) on Windows Limitations**

* **Architecture support**: Windows is currently supported on the AMD Radeon™ RX 9000 series graphics products. Other architectures are not supported with AMD ROCm Debugger for Windows.
* **Multi-GPU**: Configurations with more than one AMD GPU are not supported with AMD ROCm Debugger for Windows.
* **Core dumps**: Generating or loading AMD GPU core dumps is not supported on Windows.
* **Python scripting**: Not supported.
* **Signals**: Due to a HIP runtime limitation, intercepted signals (SIGFPE, SIGSEGV, etc.) cannot currently be passed through to the inferior on Windows; signals are always suppressed by the runtime.
* **Host debug info**: HIPCC on Windows defaults to PDB/CodeView for host debug info, which ROCgdb does not support. Workaround: compile with -gdwarf -Wl,-debug:dwarf to emit DWARF host debug info supported by ROCgdb.
* **ABI compatibility**: HIPCC emits host code targeting Microsoft x64 ABI and MSVC C++ ABI. ROCgdb does not fully support these, which may cause incorrect symbol names or misprinted C++ objects during host debugging. Device-side GPU debugging is not affected.

Known issues
============

* Intermittent soft hang may be observed in rocPRIM rocprim.device_adjacent_find.
* rocSPARSE may experience hipMemcpy errors & test abort in some cases.
* Applications using the HIP 6 runtime (amdhip64_6.dll) show ~20% lower performance on Strix Halo with Adrenalin 26.10-branch drivers (26.6.2, 26.6.4). Applications on the HIP 7 runtime (amdhip64_7.dll) are unaffected.


Quick links
============

* `AMD HIP SDK for Windows Download <https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html#downloads>`_
* `HIP SDK for Windows — HIP SDK for Windows 7.2 documentation <https://rocm.docs.amd.com/projects/install-on-windows/en/latest/index.html#supported-operating-systems-and-hardware>`_
* For the latest list of supported operating systems and GPUs, see `System requirements (Windows) <https://rocm.docs.amd.com/projects/install-on-windows/en/latest/reference/system-requirements.html>`_
* `HIP Debugger <https://amd.atlassian.net/wiki/spaces/SWPMTO/pages/1809761685?xpis=eyJicmlkZ2UiOiJzbWFydExpbmtzIiwiaWQiOiIxNzg1NDM4ODYxODAxIiwic291cmNlIjoiY29uZmx1ZW5jZSJ9>`_
