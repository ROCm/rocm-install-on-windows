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