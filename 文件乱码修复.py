def fix_mojibake(mojibake_text, source_encoding='gbk', target_encoding='utf-8'):
    """
    修复因编码错误导致的乱码问题。

    参数:
        mojibake_text (str): 乱码文本。
        source_encoding (str): 乱码文本被错误解释的编码（默认是GBK）。
        target_encoding (str): 原始文本的正确编码（默认是UTF-8）。

    返回:
        str: 修复后的正确文本。
    """
    try:
        # 将乱码文本重新编码为字节序列（使用错误的编码）
        byte_data = mojibake_text.encode(source_encoding, errors='ignore')
        # 将字节序列解码为正确的文本（使用正确的编码）
        fixed_text = byte_data.decode(target_encoding, errors='ignore')
        return fixed_text
    except Exception as e:
        print(f"修复失败: {e}")
        return None


def main():
    # 输入文件路径
    input_file = "input_garbled.txt"
    # 输出文件路径
    output_file = "output_decoded.txt"

    try:
        # 读取输入文件中的乱码内容
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile:
            garbled_text = infile.read()

        print("原始乱码内容：")
        print(garbled_text)

        # 尝试多种编码组合
        encoding_pairs = [
            ('gbk', 'utf-8'),
            ('utf-8', 'gbk'),
            ('latin1', 'utf-8'),
            ('utf-8', 'latin1'),
            ('iso-8859-1', 'utf-8'),
            ('utf-8', 'iso-8859-1')
        ]

        fixed_text = None
        for source_encoding, target_encoding in encoding_pairs:
            print(f"尝试修复乱码（源编码: {source_encoding}，目标编码: {target_encoding}）")
            fixed_text = fix_mojibake(garbled_text, source_encoding, target_encoding)
            if fixed_text:
                print(f"修复后的文本: {fixed_text}")
                break

        if fixed_text:
            # 将修复后的内容写入输出文件
            with open(output_file, 'w', encoding='utf-8') as outfile:
                outfile.write(fixed_text)

            print("还原成功，结果已保存到文件：", output_file)
        else:
            print("还原失败，未生成输出文件。")
    except FileNotFoundError:
        print(f"错误：文件 {input_file} 未找到，请确保文件路径正确。")
    except Exception as e:
        print("处理文件时发生错误：", e)


if __name__ == "__main__":
    main()