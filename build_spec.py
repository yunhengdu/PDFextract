"""
打包 PDF 解析工具为 EXE
使用 --collect-all 自动收集所有依赖
"""
import os
import sys
import shutil

packages = [
    'rapidocr_onnxruntime',
    'onnxruntime',
    'pyclipper',
    'shapely',
]

collect_args = ' '.join([f'--collect-all {p}' for p in packages])

cmd = (
    f'{sys.executable} -m PyInstaller '
    '--onedir '
    '--noconsole '
    f'{collect_args} '
    '--name "PDF解析工具" '
    '--clean '
    'pdf_parser_desktop.py'
)

print("=" * 60)
print("正在打包...")
print("=" * 60)
print()

result = os.system(cmd)

print()
if result == 0:
    exe_folder = os.path.abspath("dist/PDF解析工具")
    total_size = 0
    for root, dirs, files in os.walk(exe_folder):
        for f in files:
            total_size += os.path.getsize(os.path.join(root, f))
    print(f"✅ 打包成功!")
    print(f"  位置: {exe_folder}")
    print(f"  大小: {total_size / 1024 / 1024:.1f} MB")
    print()
    print("📌 发给朋友: 把 dist/PDF解析工具 文件夹压缩后发送")
    print()

    # 清理
    for path in ["build", "PDF解析工具.spec"]:
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
    print("已清理临时文件")
else:
    print("❌ 打包失败")
    print("直接运行: python pdf_parser_desktop.py")
