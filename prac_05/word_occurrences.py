"""
Word occurrence counter with sorted and aligned output
Estimate: 40 minutes
Actual:   45 minutes
"""

def count_words(text):
    """统计文本中各单词的出现次数"""
    words = text.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def format_output(word_count):
    """格式化输出单词统计结果（排序并对齐）"""
    sorted_words = sorted(word_count.items())
    max_word_length = max(len(word) for word, _ in sorted_words)
    for word, count in sorted_words:
        print(f"{word:{max_word_length}} : {count}")

def main():
    """主函数：获取用户输入并处理"""
    text = input("Text: ")
    word_count = count_words(text)
    format_output(word_count)

if __name__ == "__main__":
    main()