.. meta::
   :description: Install HIP SDK
   :keywords: Windows, install, HIP, SDK, ROCm, AMD, HIP SDK

.. _hip-install-full:

*******************************************************************
HIP SDK Debugger for Windows
*******************************************************************


List of Windows ROCgdb limitations
The “AMD GPU restrictions” section of the ROCgdb manual now lists the Windows-specific restrictions at the bottom.  Source here:
https://github.com/AMD-ROCm-Internal/ROCgdb/blob/70687c121649de0d217fadae7cfd71937c0deed6/gdb/doc/gdb.texinfo#L30499 

This would be rendered at the bottom of this page:

AMD GPU (Debugging with ROCGDB) 

… except that page is generated from the latest Linux ROCm release, so does not contain the Windows changes.

It will be rendered and present in the copy of the ROCgdb manual that is included with the HIP SDK (always installed when you install the debugger).

Hello World example
Debugging GPU code with ROCgdb on Windows is just like on Linux, as you’ll see with this example.

Copy the following code to a file named example.cpp to a directory or your choice.  For example, c:\rocgdb-example.  The code contains a simple GPU kernel that adds two integers and returns the result.  The result is printed on the console.

     ..  code-block::
     #include <hip/hip_runtime.h>
     #include <assert.h>
     __global__ void do_an_addition(int a, int b, int *out)
     {
       *out = a + b;
     }
     int main ()
     {
       int *result_ptr, result;
       // Allocate memory for the device to write the result to.
       hipError_t error = hipMalloc(&result_ptr, sizeof(int));
       assert(error == hipSuccess);
       // Run `do_an_addition` on one block containing one HIP thread.
       do_an_addition<<<dim3(1), dim3(1), 0, 0>>>(1, 2, result_ptr);
       // Copy result from device to host.  Note that this acts as a
       // synchronization point, waiting for the kernel dispatch to
       // complete.
       error = hipMemcpyDtoH(&result, result_ptr, sizeof(int));
       assert(error == hipSuccess);
       printf("result is %d\n", result);
       assert(result == 3);
       return 0;
     }

Open a Windows Command Prompt.  We will use this prompt to run the compiler and the debugger.

Put the HIP SDK bin directory in the PATH:

     ..  code-block::

     set "HIP_SDK_DIR=C:\Program Files\AMD\ROCm\7.1"
     set "PATH=%HIP_SDK_DIR%\bin;%PATH%"


This makes the hipcc and rocgdb programs available in the PATH.

Switch the current directory to where you put the example.cpp source file earlier:


     ..  code-block::
     cd C:\rocgdb-example
Compile the example.cpp HIP program using hipcc:


     ..  code-block::
     C:\rocgdb-example>hipcc example.cpp -o example.exe --offload-arch=gfx1201 -gdwarf -Wl,-debug:dwarf -O0
The --offload-arch=gfx1201 option targets Navi48 GPU (e.g., Radeon RX 9070 XT).  For Navi44 (e.g., Radeon RX 9060 XT), use --offload-arch=gfx1200instead.

The "-gdwarf -Wl,-debug:dwarf"options instruct hipcc to emit DWARF debug information for the host code.  Otherwise, hipcc emits PDB (Microsoft) debug information, which ROCgdb does not yet understand.  

The -O0 option disables compiler optimizations.

Run the just-compiled program to confirm it is working:


     ..  code-block::
     C:\rocgdb-example>.\example.exe
     result is 3
You can now run the just-compiled program under ROCgdb, stopping execution in the do_an_addition GPU kernel function, like so:


     ..  code-block::
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

That’s it!  <Link to documentation here.>
































To install the HIP SDK on Windows, use the :ref:`hip-install-quick` or the following instructions.

.. _hip-prerequisites:

Prerequisites
===============================================

Verify that your system meets all the installation requirements. The installation is only supported on
specific host architectures, Windows Editions, and update versions.

The HIP SDK is supported on Windows 10, 11, and Server 2022. You can install HIP on a system without AMD GPUs
to use the build toolchains, but to run HIP applications, you'll need a compatible GPU. Refer to
the :ref:`supported-gpus-win` for more details.

