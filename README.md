[中文版](README.md) | [English Version](README_eng.md)

GIF裁剪器 用户帮助文档

欢迎使用GIF裁剪器！本应用程序旨在帮助用户方便地裁剪和调整GIF动画的分辨率。本文档将指导您完成安装、使用以及解决常见问题。

目录

1. [简介](#简介)
2. [系统要求](#系统要求)
3. [安装指南](#安装指南)
4. [使用说明](#使用说明)
    - [启动程序](#启动程序)
    - [设置分辨率](#设置分辨率)
    - [选择GIF文件或目录](#选择gif文件或目录)
    - [裁剪GIF](#裁剪gif)
    - [保存裁剪后的GIF](#保存裁剪后的gif)
5. [配置文件说明](#配置文件说明)
6. [高 DPI 适配](#高-dpi-适配)
7. [常见问题](#常见问题)



简介

GIF裁剪器是一款基于PyQt5和Pillow库开发的桌面应用程序，旨在为用户提供简便的GIF动画裁剪和分辨率调整功能。用户可以通过直观的图形界面选择单个GIF文件或批量处理整个目录中的GIF文件，按照指定的分辨率裁剪并保存。

系统要求

- 操作系统：Windows、macOS 或 Linux
- Python 版本：Python 3.6 及以上
- 依赖库：
    - PyQt5
    - Pillow

安装指南

1. 安装Python

如果尚未安装Python，请访问[Python官方网站](https://www.python.org/downloads/)下载并安装最新版本的Python。

2. 安装依赖库

打开终端（Windows用户可以使用命令提示符或PowerShell），运行以下命令安装所需的Python库：

pip install PyQt5 Pillow

3. 下载程序代码

将程序代码保存到本地目录，例如`gif_cropper.py`。

4. 运行程序

在终端中导航到程序所在的目录，并运行：

python gif_cropper.py

使用说明

启动程序

双击运行`gif_cropper.py`，或在终端中使用上述命令启动程序。程序启动后，将显示主窗口“GIF裁剪器”。

设置分辨率

1. 手动输入：
    - 在“请输入分辨率（宽x高）”字段中输入所需的宽度和高度，格式为`宽x高`（例如`640x480`）。
  
2. 快捷按钮：
    - 点击“320x240”按钮，程序将自动设置分辨率为320宽×240高。
    - 点击“240x135”按钮，程序将自动设置分辨率为240宽×135高。

3. 保存分辨率：
    - 设置的分辨率将自动保存到`config.txt`文件中，程序下次启动时将加载上次保存的分辨率。

选择GIF文件或目录

1. 选择单个GIF文件：
    - 点击“选择 GIF”按钮，弹出文件选择对话框。
    - 浏览并选择您想要裁剪的GIF文件。
  
2. 选择GIF目录：
    - 点击“选择 GIF 目录”按钮，弹出目录选择对话框。
    - 选择包含多个GIF文件的目录，程序将自动处理该目录下所有的GIF文件。

裁剪GIF

1. 显示图像：
    - 选择GIF文件后，程序将在画布上显示GIF的第一帧。
  
2. 绘制裁剪区域：
    - 使用鼠标左键在图像上点击并拖动，绘制裁剪矩形。
    - 裁剪区域将根据设定的宽高比自动调整，以保持分辨率比例。

3. 调整裁剪区域：
    - 可以重新绘制裁剪区域，或修改分辨率后重新绘制。

保存裁剪后的GIF

1. 确认裁剪：
    - 绘制好裁剪区域后，点击“确认裁剪并保存”按钮。
  
2. 保存文件：
    - 程序将裁剪并调整GIF的每一帧，生成新的GIF文件，文件名将在原文件名后添加`_cropped`后缀（例如`example_cropped.gif`）。
  
3. 完成提示：
    - 保存完成后，将弹出提示框显示新文件的保存路径。

配置文件说明

程序使用`config.txt`文件来保存用户设置的分辨率。文件内容格式为`宽x高`（例如`320x240`）。如果`config.txt`不存在或内容不符合格式，程序将使用默认分辨率`320x240`。

手动编辑配置文件

您可以手动编辑`config.txt`文件以更改默认分辨率。确保文件内容符合`宽x高`格式，例如：

640x480

高 DPI 适配

程序已启用高 DPI 适配，确保在高分辨率屏幕上显示清晰。相关设置已在程序初始化时自动配置，无需用户手动调整。

常见问题

1. 程序无法启动或报错

解决方案：
- 确认已安装正确版本的Python（建议Python 3.6及以上）。
- 确认已安装所有依赖库（PyQt5 和 Pillow）。
- 检查程序代码是否完整，文件是否正确命名为`gif_cropper.py`。

2. 无法加载GIF文件

解决方案：
- 确认选择的文件为有效的GIF格式。
- 检查文件是否损坏，可以尝试使用其他查看器打开。

3. 裁剪后GIF质量下降

解决方案：
- 确认输入的目标分辨率是否过低。
- 选择合适的分辨率以平衡文件大小和画质。

4. 无法保存裁剪后的GIF

解决方案：
- 确认目标文件夹具有写入权限。
- 检查磁盘空间是否充足。


