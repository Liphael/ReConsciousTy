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

1. this code activates conda, if conda is installed in other directory, the code's dir should be modified.
2. after activation, u will see "(base)" at head of your commandline, showing the "base" env of conda is activated.

```shell
source ~/miniconda3/bin/activate
```

Then, initialize conda on all available shells by running the following command:

1. this code execute the initiation of conda configuration.

```shell
conda init --all
```

**Now, Conda has been installed. Afterward we config the sources.**

run following codes in shell to add chinese source image urls into basic config.

the cache reflesh will ask for old file removing permission, permit is ok.

this code is typically made for usage in china. because of chinese national firewall filteration of harmful contents, legal contents should be obtained from main official mirror sites, if you dont want to use any VPN tech.

this code:

1. adding mirrors
2. config url showing when start downloading

```shell
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --set show_channel_urls yes
```

- attention, if need to reverse to default, run following codes.

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



### Chinese

## 基于Conda软件的Python环境管理

### 安装 && 配置Conda

运行以下四个命令，下载并安装所选芯片架构的最新Linux安装程序。

这些命令逐行的功能分别是：

1. 在主目录中创建一个名为“miniconda3”的新目录。
2. 下载适用于所选芯片架构的Linux Miniconda安装脚本，并将该脚本另存为Miniconda.sh，保存在miniconda3目录中。
3. 使用shell在静默模式下运行miniconda.sh安装脚本。
4. 安装完成后删除miniconda.sh安装脚本文件。

```shell
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
shell ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
To download an older version
```

安装完成后，关闭并重新打开终端应用程序，或通过运行以下命令刷新它：

1. 此代码激活conda，如果conda安装在其他目录中，则应修改代码的dir。
2. 激活后，您将在命令行的头部看到“（base）”，显示conda的“base”环境已激活。

```shell
source ~/miniconda3/bin/activate
```

然后，通过运行以下命令在所有可用的shell上初始化conda：

1. 此代码执行conda初始化配置。

```shell
conda init --all
```

***现在，Conda已经安装完毕。然后我们配置源代码***

在shell中运行以下代码，将中文源图像url添加到基本配置中。

缓存刷新将请求旧文件删除权限，允许即可。

此代码通常在中国使用。由于中国国家防火墙过滤有害内容，如果你不想使用任何VPN技术，应该从主要的官方镜像网站获取合法内容。

此代码：

1. 添加数个镜像源到配置文件
2. 设置在开始下载时显示所用源

```shell
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --set show_channel_urls yes
```

- 注意，如果你需要回退到默认配置，请运行以下代码。

```shell
conda config --remove-key channels
```

要为特定项目创建新的环境变量，请参考以下代码并进行个性化修改。

```shell
conda create -n [your-new-env-name] python=[specific_python_version] [list-of-package]
```

要激活新环境，请运行以下代码：

```shell
conda activate [your-new-env-name]
```

同时停用代码并删除代码

```shell
conda deactivate [your-new-env-name]
```

```shell
conda env remove [your-new-env-name]
```

配置pip源映像url：

```shell
mkdir -p ~/.pip && nano ~/.pip/pip.conf
```

添加以下上下文，eixt&确认保存文件。

```conf
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = pypi.tuna.tsinghua.edu.cn
```