.. tab-set::

    .. tab-item:: CLI
        :sync: cli

        1. Type the following command on your system from a PowerShell command-line interface (CLI):

            ..  code-block::

                Get-ComputerInfo | Format-Table CsSystemType,OSName,OSDisplayVersion

            Running this command on a Windows system may result in the following output:

            ..  code-block::

                CsSystemType    OsName                      OSDisplayVersion
                ------------    ------                      ----------------
                x64-based PC    Microsoft Windows 11 Pro    22H2


        2. Confirm that the obtained information matches that listed in :ref:`Supported SKUs<supported-skus-win>`.

    .. tab-item:: GUI
        :sync: gui

        1. Open the **Settings** app.

            .. image:: ../data/how-to/000-settings-light.png
                :class: only-light
                :width: 400
                :alt: Gear icon of the Windows Settings app

            .. image:: ../data/how-to/000-settings-dark.png
                :class: only-dark
                :width: 400
                :alt: Gear icon of the Windows Settings app

        2. Navigate to **System > About**.

            .. image:: ../data/how-to/001-about-light.png
                :class: only-light
                :width: 400
                :alt: Settings app panel showing device and OS information.

            .. image:: ../data/how-to/001-about-dark.png
                :class: only-dark
                :width: 400
                :alt: Settings app panel showing device and OS information.

        3. Confirm that the obtained information matches that listed in :ref:`Supported SKUs<supported-skus-win>`.

.. _hip-install:

Install HIP SDK
===============================================

.. tab-set::

    .. tab-item:: CLI
        :sync: cli

        CLI options are listed in the following table:

        .. csv-table::
            :widths: 30, 70
            :header: "Install option", "Description"

            "``-install``", "Command used to install packages, both driver and applications. No output to the screen."
            "``-install -boot``", "Silent install with auto reboot."
            "``-install -log <absolute path>``", "Write install result code to the specified log file. The specified log file must be on a local machine. Double quotes are needed if there are spaces in the log file path."
            "``-uninstall``", "Command to uninstall all packages installed by this installer on the system. There is no option to specify which packages to uninstall."
            "``-uninstall -boot``", "Silent uninstall with auto reboot."
            "``/?`` or ``/help``", "Shows a brief description of all switch commands."

        .. note::

            Unlike the GUI, the CLI doesn't support selectively installing parts of the SDK bundle.

        To start the installation, follow these steps:

        1. Download the installer from the
        `HIP-SDK download page <https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html>`_.

        2. Launch the installer. Note that the installer is a graphical application with a ``WinMain`` entry
        point, even when called on the command line. This means that the application lifetime is tied to a
        window, even on headless systems where that window may not be visible.

            ..  code-block:: shell

                Start-Process $InstallerExecutable -ArgumentList $InstallerArgs -NoNewWindow -Wait

            .. important::

                Running the installer requires Administrator privileges.

            To install all components:

            ..  code-block:: shell

                Start-Process ~\Downloads\Setup.exe -ArgumentList '-install','-log',"${env:USERPROFILE}\installer_log.txt" -NoNewWindow -Wait

    .. tab-item:: GUI
        :sync: gui

        The HIP SDK installation options are listed in the following table.

        .. csv-table::
            :widths: 30, 30, 40
            :header: "HIP components", "Install type", "Additional options"

            "HIP SDK Core", "|win_rocm_version|", "Install location"
            "HIP Libraries", "Full, Partial, None", "Runtime, Development (Libs and headers)"
            "HIP Runtime Compiler", "Full, Partial, None", "Runtime, Development (headers)"
            "HIP Ray Tracing", "Full, Partial, None", "Runtime, Development (headers)"
            "Visual Studio Plugin", "Full, Partial, None", "Visual Studio 2017, 2019, 2022 Plugin"

        .. note::
            The ``select``/``deselect all`` options only apply to the installation of HIP SDK components. To
            install the bundled AMD Display Driver, manually select the install type.

        .. tip::
            Should you only wish to install a few select components, deselecting all, then selecting
            individual components may be more convenient.

        The HIP SDK installer bundles an AMD Radeon Software PRO |radeon_software_pro_version| installer.
        The supported install options and types are summarized in the following tables:

        .. csv-table::
            :widths: 30, 70
            :header: "Install option", "Description"

            "Install Location", "Location on disk to store driver files."
            "Install Type", "The breadth of components to be installed."
            "Factory Reset (optional)", "A Factory Reset will remove all prior versions of AMD HIP SDK and drivers. You will not be able to roll back to previously installed drivers."

        .. csv-table::
            :widths: 30, 70
            :header: "Install type", "Description"

            "Full Install", "Provides all AMD Software features and controls for gaming, recording, streaming, and tweaking the performance on your graphics hardware."
            "Minimal Install", "Provides only the basic controls for AMD Software features and does not include advanced features such as performance tweaking or recording and capturing content."
            "Driver Only", "Provides no user interface for AMD Software features."

        .. note::

            You must perform a system restart for a complete installation of the Display driver.

        To start the installation, follow these steps:

        1. Download the installer from the `HIP SDK download page <https://www.amd.com/en/developer/resources/rocm-hub/hip-sdk.html>`_.

        2. Launch the installer by clicking the **Setup** icon.

            .. image:: ../data/how-to/000-setup-icon.png
                :width: 400
                :alt: Icon with AMD arrow logo and User Access Control Shield overlay

            The installer requires Administrator privileges, so you may be greeted with a User Access
            Control (UAC) pop-up. Click Yes.

            .. image:: ../data/how-to/001-uac-light.png
                :class: only-light
                :width: 400
                :alt: User Access Control pop-up

            .. image:: ../data/how-to/001-uac-dark.png
                :class: only-dark
                :width: 400
                :alt: User Access Control pop-up

            The installer executable temporarily extracts installer packages to `C:\AMD`; it removes these
            after the installation completes.

            .. image:: ../data/how-to/002-initializing.png
                :width: 400
                :alt: Window with AMD arrow logo, futuristic background and progress counter

            The installer detects your system configuration to determine which installable components
            are applicable to your system.

            .. image:: ../data/how-to/003-detecting-system-config.png
                :width: 400
                :alt: Window with AMD arrow logo, futuristic background and activity indicator

        3. Customize your installation.

            .. image:: ../data/how-to/004-installer-window.png
                :width: 400
                :alt: Window with AMD arrow logo, futuristic background and activity indicator

            When the installer launches, it displays a window that lets you customize your installation. By
            default, all components are selected.

        4. Wait for the installation to complete.

            .. image:: ../data/how-to/012-install-progress.png
                :width: 400
                :alt: Window with AMD arrow logo, futuristic background and progress meter

            When installation is complete, the installer window may prompt you for a system restart.

            .. image:: ../data/how-to/013-install-complete.png
                :width: 400
                :alt: Window with AMD arrow logo, futuristic background and completion notice

            .. important::

                If the installer terminates mid-installation, the temporary directory created under `C:\AMD` can be
                safely removed. Installed components don't depend on this folder unless you explicitly choose this
                as the install folder.

