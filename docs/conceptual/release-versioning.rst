.. meta::
  :description: ROCm release versioning
  :keywords: ROCm installation, AMD, ROCm, Windows, HIP, HIP SDK, release versioning

****************************************************************************
ROCm release versioning
****************************************************************************

Windows will follow Linux version numbers, as Windows ROCm releases are based on Linux ROCm
releases. However, not all Linux ROCm releases will have a corresponding Windows ROCm release. The
following table shows all ROCm releases. Releases with both Windows and Linux are referred to as a
joint release. Releases with only Linux support are referred to as a skipped release (from a Windows
perspective).

.. csv-table::
    :widths: 40, 30, 30
    :header: "HIP components", "Install type", "Additional options"

    "5.5", "✅", "✅"
    "5.6", "✅", "❌"
    "5.7", "✅", "✅"
    "6.0", "✅", "❌"

ROCm Linux releases are versioned with following the Major.Minor.Patch version number system.
Windows releases are versioned with Major.Minor.

In general, Windows releases trail Linux releases. If you want to support both Linux and Windows using
a single ROCm version, refrain from upgrading ROCm until there is a joint release.

Windows documentation implications
=============================================================

The ROCm documentation website contains both Windows and Linux documentation. Just below each
article title, a convenient article information section states whether the page applies to Linux only,
Windows only, or both. To find the exact Windows documentation for a HIP SDK release, refer to the
ROCm documentation with the same Major.Minor version number while ignoring the patch version
(which is only relevant for Linux releases). For convenience, we will continue to include Windows
documentation in release documentation for skipped Windows releases.

Windows release notes contain only information pertinent to Windows.

Windows builds from source
=============================================================

Not all source code required to build Windows from source is available under a permissive open
source license. We only provide Windows build instructions for projects that can be built from source
on Windows using a toolchain that has closed source build prerequisites. The ROCm manifest file is not
valid for Windows. AMD does not release a manifest or tag our components in Windows. You can use
corresponding Linux tags to build on Windows.
