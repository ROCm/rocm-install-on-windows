.. meta::
  :description: ROCm component support
  :keywords: components, support, ROCm, AMD, HIP SDK, HIP

.. _component-support:

******************************************************************************
ROCm component support
******************************************************************************

Starting with ROCm 5.5, the HIP SDK brings a subset of ROCm to developers on Windows.
The collection of features enabled on Windows is referred to as the HIP SDK.
These features allow developers to use the HIP runtime, HIP math libraries
and HIP Primitive libraries. The following table shows the differences
between Windows and Linux releases.

.. csv-table::
    :widths: 40, 30, 30
    :header: "Component", "Linux", "Windows"

    "Driver", "Radeon Software for Linux", "AMD Software Pro Edition"
    "Compiler", "hipcc/amdclang++", "hipcc/clang++"
    "Debugger", "`rocgdb <https://rocm.docs.amd.com/projects/ROCgdb/en/latest/>`_", "no debugger available"
    "Profiler", "`ROCProfiler <https://rocm.docs.amd.com/projects/rocprofiler/en/latest/rocprof.html>`_", "`Radeon GPU Profiler <https://gpuopen.com/rgp/>`_"
    "Porting Tools", "`HIPIFY <https://rocm.docs.amd.com/projects/HIPIFY/en/latest/>`_", "Coming Soon"
    "Runtime", "`HIP <https://rocm.docs.amd.com/projects/HIP/en/latest/>`_ (open sourced)", "`HIP <https://rocm.docs.amd.com/projects/HIP/en/latest/>`_ (closed source)"
    "Math Libraries", "Supported", "Supported"
    "Primitives Libraries", "Supported", "Supported"
    "Communication Libraries", "Supported", "Not available"
    "AI Libraries", "`MIOpen <https://rocm.docs.amd.com/projects/MIOpen/en/latest/>`_, `MIGraphX <https://rocm.docs.amd.com/projects/AMDMIGraphX/en/latest/>`_", "Not Available"
    "System Management", "`ROCm SMI <https://rocm.docs.amd.com/projects/rocm_smi_lib/en/latest/>`_, RDC, rocminfo", "amdsmi, hipInfo"
    "AI Frameworks", "PyTorch, TensorFlow, etc.", "Not available"
    "CMake HIP Language", "Enabled", "Unsupported"
    "Visual Studio", "Not applicable", "Plugin available"
    "HIP Ray Tracing", "Supported", "Supported"

We are continuing to invest in Windows support and plan to release enhanced features in future
revisions.

.. note::

  The 5.5 Windows Installer collectively groups the Math and Primitives libraries.
