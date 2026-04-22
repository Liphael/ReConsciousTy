# 部署开发容器

可以使用“开发容器”[dev container](https://containers.dev/)软件创建一个健全的开发环境，两种使用方法的流程与原始链接如下：

使用指南

- [Github Codespaces](#github-codespaces)
- [VS Code Dev Container extension](#vs-code-dev-containers)

原始链接

- [Program: GitHub Codespaces](https://github.com/features/codespaces)
- [Program: VS Code Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

## GitHub Codespaces使用流程

点击下方按钮直接在Codespace打开：

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/langchain-ai/langchain)

或逐步跟随以下步骤：

1. Click the **Code** drop-down menu at the top of <https://github.com/langchain-ai/langchain>.
1. Click on the **Codespaces** tab.
1. Click **Create codespace on master**.

For more info, check out the [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/github/developing-online-with-codespaces/creating-a-codespace#creating-a-codespace).

## VS Code Dev Containers

[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/langchain-ai/langchain)

> [!NOTE]
> If you click the link above you will open the main repo (`langchain-ai/langchain`) and *not* your local cloned repo. This is fine if you only want to run and test the library, but if you want to contribute you can use the link below and replace with your username and cloned repo name:

```txt
https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/&lt;YOUR_USERNAME&gt;/&lt;YOUR_CLONED_REPO_NAME&gt;
```

Then you will have a local cloned repo where you can contribute and then create pull requests.

If you already have VS Code and Docker installed, you can use the button above to get started. This will use VSCode to automatically install the Dev Containers extension if needed, clone the source code into a container volume, and spin up a dev container for use.

Alternatively you can also follow these steps to open this repo in a container using the VS Code Dev Containers extension:

1. If this is your first time using a development container, please ensure your system meets the pre-reqs (i.e. have Docker installed) in the [getting started steps](https://aka.ms/vscode-remote/containers/getting-started).

2. Open a locally cloned copy of the code:

   - Fork and Clone this repository to your local filesystem.
   - Press <kbd>F1</kbd> and select the **Dev Containers: Open Folder in Container...** command.
   - Select the cloned copy of this folder, wait for the container to start, and try things out!

You can learn more in the [Dev Containers documentation](https://code.visualstudio.com/docs/devcontainers/containers).

## Tips and tricks

- If you are working with the same repository folder in a container and Windows, you'll want consistent line endings (otherwise you may see hundreds of changes in the SCM view). The `.gitattributes` file in the root of this repo will disable line ending conversion and should prevent this. See [tips and tricks](https://code.visualstudio.com/docs/devcontainers/tips-and-tricks#_resolving-git-line-ending-issues-in-containers-resulting-in-many-modified-files) for more info.
- If you'd like to review the contents of the image used in this dev container, you can check it out in the [devcontainers/images](https://github.com/devcontainers/images/tree/main/src/python) repo.
