.. meta::
  :description: HIP SDK for Windows
  :keywords: ROCm installation, AMD, ROCm, Windows, HIP, HIP SDK, changelog

********************************
HIP SDK for Windows
********************************

HIP SDK for Windows provides a subset of the ROCm platform to Microsoft Windows as described in
:doc:`ROCm component support in HIP SDK <./conceptual/component-support>`. It provides the runtime,
APIs, and tooling to leverage the computational power of AMD GPUs to create high-performance,
portable applications using the :doc:`HIP programming language <hip:index>`.

The HIP SDK consists of the AMD GPU Driver, HIP runtime, and HIP Libraries. These three parts are
distributed in the HIP SDK installer. The HIP SDK is intended for developer distribution. This is in
contrast to the AMD GPU driver, which is intended for all end users.

HIP SDK can run on your Windows system with Microsoft Visual Studio Code, and even includes solutions for use with the tool. However, it also has standalone tools like
compilers, profilers, and debuggers for use in your own development environment. 

HIP SDK code is open and hosted at https://github.com/ROCm/rocm-install-on-windows.

The documentation is structured as follows:

.. grid:: 2
  :gutter: 3

  .. grid-item-card:: Installation

    * :doc:`System requirements for HIP SDK <./reference/system-requirements>`
    * :doc:`Install HIP SDK for Windows <./install/install>`

  .. grid-item-card:: Conceptual

    * :doc:`ROCm component support in HIP SDK <./conceptual/component-support>`
    * :doc:`Deployment guidelines <./conceptual/deployment-guidelines>`

  .. grid-item-card:: How to

    * :doc:`Use ROCm Debugger for Windows <./how-to/debugger-windows>`

  .. grid-item-card:: About

    * :doc:`HIP SDK release notes<./about/releasenotes>`
    * :doc:`HIP SDK release versions <./about/release-versioning>`
