<head>
  <meta charset="UTF-8">
  <meta name="description" content="What's new in ROCm">
  <meta name="keywords" content="what's new">
</head>

# ROCm component support

Starting with ROCm 5.5, the HIP SDK brings a subset of ROCm to developers on Windows.
The collection of features enabled on Windows is referred to as the HIP SDK.
These features allow developers to use the HIP runtime, HIP math libraries
and HIP Primitive libraries. The following table shows the differences
between Windows and Linux releases.

|Component|Linux|Windows|
|---------|-----|-------|
|Driver|Radeon Software for Linux |AMD Software Pro Edition|
|Compiler|`hipcc`/`amdclang++`|`hipcc`/`clang++`|
|Debugger|`rocgdb`|no debugger available|
|Profiler|`rocprof`|[Radeon GPU Profiler](https://gpuopen.com/rgp/)|
|Porting Tools|HIPIFY|Coming Soon|
|Runtime|HIP (Open Sourced)|HIP (closed source)|
|Math Libraries|Supported|Supported|
|Primitives Libraries|Supported|Supported|
|Communication Libraries|Supported|Not Available|
|AI Libraries|MIOpen, MIGraphX|Not Available|
|System Management|`rocm-smi-lib`, RDC, `rocminfo`|`amdsmi`, `hipInfo`|
|AI Frameworks|PyTorch, TensorFlow, etc.|Not Available|
|CMake HIP Language|Enabled|Unsupported|
|Visual Studio| Not applicable| Plugin Available|
|HIP Ray Tracing| Supported|Supported|

AMD is continuing to invest in Windows support and AMD plans to release enhanced
features in subsequent revisions.

```{note}
The 5.5 Windows Installer collectively groups the Math and Primitives
libraries.
```
