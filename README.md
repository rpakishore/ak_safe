<!--- Heading --->
<div align="center">
  <h1>ak_safe</h1>
  <p>
    Python wrapper for SAFE.
    Generate/Analyze/Extract complex structural models using python.
  </p>
<h4>
    <a href="https://github.com/rpakishore/ak_safe/blob/main/documentation/Usage/GUI.md">GUI</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/ak_safe/tree/main?tab=readme-ov-file#2-getting-started">Getting Started</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/ak_safe/blob/main/documentation/Layout.md">Layout Documentation</a>
  <span> · </span>
    <a href="https://github.com/rpakishore/ak_safe/issues/">Report Bug/Request Feature</a>

  </h4>
</div>
<br />

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/rpakishore/ak_safe)
![GitHub last commit](https://img.shields.io/github/last-commit/rpakishore/ak_safe)
[![tests](https://github.com/rpakishore/ak_safe/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/rpakishore/ak_safe/actions/workflows/test.yml)

<!-- Table of Contents -->
<h2>Table of Contents</h2>

- [1. About the Project](#1-about-the-project)
- [2. Getting Started](#2-getting-started)
  - [2.1. Prerequisites](#21-prerequisites)
  - [2.2. Installation](#22-installation)
    - [2.2.1. Production](#221-production)
      - [2.2.1.1. Install from Pypi release](#2211-install-from-pypi-release)
    - [2.2.2. Development](#222-development)
- [3. Usage](#3-usage)
- [4. Roadmap](#4-roadmap)
- [5. License](#5-license)
- [6. Contact](#6-contact)
- [7. Acknowledgements](#7-acknowledgements)

<!-- About the Project -->
## 1. About the Project

<!-- Getting Started -->
## 2. Getting Started

<!-- Prerequisites -->
### 2.1. Prerequisites

1. Python 3.11 or above
2. CSI SAFE v21 or higher

<!-- Installation -->
### 2.2. Installation

#### 2.2.1. Production

##### 2.2.1.1. Install from Pypi release

```bash
pip install ak_safe
```

Note: The Pypi version does not ship with the optional streamlit gui

#### 2.2.2. Development

Download the git and install via flit

```bash
git clone https://github.com/rpakishore/ak_safe.git
cd  ak_sap
pip install flit
flit install --pth-file
```

<!-- Usage -->
## 3. Usage

Initialize the module as below

```python
from ak_safe import debug, SAFEWrapper
debug(status=False)

#Initialize
safe = SAFEWrapper(attach_to_exist=True)      #Attach to existing opened model
safe = SAFEWrapper(attach_to_exist=False)     #Create new blank model from latest SAP2000

## Create blank model from a custom version of SAP2000
safe = SAFEWrapper(attach_to_exist=False, program_path=r'Path\to\SAP2000.exe')

```

Parent level methods and attributes

```python
safe.hide(status=True)                       #Hide the SAFE window
safe.unhide(status=False)                    #Unhides SAFE window
safe.version                                 #Returns SAFE version number
safe.api_version                             #Returns SAFE version number

safe.save(r'\Path\to\save\file.FDB')
```
<!-- Roadmap -->
## 4. Roadmap

- [ ] Generate Load Patterns
- [ ] Generate Load Cases
- [ ] Apply Loads
  - [ ] Points
  - [ ] Area
  - [ ] Line
- [ ] Export joint reactions to Hilti-Profis file

<!-- License -->
## 5. License

See [LICENSE](https://github.com/rpakishore/ak_safe/blob/main/LICENSE) for more information.

<!-- Contact -->
## 6. Contact

Arun Kishore - [@rpakishore](mailto:pypi@rpakishore.co.in)

Project Link: [https://github.com/rpakishore/ak_safe](https://github.com/rpakishore/ak_safe)

<!-- Acknowledgments -->
## 7. Acknowledgements
