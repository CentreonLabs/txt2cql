[![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)](http://github.com/badges/stability-badges)

# txt2cql

`txt2cql` is a command-line tool designed to convert input text into a valid [_Centreon Query Language_ (CQL)](https://docs.centreon.com/docs/alerts-notifications/resources-status/#cql-criteria) request. The generated CQL is automatically copied to your clipboard, ready to be pasted into the research bar of the resource status page in Centreon.

![Demo Animation](https://github.com/CentreonLabs/txt2cql/blob/assets/assets/output.gif?raw=true)

## Installation

### <summary> Installing pipx </summary>

<details>

From their [documentation](https://pipx.pypa.io/stable/installation/):

#### On macOS:

```bash
brew install pipx
pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions in global scope. See "Global installation" section below.
```

#### On Linux:

##### Ubuntu 23.04 or above

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions in global scope. See "Global installation" section below.
```

##### Fedora:

```bash
sudo dnf install pipx
pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions in global scope. See "Global installation" section below.
Using pip on other distributions:
python3 -m pip install --user pipx
python3 -m pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions in global scope. See "Global installation" section below.
```

#### On Windows:

##### Install via Scoop:

```bash
scoop install pipx
pipx ensurepath
```

#### Install via pip (requires pip 19.0 or later)

```bash
# If you installed python using Microsoft Store, replace `py` with `python3` in the next line.
py -m pip install --user pipx
py -m pipx ensurepath
```
It is possible (even most likely) the above finishes with a WARNING looking similar to this:

```bash
WARNING: The script pipx.exe is installed in `<USER folder>\AppData\Roaming\Python\Python3x\Scripts` which is not on PATH
```

If so, go to the mentioned folder, allowing you to run the pipx executable directly. Enter the following line (even if you did not get the warning):

```bash
.\pipx.exe ensurepath
```

This will add both the above mentioned path and the %USERPROFILE%\.local\bin folder to your search path. Restart your terminal session and verify pipx does run.

</details>

### Installing txt2cql

```bash
pipx install git+https://github.com/CentreonLabs/txt2cql
```

### Export OpenAI API key

For the tool to work, you need to export your OpenAI API key as an environment variable. You can do this by adding the following line to your shell configuration file (e.g., `~/.bashrc`, `~/.zshrc`, etc.):

```bash
export OPENAI_API_KEY="your-api-key"
```

## Usage

```bash
txt2cql all ping services for all linux hosts

> s.description:ping h.name:linux
```
