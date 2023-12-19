.. meta::
   :description: ROCm application deployment guidelines for Windows
   :keywords: HIP, Windows, deployment guidelines

******************************************************************************************
Application deployment guidelines for Windows
******************************************************************************************

The HIP SDK consists of the AMD GPU Driver, HIP runtime, and HIP Libraries. These three parts are
distributed in the HIP SDK installer. The HIP SDK is intended for developer distribution. This is in
contrast to the AMD GPU driver, which is intended for all end users.

AMD GPU drivers are distributed with the HIP runtime included. Each HIP runtime is associated with a
HIP compiler version. Applications built with a particular HIP compiler should document its associated
HIP runtime version and AMD GPU driver as minimum version requirements.

.. note::
    Applications do not distribute the HIP runtime. Instead, end users use the HIP runtime provided by
    an AMD GPU Driver.

Independent Software Vendors (ISVs) deploying applications using the HIP SDK depend on the AMD
GPU drivers, HIP runtime library and HIP SDK libraries. Our support policies for developer tools allow
Independent Software Vendors (ISVs) the stability to plan the usage of a tool chain--AMD provides
backward compatibility for applications dynamically linked to the HIP runtime.

We recommend that ISV applications using the HIP SDK libraries distribute the HIP SDK Library as part
of its installer package. This avoids requiring your end users to install the HIP SDK.

Recommended library distribution model
========================================================

The HIP SDK is distributed via a Windows installer. This distribution system is `only intended for
software developers and testers`. There are two types of ISV applications that use the HIP
SDK.

* **ISV applications with a dependency on the HIP runtime and select HIP header-only libraries
  (rocPRIM, hipCUB, and rocThrust).**

    These ISV applications require end users to install an AMD GPU driver, which has a HIP runtime library
    bundled with it. Developers should ensure that these ISV applications have a minimum HIP runtime
    library version associated with them. Because the HIP runtime library doesn't have semantic
    versioning, the ISV application can't check for compatibility.

    .. tip::
        We work to avoid breaking API/ABI compatibility unless the major version number of the HIP
        runtime is incremented.

    ISV applications can run without a warning if the driver's HIP major version is the same as that
    associated with its build compiler. You can set your ISV applications to throw a warning if the HIP
    major version is higher than that associated with its build compiler.

* **ISV applications with a dependency on the HIP runtime and one or more dynamically linked
  HIP libraries (including the HIP runtime library).**

    These ISV applications should distribute the dynamically linked HIP library in their installer package.
    This avoids having your end users manually install the HIP SDK. One benefit of this model is that less
    disk space is need, as only the required binaries are distributed in the ISV application. This method
    also avoids having your end user required to agree to the licensing agreements for the entire HIP
    SDK.

    With this approach, the version checks recommended for the ISV application (including dynamically
    linked HIP libraries) follows the same requirements as the previous category.

    Each dynamically linked HIP library also has a minimum HIP runtime requirement. You can add
    minimum HIP version checks for each dynamically linked HIP library. The minimum HIP version
    check for the HIP runtime is usually sufficient if dynamically linked HIP libraries are from the same
    SDK package as the HIP compiler.

    Note that we don't support static linking to any components distributed in the HIP SDK.
