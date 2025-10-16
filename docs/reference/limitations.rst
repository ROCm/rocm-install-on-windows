.. meta::
  :description: Windows GPU and OS support
  :keywords: Windows support, ROCm distributions, ROCm, AMD, HIP SDK, HIP

.. _limitations-win:

******************************************************************************
Limitations
******************************************************************************

.. _known-issues-win:

6.4.2 known issues
===============================================

* ds_gws_barrier can cause compilation errors with gfx1200/1201
* Long running kernels using rocFFT can cause occasional crashes with gfx1151 and gfx1002
* Manual building hipBLAS can fail under certain conditions
* Intermittent system or application crash may be observed while running long running kernels using rocFFT and rocSPARSE on AMD Ryzen™ AI Max 380, 390, and AMD Radeon™ RX 7000 Series products.
* Manual build failure may be observed under certain conditions while building hipBLAS.
* Manual build failure may be observed under certain conditions while building hipSOLVER.
* Manual build failure may be observed under certain conditions while building rocTHRUST.
* hipify clang may experience failures when using the VS2019 MSVC toolchain.
* Intermittent compilation errors may be observed while running cooperative_groups examples due to ds_gws_barrier on AMD Radeon™ RX 9060 and RX 9070 Series products.
* Intermittent failure may be observed for HIP memory API calls on AMD Radeon™ RX 9070 Series products.
* TDR (Timeout Detection and Recovery) may be observed while running Orochi tests on AMD Radeon™ RX 7000 Series products with multi-GPU configurations.
