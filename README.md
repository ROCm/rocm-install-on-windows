# HIP SDK installation documentation (Windows)

This repository contains installation instructions for the HIP SDK on Windows, along with installation-related information.

For Linux-related installation information, refer to the [Linux installation GitHub repository](https://github.com/ROCm/rocm-install-on-linux) or the [ROCm docs Linux install page]().

## Building our documentation

For a quick-start build, use the following code. For more options and detail, refer to
[Building documentation](https://rocm.docs.amd.com/en/latest/contribute/building.html).

```bash
cd docs

pip3 install -r sphinx/requirements.txt

python3 -m sphinx -T -E -b html -d _build/doctrees -D language=en . _build/html
```
