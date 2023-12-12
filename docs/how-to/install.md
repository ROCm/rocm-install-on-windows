# Install HIP SDK on Windows

To install the HIP SDK on Windows, use the [quick-start guide](./install-quick.md) or follow the instructions below.

follow the instructions listed below.

**Topics:**

* [Prerequisites](#prerequisites)
* [Install HIP SDK](#install-hip-sdk)
* [Upgrade HIP SDK](#upgrade-hip-sdk)
* [Uninstall HIP SDK](#uninstall-hip-sdk)

## Prerequisites

Verify that your system meets all the installation requirements. The installation is only supported
only on specific host architectures, Windows Editions, and update versions.

The HIP SDK is supported on Windows 10 and 11. It can be installed on a
system without AMD GPUs to use the build toolchains, but to run HIP applications, a
compatible GPU is required. Please see the
[supported GPU guide](../../about/compatibility/windows-support.md) for more details.

::::{tab-set}

:::{tab-item} CLI
:sync: cli

1. Type the following command on your system from a PowerShell command-line interface (CLI):

   ```pwsh
   Get-ComputerInfo | Format-Table CsSystemType,OSName,OSDisplayVersion
   ```

   Running this command on a Windows system may result in the following output:

   ```output
   CsSystemType OsName                   OSDisplayVersion
   ------------ ------                   ----------------
   x64-based PC Microsoft Windows 11 Pro 22H2
   ```

2. Confirm that the obtained information matches with those listed in {ref}`windows-support`.

:::

:::{tab-item} GUI
:sync: gui

1. Open the **Settings** app.

   ![Gear icon of the Windows Settings app](../../data/install/000-settings-light.png "Windows Settings app icon")

2. Navigate to **System > About**.

   ![Settings app panel showing device and OS information](../../data/install/001-about-light.png "Settings > About page")

3. Confirm that the obtained information matches {ref}`windows-support`.

:::
::::

## Install HIP SDK

::::{tab-set}

:::{tab-item} CLI
:sync: cli

CLI options are listed in the following table:

```{table}
:name: hip-sdk-cli-install
| **Install Option** | **Description** |
|:------------------|:---------------|
| `-install` | Command used to install packages, both driver and applications. No output to the screen. |
| `-install -boot` | Silent install with auto reboot. |
| `-install -log <absolute path>` | Write install result code to the specified log file. The specified log file must be on a local machine. Double quotes are needed if there are spaces in the log file path. |
| `-uninstall` | Command to uninstall all packages installed by this installer on the system. There is no option to specify which packages to uninstall. |
| `-uninstall -boot` | Silent uninstall with auto reboot. |
| `/?` or `/help` | Shows a brief description of all switch commands. |
```

```{note}
Unlike the GUI, the CLI doesn't support selectively installing parts of the SDK bundle.
```

To start the installation, follow these steps:

1. Download the installer from the
[HIP-SDK download page](https://www.amd.com/en/developer/rocm-hub/hip-sdk.html).

2. Launch the installer. Note that the installer is a graphical application with a `WinMain` entry
   point, even when called on the command line. This means that the application lifetime is tied to a
   window, even on headless systems where that window may not be visible.

    ```pwsh
    Start-Process $InstallerExecutable -ArgumentList $InstallerArgs -NoNewWindow -Wait
    ```

    ```{important}
    Running the installer requires Administrator Privileges.
    ```

    To install all components:

    ```pwsh
    Start-Process ~\Downloads\Setup.exe -ArgumentList '-install','-log',"${env:USERPROFILE}\installer_log.txt" -NoNewWindow -Wait
    ```

:::

:::{tab-item} GUI
:sync: gui

The HIP SDK installation options are listed in the following table.

```{table}
:name: hip-sdk-options
| **HIP Components** | **Install Type** | **Additional Options** |
|:------------------|:----------------|:----------------------|
| HIP SDK Core         | 5.5.0               | Install location                        |
| HIP Libraries        | Full, Partial, None | Runtime, Development (Libs and headers) |
| HIP Runtime Compiler | Full, Partial, None | Runtime, Development (Headers)          |
| HIP Ray Tracing      | Full, Partial, None | Runtime, Development (Headers)          |
| Visual Studio Plugin | Full, Partial, None | Visual Studio 2017, 2019, 2022 Plugin   |
```

```{note}
The Select/DeSelect All option only applies to the installation of HIP SDK
components. To install the bundled AMD Display Driver, manually select the
install type.
```

```{tip}
Should you only wish to install a few select components,
DeSelecting All and then picking the individual components may be more
convenient.
```

The HIP SDK installer bundles an AMD Radeon Software PRO 23.10 installer. The
supported install options are summarized in the following table:

```{table}
:name: display-driver-install-options
| **Install Option** | **Description** |
|:------------------|:---------------|
| Install Location         | Location on disk to store driver files. |
| Install Type             | The breadth of components to be installed. |
| Factory Reset (Optional) | A Factory Reset will remove all prior versions of AMD HIP SDK and drivers. You will not be able to roll back to previously installed drivers. |
```

```{table} AMD Display Driver Install Types
:name:
| **Install Type** | **Description** |
|:----------------|:---------------|
| Full Install     | Provides all AMD Software features and controls for gaming, recording, streaming, and tweaking the performance on your graphics hardware. |
| Minimal Install  | Provides only the basic controls for AMD Software features and does not include advanced features such as performance tweaking or recording and capturing content. |
| Driver Only      | Provides no user interface for AMD Software features. |
```

```{note}
You must perform a system restart for a complete installation of the
Display Driver.
```

To start the installation, follow these steps:

1. Download the installer from the
[HIP-SDK download page](https://www.amd.com/en/developer/rocm-hub/hip-sdk.html).

2. Launch the installer by clicking the **Setup** icon.

    ![Icon with AMD arrow logo and User Access Control Shield overlay](../../data/install/000-setup-icon.png "Setup Icon")

    The installer requires Administrator Privileges, so you may be greeted with a
    User Access Control (UAC) pop-up. Click Yes.

    ![User Access Control pop-up](../../data/install/001-uac-light.png "User Access Control pop-up")

    The installer executable temporarily extracts installer packages to `C:\AMD`; it removes these after the
    installation completes.

    ![Window with AMD arrow logo, futuristic background and progress counter](../../data/install/002-initializing.png "Installer initialization window")

    The installer detects your system configuration to determine which installable components
    are applicable to your system.

    ![Window with AMD arrow logo, futuristic background and activity indicator](../../data/install/003-detecting-system-config.png "Installer initialization window")

3. Customize your installation. When the installer launches, it displays a window that lets you customize
    your installation. By default, all components are selected.

    ![Window with AMD arrow logo, futuristic background and activity indicator](../../data/install/004-installer-window.png "Installer initialization window")

4. Wait for the installation to complete.

    ![Window with AMD arrow logo, futuristic background and progress meter](../../data/install/012-install-progress.png "Installation progress")

    When installation is complete, the installer window may prompt you for a system restart.

    ![Window with AMD arrow logo, futuristic background and completion notice](../../data/install/013-install-complete.png "Installation complete")

    ```{error}
    If the installer terminates mid-installation, the temporary directory created under `C:\AMD` can be
    safely removed. Installed components don't depend on this folder unless you explicitly choose this
    as the install folder.
    ```

:::

::::

## Upgrade HIP SDK

To upgrade the HIP SDK, you can run the installer for the newer version without uninstalling the
existing version. You can also uninstall the HIP SDK before installing the newest version.

## Uninstall HIP SDK

::::{tab-set}

:::{tab-item} CLI
:sync: cli

Launch the installer. Note that the installer is a graphical application with a `WinMain` entry
point, even when called on the command line. This means that the application lifetime is tied to a
window, even on headless systems where that window may not be visible.

```pwsh
Start-Process $InstallerExecutable -ArgumentList $InstallerArgs -NoNewWindow -Wait
```

```{important}
Running the installer requires Administrator Privileges.
```

To uninstall all components:

```pwsh
Start-Process ~\Downloads\Setup.exe -ArgumentList '-uninstall' -NoNewWindow -Wait
```

:::

:::{tab-item} GUI
:sync: gui

Uninstallation of HIP SDK components can be done through the Windows Settings app. Navigate to
"Apps > Installed apps" and click the ellipsis (...) on the far right next to the component you want to uninstall. Click "Uninstall".

![Installed apps section of the settings app showing installed HIP SDK components](../../data/install/014-uninstall-light.png "Removing the SDK via the settings app")

For visual studio extension uninstallation, refer to
<https://github.com/ROCm-Developer-Tools/HIP-VS/blob/master/README.md>.
:::

::::
