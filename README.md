# 📄 PDF 智能解析工具

一款开箱即用的 PDF 文字提取与 OCR 识别桌面工具。支持文字型 PDF 直接提取和扫描型 PDF 的中文 OCR 识别，输出为 Markdown / TXT / JSON 格式。

## ✨ 功能特性

- **双模式解析**：自动检测 PDF 类型，文字层直接提取，扫描版自动切换 OCR
- **OCR 中文识别**：基于 RapidOCR (ONNX Runtime)，中文识别率高，无需 GPU
- **多格式导出**：支持 Markdown / 纯文本 / JSON 分块导出
- **图形界面**：Tkinter 原生界面，无需浏览器，双击即用
- **页面预览**：左侧操作 + 右侧实时预览，支持翻页导航

## 🖥️ 界面预览

```
┌─────────────────────────────────────────────────────┐
│  📄 PDF 智能解析工具    by YunHengDu                 │
├──────────────┬──────────────────────────────────────┤
│ 📂 选择文件   │  📝 预览                            │
│ [浏览...]     │  ══════════ 第 1 页 ══════════      │
│               │  医学免疫学是生物医学领域中...      │
│ 📋 文件信息   │                                      │
│ 标题: xxx     │                                      │
│ 页数: 302     │                                      │
│               │                                      │
│ ⚙️ 解析设置   │                                      │
│ ○自动 ○文字   │                                      │
│               │                                      │
│ [🚀 开始解析]  │                                      │
│ ████████░░░░  │                                      │
│               │                                      │
│ [导出MD][TXT] │                                      │
├──────────────┴──────────────────────────────────────┤
│ YunHengDu © 2026          就绪 | 支持文字和扫描件   │
└─────────────────────────────────────────────────────┘
```

## 📦 安装与使用

### 方式一：直接运行 Python 脚本

```bash
# 1. 安装依赖
pip install pymupdf rapidocr-onnxruntime

# 2. 运行
python pdf_parser_desktop.py
```

### 方式二：打包为独立 EXE

```bash
# 1. 安装 PyInstaller
pip install pyinstaller

# 2. 打包
pyinstaller --onefile --noconsole --name "PDF解析工具" pdf_parser_desktop.py

# 3. 在 dist/ 目录找到 exe，可直接分享给他人使用
```

## 🏗️ 技术栈

| 组件 | 选型 | 说明 |
|------|------|------|
| 界面 | Tkinter | Python 原生 GUI，无需额外依赖 |
| PDF 解析 | PyMuPDF (fitz) | 支持文字提取 + 页面渲染 |
| OCR 引擎 | RapidOCR | ONNX Runtime 推理，中文优化 |
| 打包 | PyInstaller | 打包为独立 EXE |
| 导出格式 | Markdown / TXT / JSON | 适配 RAG 知识库场景 |

## 📂 项目结构

```
pdf-parser-tool/
├── pdf_parser_desktop.py    # 主程序（Tkinter 桌面版）
├── pdf_parser_app.py        # Streamlit Web 版
├── pack_for_sharing.py      # 一键打包脚本
├── build_exe.bat            # 打包批处理
├── install_and_run.ps1      # 一键安装运行
└── README.md
```

## 🧠 开发动机

该项目源于实际需求：需要将一本 302 页的扫描版医学教材（无文字层）转化为结构化的文本知识库，用于搭建 AI 复习助手。在调研了多种方案后，选择了 PyMuPDF + RapidOCR 的组合，并封装为图形界面工具，方便非技术用户使用。

## 🔮 未来计划

- [ ] 多线程加速 OCR 解析
- [ ] 表格结构识别与导出
- [ ] 批量 PDF 处理
- [ ] 提取结果的可视化统计

## 📄 许可证

MIT License

---

*由 YunHengDu 开发维护*
