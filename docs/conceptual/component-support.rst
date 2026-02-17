.. meta::
  :description: ROCm component support
  :keywords: components, support, ROCm, AMD, HIP SDK, HIP

.. _component-support:

******************************************************************************
ROCm components supported in HIP SDK
******************************************************************************

The HIP SDK brings a subset of ROCm to developers on Windows. The collection of features enabled on Windows
is referred to as the HIP SDK. These features allow developers to use the HIP runtime, HIP math libraries
and HIP Primitive libraries. The following table shows the differences between Windows and Linux releases.

.. note::

   HIPBlasLT is now available for Windows users in HIP SDK version 6.4.2 and later, supported on gfx1101.


.. csv-table::
    :widths: 40, 30, 30
    :header: "Component", "Linux", "Windows"

    "Driver", "`AMD GPU driver <https://www.amd.com/en/support/download/drivers.html>`_", "AMD GPU driver"
    "Compiler", "hipcc/amdclang++", "hipcc/clang++"
    "Debugger", "`rocgdb <https://rocm.docs.amd.com/projects/ROCgdb/en/latest/>`_", ":doc:`ROCm Debugger for Windows <../how-to/debugger-windows>`"
    "Profiler", "`ROCProfiler <https://rocm.docs.amd.com/projects/rocprofiler/en/latest/>`_", "`Radeon GPU Profiler <https://gpuopen.com/rgp/>`_"
    "Porting Tools", "`HIPIFY <https://rocm.docs.amd.com/projects/HIPIFY/en/latest/>`_", "`HIPIFY <https://rocm.docs.amd.com/projects/HIPIFY/en/latest/>`_"
    "Runtime", "`HIP <https://rocm.docs.amd.com/projects/HIP/en/latest/>`_ (open sourced)", "`HIP <https://rocm.docs.amd.com/projects/HIP/en/latest/>`_ (closed source)"
    "Math Libraries", "Supported", "Supported"
    "Primitives Libraries", "Supported", "Supported"
    "Communication Libraries", "Supported", "Not available"
    "AI Libraries", "`MIOpen <https://rocm.docs.amd.com/projects/MIOpen/en/latest/>`_, `MIGraphX <https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/>`_", "Not available"
    "System Management", "`ROCm SMI <https://rocm.docs.amd.com/projects/rocm_smi_lib/en/latest/>`_, RDC, rocminfo", "hipInfo"
    "AI Frameworks", "PyTorch, TensorFlow, etc.", "Not available"
    "CMake HIP Language", "Enabled", "Unsupported"
    "Visual Studio", "Not applicable", "Plugin available"
    "HIP Ray Tracing", "Supported", "Supported"
