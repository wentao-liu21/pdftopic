# PDF转图片工具

一个简单易用的命令行工具，用于将PDF文件转换为图片格式。

## 功能特点

- 支持将单个PDF文件转换为图片
- 支持批量转换目录中的所有PDF文件
- 支持多种输出格式：PNG、JPG、JPEG
- 自动创建输出目录（如果不存在）
- 兼容Windows和Linux文件系统路径

## 安装依赖

```bash
pip install pymupdf
```

## 使用方法

### 基本语法

```bash
python pdf_to_image.py <输入路径> <输出目录> [选项]
```

### 参数说明

| 参数 | 说明 | 必需 |
|------|------|------|
| `input_path` | PDF文件路径或包含PDF文件的目录路径 | 是 |
| `output_dir` | 转换后图片的输出目录路径 | 是 |
| `--format` / `-f` | 输出图片格式，可选值：png、jpg、jpeg，默认值：png | 否 |

### 使用示例

#### Windows 系统

```cmd
:: 转换单个PDF文件为PNG格式
python pdf_to_image.py "C:\Documents\test.pdf" "C:\Documents\output"

:: 转换单个PDF文件为JPG格式
python pdf_to_image.py "C:\Documents\test.pdf" "C:\Documents\output" --format jpg

:: 批量转换目录中的所有PDF文件
python pdf_to_image.py "C:\Documents\pdfs" "C:\Documents\output"
```

#### Linux 系统

```bash
# 转换单个PDF文件为PNG格式
python pdf_to_image.py /home/user/documents/test.pdf /home/user/documents/output

# 转换单个PDF文件为JPG格式
python pdf_to_image.py /home/user/documents/test.pdf /home/user/documents/output --format jpg

# 批量转换目录中的所有PDF文件
python pdf_to_image.py /home/user/documents/pdfs /home/user/documents/output
```

## 路径格式说明

### Windows 路径格式

- 使用反斜杠 `\` 分隔目录：`C:\Users\Name\Documents\file.pdf`
- 如果路径包含空格，需要用双引号包裹：`"C:\My Documents\file.pdf"`

### Linux 路径格式

- 使用正斜杠 `/` 分隔目录：`/home/user/documents/file.pdf`
- 如果路径包含空格，需要用双引号包裹或转义：`"/home/user/My Documents/file.pdf"`

## 输出说明

- 对于单页PDF，输出文件名格式：`原文件名.扩展名`
- 对于多页PDF，输出文件名格式：`原文件名_页码.扩展名`
- 输出目录会自动创建（包括所有父目录）
- 如果PDF文件名包含图片格式扩展名（如 `xxx.png.pdf`），程序会自动去除重复扩展名，输出为 `xxx.png`

## 示例输出

```
正在处理PDF文件: /home/user/documents/test.pdf
已保存: /home/user/documents/output/test_1.png
已保存: /home/user/documents/output/test_2.png
已保存: /home/user/documents/output/test_3.png
转换完成！共 3 页
```

## 注意事项

1. 请确保已安装 `pymupdf` 库
2. 输入路径可以是单个PDF文件或包含PDF文件的目录
3. 输出目录如果不存在会自动创建
4. 仅支持 `.pdf` 后缀的文件
5. 建议使用绝对路径以避免路径解析问题
6. **重要**：如果路径中包含空格、中文或特殊字符，**必须使用双引号包裹路径**
7. Windows路径使用反斜杠 `\`，Linux路径使用正斜杠 `/`
8. **重要**：**避免在路径末尾添加斜杠或反斜杠**，Windows下反斜杠会转义引号导致参数解析失败
9. 输出目录参数为可选，如果不提供，程序会在输入路径下自动创建 `output` 子目录

## 常见问题

### Q: 提示 "the following arguments are required: output_dir"

**原因**：路径中包含空格、中文或特殊字符没有用双引号包裹，或者路径末尾带有斜杠/反斜杠导致引号被转义。

**解决方案**：使用双引号包裹路径，并且**不要在路径末尾添加斜杠或反斜杠**


### Q: 提示 "文件未找到错误"

**原因**：输入路径不存在或拼写错误。

**解决方案**：检查路径是否正确，确保文件或目录存在。

### Q: 提示 "权限错误"

**原因**：没有读取输入文件或写入输出目录的权限。

**解决方案**：检查文件和目录的权限设置，确保有足够的读写权限。