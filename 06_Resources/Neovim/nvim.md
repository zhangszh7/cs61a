# VSCode-Neovim (Windows 版)

---

## 架构说明

本环境采用“双引擎”架构：

**前端 UI 与语言服务**：Visual Studio Code (接管文件树、侧边栏、终端，以及基于 Pylance 的 Python 代码提示与补全)。
**后端纯文本操纵引擎**：Neovim (完全接管 Normal/Visual 模式下的按键映射、文本对象提取、宏录制与寄存器调用)。

---

## 第二阶段：安装真实的 Neovim 核心引擎

我们需要在 Windows 系统底层的物理机上安装纯净的 Neovim 引擎。

1. 按下 `Win` 键，搜索并打开 **PowerShell**。
2. 使用 Windows 包管理器 (winget) 执行一键安装：
```powershell
winget install Neovim.Neovim
```

3. 等待安装进度条完成。
4. **获取引擎绝对路径**：在 PowerShell 中继续输入以下命令并回车：
```powershell
where.exe nvim
```


*系统会输出一段绝对路径（例如 `C:\Program Files\Neovim\bin\nvim.exe`）。请将该路径**完整复制**备用。*

---

## 第三阶段：部署 VS Code 桥接插件

1. 回到 VS Code，打开扩展市场。
2. 搜索并安装 **`VSCode Neovim`**（认准作者：`asvetliakov`，图标为绿色 Neovim 标志）。
3. 按下 `Ctrl + ,` 打开 VS Code 设置。
4. 在搜索框输入：`neovim executable win32`
5. 在对应的输入框中，**粘贴**刚才复制的 Neovim 绝对路径（必须包含 `nvim.exe` 后缀）。

---

## 第四阶段：(编写 `init.lua` 配置)

Neovim 引擎需要在后台读取一份极其精简的配置文件，用来定义底层编辑逻辑。

### 1. 创建配置文件

1. 按下 `Win + R` 呼出运行窗口，输入 `%LOCALAPPDATA%` 并回车。
2. 在打开的目录中，新建一个名为 **`nvim`** 的文件夹。
3. 进入 `nvim` 文件夹，新建一个文本文档，重命名为 **`init.lua`**。
* *( 致命警告：请务必在 Windows 文件夹选项中开启“显示已知文件扩展名”，确保文件名绝对不是 `init.lua.txt`！)*



### 2. 写入配置

使用编辑器打开 `init.lua`，完整粘贴以下 Lua 代码并保存：

