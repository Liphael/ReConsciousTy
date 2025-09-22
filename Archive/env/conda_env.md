# All Baisc Environments Config

## Language select

- [English](#english)
- [中文](#chinese)

---

### English

## Conda For Python Env Management

### Install && Config Conda

Run the following four commands to download and install the latest Linux installer for your chosen chip architecture. Line by line, these commands:

1. create a new directory named “miniconda3” in your home directory.
2. download the Linux Miniconda installation script for your chosen chip architecture and save the script as miniconda.sh in the miniconda3 directory.
3. run the miniconda.sh installation script in silent mode using shell.
4. remove the miniconda.sh installation script file after installation is complete.

```shell
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
shell ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
To download an older version
```

After installing, close and reopen your terminal application or refresh it by running the following command:

```shell
source ~/miniconda3/bin/activate
```

Then, initialize conda on all available shells by running the following command:

```shell
conda init --all
```

**Now, Conda has been installed. Afterward we config the sources.**

run following codes in shell to add chinese source image urls into basic config.

the cache reflesh will ask for old file removing permission, permit is ok.

```shell
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --set show_channel_urls yes
```

- if need to reverse to default, run following codes.

```shell
conda config --remove-key channels
```

to create new env for specific project, Refer to the following code with personalized modifications.

```shell
conda create -n [your-new-env-name] python=[specific_python_version] [list-of-package]
```

to activate your new environment, run following codes:

```shell
conda activate [your-new-env-name]
```

also deactivate codes and delete codes

```shell
conda deactivate [your-new-env-name]
```

```shell
conda env remove [your-new-env-name]
```

config pip source image urls:

```shell
mkdir -p ~/.pip && nano ~/.pip/pip.conf
```

adding following contexts, eixt & confirm save file.

```conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
```



### 