.. _hip-upgrade:

Upgrade HIP SDK
===============================================

To upgrade the HIP SDK, you can run the installer for the newer version without uninstalling the
existing version. You can also uninstall the HIP SDK before installing the newest version.

.. _hip-uninstall:

Uninstall HIP SDK
===============================================

.. tab-set::

    .. tab-item:: CLI
        :sync: cli

        Launch the installer. Note that the installer is a graphical application with a ``WinMain`` entry
        point, even when called on the command line. This means that the application lifetime is tied to a
        window, even on headless systems where that window may not be visible.

        ..  code-block:: shell

            Start-Process $InstallerExecutable -ArgumentList $InstallerArgs -NoNewWindow -Wait

        .. important::

            Running the installer requires Administrator privileges.

        To uninstall all components, use the following code:

        ..  code-block:: shell

            Start-Process ~\Downloads\Setup.exe -ArgumentList '-uninstall' -NoNewWindow -Wait

    .. tab-item:: GUI
        :sync: gui

        Uninstallation of HIP SDK components can be done through the Windows Settings app. Navigate to
        "Apps > Installed apps" and click the ellipsis (...) on the far right next to the component you want to uninstall. Click "Uninstall".

        .. image:: ../data/how-to/014-uninstall-light.png
            :class: only-light
            :width: 400
            :alt: Installed apps section of the settings app showing installed HIP SDK components

        .. image:: ../data/how-to/014-uninstall-dark.png
            :class: only-dark
            :width: 400
            :alt: Installed apps section of the settings app showing installed HIP SDK components
