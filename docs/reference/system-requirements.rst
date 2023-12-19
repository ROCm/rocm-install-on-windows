.. meta::
  :description: Windows GPU and OS support
  :keywords: Windows support, ROCm distributions

******************************************************************************
GPU and OS support (Windows)
******************************************************************************

Supported SKUs
===============================================

AMD HIP SDK supports the following Windows variants.

.. csv-table::
  :widths: 40, 30, 30
  :header: "Distribution", "Processor architectures", "Validated update"

  "Windows 10", "x86-64", "22H2 (GA)"
  "Windows 11", "x86-64", "22H2 (GA)"
  "Windows Server 2022", "x86-64", "22H2 (GA)"

Windows-supported GPUs
===============================================

The tables below show supported GPUs for Radeon Pro™ and Radeon™ GPUs.
If a GPU is not listed on this table, it is not officially supported by AMD.

Radeon Pro™
~~~~~~~~~~~~~~~~~~~

.. csv-table::
  :widths: 20, 20, 20, 20, 20
  :header: "Name", "Architecture", "LLVM target", "Runtime", "HIP SDK"

  "AMD Radeon Pro™ W7900", "RDNA3", "gfx1100", "✅", "✅"
  "AMD Radeon Pro™ W7800", "RDNA3", "gfx1100", "✅", "✅"
  "AMD Radeon Pro™ W6800", "RDNA2", "gfx1030", "✅", "✅"
  "AMD Radeon Pro™ W6600", "RDNA2", "gfx1032", "✅", "❌"
  "AMD Radeon Pro™ W5500", "RDNA1", "gfx1012", "❌", "❌"
  "AMD Radeon Pro™ VII", "GCN5.1", "gfx906", "❌", "❌"

Radeon™
~~~~~~~~~~~~~~~~~~~

.. csv-table::
  :widths: 20, 20, 20, 20, 20
  :header: "Name", "Architecture", "LLVM target", "Runtime", "HIP SDK"

  "AMD Radeon™ RX 7900 XTX", "RDNA3", "gfx1100", "✅", "✅"
  "AMD Radeon™ RX 7900 XT", "RDNA3", "gfx1100", "✅", "✅"
  "AMD Radeon™ RX 7600", "RDNA3", "gfx1102", "✅", "✅"
  "AMD Radeon™ RX 6950 XT", "RDNA2", "gfx1030", "✅", "✅"
  "AMD Radeon™ RX 6900 XT", "RDNA2", "gfx1030", "✅", "✅"
  "AMD Radeon™ RX 6800 XT", "RDNA2", "gfx1030", "✅", "✅"
  "AMD Radeon™ RX 6800", "RDNA2", "gfx1030", "✅", "✅"
  "AMD Radeon™ RX 6750 XT", "RDNA2", "gfx1031", "✅", "❌"
  "AMD Radeon™ RX 6700 XT", "RDNA2", "gfx1031", "✅", "❌"
  "AMD Radeon™ RX 6700", "RDNA2", "gfx1031", "✅", "❌"
  "AMD Radeon™ RX 6650 XT", "RDNA2", "gfx1032", "✅", "❌"
  "AMD Radeon™ RX 6600 XT", "RDNA2", "gfx1032", "✅", "❌"
  "AMD Radeon™ RX 6600", "RDNA2", "gfx1032", "✅", "❌"

Component support
===============================================

ROCm components are described in `What is ROCm? <https://rocm.docs.amd.com/en/latest/what-is-rocm.html>`_ Support
on Windows is provided with two levels on enablement.

* **Runtime**: Runtime enables the use of the HIP and OpenCL runtimes only.
* **HIP SDK**: Runtime plus additional components are listed in `Libraries <https://rocm.docs.amd.com/en/latest/reference/library-index.html>`_.
 Note that some math libraries are Linux exclusive.

Support status
===============================================

✅: **Supported** - AMD enables these GPUs in our software distributions for
  the corresponding ROCm product.\
⚠️: **Deprecated** - Support will be removed in a future release.\
❌: **Unsupported** - This configuration is not enabled in our software distributions.\

CPU support
===============================================

ROCm requires CPUs that support PCIe™ atomics. Modern CPUs after the release of
1st generation AMD Zen CPU and Intel™ Haswell support PCIe atomics.