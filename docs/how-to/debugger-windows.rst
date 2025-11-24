.. meta::
   :description: Install HIP SDK
   :keywords: Windows, install, HIP, SDK, ROCm, AMD, HIP SDK

.. _hip-install-full:

*******************************************************************
HIP SDK Debugger for Windows
*******************************************************************

List of Windows ROCgdb limitations
=================================

The “AMD GPU restrictions” section of the ROCgdb manual now lists the Windows-specific restrictions at the bottom. Source here:

https://github.com/AMD-ROCm-Internal/ROCgdb/blob/70687c121649de0d217fadae7cfd71937c0deed6/gdb/doc/gdb.texinfo#L30499

This would be rendered at the bottom of this page: `AMD GPU (Debugging with ROCGDB) <https://rocm.docs.amd.com/projects/ROCgdb/en/latest/ROCgdb/gdb/doc/gdb/AMD-GPU.html#AMD-GPU-Restrictions>`_.

.. note::
   This page is generated from the latest Linux ROCm release, and does not contain the Windows changes.
   It will be rendered and present in the copy of the ROCgdb manual that is included with the HIP SDK (always installed when you install the debugger).

Hello World example
===================

Debugging GPU code with ROCgdb on Windows is just like on Linux, as you’ll see with this example.

1.  Copy the following code to a file named ``example.cpp`` in a directory of your choice (for example, ``C:\rocgdb-example``). The code contains a simple GPU kernel that adds two integers and returns the result. The result is printed on the console.

    .. code-block:: c++

        #include <hip/hip_runtime.h>
        #include <assert.h>

        __global__ void do_an_addition(int a, int b, int *out)
        {
          *out = a + b;
        }

        int main ()
        {
          int *result_ptr, result;
          /* Allocate memory for the device to write the result to. */
          hipError_t error = hipMalloc(&result_ptr, sizeof(int));
          assert(error == hipSuccess);

          /* Run `do_an_addition` on one block containing one HIP thread. */
          do_an_addition<<<dim3(1), dim3(1), 0, 0>>>(1, 2, result_ptr);

          /* Copy result from device to host. This acts as a
             synchronization point, waiting for the kernel dispatch to
             complete. */
          error = hipMemcpyDtoH(&result, result_ptr, sizeof(int));
          assert(error == hipSuccess);

          printf("result is %d\n", result);
          assert(result == 3);
          return 0;
        }

2.  Open a Windows Command Prompt. We will use this prompt to run the compiler and the debugger.

3.  Put the HIP SDK bin directory in the PATH:

    .. code-block:: console

        set "HIP_SDK_DIR=C:\Program Files\AMD\ROCm\7.1"
        set "PATH=%HIP_SDK_DIR%\bin;%PATH%"

4.  This makes the ``hipcc`` and ``rocgdb`` programs available in the PATH.

5.  Switch the current directory to where you put the ``example.cpp`` source file earlier:

    .. code-block:: console

        cd C:\rocgdb-example

6.  Compile the ``example.cpp`` HIP program using ``hipcc``:

    .. code-block:: console

        C:\rocgdb-example>hipcc example.cpp -o example.exe --offload-arch=gfx1201 -gdwarf -Wl,-debug:dwarf -O0

    Notes:

    - The ``--offload-arch=gfx1201`` option targets Navi48 GPU (for example, Radeon RX 9070 XT). For Navi44 (for example, Radeon RX 9060 XT), use ``--offload-arch=gfx1200`` instead.
    - The ``-gdwarf -Wl,-debug:dwarf`` options instruct ``hipcc`` to emit DWARF debug information for the host code. Otherwise, ``hipcc`` emits PDB (Microsoft) debug information, which ROCgdb does not yet understand.
    - The ``-O0`` option disables compiler optimizations.

7.  Run the just-compiled program to confirm it is working:

    .. code-block:: console

        C:\rocgdb-example>.\example.exe
        result is 3

    You can now run the just-compiled program under ROCgdb, stopping execution in the ``do_an_addition`` GPU kernel function, like so:

    .. code-block:: console

        C:\rocgdb-example>rocgdb example.exe
        GNU gdb (ROCm) 18.0.50.20251029-git
        Copyright (C) 2025 Free Software Foundation, Inc.
        License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
        This is free software: you are free to change and redistribute it.
        There is NO WARRANTY, to the extent permitted by law.
        Type "show copying" and "show warranty" for details.
        This GDB was configured as "x86_64-w64-mingw32".
        Type "show configuration" for configuration details.
        For bug reporting instructions, please see:
            <https://github.com/ROCm-Developer-Tools/ROCgdb/issues>.
        Find the GDB manual and other documentation resources online at:
            <http://www.gnu.org/software/gdb/documentation/>.
        For help, type "help".
        Type "apropos word" to search for commands related to "word"...
        Reading symbols from example.exe...
        (gdb) break do_an_addition
        Function "do_an_addition" not defined.
        Make breakpoint pending on future shared library load? (y or [n]) y
        Breakpoint 1 (do_an_addition) pending.
        (gdb) run
        Starting program: C:\rocgdb-example\example.exe
        [New Thread 12180.0x286c]
        [New Thread 12180.0x1aa4]
        [New Thread 12180.0x4e8c]
        [New Thread 12180.0x3578]
        [New Thread 12180.0x3af4]
        [Switching to thread 7, lane 0 (AMDGPU Lane 1:2:1:1/0 (0,0,0)[0,0,0])]
        Thread 7 "do_an_addition" hit Breakpoint 1, with lane 0, do_an_addition (a=1, b=2, out=0x300004000) at example.cpp:6
        6         *out = a + b;
        (gdb)

That’s it! See the ROCgdb documentation for more details.

