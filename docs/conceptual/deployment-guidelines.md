# Application deployment guidelines for Windows

ISVs deploying applications using the HIP SDK depend on the AMD GPU Drivers, HIP
Runtime Library and HIP SDK Libraries. A compatibility matrix table provides
details on AMD’s support model. AMD GPU Drivers are distributed with a HIP
Runtime included. Each HIP runtime is associated with a HIP compiler version.
Applications built with a particular HIP compiler should document its associated
HIP runtime version and AMD GPU Driver as minimum version requirements for its
end users. Applications do not distribute the HIP runtime. Instead, end users
will use the HIP runtime provided by an AMD GPU Driver. AMD provides backward
compatibility for applications dynamically linked to the HIP runtime based on
our Driver and HIP support policy. ISV applications using the HIP SDK Libraries,
for example hipBLAS, should distribute the HIP SDK Library as part of its
installer package. It is recommended not to require end users to install the
HIP SDK. AMD provides backward compatibility for AMD Driver and HIP runtime for
the HIP SDK Libraries based on our support policy. AMD support policy for Visual
Studio and other third-party compilers are documented here.

## Usage scenario

This guide is intended for Independent Software Vendors (ISVs) and other
software developers intending to build applications with the HIP SDK for
Windows. The HIP SDK is intended for developer distribution in contrast to the
AMD GPU driver which is intended for all end users. The guide discusses how to
use and distribute components from the HIP SDK. The HIP SDK is the collection of
the AMD GPU Driver, HIP runtime and the HIP Libraries. These three parts are
distributed in the HIP SDK installer. The compatibility and versioning relation
between these three parts is documented here. AMD’s support policies for the
developer tools allows the ISVs the stability to plan the usage of a tool chain.

## Recommended library distribution model

The HIP SDK is distributed via a Windows installer. This distribution system is
only intended for software developers and testers. AMD recommends that end users
of the program built against HIP SDK components do not have a requirement to
install the HIP SDK. There are two types of ISV applications that use the HIP
SDK as follows.

The first group of ISV applications have a dependency on the HIP runtime and
select HIP Header Only Libraries (rocPRIM, hipCUB and rocThrust). This group of
ISV applications need to require their end users install an AMD GPU Driver. Each
AMD GPU driver has a HIP runtime library bundled with it. The ISV application
should ensure that the HIP runtime library has a minimum version associated with
it. As the HIP runtime library does not have semantic versioning, the ISV
application cannot check for compatibility. However, AMD is committed to not
breaking API/ABI compatibility unless the major version number of the HIP
runtime is incremented. ISV applications may run without user warning if the HIP
major version available in the driver is the same as the HIP major version
associated with the compiler it was built with. The ISV at its discretion may
throw a warning if the HIP major version is higher than the associate HIP major
version of the compiler it was built with.

The second group of ISV application has a dependency on the HIP runtime and one
or more Dynamically Linked HIP Libraries including the HIP RT library. ISV
applications with this dependency need to ensure the end user installs an AMD
GPU Driver and is recommended to distribute the dynamically linked HIP library
in the installer package of its application. This allows end users to avoid
installing the HIP SDK. One benefit of this model is smaller disk space required
as only required binaries are distributed by the ISV application. It also avoids
the end user to have to agree to licensing agreements for the entire HIP SDK.
The version checks recommended for the ISV application including dynamically
linked HIP Libraries follow the same requirements as the ISV applications that
only have the HIP runtime and header only library. In addition, each dynamically
linked HIP library also has a minimum HIP runtime requirement. Checks for the
minimum HIP version for each dynamically linked HIP library may be added at the
ISVs discretion. Usually, the minimum HIP version check for the HIP runtime is
sufficient if dynamically linked HIP libraries come from the same SDK package as
the HIP compiler.

Please note AMD does not support static linking to any components distributed in
the HIP SDK.
