import fitz
import argparse
from pathlib import Path


def pdf_to_images(pdf_path, output_dir, output_format='png'):
    doc = fitz.open(str(pdf_path))
    base_name = pdf_path.stem
    
    image_extensions = {'.png', '.jpg', '.jpeg'}
    while True:
        temp_path = Path(base_name)
        if temp_path.suffix.lower() in image_extensions:
            base_name = temp_path.stem
        else:
            break
    
    for page_index in range(len(doc)):
        page = doc[page_index]
        pix = page.get_pixmap(dpi=300)
        if len(doc) == 1:
            output_path = output_dir / f"{base_name}.{output_format}"
        else:
            output_path = output_dir / f"{base_name}_{page_index + 1}.{output_format}"
        pix.save(str(output_path))
        print(f"已保存: {output_path}")
    
    page_count = len(doc)
    doc.close()
    print(f"转换完成！共 {page_count} 页")


def process_pdfs_in_directory(input_dir, output_dir, output_format='png'):
    pdf_files = sorted(f for f in input_dir.iterdir() if f.is_file() and f.suffix.lower() == '.pdf')
    
    if not pdf_files:
        print("未找到PDF文件")
        return
    
    print(f"找到 {len(pdf_files)} 个PDF文件")
    for pdf_file in pdf_files:
        print(f"\n正在处理: {pdf_file.name}")
        pdf_to_images(pdf_file, output_dir, output_format)


def main():
    parser = argparse.ArgumentParser(description='将PDF文件转换为图片')
    parser.add_argument('input_path', help='PDF文件路径或包含PDF文件的目录路径')
    parser.add_argument('output_dir', nargs='?', default=None,
                        help='转换后图片的输出目录路径，默认与输入路径同目录或创建output子目录')
    parser.add_argument('--format', '-f', default='png', choices=['png', 'jpg', 'jpeg'],
                        help='输出图片格式，默认为png')
    
    args = parser.parse_args()
    
    input_path = Path(args.input_path.rstrip('/\\'))
    output_dir = Path(args.output_dir.rstrip('/\\')) if args.output_dir else None
    output_format = args.format.lower()
    
    try:
        if not input_path.exists():
            print(f"错误：输入路径不存在: {input_path}")
            return
        
        if output_dir is None:
            if input_path.is_file():
                output_dir = input_path.parent / 'output'
            else:
                output_dir = input_path / 'output'
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        if input_path.is_file():
            if input_path.suffix.lower() != '.pdf':
                print(f"错误：输入文件不是PDF文件: {input_path}")
                return
            print(f"正在处理PDF文件: {input_path}")
            pdf_to_images(input_path, output_dir, output_format)
        elif input_path.is_dir():
            print(f"正在处理目录中的PDF文件: {input_path}")
            process_pdfs_in_directory(input_path, output_dir, output_format)
        else:
            print(f"错误：无效的输入路径: {input_path}")
    
    except FileNotFoundError as e:
        print(f"文件未找到错误: {e}")
    except PermissionError as e:
        print(f"权限错误: {e}")
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == '__main__':
    main()