****************************************************************************
ROCm release versioning
****************************************************************************

Windows will follow Linux version numbers as Windows releases are based on Linux ROCm
releases. However, not all Linux ROCm releases will have a corresponding Windows
release. The following table shows the ROCm releases on Windows and Linux. Releases
with both Windows and Linux are referred to as a joint release. Releases with
only Linux support are referred to as a skipped release from the Windows
perspective.

.. csv-table::
    :widths: 40, 30, 30
    :header: "HIP components", "Install type", "Additional options"

    "5.5", "✅", "✅"
    "5.6", "✅", "❌"

ROCm Linux releases are versioned with following the Major.Minor.Patch
version number system. Windows releases will only be versioned with Major.Minor.

In general, Windows releases will trail Linux releases. Software developers that
wish to support both Linux and Windows using a single ROCm version should
refrain from upgrading ROCm unless there is a joint release.

Windows documentation implications
=============================================================

The ROCm documentation website contains both Windows and Linux documentation.
Just below each article title, a convenient article information section states
whether the page applies to Linux only, Windows only or both OSes. To find the
exact Windows documentation for a release of the HIP SDK, please view the ROCm documentation
with the same
Major.Minor version number while ignoring the Patch version. The Patch version
only matters for Linux releases.  For convenience,
Windows documentation will continue to be included in the overall ROCm
documentation for the skipped Windows releases.

Windows release notes will contain only information pertinent to Windows.
The software developer must read all the previous ROCm release notes (including)
skipped ROCm versions on Windows for information on all the changes present in
the Windows release.

Windows builds from source
=============================================================

Not all source code required to build Windows from source is available under a
permissive open source license. Build instructions on Windows is only provided
for projects that can be built from source on Windows using a toolchain that
has closed source build prerequisites. The ROCm manifest file is not valid for
Windows. AMD does not release a manifest or tag our components in Windows.
Users may use corresponding Linux tags to build on Windows.