```lua
-- ==============================================================================
-- 核心配置 (Lua 架构，专为 VSCode Neovim 优化)
-- ==============================================================================

-- 【核心】将 Leader 键映射为空格 (Space)
vim.g.mapleader = " "

-- --- 1. 基础物理编辑体验 ---
vim.opt.scrolloff = 5           -- 光标距离上下边缘 5 行时触发屏幕滚动
vim.opt.ignorecase = true       -- 搜索时默认忽略大小写
vim.opt.smartcase = true        -- 若搜索词包含大写字母，则自动切换为精确匹配
vim.opt.hlsearch = true         -- 高亮所有搜索匹配项
vim.opt.incsearch = true        -- 边输入边实时高亮匹配

-- ==============================================================================
-- 2. VS Code 专属映射区域 (借壳调用 VS Code 原生 API)
-- ==============================================================================
if vim.g.vscode then
    -- --- 文件生命周期管理 ---
    vim.keymap.set("n", "<Leader>w", "<Cmd>call VSCodeNotify('workbench.action.files.save')<CR>")          -- 空格+w: 保存
    vim.keymap.set("n", "<Leader>q", "<Cmd>call VSCodeNotify('workbench.action.closeActiveEditor')<CR>")   -- 空格+q: 关闭标签页

    -- --- UI 与面板调度 ---
    vim.keymap.set("n", "<Leader>e", "<Cmd>call VSCodeNotify('workbench.action.toggleSidebarVisibility')<CR>") -- 空格+e: 开关左侧文件树
    vim.keymap.set("n", "<Leader>v", "<Cmd>call VSCodeNotify('workbench.files.action.showActiveFileInExplorer')<CR>") -- 空格+v: 在文件树高亮当前文件
    vim.keymap.set("n", "<Leader>t", "<Cmd>call VSCodeNotify('outline.focus')<CR>")                        -- 空格+t: 聚焦大纲(Tagbar)
    vim.keymap.set("n", "<Leader>c", "<Cmd>call VSCodeNotify('workbench.action.focusActiveEditorGroup')<CR>") -- 空格+c: 焦点切回代码区

    -- --- 维度穿梭 (跨文件与大纲) ---
    vim.keymap.set("n", "<C-p>", "<Cmd>call VSCodeNotify('workbench.action.quickOpen')<CR>")               -- Ctrl+p: 全局秒搜文件
    vim.keymap.set("n", "<C-]>", "<Cmd>call VSCodeNotify('editor.action.revealDefinition')<CR>")           -- Ctrl+]: 深入定义 (ctags平替)
    vim.keymap.set("n", "gd", "<Cmd>call VSCodeNotify('editor.action.revealDefinition')<CR>")              -- gd: 深入定义
    vim.keymap.set("n", "<C-t>", "<Cmd>call VSCodeNotify('workbench.action.navigateBack')<CR>")            -- Ctrl+t: 源码原路弹栈
    vim.keymap.set("n", "gr", "<Cmd>call VSCodeNotify('editor.action.referenceSearch.trigger')<CR>")       -- gr: 追溯全项目引用

    -- --- 分屏窗口越界跳转 ---
    vim.keymap.set("n", "<C-h>", "<Cmd>call VSCodeNotify('workbench.action.navigateLeft')<CR>")
    vim.keymap.set("n", "<C-j>", "<Cmd>call VSCodeNotify('workbench.action.navigateDown')<CR>")
    vim.keymap.set("n", "<C-k>", "<Cmd>call VSCodeNotify('workbench.action.navigateUp')<CR>")
    vim.keymap.set("n", "<C-l>", "<Cmd>call VSCodeNotify('workbench.action.navigateRight')<CR>")

    -- --- 生产力增强指令 ---
    vim.keymap.set("n", "<Leader><CR>", ":nohlsearch<CR>")                                                 -- 空格+回车: 清除搜索底色
    vim.keymap.set("n", "<Leader>f", "<Cmd>call VSCodeNotify('editor.action.formatDocument')<CR>")         -- 空格+f: 一键排版对齐
    vim.keymap.set("n", "<Leader>r", "<Cmd>call VSCodeNotify('python.execInTerminal')<CR>")                -- 空格+r: 纯净终端极速运行
end

```

---

## 第五阶段：突破物理隔离 ( `jj` 修复方案)

由于 VS Code 在 Insert (插入) 模式下会完全夺走键盘控制权，导致 Neovim 无法监听到 `jj` 连击。我们必须直接在 VS Code 的底层 JSON 中开启“复合按键 (Composite Keys)”后门。

1. 在 VS Code 中按下 `Ctrl + Shift + P`。
2. 输入 `open settings json`，选择 **首选项: 打开用户设置(JSON)**。
3. 在打开的 `settings.json` 文件最外层的 `{}` 内部，新增以下配置模块（注意用逗号与上下配置隔开）：

```json
    "vscode-neovim.compositeKeys": {
        "jj": {
            "command": "vscode-neovim.escape"
        }
    }
```

---

## 第六阶段：视觉与排版重塑 

为了彻底还原纯正的 Unix 体验，需对 VS Code 进行最后的外观整定：

1. **复古主题注入**：
* 在插件市场搜索安装 **`Gruvbox Theme`** (推荐作者: jdinhlife)。
* 按 `Ctrl + K` 然后按 `Ctrl + T`，选择 **`Gruvbox Dark Hard`** 激活高对比度复古配色。


2. **UI 比例校准**：
* 打开设置，将 `Window: Zoom Level` 调为 `1` (放大全局 UI 与状态栏)。
* 将 `Editor: Font Size` 稍微调小 (如 13)，使“大状态栏与精细代码”达成完美视觉平衡。


3. **状态栏大清洗**：
* 右键点击底部状态栏，**取消勾选**所有无用通知与插件图标。仅保留行号列号、Git 分支、Python 环境以及缩进规范 (Spaces: 4)。


**至此，VSCode-Neovim 双引擎架构已全部部署完毕。请彻底重启一次 VS Code 使所有底层挂载生效。**

---
